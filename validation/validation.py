from processing.open_image import *
from ocr.get_text import *
from processing.get_doc_type import *
from validation.data_compare import *

def processing(path, typeDoc):
    path_enhanced_image = "processed_photos/enhanced_image.png"
   
    image = ImageEnhancer(path)
    image.process(typeDoc)
    image.display_image()
    
    original_image = ImageEnhancer(path)
    original_image.load_image()
    original_image.resize()
    original_image.display_concatenated_image(image.image)
    return path_enhanced_image


def validate(path):
    value = False
    typeDoc = categorize_local(path)
    path_enhanced_image = processing(path, typeDoc)
    if typeDoc  == "cedula":
        data = get_text_img_identity(path_enhanced_image)
        value = identitycard_compare(data)


    elif typeDoc == "carnet":
        data = get_text_img_stundent(path_enhanced_image)
        value = studentcard_compare(data)
    elif typeDoc == "licencia":
        data = get_text_img_license(path_enhanced_image)
        value = license_compare(data)
       
    else:
        print("El documento no es del tipo adecuado")

    if value == True:
        print("Documento Valido")
    else:
        print("Documento Invalido")