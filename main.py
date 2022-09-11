from distutils.command.config import config
import cv2

objectNames = []
objectNamesFile = './assets/coco.names'
with open(objectNamesFile, 'rt') as f:
    objectNames = f.read().rstrip('\n').split('\n')
print(objectNames)

configPath = ''

img = cv2.imread('./assets/images/lily.png')
# cv2.imshow('Lucy', img)
# cv2.waitKey(0)
