lista = []

while True:
    print('Selecione a opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)    
        
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar esse item da lista')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
        
    else:
        print('Por favor, escolha Incluir, Alterar ou Listar.')
        