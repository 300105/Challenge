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

def procurar_palavra_em_txt(txt_file, palavra):
    # Abrir o arquivo TXT
    with open(txt_file, 'r', encoding='utf-8') as file:
        texto = file.read()
        
        # Procurar a palavra no texto do arquivo
        if palavra.lower() in texto.lower():
            print("A palavra '{}' foi encontrada no arquivo TXT.".format(palavra))

def procurar_palavra_em_arquivo(file_path, palavra):
    if file_path.endswith('.pdf'):
        procurar_palavra_em_pdf(file_path, palavra)
    elif file_path.endswith('.txt'):
        procurar_palavra_em_txt(file_path, palavra)
    else:
        print('Formato de arquivo não suportado')

# Exemplo de uso
procurar_palavra_em_arquivo("fichapdf1.pdf", "CPF:")
procurar_palavra_em_arquivo("txt teste.txt", "RG")