from processing.open_image import *
from ocr.get_text3 import *
if __name__ == "__main__":
    path = "photo/image.jpeg"
    path_enhanced_image = "processed_photos/enhanced_image.png"
    image = ImageEnhancer(path)
    image.process()
    image.display_image()

    original_image = ImageEnhancer(path)
    original_image.load_image()
    original_image.resize()
    original_image.display_concatenated_image(image.image)

    get_text_img(path_enhanced_image)