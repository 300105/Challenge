from PyPDF2 import PdfReader

def procurar_palavra_em_pdf(pdf_file, palavra):
    # Abrir o arquivo PDF
    with open(pdf_file, "rb") as file:
        reader = PdfReader(file)

        # Percorrer todas as páginas do PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]

            # Extrair texto da página
            texto = page.extract_text()

            # Procurar a palavra no texto da página
            if palavra.lower() in texto.lower():
                print("A palavra '{}' foi encontrada na página {} do PDF.".format(palavra, page_num + 1))

# Exemplo de uso
pdf_file = "fichapdf1.pdf"
palavra = "CPF:"
procurar_palavra_em_pdf(pdf_file, palavra)