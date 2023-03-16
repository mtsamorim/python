# Definindo a string a ser invertida
string = "Olá, mundo!"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Obtendo o tamanho da string
tamanho_string = len(string)

# Loop para trocar a posição dos caracteres
for i in range(tamanho_string // 2):
    # Trocando os caracteres de posição
    lista_caracteres[i], lista_caracteres[tamanho_string - 1 - i] = lista_caracteres[tamanho_string - 1 - i], lista_caracteres[i]

# Convertendo a lista de volta para uma string
string_invertida = "".join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)
