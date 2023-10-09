import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from processing.get_doc_type import *
from validation.data_compare import *
from validation.validation import *

path = "photo/image.jpeg"

initial_path = "utils/initial.png"
initial_image1 = Image.open(initial_path)
data_container = None

# Función para manejar el evento del botón y actualizar los datos
def update_data():
    clear_screen()
    
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
    validated_label.config(text = "¡FALSO!", foreground = "white", background = "red", font = ("Arial", 40))
    
def show_valid_message():
    validated_label.config(text = "Valido!", foreground = "white", background = "#BFFF7F", font = ("Arial", 40))

# Función para mostrar las imágenes
def show_images():
    global image1, image2
    image1 = Image.open(path)
    width, height = image1.size
    image1 = image1.resize((width // 2, height // 2))
    photo1 = ImageTk.PhotoImage(image1)
    image_label1.config(image = photo1)
    image_label1.image = photo1  # Actualizar referencia de la imagen

    new_image_path = "processed_photos\enhanced_image.png"
    image2 = Image.open(new_image_path)
    width, height = image2.size
    image2 = image2.resize((width // 2, height // 2))
    photo2 = ImageTk.PhotoImage(image2)
    image_label2.config(image = photo2)
    image_label2.image = photo2  # Actualizar referencia de la imagen

def show_data(data_labels):
    global data_container
    data_container = ttk.Frame(root)
    data_container.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    
    canvas = tk.Canvas(data_container, background="black")
    canvas.pack(fill="both", expand=True)

    for key, value in data_labels.items():
        label = ttk.Label(canvas, text=f"{key}: {value}", foreground="white", background="black")
        label.pack(padx=10, pady=5)

def clear_screen():
    validated_label.config(text = "", font = ("", 40), foreground="black", background="black")
    image_label1.config(image = initial_photo1)
    image_label2.config(image = initial_photo1)
    global data_container
    # Eliminar etiquetas de datos anteriores
    if data_container:
        data_container.destroy()


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Imágenes Reducidas y Botón")
root.geometry("1360x760")
root.configure(bg="black")

# Agregar un Label debajo de la primera imagen para mostrar el tipo de imagen
photo_label1 = ttk.Label(root, text="Foto Original", foreground="white", background="black")
photo_label1.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

photo_label2 = ttk.Label(root, text="Foto Mejorada", foreground="white", background="black")
photo_label2.grid(row=0, column=2, padx=10, pady=5, columnspan=2)

type_label = ttk.Label(root, text="Tipo de foto", foreground="white", background="black")
type_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

# Crear un botón para actualizar los datos
button = ttk.Button(root, text="Actualizar Datos", command=update_data)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Crear un espacio para datos (inicialmente vacío)
data_label = ttk.Label(root, text = "Datos:", foreground="white", background="black")
data_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Crear etiquetas para las imágenes (inicialmente vacías)
initial_photo1 = ImageTk.PhotoImage(initial_image1)
image_label1 = ttk.Label(root, image = initial_photo1)
image_label1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

image_label2 = ttk.Label(root, image = initial_photo1)
image_label2.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

validated_label = ttk.Label(root, text="", foreground="black", background="black")
validated_label.grid(row=3, column=2, columnspan=2, padx=10, pady=5)
# Iniciar el bucle principal de tkinter
root.mainloop()