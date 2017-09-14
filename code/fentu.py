# coding=utf-8
__author__ = 'xuxuan'
import tifffile as tiff
import matplotlib.pyplot as plt

FILE_2015 = '../data/quickbird2015.tif'
FILE_2017 = '../data/quickbird2017.tif'
FILE_cadastral2015 = '../data/cadastral2015.tif'
FILE_tinysample = '../data/tinysample.tif'

im_2015 = tiff.imread(FILE_2015).transpose([1, 2, 0])
im_2017 = tiff.imread(FILE_2017).transpose([1, 2, 0])
im_tiny = tiff.imread(FILE_tinysample)
im_cada = tiff.imread(FILE_cadastral2015)

a, b = im_tiny.shape
print(a, b)

each_weight = 3 * 37
each_width = 2 * 83
print('each_pic_size =', each_weight * each_width, '=', each_weight, '*', each_width)
weight_step = each_weight
width_step = each_width

for i in range(int(((a - each_weight) / weight_step))):
    for j in range(int((b - each_width) / width_step)):
        hs = i * weight_step
        he = hs + each_weight
        ws = j * width_step
        we = ws + each_width
        sum_cada = im_cada[hs:he, ws:we].sum()
        sum_tiny = im_tiny[hs:he, ws:we].sum()
        if sum_cada > 0 or sum_tiny > 0:
            print(hs, ws, sum_cada, sum_tiny)
            tiff.imsave('../fentu/quickbird2015/%d-%d&%d-%d.tiff' % (hs, he - 1, ws, we - 1), im_2015[hs:he, ws:we, :])
            tiff.imsave('../fentu/quickbird2017/%d-%d&%d-%d.tiff' % (hs, he - 1, ws, we - 1), im_2017[hs:he, ws:we, :])
            tiff.imsave('../fentu/cadastral2015/%d-%d&%d-%d.tiff' % (hs, he - 1, ws, we - 1), im_cada[hs:he, ws:we])
            tiff.imsave('../fentu/tinysample/%d-%d&%d-%d.tiff' % (hs, he - 1, ws, we - 1), im_tiny[hs:he, ws:we])
