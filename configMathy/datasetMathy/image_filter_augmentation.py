import argparse
import os
import Augmentor
from PIL import Image, ImageDraw, ImageFont

import numpy as np
from PIL import ImageFilter


NAME = 'Image Filter'
DESR = 'A set of image filters.'
VERSION = '0.1.1'
FILTERS = {
     'grey': 'Greyscale',
#    'hand_drawn': 'HandDrawn',
#    'contour': 'Contour',
    'edge_enhance': 'EdgeEnhance',
    'edge_enhance_more': 'EdgeEnhanceMore',
#    'emboss': 'Emboss',
    'smooth': 'Smooth',
    'sharpen': 'Sharpen',
#    'emboss_45d': 'Emboss45d',
    'sharp_edge': 'SharpEdge',
    'sharp_center': 'SharpCenter',
}


class Emboss45DegreeFilter(ImageFilter.BuiltinFilter):
        name = "Emboss_45_degree"
        filterargs = (3, 3), 1, 0, (
                -1, -1, 0,
                -1, 1, 1,
                0, 1, 1
        )

class DiffHorizFilter(ImageFilter.BuiltinFilter):
        name = "Diff_Horiz_Filter"
        filterargs = (3, 3), 1, 0, (
                1, 1, 2,
                1, 1, 1,
                1, 1, 1
        )

class SharpEdgeFilter(ImageFilter.BuiltinFilter):
        name = "Sharp_Edge"
        filterargs = (3, 3), 1, 0, (
                1, 1, 1,
                1, -7, 1,
                1, 1, 1
        )

class SharpCenterFilter(ImageFilter.BuiltinFilter):
        name = "Sharp_Center"
        filterargs = (3, 3), -1, 0, (
                1, 1, 1,
                1, -9, 1,
                1, 1, 1
        )

def Greyscale(image)-> Image:
    return image.convert('L')


def HandDrawn(image)-> Image:
    a = np.asarray(image.convert('L')).astype('float')
    depth = 10.  # (0-100)
    grad = np.gradient(a)  
    grad_x, grad_y = grad  
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    vec_el = np.pi / 2.2 
    vec_az = np.pi / 4. 
    dx = np.cos(vec_el) * np.cos(vec_az)  
    dy = np.cos(vec_el) * np.sin(vec_az)  #
    dz = np.sin(vec_el)  

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z) 
    b = b.clip(0, 255)

    im = Image.fromarray(b.astype('uint8'))  
    return im



def Contour(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.CONTOUR)

def EdgeEnhance(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.EDGE_ENHANCE)

def EdgeEnhanceMore(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.EDGE_ENHANCE_MORE)

def Emboss(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.EMBOSS)

def Smooth(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.SMOOTH)

def SmoothMore(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.SMOOTH_MORE)

def Sharpen(image)-> Image:
    return image.convert('RGB').filter(ImageFilter.SHARPEN)

def Emboss45d(image)-> Image:
    return image.convert('RGB').filter(Emboss45DegreeFilter)

def SharpEdge(image)-> Image:
    return image.convert('RGB').filter(SharpEdgeFilter)

def SharpCenter(image)-> Image:
    return image.convert('RGB').filter(SharpCenterFilter)

def DiffHoriz(image)-> Image:
    return image.convert('RGB').filter(DiffHorizFilter)


def myfilter(image,filtertype)-> Image:
    if filtertype == 'grey':
            im=Greyscale(image)
#    elif filtertype == 'hand_drawn':
#            im=HandDrawn(image)
    elif filtertype == 'contour':
            im=Contour(image)
    elif filtertype == 'edge_enhance':
            im=EdgeEnhance(image)
    elif filtertype == 'edge_enhance_more':
            im=EdgeEnhanceMore(image)
#    elif filtertype == 'emboss':
#            im=Emboss(image)
    elif filtertype == 'Diff_Horiz_Filter':
            im=DiffHoriz(image)
    elif filtertype == 'smooth':
            im=Smooth(image)
    elif filtertype == 'smooth_more':
            im=SmoothMore(image)
    elif filtertype == 'sharpen':
            im=Sharpen(image)
#    elif filtertype == 'emboss_45d':
#            im=Emboss45d(image)
    elif filtertype == 'sharp_edge':
            im=SharpEdge(image)
    elif filtertype == 'sharp_center':
            im=SharpCenter(image)
    else:
            im=None
    return im

def show_filters():
    print('Filter: ')
    [print(x) for x in FILTERS]

def usage():
    print('Usage: ')
    print("-i or --input 'Input images path.'")
    print("-o or --output 'Output image path.'")
    print("-a or --augmentation Image data augmentation.'")
    print("-p or --probability 'Probability for data augmentatio'")
    print("-n or --nsample 'Number of sample for data augmentation.'")
    print("-s or --suffix 'Suffix Index.'")
    print("-v or --version 'Program version'")



def parse_args(args):
    print(args)
    if not args.input or not os.path.exists(args.input):
        print("input "+args.input)
        print("ERR")
        usage()
        show_filters()
        return None
    inp = args.input
    output = args.output
    if not output:
        output = './'
    print("augmentation "+args.augmentation)
    print("probability "+args.augmentation)
    augmen=args.augmentation
    augmen.upper()
    probability=0
    nsample=0
    if not augmen and (augmen!='Y' and augmen!='N'):
        print("ERR1")
        print(augmen)
        usage()
        show_filters()
        return None
    if augmen =="Y":
        probability=int(args.probability)
        nsample=int(args.nsample)

        if probability>1 or probability<0:
           print("ERR2")
           usage()
           show_filters()
           return None

    output_type = os.path.splitext(args.input)[1].strip('.')
    suffix=args.suffix
    return {'augmentation': augmen,'probability': probability,'nsample':nsample, 'input': inp, 'output': output, 'output_type': output_type,'output_suffix_index': suffix}



def call_filter(filtername, image, output,outputfilename,outtype):
    print('Filter image by %s' % filtername)

    im2 = myfilter(image,filtername)

    # output
    im2 = im2.convert('RGB')
    if os.path.isdir(output):
        fout = output + outputfilename + '.' + outtype
    else:
        fout = output
    im2.save(fout, outtype)
    print('Output to %s' % fout)
    return fout


def call_augmentation(prob,nsample, inputdir):

    p = Augmentor.Pipeline(inputdir)
 
    p.flip_left_right(probability=prob)
    p.skew_top_bottom(probability=prob , magnitude=0.3)
    p.rotate(probability=prob, max_left_rotation=4, max_right_rotation=4)
    p.zoom(probability=prob, min_factor = 1, max_factor = 1.1)
    p.random_distortion(probability=prob, grid_width=7, grid_height=8, magnitude=9)
    p.sample(nsample)


def run(args):
    a = parse_args(args)
    if a is None:
        return
   
    if a['augmentation'] == 'N':
        image = Image.open(a['input'])
        filename= os.path.splitext(a['input'])[0].strip('.')
        outsuffix=int(a['output_suffix_index'])
        for f in FILTERS:
            outputfilename=filename+str(outsuffix)
            out = call_filter(f, image,a['output'],outputfilename,a['output_type']) 
            outsuffix=outsuffix+1
    else:
        call_augmentation(a['probability'],a['nsample'],a['input']) 


def main():
    arg = argparse.ArgumentParser(description=DESR)
    arg.add_argument('-v', '--version', action='version', version=NAME + ' ' + VERSION)
    arg.add_argument('-a', '--augmentation', help='Image data augmentation.')
    arg.add_argument('-p', '--probability', help='Probability for data augmentation.')
    arg.add_argument('-n', '--nsample', help='Number of sample for data augmentation.')
    arg.add_argument('-i', '--input', help='Input images path.')
    arg.add_argument('-s', '--suffix', help='Suffix Index.')
    arg.add_argument('-o', '--output', help='Output image path or directory (for multi filters).')

    parser = arg.parse_args()
    run(parser)


if __name__ == '__main__':
    main()
