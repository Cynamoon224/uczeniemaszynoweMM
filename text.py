import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
pliki=['obrazek.png','obrazek2.png','obrazek3.png','obrazek4.png','obrazek5.png']
for i in pliki:
    img = cv2.imread(i)
    print(type(img))
    print(img.shape)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(img_convert))






