import os.path

import numpy as np
import cv2
from pip._internal.cli.spinners import open_spinner

img = cv2.imread('image/image.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 1
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# cv2.imshow('res2',res2)
directory = os.path.join('image-result', 'output_image.jpg')
cv2.imwrite(directory, res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# info imagem original
heigth_origin, width_origin, chanel_origin = img.shape
size_origin = os.path.getsize('image/image.jpg')/1024

print('\n')
print(f'Info Image Origin')
print(f'Heigth: {heigth_origin} pixels')
print(f'Witdh: {width_origin} pixels')
print(f'Size Image: {size_origin:.0f}')
print('\n')

# info imagem result
heigth_result, width_result, chanel_result = res2.shape
size_result = os.path.getsize(directory)/1024

print(f'Info Image Result')
print(f'Heigth: {heigth_result} pixels')
print(f'Witdh: {width_result} pixels')
print(f'Size Image: {size_result:.0f}')