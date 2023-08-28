import cv2
import numpy as np
import os

class ImageEnhancer:
    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        try:
            self.image = cv2.imread(self.image_path)
            return self.image is not None
        except Exception as e:
            print(f"Error opening the image: {str(e)}")
            return False

    def resize(self, factor=0.3):
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
        if self.image is not None:
            gamma_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
            self.image = cv2.LUT(self.image, gamma_table)

    def smooth(self):
        if self.image is not None:
            self.image = cv2.GaussianBlur(self.image, (3, 3), 0)

    def save_enhanced_image(self, file_name="enhanced_image.jpg"):
        if self.image is not None:
            output_folder = "processed_photos"

            # Check if the output folder exists, if not, create it
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Full path to save the enhanced image
            output_path = os.path.join(output_folder, file_name)

            # Save the processed image
            cv2.imwrite(output_path, self.image)

            print(f"Enhanced image saved at {output_path}")

    def display_image(self):
        if self.image is not None:
            cv2.imshow("Image", self.image)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def process(self):
        if self.load_image():
            self.resize()
            self.apply_sharpening_filter()
            self.adjust_gamma()
            self.smooth()
            self.save_enhanced_image()

    def display_concatenated_image(self, enhanced_image):
        concatenated_image = cv2.hconcat([self.image, enhanced_image])
        if concatenated_image is not None:
            height, width = concatenated_image.shape[:2]
            new_height = int(height * 0.5)
            new_width = int(width * 0.5)
            concatenated_image = cv2.resize(concatenated_image, (new_width, new_height))
            cv2.imshow("Original and Enhanced Image", concatenated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
