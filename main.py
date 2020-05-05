from image import *
from transform import *
import numpy as np
import keygen
import chaos
import sys

if (len(sys.argv) < 3):
	print("Please enter a filepath and image name of the image to process.")
	exit()

filepath = sys.argv[1]
name = sys.argv[2]
image = getImageData(filepath).astype(float)

transformed_image = blockwiseDCT(image)

thresh = 0.02
threshold = transformed_image * (abs(transformed_image) > (thresh*np.max(transformed_image)))

imsize = image.shape
percent_nonzeros = np.sum( threshold != 0.0 ) / (imsize[0]*imsize[1]*1.0)
print("Keeping only %f%% of the DCT coefficients" %(percent_nonzeros*100.0))

dct_image = blockwiseIDCT(image, threshold)
dct_image = normalize(0.0, 1.0, dct_image)

saveImage(dct_image, "compressed" + name + ".jpg")

states_and_key = keygen.create_key_and_init_states(dct_image)
init_x = states_and_key[0]
init_y = states_and_key[1]
init_r = states_and_key[2]
key = states_and_key[3]
r = 1.15
x0 = init_x[0]
y0 = init_y[0]
[row_permutations, column_permutations] = chaos.log_map_sequences(1.13, x0, y0, imsize[0])
permuted_image = swap_rows(dct_image, row_permutations)
saveImage(permuted_image, "row_permuted_" + name + ".jpg")
permuted_image = swap_columns(permuted_image, column_permutations)
saveImage(permuted_image, "rowcolumn_permuted" + name + ".jpg")
