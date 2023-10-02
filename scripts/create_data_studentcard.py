from PIL import Image, ImageDraw, ImageFont
import scripts.generator_data as gn


def create_image(index):
    # Ruta de la imagen de fondo en la que deseas escribir
    imagen_de_fondo = "dataset\Costa Rica\carnet.png"

    # Abre la imagen de fondo
    imagen = Image.open(imagen_de_fondo)

    # Crea un objeto ImageDraw para dibujar en la imagen
    draw = ImageDraw.Draw(imagen)

    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero_con_año()
    fecha = gn.generar_fecha()
    # Coordenadas y texto que deseas escribir en la imagen
    coordenadas_y_texto = [
        ((285, 460), apellido2 + " " + apellido1 + " " +nombre ),
        ((285, 540), numero),
    ]


    # Fuente y tamaño del texto
    fuente = ImageFont.truetype("ARLRDBD.TTF", 36)
    fuente_fecha = ImageFont.truetype("ARLRDBD.TTF",26)

    # Color del texto (en este caso, blanco)
    color_texto = (0, 0, 0)
    


    # Itera sobre las coordenadas y el texto y escribe cada frase en la imagen
    for (x, y), texto in coordenadas_y_texto:
        draw.text((x, y), texto, fill=color_texto, font=fuente)

    draw.text((840, 600), fecha, fill=color_texto, font=fuente_fecha)
    # Guarda la imagen con las frases escritas
    imagen_guardada = "salida/carnet/TEC"+str(index)+".png"
    imagen.save(imagen_guardada)

    # Cierra la imagen
    imagen.close()

    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")

