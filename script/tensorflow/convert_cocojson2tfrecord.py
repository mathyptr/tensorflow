""" Sample TensorFlow COCO_JSON-to-TFRecord converter

usage: convert_cocojson2tfrecord.py [-h] [-j JSON_DIR] [-l LABELS_PATH] [-o OUTPUT_PATH] [-i IMAGE_DIR] [-c CSV_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -j JSON_DIR, --json_dir JSON_DIR
                        Path to the folder where the input .json files are stored.
  -l LABELS_PATH, --labels_path LABELS_PATH
                        Path to the labels (.pbtxt) file.
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Path of augmentation_output TFRecord (.record) file.
  -i IMAGE_DIR, --image_dir IMAGE_DIR
                        Path to the folder where the input image files are stored.
                        Defaults to the same directory as JSON_DIR.
  -c CSV_PATH, --csv_path CSV_PATH
                        Path of augmentation_output .csv file. If none provided, then no file will be written.
"""

import os
import glob
import pandas as pd
import io
import argparse
import tensorflow as tf
from PIL import Image
from object_detection.utils import dataset_util, label_map_util
from collections import namedtuple
from coco_utils import COCOManager

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging (1)

# Initiate argument parser
parser = argparse.ArgumentParser(
    description="Sample TensorFlow COCO_JSON-to-TFRecord converter")
parser.add_argument("-j",
                    "--json_dir",
                    help="Path to the folder where the input COCO .json files are stored.",
                    type=str)
parser.add_argument("-l",
                    "--labels_path",
                    help="Path to the labels (.pbtxt) file.", type=str)
parser.add_argument("-o",
                    "--output_path",
                    help="Path of augmentation_output TFRecord (.record) file.", type=str)
parser.add_argument("-i",
                    "--image_dir",
                    help="Path to the folder where the input image files are stored. "
                         "Defaults to the same directory as JSON_DIR.",
                    type=str, default=None)
parser.add_argument("-c",
                    "--csv_path",
                    help="Path of augmentation_output .csv file. If none provided, then no file will be "
                         "written.",
                    type=str, default=None)

args = parser.parse_args()

if args.image_dir is None:
    args.image_dir = args.json_dir

label_map = label_map_util.load_labelmap(args.labels_path)
label_map_dict = label_map_util.get_label_map_dict(label_map)


def json_to_csv(path):
    """Iterates through all COCO .json files (considers only BBOXES) in a given directory and combines
    them in a single Pandas dataframe.

    Parameters:
    ----------
    path : str
        The path containing the .xml files
    Returns
    -------
    Pandas DataFrame
        The produced dataframe
    """

    json_list = []
    for json_file in glob.glob(path + '/*.json'):
        coco = COCOManager(json_file)
        images, images_sizes, bboxes, titles = coco.get_all_images_annotation()
        for image_idx in range(len(images)):
            filename = images[image_idx]
            width = int(images_sizes[image_idx][0])
            height = int(images_sizes[image_idx][1])
            for bbox_idx in range(len(bboxes[image_idx])):
                xmin = int(width*bboxes[image_idx][bbox_idx][0])
                ymin = int(height*bboxes[image_idx][bbox_idx][1])
                xmax = xmin + int(width*bboxes[image_idx][bbox_idx][2])
                ymax = ymin + int(height*bboxes[image_idx][bbox_idx][3])
                name = titles[image_idx][bbox_idx]
                value = (filename,
                         width,
                         height,
                         name,
                         xmin,
                         ymin,
                         xmax,
                         ymax,
                         )
                json_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(json_list, columns=column_name)
    print(f'Processed {len(json_list)} JSON files.')
    return xml_df


def class_text_to_int(row_label):
    return label_map_dict[row_label]


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.compat.v1.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.io.TFRecordWriter(args.output_path)
    path = os.path.join(args.image_dir)
    print('Creating intermediate CVS representation')
    examples = json_to_csv(args.json_dir)
    print('Converting intermediate CSV representation to TFRecord')
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())
    writer.close()
    print('Successfully created the TFRecord file: {}'.format(args.output_path))
    if args.csv_path is not None:
        examples.to_csv(args.csv_path, index=None)
        print('Successfully created the CSV file: {}'.format(args.csv_path))


if __name__ == '__main__':
    tf.compat.v1.app.run()
