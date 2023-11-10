from PIL import Image, ImageDraw, ImageFont
import generator_data as gn


def create_image(index):
     """
    The `create_image` function takes an index as input and generates an image with personalized
    information, such as name, number, and date, and saves it as a PNG file.
    
    :param index: The `index` parameter is used to specify the index or number of the image being
    created. It is used to generate a unique filename for the image
    """
    imagen_de_fondo = "..\dataset\Costa Rica\original.jpg"
    imagen = Image.open(imagen_de_fondo)

    draw = ImageDraw.Draw(imagen)

    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero()

    coordenadas_y_texto = [
        ((447, 640), nombre),
        ((447, 683), apellido1),
        ((447, 724), apellido2),
    ]

    coordenadas_firma = [
        ((340, 510), nombre+ " " + apellido1 + " " + apellido2),
    ]
    coordenadas_numero = [
        ((458, 188), numero),
    ]

    fuente = ImageFont.truetype("arialbd.ttf", 30)
    fuente_firma = ImageFont.truetype("LHANDW.TTF", 36)
    fuente_numero = ImageFont.truetype("arialbd.ttf", 36)

    color_texto = (0, 0, 0)
    for (x, y), texto in coordenadas_y_texto:
        draw.text((x, y), texto, fill=color_texto, font=fuente)


    for (x, y), texto in coordenadas_firma:
        draw.text((x, y), texto, fill=color_texto, font=fuente_firma)
    for (x, y), texto in coordenadas_numero:
        draw.text((x, y), texto, fill=color_texto, font=fuente_numero)
    imagen_guardada = "../salida/cedula/CR"+str(index)+".png"
    imagen.save(imagen_guardada)

    imagen.close()
    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")
