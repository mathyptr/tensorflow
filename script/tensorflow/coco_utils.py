import json
import pycocotools.coco as coco
import os


class COCOManager:
    def __init__(self, input_file):
        self.annotations = coco.COCO(input_file)

    def get_image_annotations(self, filename):
        '''

        :param filename: name of the image for which we want an annotation
        :type filename: string
        :return: bboxes and associated class name
        :rtype: lists
        '''
        _, filename = os.path.split(filename)
        bboxes = []
        titles = []
        for image in self.annotations.imgs.items():
            if filename == image[1]['file_name']:
                img_id = image[1]['id']
                img_desc = self.annotations.loadImgs(img_id)
                ann_ids = self.annotations.getAnnIds(imgIds=[img_id])
                anns = self.annotations.loadAnns(ann_ids)
                cat_ids = [ann['category_id'] for ann in anns]
                ann_names = self.annotations.loadCats(cat_ids)

                for gt in anns:
                    object_name = [sub['name'] for sub in ann_names if sub['id'] == gt['category_id']]
                    bboxes.append(gt['bbox'])
                    titles.append(object_name[0])
                    # print(gt['bbox'], object_name)
        return bboxes, titles

    def get_all_images_annotation(self):
        '''
        Get all the annotations of all the images
        :return: names of the images, sizes of the images, bboxes and associated class name
        :rtype: lists
        '''
        images = []
        image_sizes = []
        bboxes = []
        titles = []
        for image in self.annotations.imgs.items():
            filename = image[1]['file_name']
            image_size = [image[1]['width'], image[1]['height']]
            img_bboxes, img_titles = self.get_image_annotations(filename)
            images.append(filename)
            image_sizes.append(image_size)
            bboxes.append(img_bboxes)
            titles.append(img_titles)
        return images, image_sizes, bboxes, titles


    def save_pbtxt_classes(self, filename):
        '''
        Save the list of COCO JSON class names as TensorFlow .PBTXT file for use with .tfrecord files.
        Note that .pbtxt files have IDs that start from 1, while IDs of COCO JSON files may be 1
        :param filename: output name of the .pbtxt file
        :type filename:
        :return:
        :rtype:
        '''
        pass  # TODO implementare slavataggio .pbtxt - le ID cominciano da 1 !

    def save_coco_boxes(self, filename, image_names, image_sizes, bboxes, classes):
        '''
        Save COCO JSON files of annotations. A single JSON file may contain annotations of different images.
        :param filename: name of the COCO JSON file
        :type filename: string
        :param image_names: names of the images
        :type image_names: list of strings
        :param image_sizes: size of the image
        :type image_sizes: list of sizes
        :param bboxes: list of bboxes
        :type bboxes:
        :param classes: list of classes
        :type classes:
        :return:
        :rtype:
        '''
        json_results = dict()

        categories = []
        inverted_classes_data = dict()
        class_set = set()
        for class_list in classes:
            for class_name in class_list:
                class_set.add(class_name)
        all_classes = self.annotations.loadCats(self.annotations.getCatIds())
        for class_name in class_set:
            classes_data = dict()
            classes_data['id'] = [sub['id'] for sub in all_classes if sub['name'] == class_name][0]
            classes_data['name'] = class_name
            inverted_classes_data[class_name] = classes_data['id']
            categories.append(classes_data)

        images_data = []
        annotations = []
        annotation_id = 0
        for img_idx in range(len(image_names)):
            img_data = dict()
            img_data['id'] = img_idx
            img_data['file_name'] = image_names[img_idx]
            img_data['width'] = image_sizes[img_idx][0]
            img_data['height'] = image_sizes[img_idx][1]
            images_data.append(img_data)
            for bbox_idx in range(len(bboxes[img_idx])):
                bbox_data = dict()
                bbox_data['id'] = annotation_id
                annotation_id += 1
                bbox_data['image_id'] = img_idx
                bbox_data['bbox'] = bboxes[img_idx][bbox_idx]
                bbox_data['category_id'] = inverted_classes_data[classes[img_idx][bbox_idx]]
                annotations.append(bbox_data)
        json_results['images'] = images_data
        json_results['annotations'] = annotations
        json_results['categories'] = categories

        with open(filename, 'w') as outfile:
            json.dump(json_results, outfile)

    def save_coco_boxes_files(self, output_dir, image_names, image_sizes, bboxes, classes):
        '''
        Save the annotations of the selected images in separate COCO JSON files, one for each image
        :param output_dir: output directory where to store all the COCO JSON files
        :type output_dir:
        :param image_names: list of image namses
        :type image_names:
        :param image_sizes: list of image sizes
        :type image_sizes:
        :param bboxes: list of bboxes
        :type bboxes:
        :param classes: list of class names
        :type classes:
        :return:
        :rtype:
        '''
        categories = []
        inverted_classes_data = dict()
        class_set = set()
        for class_list in classes:
            for class_name in class_list:
                class_set.add(class_name)
        all_classes = self.annotations.loadCats(self.annotations.getCatIds())
        for class_name in class_set:
            classes_data = dict()
            classes_data['id'] = [sub['id'] for sub in all_classes if sub['name'] == class_name][0]
            classes_data['name'] = class_name
            inverted_classes_data[class_name] = classes_data['id']
            categories.append(classes_data)

        for img_idx in range(len(image_names)):
            json_results = dict()
            images_data = []
            annotations = []
            annotation_id = 0

            img_data = dict()
            img_data['id'] = img_idx
            filename = image_names[img_idx]
            img_data['file_name'] = filename
            img_data['width'] = image_sizes[img_idx][0]
            img_data['height'] = image_sizes[img_idx][1]
            images_data.append(img_data)
            for bbox_idx in range(len(bboxes[img_idx])):
                bbox_data = dict()
                bbox_data['id'] = annotation_id
                annotation_id += 1
                bbox_data['image_id'] = img_idx
                bbox_data['bbox'] = bboxes[img_idx][bbox_idx]
                bbox_data['category_id'] = inverted_classes_data[classes[img_idx][bbox_idx]]
                annotations.append(bbox_data)

            json_results['images'] = images_data
            json_results['annotations'] = annotations
            json_results['categories'] = categories

            with open(os.path.join(output_dir, os.path.splitext(filename)[0] + ".json"), 'w') as outfile:
                json.dump(json_results, outfile)
