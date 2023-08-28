import cv2
import numpy as np

# Ruta de la imagen (en este caso, asumimos que la imagen se llama "imagen.jpg")
ruta_imagen = "foto/imagen.jpg"

# Intentar abrir la imagen
try:
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se cargó correctamente
    if imagen is not None:
        # Aplicar un desenfoque gaussiano a la imagen
        desenfoque = cv2.GaussianBlur(imagen, (0, 0), 3)

        # Calcular la máscara de detalle restando el desenfoque de la imagen original
        mascara_detalle = cv2.addWeighted(imagen, 1.5, desenfoque, -0.5, 0)

        # Mostrar la imagen original y la imagen con enfoque mejorado
        cv2.imshow("Imagen Original", imagen)
        cv2.imshow("Imagen con Enfoque Mejorado", mascara_detalle)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No se pudo cargar la imagen.")
except Exception as e:
    print(f"Error al abrir la imagen: {str(e)}")
