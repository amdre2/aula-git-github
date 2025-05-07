import time

bd_filmes = [
    ['interestelar' , 2015],
    ['titanic', 1997],
    ['star wars: episodio 6', 2022]

]

#listar filmes

def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][1]} - {bd[i][0]}')

#cadastro de filmes
def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

while True:
    print('bem bindo ao cadfilme')
    print('1 - cadastrar filme')
    print('2 - alterar filme')
    print('3 - listar filmes')
    print('0 - sair')


    try:
            op = int(input('digite a opção desejada:'))
    except  Exception as e:
        print(f' Error: {e}')
        op= -1

    time.sleep(1)

    if op ==1:
        print(f'----filme cadastrado-----')
        titulo = input('digite o titulo do novo filme: ')
        ano = int(input('digite o ano do novo filme: '))
        bd_filmes = cadastrar_filme(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )

        print(f'--- CADASTRO DE FILMES ---')
    elif op == 2:
        print(f' ---- alterar filme ----')
        listar_filmes(bd=bd_filmes)
        i= int(input('qual filme deseja alterar? '))

        n_titulo = input('digite o novo titulo: ')
        n_ano = int(input(' digite o novo ano: '))

        print('filme alterado')
    elif op == 3:
        listar_filmes(bd=bd_filmes)
    elif op == 0:
        print('saindo do programa...')
        break

    else:
        print('opção inválida! tente novamente!')

    time.sleep(2)
