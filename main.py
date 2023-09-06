from processing.open_image import *

if __name__ == "__main__":
    path = "photo/image.jpeg"
    image = ImageEnhancer(path)
    image.process()
    image.display_image()



    original_image = ImageEnhancer(path)
    original_image.load_image()
    original_image.resize()

    original_image.display_concatenated_image(image.image)