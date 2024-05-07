import cv2
import pytesseract

def procurar_palavra_em_imagem(imagem, palavra):
    # Carregar a imagem
    imagem = cv2.imread(imagem)
    
    # Usar o Tesseract para fazer a OCR (Reconhecimento Óptico de Caracteres)
    texto = pytesseract.image_to_string(imagem)
    
    # Procurar a palavra no texto extraído
    if palavra.lower() in texto.lower():
        print("A palavra '{}' foi encontrada na imagem.".format(palavra))
    else:
        print("A palavra '{}' não foi encontrada na imagem.".format(palavra))

# Exemplo de uso
imagem = "fotoRG.png"
palavra = "filiação"
procurar_palavra_em_imagem(imagem,palavra)