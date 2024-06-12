from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (you need to install Tesseract OCR on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image):
    # Open the image file
    img = Image.open(image)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text
