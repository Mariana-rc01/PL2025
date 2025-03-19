import ply.lex as lex
import sys
import json
from datetime import datetime

tokens = ("LISTAR", "MOEDA", "SELECIONAR", "SAIR", "ADD", "REMOVE", "UPDATE", "HELP")

def t_LISTAR(t):
    r'LISTAR\b'
    return t

def t_MOEDA(t):
    r'MOEDA\s+(\d+[eEcC]\s*,\s+)*(\d+[eEcC])\s*.?'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+\w+'
    return t

def t_SAIR(t):
    r'SAIR\b'
    return t

def t_ADD(t):
    r'ADD\b'
    return t

def t_REMOVE(t):
    r'REMOVE\s+\w+'
    return t

def t_UPDATE(t):
    r'UPDATE\b'
    return t

def t_HELP(t):
    r'HELP\b'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

balance = 0
stock = []

def load_stock(fname):
    try:
        with open(fname, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_stock(stock, fname):
    with open(fname, 'w') as f:
        json.dump(stock, f, indent=4)

def add_produto(stock):
    codigo = input("maq: Qual o código do produto que deseja adicionar?: ")
    if codigo in stock:
        quantity = int(input("maq: Que quantidade gostaria de adicionar?: "))
        stock[codigo]["quantidade"] += quantity
        print("maq: Stock atualizado com sucesso.")
    else:
        name = input("maq: Qual o nome do produto que deseja adicionar?: ")
        quantity = int(input("maq: Que quantidade deseja adicionar?: "))
        price = float(input("maq: Qual o preço do produto?: "))
        stock[codigo] = {
            "nome_produto": name,
            "quantidade": quantity,
            "preco": price
        }
        print("maq: Novo produto adicionado com sucesso.")

def remover_produto(stock, codigo):
    if codigo in stock:
        del stock[codigo]
        print("maq: Produto removido com sucesso.")
    else:
        print("maq: Produto não encontrado.")

def update(stock):
    codigo = input("maq: Qual o código do produto que deseja alterar?: ")
    if codigo in stock:
        name = input("maq: Qual o novo nome do produto?: ")
        stock[codigo]["nome_produto"] = name
        quantity = int(input("maq: Que quantidade existe de momento?: "))
        stock[codigo]["quantidade"] = quantity
        price = float(input("maq: Qual o novo preço do produto?: "))
        stock[codigo]["preco"] = price
        print("maq: Produto atualizado com sucesso.")
    else:
        print("maq: Produto não encontrado.")

def help():
    print("maq: Comandos disponíveis:")
    print("- LISTAR: Lista todos os produtos no stock.")
    print("- MOEDA <valor>: Adiciona moedas ao saldo da máquina. Exemplo: MOEDA 1E, 50C")
    print("- SELECIONAR <código>: Seleciona um produto para compra. Exemplo: SELECIONAR ABC123")
    print("- ADD: Adiciona um novo produto ao stock.")
    print("- REMOVE <código>: Remove um produto do estoque. Exemplo: REMOVE ABC123")
    print("- UPDATE: Atualiza as informações de um produto no estoque.")
    print("- HELP: Mostra esta mensagem de ajuda.")
    print("- SAIR: Sai da aplicação.")

def listar_stock(stock):
    header = "cod | nome | quantidade |  preço"
    print(header)
    print("-" * len(header))

    for codigo, produto in stock.items():
        nome_produto = produto['nome_produto']
        quantidade = produto['quantidade']
        preco = produto['preco']
        linha = f"{codigo} | {nome_produto} | {quantidade} | {preco:.2f}"
        print(linha)

def comprar_produto(stock, balance, codigo):
    if codigo in stock and stock[codigo]["quantidade"] != 0:
        preco = round(stock[codigo]["preco"] * 100,2)
        if balance >= preco:
            balance -= preco
            stock[codigo]["quantidade"] -= 1
            print(f"maq: Pode retirar o produto dispensado \"{stock[codigo]['nome_produto']}\".")
            balance_euros = balance // 100
            balance_centimos = balance % 100
            print(f"maq: balance = {balance_euros}e {balance_centimos}c .")
            save_stock(stock, "stock.json")
            return stock, balance
        else:
            print(f"maq: Saldo insuficiente para satisfazer o seu pedido.")
            balance_euros = balance // 100
            balance_centimos = balance % 100
            preco_euros = preco // 100
            preco_centimos = round(preco % 100,3)
            print(f"maq: Saldo = {balance_euros}e {balance_centimos}c; Pedido = {preco_euros}e {preco_centimos}c")
    elif not (codigo in stock):
        print("maq: Produto não encontrado.")
    elif stock[codigo]["quantidade"] == 0:
        print("maq: Stock Insuficiente.")
    return stock, balance

def token_parser(stock, balance, t):
    if t.type == 'LISTAR':
        listar_stock(stock)
    elif t.type == 'MOEDA':
        moedas = t.value.split()[1:]
        for moeda in moedas:

            if moeda.endswith('E') or moeda.endswith('e'):
                coin_value = moeda[:-1]
                if coin_value.isdigit():
                    valor = int(coin_value) * 100
                    balance += valor
                else:
                    print(f"maq: Moeda inválida: {moeda}")
            elif moeda.endswith('E,') or moeda.endswith('e,') or moeda.endswith('e.') or moeda.endswith('E.'):
                coin_value = moeda[:-2]
                if coin_value.isdigit():
                    valor = int(coin_value) * 100
                    balance += valor
                else:
                    print(f"maq: Moeda inválida: {moeda}")
            elif moeda.endswith('C') or moeda.endswith('c'):
                coin_value = moeda[:-1]
                if coin_value.isdigit():
                    valor = int(coin_value)
                    balance += valor
                else:
                    print(f"maq: Moeda inválida: {moeda}")
            elif moeda.endswith('C,') or moeda.endswith('c,') or moeda.endswith('c.') or moeda.endswith('C.'):
                coin_value = moeda[:-2]
                if coin_value.isdigit():
                    valor = int(coin_value)
                    balance += valor
                else:
                    print(f"maq: Moeda inválida: {moeda}")
            elif moeda.endswith('.'):
                break
            else:
                print(f"maq: Moeda inválida: {moeda}")
        print(f"maq: Saldo = {balance // 100}e {balance % 100}c")
    elif t.type == 'SELECIONAR':
        code = t.value.split()[1]
        stock, balance = comprar_produto(stock, balance, code)
    elif t.type == 'ADD':
        add_produto(stock)
        print("maq: Stock atualizado: ")
        listar_stock(stock)
    elif t.type == 'REMOVE':
        code = t.value.split()[1]
        remover_produto(stock, code)
        print("maq: Stock atualizado: ")
        listar_stock(stock)
    elif t.type == 'UPDATE':
        listar_stock(stock)
        update(stock)
        print("maq: Produto atualizado: ")
        listar_stock(stock)
    elif t.type == 'HELP':
        help()
    return stock, balance

def calcular_troco(balance):
    troco = []
    moedas = [100, 50, 20, 10, 5, 2, 1]
    for moeda in moedas:
        quantidade = balance // moeda
        if quantidade > 0:
            troco.append((moeda, quantidade))
            balance -= quantidade * moeda
    return troco

def mostrar_troco(troco):
    print("maq: Troco a ser devolvido:")
    for moeda, quantidade in troco:
        if quantidade > 1: moedaS = "moedas"
        else: moedaS = "moeda"
        if moeda >= 100:
            if moeda == 100: euroS = "euro"
            else: euroS = "euros"
            print(f"{quantidade} {moedaS} de {moeda // 100} {euroS}.")
        else:
            if moeda == 1: cS = "cêntimo"
            else: cS = "cêntimos"
            print(f"{quantidade} {moedaS} de {moeda} {cS}.")

def input_parser(stock, balance):
    data_atual = datetime.now()
    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Olá! Estou disponível para atender o seu pedido.")

    while True:
        try:
            linha = input(">> ").strip().upper()
            if not linha:
                continue
            lexer.input(linha)
            while True:
                t = lexer.token()
                if not t:
                    break
                stock, balance = token_parser(stock, balance, t)
                if t.type == 'SAIR':
                    troco = calcular_troco(balance)
                    mostrar_troco(troco)
                    print("maq: Até à próxima.")
                    return stock, balance
        except KeyboardInterrupt:
            print("\nmaq: Operação interrompida. Até à próxima.")
            sys.exit(0)

def main():
    stock = load_stock("stock.json")
    balance = 0
    stock, balance = input_parser(stock, balance)
    save_stock(stock, "stock.json")

if __name__ == "__main__":
    main()