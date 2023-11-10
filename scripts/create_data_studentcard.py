from PIL import Image, ImageDraw, ImageFont
import generator_data as gn


def create_image(index):
    """
    The `create_image` function takes an index as input and generates an image with personalized
    information, such as name, number, and date, and saves it as a PNG file.
    
    :param index: The `index` parameter is used to specify the index or number of the image being
    created. It is used to generate a unique filename for the image
    """
    imagen_de_fondo = "../dataset\Costa Rica\carnet.png"
    imagen = Image.open(imagen_de_fondo)
    draw = ImageDraw.Draw(imagen)
    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero_con_año()
    fecha = gn.generar_fecha()

    coordenadas_y_texto = [
        ((285, 460), apellido2 + " " + apellido1 + " " +nombre ),
        ((285, 540), numero),
    ]
    fuente = ImageFont.truetype("ARLRDBD.TTF", 36)
    fuente_fecha = ImageFont.truetype("ARLRDBD.TTF",26)
    color_texto = (0, 0, 0)
    for (x, y), texto in coordenadas_y_texto:
        draw.text((x, y), texto, fill=color_texto, font=fuente)

    draw.text((840, 600), fecha, fill=color_texto, font=fuente_fecha)
    imagen_guardada = "../salida/carnet/TEC"+str(index)+".png"
    imagen.save(imagen_guardada)
    imagen.close()

    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")

