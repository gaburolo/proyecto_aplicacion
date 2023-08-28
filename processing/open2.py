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

        
        gamma = 1.2  # Factor gamma (ajustar según sea necesario)
        tabla_gamma = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        imagen_corregida_gamma = cv2.LUT(imagen, tabla_gamma)

        # Mostrar la imagen original y la imagen con enfoque mejorado
        cv2.imshow("Imagen Original", imagen)
        cv2.imshow("Imagen con Enfoque Mejorado", imagen_corregida_gamma)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No se pudo cargar la imagen.")
except Exception as e:
    print(f"Error al abrir la imagen: {str(e)}")
