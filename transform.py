import numpy as np
import scipy, scipy.fftpack

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc


def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def blockwiseDCT(image):
    imsize = image.shape
    dct = np.zeros(imsize)
    #Do 8x8 DCT on image (in-place)

    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            dct[i:(i+8),j:(j+8)] = dct2( image[i:(i+8),j:(j+8)] )
    return dct

def blockwiseIDCT(image, threshold):
    imageSize = image.shape
    dct_image = np.zeros(imageSize)
    for i in r_[:imageSize[0]:8]:
        for j in r_[:imageSize[1]:8]:
            dct_image[i:(i+8),j:(j+8)] = idct2( threshold[i:(i+8),j:(j+8)] )
    return image

def normalize(min, max, values):
    return (values - np.min(values)) / np.ptp(values)
