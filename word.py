from docx import Document

def procurar_palavra_em_docx(docx_file, palavra):
    # Abrir o arquivo docx
    doc = Document(docx_file)
    
    # Iterar sobre todos os parágrafos do documento
    for para in doc.paragraphs:
        # Verificar se a palavra está no texto do parágrafo
        if palavra.lower() in para.text.lower():
            print("A palavra '{}' foi encontrada no documento Word.".format(palavra))
            return

    print("A palavra '{}' não foi encontrada no documento Word.".format(palavra))

# Exemplo de uso
docx_file = "word 2.docx"
palavra = "ENDEREÇO"
procurar_palavra_em_docx(docx_file,palavra)