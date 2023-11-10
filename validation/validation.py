from processing.open_image import *
from ocr.get_text import *
from processing.get_doc_type import *
from validation.data_compare import *

def processing(path, typeDoc):
    """
    The function "processing" takes a path and a type of document as input, enhances the image at the
    given path based on the document type, and returns the path of the enhanced image.
    
    :param path: The path parameter is the file path of the image that you want to process. It should be
    a string representing the file path, for example, "photos/image.png"
    :param typeDoc: The type of document to be processed. It could be "passport", "driver's license",
    "ID card", etc
    :return: the path to the enhanced image.
    """
    path_enhanced_image = "processed_photos/enhanced_image.png"
   
    image = ImageEnhancer(path)
    image.process(typeDoc)
    return path_enhanced_image


def validate(path_enhanced_image, typeDoc):
    """
    The function `validate` takes in the path of an enhanced image and the type of document, and returns
    the extracted data from the image and a boolean value indicating whether the document is valid or
    not.
    
    :param path_enhanced_image: The path to the enhanced image file of the document
    :param typeDoc: The parameter "typeDoc" is a string that represents the type of document being
    validated. It can have one of the following values: "cedula", "carnet", or "licencia"
    :return: two values: "data" and "value".
    """
    value = False
    if typeDoc  == "cedula":
        data = get_text_img_identity(path_enhanced_image)
        value = identitycard_compare(data)
        return data, value
    elif typeDoc == "carnet":
        data = get_text_img_stundent(path_enhanced_image)
        value = studentcard_compare(data)
        return data, value
    elif typeDoc == "licencia":
        data = get_text_img_license(path_enhanced_image)
        value = license_compare(data)
        return data, value
    else:
        print("El documento no es del tipo adecuado")
        return None, None
    if value == True:
        print("Documento Valido")
    else:
        print("Documento Invalido")