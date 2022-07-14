nome_cidade = input ('Qual cidade é conhecida como cidade maravilhosa:  ')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print ('Tente de novo!')
    nome_cidade = input ('Qual cidade é conhecida como cidade maravilhosa: ')

print ('Você acertou!')