import os
restaurantes=[{'nome': 'Tempero Salgado', 'categoria': 'Salgada','ativo':False}, 
              {'nome': 'Tempero Mineiro', 'categoria': 'Mineira','ativo':True},
              {'nome': 'Sushi Nadya', 'categoria': 'Japonesa','ativo':False}
              ]
 
def exibir_nome_do_programa():
    ''' E para exibrir o nome do programa'''
    print ('      𝓣𝓮𝓶𝓹𝓮𝓻𝓸 𝓢𝓮𝓬𝓻𝓮𝓽𝓸\n')

def exibir_opções():
    '''E para exibrir as opçoes'''
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Alternar estado de restaurante')
    print('4- Sair\n')

def Encerrando_programa():
    '''E para encerrar o programa'''
    exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu_principal():
    '''E para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    ''' e para opiçoes invalidas que nao servem pra nada'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''E para exibir o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
  '''Essa funçao e respomsavel para cadastrar um novo restaurante'''
  exibir_subtitulo('Cadastro de novos restaurantes')

nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
dados_do_restaurante ={'nome': nome_do_restaurante,'categoria': categoria, 'ativo':False}
restaurantes.append(dados_do_restaurante)
print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

voltar_ao_menu_principal()

def listar_restaurantes():
    '''A lista e para listar o restaurante'''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Alterna o estado do restaurante'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()

def escolher_opcao():
    '''E para escolher a opçao'''
    try:
        opcao_escolhida= int(input('Escolha uma opção: '))
        print (f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            Encerrando_programa()
        else:
         opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()