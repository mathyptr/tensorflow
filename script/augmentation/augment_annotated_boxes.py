from coco_utils import COCOManager
import box_augmentations_transformer as atf
import cv2
import argparse
import os
import sys
from multiprocessing import Pool, current_process, Value
import logging

def init_globals(counter):
    global cnt
    cnt = counter

def drawProgressBar(percent, barLen = 20):
    # percent float from 0 to 1.
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()


def augment_image(img_filename, img_coco_bboxes, img_title):
    global num_iterations
    curr_proc = current_process()
    print(curr_proc.name, " - ", img_filename, img_coco_bboxes, img_title)

    augmented_transformed_filenames = []
    augmented_transformed_image_sizes = []
    augmented_transformed_bboxes = []
    augmented_transformed_class_labels = []

    try:
        # read image and convert to RGB format
        bgr_image = cv2.imread(os.path.join(dataset_dir, img_filename))
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

        num_augmentations = 0
        for i in range(num_iterations):
            if num_augmentations % 100 == 0:
                with cnt.get_lock():
                    cnt.value += 100
                    print(f'Current augmented images {cnt.value}')
            for transform_name in atf.TRANSFORMS_DICT:
                logging.info(f"[*] Trasformazione {transform_name}")      

                transforms = atf.TRANSFORMS_DICT[transform_name]
                transform = transforms(args.min_visibility)
                logging.debug(f"[*] Img coco bboxes {img_coco_bboxes}")                      
                transformed_instance = transform(image=rgb_image, bboxes=img_coco_bboxes, class_labels=img_title)
                transformed_filename = img_filename + "_" + transform_name + "_iter" + str(i) + ".jpg"

                transformed_rgb_image = transformed_instance['image']
                transformed_bboxes = transformed_instance['bboxes']
                transformed_class_labels = transformed_instance['class_labels']
                logging.debug(f"[*] Transformed bboxes {transformed_bboxes}")                      
                if not transformed_bboxes:
                    continue  # transformation resulted in an image below min_visibility threshold, skip it
                # else if transformation provided results add them to list
                augmented_transformed_filenames.append(transformed_filename)
                transformed_bgr_image = cv2.cvtColor(transformed_rgb_image, cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(output_dir, transformed_filename), transformed_bgr_image)
                num_augmentations += 1
#MATHY                     augmented_transformed_image_sizes.append([transformed_bgr_image.shape[0], transformed_bgr_image.shape[1]])
                augmented_transformed_image_sizes.append([transformed_bgr_image.shape[1], transformed_bgr_image.shape[0]]) #MATHY
                augmented_transformed_bboxes.append(transformed_bboxes)
                augmented_transformed_class_labels.append(transformed_class_labels)
    except Exception as e:
        print("Exception while processing image: ", img_filename)
        print(e)
    return augmented_transformed_filenames, augmented_transformed_image_sizes, augmented_transformed_bboxes, augmented_transformed_class_labels


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', type=str,
                        help='Input file name (.json file with COCO annotation)')
    parser.add_argument('output_directory', type=str,
                        help='Output directory to store augmented images and associated JSON file with COCO annotations')
    parser.add_argument('-n', '--num_iterations', help='Number of iterations for each transformation set', default=5,
                        type=int)
    parser.add_argument('-m', '--min_visibility', type=float, default=0.2, help='Minimum visibility of augmented boxes')
    parser.add_argument('-c', '--output_type_csv', action='store_true', default=False,
                        help='Produce a CSV file otherwise JSON file')
    parser.add_argument('-s', '--single_file', action='store_true', default=False,
                        help='Produce a single COCO file for each augmentation')
    args = parser.parse_args()

    output_dir = args.output_directory
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    dataset_dir, filename = os.path.split(args.input_filename)
    num_iterations = args.num_iterations

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)    
    logging.info(f"[*] Start augmentation")      
    print('Augment annotation boxes')
    print(f'Input COCO JSON file: {args.input_filename} - Dataset directory: {dataset_dir}\n'
          f'augmentation_output directory: {output_dir} - num iterations: {num_iterations} - min. visibility: {args.min_visibility}')

    coco = COCOManager(args.input_filename)
    images, images_sizes, bboxes, titles = coco.get_all_images_annotation()
    num_images = len(images)
    print(f'Processing {num_images} images. Creating up to {num_images * num_iterations * len(atf.TRANSFORMS_DICT)} augmented images per image')
    logging.info(f"[*] images: {images} images_sizes: {images_sizes} bboxes: {bboxes} titles: {titles}")   
    print('Augmentation started...')
    num_images = len(images)
    all_transformed_filenames = []
    all_transformed_image_sizes = []
    all_transformed_bboxes = []
    all_transformed_class_labels = []

    cnt = Value('i', 0)
    old_cnt = Value('i', 0)
    with Pool(initializer=init_globals, initargs=(cnt,)) as pool:
        logging.info(f"[*] Pool: {bboxes}")                 
        transformed_filenames, transformed_image_sizes, transformed_bboxes, transformed_class_labels = zip(*pool.starmap(augment_image, zip(images, bboxes, titles)))
        logging.info(f"[*] Transformed filename and image sizes: {transformed_filenames} {transformed_image_sizes}")   
        [all_transformed_filenames.extend(transformed_filenames_el) for transformed_filenames_el in transformed_filenames]
        [all_transformed_image_sizes.extend(transformed_image_sizes_el) for transformed_image_sizes_el in transformed_image_sizes]
        [all_transformed_bboxes.extend(transformed_bboxes_el) for transformed_bboxes_el in transformed_bboxes]
        [all_transformed_class_labels.extend(transformed_class_labels_el) for transformed_class_labels_el in transformed_class_labels]
    print('Augmentation completed.')

    if args.output_type_csv:
        print('Creating CSV annotations for augmentations')
        if args.single_file:
#            coco.save_csv_boxes(os.path.join(output_dir, "augmented_files.csv"), all_transformed_filenames,                             all_transformed_image_sizes, all_transformed_bboxes, all_transformed_class_labels)
            coco.save_csv_boxes(output_dir,os.path.join(output_dir,"augmented_files.csv"), all_transformed_filenames,
                             all_transformed_image_sizes, all_transformed_bboxes, all_transformed_class_labels)
        else:
            coco.save_csv_boxes_files(output_dir, all_transformed_filenames,
                                   all_transformed_image_sizes, all_transformed_bboxes,
                                   all_transformed_class_labels)
    else:    
        print('Creating JSON annotations for augmentations')
        if args.single_file:
            coco.save_coco_boxes(os.path.join(output_dir, "augmented_files.json"), all_transformed_filenames,
                             all_transformed_image_sizes, all_transformed_bboxes, all_transformed_class_labels)
        else:
            coco.save_coco_boxes_files(output_dir, all_transformed_filenames,
                                   all_transformed_image_sizes, all_transformed_bboxes,
                                   all_transformed_class_labels)
    print('Annotations completed.')



