import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from processing.get_doc_type import *
from validation.data_compare import *
from validation.validation import *
from client.client import *

path = "client/photo.png"
initial_path = "utils/initial.png"
initial_image1 = Image.open(initial_path)
data_container = None

def update_data():
    """
    The function `update_data` performs various tasks such as clearing the screen, requesting a photo,
    categorizing the photo, processing the photo, validating the processed data, and displaying the
    results.
    """
    clear_screen()
    requestPhoto()
    type_doc = categorize_local(path)
    new_path = processing(path, type_doc)
    data_labels, should_show  = validate(new_path, type_doc)
    type_label.config(text = "Tipo de documento: " + type_doc)
    if should_show:
        show_images()
        root.after(2000, lambda: show_data(data_labels))
        root.after(5000, lambda: show_valid_message())
    else:
        show_images()
        root.after(2000, lambda: show_data(data_labels))
        root.after(2000, lambda: show_invalid_message())

def show_invalid_message():
    """
    The function `show_invalid_message` displays a message "¡FALSO!" in a label with a red background
    and white foreground, using a font size of 40.
    """
    validated_label.config(text = "¡FALSO!", foreground = "white", background = "red", font = ("Arial", 40))
    
def show_valid_message():
    """
    The function `show_valid_message()` updates the text, foreground color, background color, and font
    of a label widget to display a message indicating that something is valid.
    """
    validated_label.config(text = "Valido!", foreground = "white", background = "#BFFF7F", font = ("Arial", 40))

def show_images():
    """
    The function `show_images` opens two images, resizes them, and displays them in two separate labels.
    """
    global image1, image2
    image1 = Image.open(path)
    width, height = image1.size
    image1 = image1.resize((width // 4, height // 4))
    photo1 = ImageTk.PhotoImage(image1)
    image_label1.config(image = photo1)
    image_label1.image = photo1 

    new_image_path = "processed_photos\enhanced_image.png"
    image2 = Image.open(new_image_path)
    width, height = image2.size
    image2 = image2.resize((width // 4, height // 4))
    photo2 = ImageTk.PhotoImage(image2)
    image_label2.config(image = photo2)
    image_label2.image = photo2 

def show_data(data_labels):
    """
    The function `show_data` creates a frame and a canvas to display data labels in a graphical user
    interface.
    
    :param data_labels: The `data_labels` parameter is a dictionary that contains the labels and
    corresponding values to be displayed in the GUI. Each key-value pair in the dictionary represents a
    label and its associated value
    """
    global data_container
    data_container = ttk.Frame(root)
    data_container.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    
    canvas = tk.Canvas(data_container, background="black")
    canvas.pack(fill="both", expand=True)

    for key, value in data_labels.items():
        label = ttk.Label(canvas, text=f"{key}: {value}", foreground="white", background="black")
        label.pack(padx=10, pady=5)

def clear_screen():
    """
    The function "clear_screen" clears the screen by resetting the text, font, and background color of a
    label, and also resets the images displayed on two image labels. Additionally, it destroys a data
    container if it exists.
    """
    validated_label.config(text = "", font = ("", 40), foreground="black", background="black")
    image_label1.config(image = initial_photo1)
    image_label2.config(image = initial_photo1)
    global data_container
    if data_container:
        data_container.destroy()

def closeApp():
    """
    The closeApp function closes the server and quits the root application.
    """
    closeServer()
    root.quit()


# This code is creating the main window for the GUI application.
root = tk.Tk()
root.title("Interfaz con Imágenes Reducidas y Botón")
root.geometry("1360x760")
root.configure(bg="black")

photo_label1 = ttk.Label(root, text="Foto Original", foreground="white", background="black")
photo_label1.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

photo_label2 = ttk.Label(root, text="Foto Mejorada", foreground="white", background="black")
photo_label2.grid(row=0, column=2, padx=10, pady=5, columnspan=2)

type_label = ttk.Label(root, text="Tipo de foto", foreground="white", background="black")
type_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

button = ttk.Button(root, text="Actualizar Datos", command=update_data)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

data_label = ttk.Label(root, text = "Datos:", foreground="white", background="black")
data_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

initial_photo1 = ImageTk.PhotoImage(initial_image1)
image_label1 = ttk.Label(root, image = initial_photo1)
image_label1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

image_label2 = ttk.Label(root, image = initial_photo1)
image_label2.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

validated_label = ttk.Label(root, text="", foreground="black", background="black")
validated_label.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

button = ttk.Button(root, text="Cerrar", command=closeApp)
button.grid(row=5, column=3, columnspan=2, padx=10, pady=10)

root.mainloop()