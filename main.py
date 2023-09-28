from processing.open_image import *
from ocr.get_text3 import *
from processing.get_doc_type import *
from data_compare import *
if __name__ == "__main__":
    #path = "photo/image.jpeg"
    path = "photo/carnet.jpeg"
    path_enhanced_image = "processed_photos/enhanced_image.png"
    image = ImageEnhancer(path)
    image.process()
    image.display_image()

    original_image = ImageEnhancer(path)
    original_image.load_image()
    original_image.resize()
    original_image.display_concatenated_image(image.image)
    value = False
    typeDoc = categorizar_local(path_enhanced_image)
    if typeDoc  == "cedula":
        data = get_text_img(path_enhanced_image)
        value = identitycard_compare(data)


    elif typeDoc == "carnet":
        data = get_text_img_stundent(path_enhanced_image)
        value = studentcard_compare(data)
    elif typeDoc == "licencia":
        print("es un licencia")
    else:
        print("El documento no es del tipo adecuado")

    if value == True:
        print("Documento Valido")
    else:
        print("Documento Invalido")
    