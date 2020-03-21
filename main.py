from image import *
from transform import *
import numpy as np
import keygen

image = getImageData("images/baboon.gif").astype(float)

transformed_image = blockwiseDCT(image)

thresh = 0.02
threshold = transformed_image * (abs(transformed_image) > (thresh*np.max(transformed_image)))

imsize = image.shape
percent_nonzeros = np.sum( threshold != 0.0 ) / (imsize[0]*imsize[1]*1.0)
print("Keeping only %f%% of the DCT coefficients" %(percent_nonzeros*100.0))

dct_image = blockwiseIDCT(image, threshold)
dct_image = normalize(0.0, 1.0, dct_image)

key = keygen.create_key(dct_image)
print(key)
