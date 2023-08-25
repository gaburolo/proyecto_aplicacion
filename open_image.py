import cv2
import numpy as np

# Ruta de la imagen (en este caso, asumimos que la imagen se llama "imagen.jpg")
ruta_imagen = "foto/imagen.jpg"

# Intentar abrir la imagen
try:
    imagen = cv2.imread(ruta_imagen)

    # Verificar si la imagen se cargó correctamente
    if imagen is not None:

        alto, ancho = imagen.shape[:2]
        
        if alto > 600 and ancho > 800:
            nuevo_alto = int(alto * 0.3)
            nuevo_ancho = int(ancho * 0.3)
            imagen_nueva = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
        else:
            imagen_nueva = imagen
        # Aplicar el filtro de máscara de nitidez
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

        imagen_nitida = cv2.filter2D(imagen_nueva, -1, kernel)
    
        gamma = 1.2  # Factor gamma (ajustar según sea necesario)
        tabla_gamma = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        imagen_corregida_gamma = cv2.LUT(imagen_nitida, tabla_gamma)
        imagen_suavizada = cv2.GaussianBlur(imagen_corregida_gamma, (3, 3), 0)


        # Aplicar un desenfoque gaussiano a la imagen
        desenfoque = cv2.GaussianBlur(imagen_suavizada, (0, 0), 3)

        # Calcular la máscara de detalle restando el desenfoque de la imagen original
        mascara_detalle = cv2.addWeighted(imagen_suavizada, 1.5, desenfoque, -0.5, 0)

        #Crear una imagen concatenada
        imagen_concatenada = cv2.hconcat([imagen, mascara_detalle])

        # Mostrar la imagen concatenada
        cv2.imshow("Imagen Original y Mejorada", imagen_concatenada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("No se pudo cargar la imagen.")
except Exception as e:
    print(f"Error al abrir la imagen: {str(e)}")