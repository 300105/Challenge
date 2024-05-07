def procurar_palavra_em_txt(txt_file, palavra):
    # Abrir o arquivo TXT
    with open(txt_file, 'r', encoding='utf-8') as file:
        texto = file.read()
        
        # Procurar a palavra no texto do arquivo
        if palavra.lower() in texto.lower():
            print("A palavra '{}' foi encontrada no arquivo TXT.".format(palavra))

# Exemplo de uso
txt_file = "documento.txt"
palavra = "RG"
procurar_palavra_em_txt(txt_file,palavra)