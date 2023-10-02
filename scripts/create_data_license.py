from PIL import Image, ImageDraw, ImageFont
import scripts.generator_data as gn


def create_image(index):
    # Ruta de la imagen de fondo en la que deseas escribir
    imagen_de_fondo = "dataset\Costa Rica\licencia.png"

    # Abre la imagen de fondo
    imagen = Image.open(imagen_de_fondo)

    # Crea un objeto ImageDraw para dibujar en la imagen
    draw = ImageDraw.Draw(imagen)

    nombre = gn.generar_nombre()
    apellido1 = gn.generar_apellido1()
    apellido2 = gn.generar_apellido2()
    numero = gn.generar_numero_con_tipo()
    tipo = gn.generar_texto_tipo()
    fecha = gn.generar_fechas()
    codigo1, codigo2 = gn.generar_codigos()
    sangre = gn.generar_tipo_sangre()
    # Coordenadas y texto que deseas escribir en la imagen
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


    # Fuente y tamaño del texto
    fuente = ImageFont.truetype("ARLRDBD.TTF", 36)
    fuente_pequeña = ImageFont.truetype("ARLRDBD.TTF", 30)
    # Itera sobre las coordenadas y el texto y escribe cada frase en la imagen
    for (x, y), texto in coordenadas_rojo:
        draw.text((x, y), texto, fill=(200, 50, 30), font=fuente)

    for (x, y), texto in coordenadas_negro:
        draw.text((x, y), texto, fill=(0, 0, 0), font=fuente)
    
    for (x, y), texto in coordenadas_pequeño:
        draw.text((x, y), texto, fill=(0, 0, 0), font=fuente_pequeña)
    #draw.text((840, 600), fecha, fill=color_texto, font=fuente_fecha)
    # Guarda la imagen con las frases escritas
    imagen_guardada = "salida/licencia/LIC"+str(index)+".png"
    imagen.save(imagen_guardada)

    # Cierra la imagen
    imagen.close()

    print(f"La imagen con frases ha sido guardada como '{imagen_guardada}'.")

