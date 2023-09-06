from PIL import Image, ImageDraw, ImageFont
import generator_names as gn


def create_image(index):
    # Ruta de la imagen de fondo en la que deseas escribir
    imagen_de_fondo = "dataset\Costa Rica\original.jpg"

    # Abre la imagen de fondo
    imagen = Image.open(imagen_de_fondo)

    # Crea un objeto ImageDraw para dibujar en la imagen
    draw = ImageDraw.Draw(imagen)

    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero()
    # Coordenadas y texto que deseas escribir en la imagen
    coordenadas_y_texto = [
        ((342, 533), nombre),
        ((342, 563), apellido1),
        ((342, 593), apellido2),
    ]

    coordenadas_firma = [
        ((280, 460), nombre+ " " + apellido1 + " " + apellido2),
    ]
    coordenadas_numero = [
        ((360, 170), numero),
    ]
    # Fuente y tamaño del texto
    fuente = ImageFont.truetype("arialbd.ttf", 28)
    fuente_firma = ImageFont.truetype("LHANDW.TTF", 36)
    fuente_numero = ImageFont.truetype("arialbd.ttf", 36)
    # Color del texto (en este caso, blanco)
    color_texto = (0, 0, 0)
    


    # Itera sobre las coordenadas y el texto y escribe cada frase en la imagen
    for (x, y), texto in coordenadas_y_texto:
        draw.text((x, y), texto, fill=color_texto, font=fuente)


    for (x, y), texto in coordenadas_firma:
        draw.text((x, y), texto, fill=color_texto, font=fuente_firma)
    for (x, y), texto in coordenadas_numero:
        draw.text((x, y), texto, fill=color_texto, font=fuente_numero)
    # Guarda la imagen con las frases escritas
    imagen_guardada = "salida/CR"+str(index)+".png"
    imagen.save(imagen_guardada)

    # Cierra la imagen
    imagen.close()

    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")
