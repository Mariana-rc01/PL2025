# Máquina de Vending 🍫

## Autor 🌻
Mariana Rocha (A90817)

## Explicação 📋

Este TPC consiste no desenvolvimento de um sistema de simulação de uma **máquina de vending**, que
permite a gestão do stock, a inserção de moedas e a compra de produtos através de input.
O programa faz uso de **expressões regulares** para interpretar os comandos inseridos pelo
utilizador e executar a ação correspondente.

## Funcionalidades

### 1. **Gestão do Stock**

- O programa permite **listar** os produtos disponíveis na máquina, acompanhados com o preço e
quantidade em stock.
- Permite também **adicionar, remover e atualizar** produtos no stock.

### 2. **Inserção de Moedas**

- Os utilizadores podem inserir moedas na máquina utilizando o comando `MOEDA <valor>`.
- O saldo é atualizado e exibido sempre que uma moeda válida for inserida.
- São aceites euros (`E/e`) e cêntimos (`C/c`), por exemplo: `MOEDA 1E, 50C`.

### 3. **Compra de Produtos**
- Através do comando `SELECIONAR <código>`, o utilizador pode escolher um produto.
- O programa verifica se há stock suficiente e se o saldo do utilizador é suficiente para a compra.
- Se a compra for bem sucedida, o stock é atualizado.

### 4. **Troco Automático**
- Ao sair (`SAIR`), a máquina calcula e devolve o troco em moedas válidas.

### 5. **Ajuda e Desliga**
- O comando `HELP` exibe a lista de comandos disponíveis e as suas funcionalidades.
- O comando `SAIR` termina o programa e devolve o saldo restante do utilizador.

## Expressões Regulares (Regex)

Para interpretar os comandos do utilizador, foram utilizadas **expressões regulares** na construção
do analisador léxico (`lexer`).
Cada comando possui uma **expressão regular específica** que permite identificá-lo:

### 1. **`LISTAR`**: `r'LISTAR\b'`

O `\b` assegura que a palavra "LISTAR" é reconhecida apenas se encontrar isolada.

### 2. **`MOEDA`**: `r'MOEDA\s+(\d+[eEcC]\s*,\s+)*(\d+[eEcC])\s*.?'`

Reconhece a sequências de valores numéricos seguidos de `E/e` (euros) ou `C/c` (cêntimos).
Suporta múltiplos valores separados por vírgula e espaço (`, `).

### 3. **`SELECIONAR`**: `r'SELECIONAR\s+\w+'`

Identifica um código alfanumérico associado ao produto que irá comprar.

### 4. **`REMOVE`**: `r'REMOVE\s+\w+'`

Captura a remoção de um produto específico através do código.

### 5. **`HELP`**: `r'HELP\b'`

Exibe a ajuda do programa.

### 6. **`SAIR`**: `r'SAIR\b'`

Encerra o programa.

## Como Usar 🛠️

### Execução
Abra o terminal e execute:

```bash
python vending_machine.py stock.json
```

O programa aguardará comandos do utilizador, como `LISTAR`, `MOEDA 1E, 50C`, `SELECIONAR A1`, `SAIR`, etc.

## Exemplos e Resultados 📊

### Exemplo de Interação
```
maq: Olá! Estou disponível para atender o seu pedido.
>> LISTAR
cod | nome | quantidade | preço
----------------------------------
A1  | Água | 10         | 1.00
B2  | Snack| 5          | 1.50

>> MOEDA 2E, 50C.
maq: Saldo = 2e 50c

>> SELECIONAR A1
maq: Pode retirar o produto "Água".
maq: Saldo = 1e 50c

>> SAIR
maq: Troco a ser devolvido:
1 moeda de 1 euro.
1 moeda de 50 cêntimos.
maq: Até à próxima.
```