import os
restaurantes=[{'nome':'sabores do mundo','categoria': 'salgada','ativo':False},
              {'nome': 'sushi do limao', 'categoria': 'peixe','ativo':False},
              {'nome':'churrasco da Mafia azul','categoria':'carne','ativo':False}
             ]
def exibir_nome_do_programa():
    print ('  sabores do mundo\n')

def exibir_opções():
   print('1- Cadastrar restaurante')
   print('2- Listar restaurante')
   print('3- Ativar restaurante')
   print('4- Sair\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrando novo restaurante ')
    nome_do_restaurante=input('Digite o nome do restaurante ')
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso! ')
    voltar_ao_menu_prinipal()

def listar_restaurante():
    exibir_subtitulo('listando restaurante ')
    for restaurante in restaurantes:
        nome_restaurante= restaurante['nome']
        print(f' {nome_restaurante}')

def Encerrando_programa():
   exibir_subtitulo ('Encerrando o programa')

def voltar_ao_menu_prinipal():  
 input("\nDigite uma tecla para voltar ao menu prinçipal: ")
 main()


def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_prinipal()
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

  


def escolher_opcao():
    try:
        opcao_escolhida= int(input('Escolha uma opção: '))
        print (f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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