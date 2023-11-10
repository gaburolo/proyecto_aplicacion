from PIL import Image, ImageDraw, ImageFont
import generator_data as gn


def create_image(index):
     """
    The `create_image` function takes an index as input and generates an image with personalized
    information, such as name, number, and date, and saves it as a PNG file.
    
    :param index: The `index` parameter is used to specify the index or number of the image being
    created. It is used to generate a unique filename for the image
    """
    imagen_de_fondo = "../dataset\Costa Rica\licencia.png"
    imagen = Image.open(imagen_de_fondo)
    draw = ImageDraw.Draw(imagen)
    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero_con_tipo()
    tipo = gn.generar_texto_tipo()
    fecha = gn.generar_fechas()
    codigo1, codigo2 = gn.generar_codigos()
    sangre = gn.generar_tipo_sangre()

    coordenadas_rojo = [
        
        ((408, 155), numero),
        ((970, 233), tipo),
        ((520, 310), fecha["Vencimiento"]),
        ((670, 365), sangre)
        
    ]
    coordenadas_negro = [
        ((29, 420), apellido2.upper()+ " " + apellido1.upper() + " " + nombre.upper()),
        ((520, 207), fecha["Expediente"]),
        ((520, 258), fecha["Nacimiento"]),
    ]
    coordenadas_pequeño = [
        ((875, 560), codigo1),
        ((420, 605), codigo2)
    ]

    fuente = ImageFont.truetype("ARLRDBD.TTF", 36)
    fuente_pequeña = ImageFont.truetype("ARLRDBD.TTF", 30)

    for (x, y), texto in coordenadas_rojo:
        draw.text((x, y), texto, fill=(200, 50, 30), font=fuente)

    for (x, y), texto in coordenadas_negro:
        draw.text((x, y), texto, fill=(0, 0, 0), font=fuente)
    
    for (x, y), texto in coordenadas_pequeño:
        draw.text((x, y), texto, fill=(0, 0, 0), font=fuente_pequeña)

    imagen_guardada = "../salida/licencia/LIC"+str(index)+".png"
    imagen.save(imagen_guardada)

    imagen.close()

    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")

