import albumentations as A


## NOTE: these transformations do not have flips. Flips are useful for object detection
## the current goal is to perform instance recognition, so they are substituted by perspective and affine transforms

def transforms_preset_1(min_visibility):
    preset = A.Compose([
        A.Resize(width=550, height=550),
        A.RandomCrop(width=450, height=450, p=1.0),
        A.RandomBrightnessContrast(p=0.4),
        A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3),
    ], bbox_params=A.BboxParams(
        format='coco', label_fields=['class_labels'],
        min_visibility=min_visibility)
    )
    return preset


def transforms_preset_2(min_visibility):
    preset = A.Compose([
        A.RandomBrightnessContrast(p=0.5),
        A.CLAHE(p=0.5),
        A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3)
    ], bbox_params=A.BboxParams(
        format='coco', label_fields=['class_labels'],
        min_visibility=min_visibility)
    )
    return preset


def transforms_preset_3(min_visibility):
    preset = A.Compose([
        A.RandomBrightnessContrast(p=0.5),
        A.CLAHE(p=0.5),
        A.Perspective(p=0.5)
    ], bbox_params=A.BboxParams(
        format='coco', label_fields=['class_labels'],
        min_visibility=min_visibility)
    )
    return preset


def transforms_preset_4(min_visibility):
    preset = A.Compose([
        A.RandomBrightnessContrast(p=0.5),
        A.Blur(p=0.5),
        A.RandomFog(p=0.5),
        A.CLAHE(p=0.5),
        A.Perspective(p=0.5),
        A.RandomRotate90(p=0.5),
        A.MotionBlur(p=0.2),
        A.MedianBlur(blur_limit=3, p=0.1),
    ], bbox_params=A.BboxParams(
        format='coco', label_fields=['class_labels'],
        min_visibility=min_visibility)
    )
    return preset


def transforms_preset_5(min_visibility):
    preset = A.Compose([
        A.SmallestMaxSize(max_size=550),
        A.RandomCrop(width=450, height=450),
        A.Affine(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_6(min_visibility):
    preset = A.Compose([
        A.Affine(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
        A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_7(min_visibility):
    preset = A.Compose([
        A.Perspective(p=0.8),
        A.RandomBrightnessContrast(p=0.2),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_8(min_visibility):
    preset = A.Compose([
        A.Perspective(p=0.8),
        A.Blur(p=0.3),
        A.RGBShift(r_shift_limit=20, g_shift_limit=20, b_shift_limit=20, p=0.3),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_9(min_visibility):
    preset = A.Compose([
        A.ShiftScaleRotate(p=0.5),
        A.RandomBrightnessContrast(p=0.3),
        A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_10(min_visibility):
    preset = A.Compose([
        A.SmallestMaxSize(max_size=550),
        A.RandomCrop(width=450, height=450),
        A.RandomBrightnessContrast(p=0.3),
        A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility)
    )
    return preset


def transforms_preset_11(min_visibility):
    preset = A.Compose([
        A.CLAHE(),
        A.RandomRotate90(),
        #A.Transpose(),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.50, rotate_limit=45, p=.75),
        A.Blur(blur_limit=3),
        A.OpticalDistortion(),
        A.GridDistortion(),
        A.HueSaturationValue(),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility))
    return preset


def transforms_preset_12(min_visibility):
    preset = A.Compose(
        [
            A.SmallestMaxSize(max_size=450),
            A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.5),
            A.RandomCrop(height=350, width=250),
            A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.5),
            A.RandomBrightnessContrast(p=0.5),
            #A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
        ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                    min_visibility=min_visibility)
    )
    return preset


def transforms_preset_13(min_visibility):
    preset = A.Compose([
        A.RandomRotate90(),
        A.Perspective(p=0.2),
        #A.Transpose(),
        A.OneOf([
            A.ISONoise(),
            A.GaussNoise(),
        ], p=0.2),
        A.OneOf([
            A.MotionBlur(p=.2),
            A.MedianBlur(blur_limit=3, p=0.1),
            A.Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        A.OneOf([
            A.OpticalDistortion(p=0.3),
            A.GridDistortion(p=.1),
            A.PiecewiseAffine(p=0.3),
        ], p=0.2),
        A.OneOf([
            A.CLAHE(clip_limit=2),
            A.Sharpen(),
            #A.Emboss(),
            A.RandomBrightnessContrast(),
        ], p=0.3),
        A.HueSaturationValue(p=0.3),
    ], bbox_params=A.BboxParams(format='coco', label_fields=['class_labels'],
                                min_visibility=min_visibility))
    return preset


TRANSFORMS_DICT = {
    'preset_1': transforms_preset_1,
    'preset_2': transforms_preset_2,
    'preset_3': transforms_preset_3,
    'preset_4': transforms_preset_4,
    'preset_5': transforms_preset_5,
    'preset_6': transforms_preset_6,
    'preset_7': transforms_preset_7,
    'preset_8': transforms_preset_8,
    'preset_9': transforms_preset_9,
    'preset_10': transforms_preset_10,
    'preset_11': transforms_preset_11,
    'preset_12': transforms_preset_12,
    'preset_13': transforms_preset_13
}
