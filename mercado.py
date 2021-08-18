from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('====================================')
    print('=========== Bem vindo(a) ===========')
    print('===========      Shop    ===========')
    print('====================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opção: int = int(input())

    if opção == 1:
        cadastrar_produto()
    elif opção == 2:
        listar_produto()
    elif opção == 3:
        comprar_produto()
    elif opção == 4:
        visualizar_carrinho()
    elif opção == 5:
        fechar_pedido()
    elif opção == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida!')
        sleep(2)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('--------------------')
    else:
        print('Ainda não existem produtos cadastrados.')
        sleep(2)
    menu()

def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
        return p

if __name__ == '__main__':
    main()