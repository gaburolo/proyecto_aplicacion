import cv2
import numpy as np
import os

# The ImageEnhancer class is used to enhance images.
class ImageEnhancer:
    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        """
        The function attempts to load an image using OpenCV and returns True if successful, otherwise it
        prints an error message and returns False.
        :return: a boolean value. It returns True if the image is successfully loaded and assigned to
        the "self.image" attribute, and False if there is an error opening the image.
        """
        try:
            self.image = cv2.imread(self.image_path)
            return self.image is not None
        except Exception as e:
            print(f"Error opening the image: {str(e)}")
            return False

    def resize(self, factor=0.3):
        """
        The `resize` function resizes an image based on its current dimensions and a given factor, with
        a condition to resize only if the image is larger than a certain size.
        
        :param factor: The `factor` parameter is a scaling factor that determines how much the image
        should be resized. By default, it is set to 0.3, which means the image will be resized to 30%
        larger than its original size. However, if the height and width of the image are both
        """
        if self.image is not None:
            height, width = self.image.shape[:2]
            if height > 600 and width > 800:
                new_height = int(height * 1)
                new_width = int(width * 1)
                self.image = cv2.resize(self.image, (new_width, new_height))
            else:
                new_height = int(height * (factor + 1.5))
                new_width = int(width * (factor + 1.5))
                self.image = cv2.resize(self.image, (new_width, new_height))

    def apply_sharpening_filter(self):
        """
        The function applies a sharpening filter to an image using a specified kernel.
        """
        if self.image is not None:
            """Otra opcion de kernel
            kernel = np.array([[-2, 0, -2],
                   [0,  9, 0],
                   [-2, 0, -2]])"""
            
            kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

            self.image = cv2.filter2D(self.image, -1, kernel)

    def adjust_gamma(self, gamma=1.2):
        """
        The function adjusts the gamma value of an image using a lookup table.
        
        :param gamma: The gamma parameter in the adjust_gamma function is used to adjust the gamma
        correction of an image. Gamma correction is a non-linear operation that adjusts the brightness
        and contrast of an image. A gamma value less than 1.0 will make the image darker, while a gamma
        value greater than 1
        """
        if self.image is not None:
            gamma_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
            self.image = cv2.LUT(self.image, gamma_table)

    def smooth(self):
        """
        The function smooths an image using a Gaussian blur filter.
        """
        if self.image is not None:
            self.image = cv2.GaussianBlur(self.image, (3, 3), 0)

    def save_enhanced_image(self, file_name="enhanced_image.png"):
        """
        The function saves an enhanced image to a specified file path.
        
        :param file_name: The file_name parameter is a string that specifies the name of the enhanced
        image file. By default, it is set to "enhanced_image.png", defaults to enhanced_image.png
        (optional)
        """
        if self.image is not None:
            output_folder = "processed_photos"

            # Check if the output folder exists, if not, create it
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Full path to save the enhanced image
            output_path = os.path.join(output_folder, file_name)

            # Save the processed image
            cv2.imwrite(output_path, self.image)


    def display_image(self):
        """
        The function displays an image using OpenCV.
        """
        if self.image is not None:
            cv2.imshow("Image", self.image)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def process(self, typeDoc):
        """
        The function processes an image by loading it, resizing it, applying various filters and
        adjustments depending on the type of document, and then saving the enhanced image.
        
        :param typeDoc: The parameter "typeDoc" is a string that represents the type of document being
        processed. It is used to determine whether certain image processing operations should be applied
        or not. In this code, if the value of "typeDoc" is not equal to "licencia1", then the sharpening
        filter
        """
        if self.load_image():
            self.resize()
            if typeDoc != "licencia1":
                self.apply_sharpening_filter()
                self.adjust_gamma()
                self.smooth()   
            self.save_enhanced_image()

    def display_concatenated_image(self, enhanced_image):
        """
        The function displays the original and enhanced images side by side in a resized window.
        
        :param enhanced_image: The `enhanced_image` parameter is an image that has been enhanced or
        modified in some way. It is used to create a concatenated image by horizontally stacking it next
        to the original image
        """
        concatenated_image = cv2.hconcat([self.image, enhanced_image])
        if concatenated_image is not None:
            height, width = concatenated_image.shape[:2]
            new_height = int(height * 0.5)
            new_width = int(width * 0.5)
            concatenated_image = cv2.resize(concatenated_image, (new_width, new_height))
            cv2.imshow("Original and Enhanced Image", concatenated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
