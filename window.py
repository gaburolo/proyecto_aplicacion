import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Función para manejar el evento del botón
def on_button_click():
    image2 = Image.open("processed_photos\enhanced_image.png")  # Reemplaza "imagen2.png" con la ruta de tu segunda imagen
    width, height = image2.size
    image2 = image2.resize((width // 2, height // 2))
    photo2 = ImageTk.PhotoImage(image2)
    image_label2 = ttk.Label(root, image=photo2)
    image_label2.grid(row=0, column=1, padx=10, pady=10)
    messagebox.showinfo("Mensaje", "¡Botón clickeado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Imágenes Reducidas y Botón")

# Cargar las imágenes y reducir al 50%
image1 = Image.open("photo/image.jpeg")  # Reemplaza "imagen1.png" con la ruta de tu primera imagen
width, height = image1.size
image1 = image1.resize((width // 2, height // 2))
photo1 = ImageTk.PhotoImage(image1)



# Crear un Label para mostrar la primera imagen reducida
image_label1 = ttk.Label(root, image=photo1)
image_label1.grid(row=0, column=0, padx=10, pady=10)

# Crear un Label para mostrar la segunda imagen reducida


# Crear un botón
button = ttk.Button(root, text="Clic aquí", command=on_button_click)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear un espacio para datos (por ejemplo, un Label)
data_label = ttk.Label(root, text="Datos:")
data_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Agregar datos
datos = {
    "nombre": "Martin",
    "Apellido1": "Calderon",
    "Apellido2": "Blanco",
    "Numero": "1 1234 1234"
}

row_num = 3
for key, value in datos.items():
    label = ttk.Label(root, text=f"{key}: {value}")
    label.grid(row=row_num, column=0, columnspan=2, padx=10, pady=5)
    row_num += 1

# Iniciar el bucle principal de tkinter
root.mainloop()
