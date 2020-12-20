"""import cv2
from pylibdmtx.pylibdmtx import decode
print(decode(cv2.imread('test.png')))"""
import cv2
from pylibdmtx.pylibdmtx import decode

image = cv2.imread("test.png")
h, w  = image.shape[:2]
decdd = decode((image[:, :, :1].tobytes(), w, h))
print(decdd)
