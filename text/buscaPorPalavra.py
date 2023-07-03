print()




def buscar_palavra(texto, palavra):
    palavras = texto.split()
    encontrada = False
    
    for p in palavras:
        if p.lower() == palavra.lower():
            encontrada = True
            break
    
    return encontrada

# Exemplo de uso
texto = ("The standard Lorem Ipsum passage, used since the 1500s exemplo"
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"
"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
"nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
"deserunt mollit anim id est laborum.")
# texto = "Este é um exemplo de texto para busca de palavra."
palavra_desejada = input("Digite a palavra desejada:\n")

if buscar_palavra(texto, palavra_desejada):
    print("\nA palavra foi encontrada no texto.")
    print("\nA palavra desejada é ",palavra_desejada,".\n")
else:
    print("\nA palavra não foi encontrada no texto.")
