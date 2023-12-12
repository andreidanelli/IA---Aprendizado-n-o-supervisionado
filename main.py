import os.path
import numpy as np
import cv2

from pip._internal.cli.spinners import open_spinner

import constants.const


def saveImageResultDirectory():
    cv2.imwrite(directory, res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def showConfgAllImageOrigin():
    heigth_origin, width_origin, chanel_origin = img.shape
    count = validatorColorUniqueImageOrigin()

    with open (f'{constants.const.NAME_IMAGE_ORIGIN}'+'_K'+str(K)+'.txt','w') as arquivo:
        arquivo.write('Info Image Origin\n')
        arquivo.write(f'Dimension: {heigth_origin}x{width_origin}\n')
        arquivo.write(f'Heigth: {heigth_origin} pixels\n')
        arquivo.write(f'Witdh: {width_origin} pixels\n')
        arquivo.write(f'Size Image: {os.path.getsize(constants.const.PATH_IMAGE_ORIGIN) / 1024:.0f} Kb\n')
        arquivo.write(f'Color Unique: {count}\n\n\n')

def showConfgAllImagemResult():
    heigth_result, width_result, chanel_result = res2.shape
    count = validatorColorUniqueImageResult()
    with open (f'{constants.const.NAME_IMAGE_ORIGIN}'+'_K'+str(K)+'.txt','a') as arquivo_result:
        arquivo_result.write(f'Info result Image \n')
        arquivo_result.write(f'Dimension: {heigth_result}x{width_result}\n')
        arquivo_result.write(f'Heigth: {heigth_result} pixels\n')
        arquivo_result.write(f'Witdh: {width_result} pixels\n')
        arquivo_result.write(f'Size Image: {os.path.getsize(directory) / 1024:.0f} Kb\n')
        arquivo_result.write(f'Color Unique: {count}\n')


def validatorColorUniqueImageOrigin():
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))
    color_unique = np.unique(pixels, axis=0)
    return len(color_unique)


def validatorColorUniqueImageResult():
    img_result = cv2.imread(directory)
    image_rgb = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))
    color_unique = np.unique(pixels, axis=0)
    return len(color_unique)


img = cv2.imread(constants.const.PATH_IMAGE_ORIGIN)
Z = img.reshape((-1, 3))
K = 6

Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape(img.shape)

print(f'Save Image Result in Directory')
directory = os.path.join(constants.const.PATH_IMAGE_RESULT, constants.const.NAME_IMAGE_RESULT+'_K'+str(K)+'.png')

saveImageResultDirectory()

showConfgAllImageOrigin()

showConfgAllImagemResult()