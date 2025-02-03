
def adicionar_contato(contatos, nome, telefone, email, favorito=False):
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contato['favorito'] = favorito
    contatos.append(contato)
    print(f'Contato {nome} adicionado com sucesso.')
    return

def visualizar_contatos(contatos, visualizar_favoritos: bool=None):
    msg_favoritos = '\nContatos favoritos:\n'
    msg_todos_contatos = "\nContatos:\n"

    for index,contato in enumerate(contatos):
        if contato['favorito']:
            msg_favoritos += f"{index+1} - {contato['nome']}\n"  
        
        msg_todos_contatos += f"{index+1} -  {contato['nome']}\n"

    msg = msg_favoritos if visualizar_favoritos else msg_todos_contatos
    print(msg)
    return

def editar_um_contato(contatos, index, nome=None, email=None):
    contato = contatos[index-1]
    if nome:
        contato['nome'] = nome
    if email:
        contato['email'] = email
    print(contato)
    return

def marcar_desmarcar_um_contato_como_favorito(contatos, index):

    contato_marcado = contatos[index-1].get('favorito')

    deseja_marcar_ou_desmarcar = "Marcar" if contato_marcado == False else "Desmarcar"

    print(f"Voce deseja {deseja_marcar_ou_desmarcar} o contato {contatos[index-1].get('nome')} como favorito?")

    deseja_marcar_ou_desmarcar = input("Digite 'sim' para marcar ou 'nao' para desmarcar: ")

    if deseja_marcar_ou_desmarcar == "sim":
        contatos[index-1]['favorito'] = True if contato_marcado == False else False

    return

def deletar_contatos(contatos, index):
    del contatos[index-1]
    print(f'Contato {contatos[index-1].get("nome")} deletado com sucesso.')
    return

contatos = []

while True:
    print('1 - Adicionar Contato')
    print('2 - visualizar a lista de contatos cadastrados')
    print('3 - Editar um contato')
    print('4 - marcar/desmarcar um contato como favorito')
    print('5 - Listar Contatos Favoritos') 
    print('6 - Deletar Contato')
    print('7 - Sair')
    try:
        opcao = int(input('Digite a opção: '))
        
        if opcao == 1: 
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            favoritar = input('Deseja marcar o contato como favorito? (sim): ')
            favorito = True if favoritar == 'sim' else False
            adicionar_contato(contatos, nome, telefone, email, favorito) 
        elif opcao == 2:    
            visualizar_contatos(contatos)
        elif opcao == 3:   
            index = int(input('Digite o numero do contato: '))
            nome = input('Digite o nome do contato para alterar: ')
            email = input('Digite o email do contato para alterar: ')
            editar_um_contato(contatos, index, nome, email)
        elif opcao == 4:        
            index = int(input('Digite o numero do contato que voce deseja marcar ou desmarcar como favorito: '))
            marcar_desmarcar_um_contato_como_favorito(contatos, index)
        elif opcao == 5:        
            visualizar_contatos(contatos, True)
        elif opcao == 6:
            index = int(input('Digite o numero do contato que voce deseja deletar: '))
            deletar_contatos(contatos, index)
        elif opcao == 7:
            print('Saindo do programa...')
            break
    except ValueError:
        print('Opcao invalida. Digite um numero inteiro.')
    except Exception as e:
        print(f'Opcao invalida {e}') 
    else:
        print(f'Success')
    finally:
        print('\nfinalizando programa...')