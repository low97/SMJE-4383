import pytesseract
from PIL import Image
import cv2
abc = cv2.imread('RECEIPT.png',cv2.IMREAD_COLOR)
def = cv2.cvtColor(abc, cv2.COLOR_BGR2GRAY) 
text = pytesseract.image_to_string(def, 'jpn')
print (text)