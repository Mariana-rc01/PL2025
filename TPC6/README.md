# Avaliador de Expressões Aritméticas 🤖

## Autor 🌻
Mariana Rocha (A90817)

## Explicação 📝

Este TPC tem como objetivo implementar um parser **LL(1) recursivo descendente** para avaliar
expressões matemáticas simples, garantindo que a ordem das operações está corretamente implementada.
O programa interpreta e avalia expressões aritméticas que envolvem números inteiros e as operações
**adição (+)**, **subtração (-)**, **multiplicação (*)** e **divisão (/)**, respeitando a prioridade dos operadores, bem como parênteses.

## Funcionalidades:

### 1. **Analisador Léxico - Reconhecimento de Tokens**
   - Identifica números inteiros e operadores com o uso de expressões regulares.

   - Tokens suportados: NUM, ADD (+), SUB (-), MUL (*), DIV (/), PO (, PC ).

### 2. **Analisador Sintático**
   - Implementa a gramática LL(1) com funções recursivas para cada símbolo não-terminal.

   - Garante a prioridade correta (multiplicação/divisão antes de adição/subtração) e associatividade à esquerda.

   - Trata de parênteses para alterar a ordem de avaliação.

### 3. **Avaliação Semântica**
   - Aplica as regras de prioridade matemática e calcula o valor final da expressão corretamente.
   - Em caso de erro sintático, exibe uma mensagem indicando a ocorrência do erro.

## Raciocínio 🧠

O sistema é composto por dois ficheiros principais:

- <a href="exp_lex.py">exp_lex.py</a> (Analisador Léxico): Responsável por reconhecer os tokens.
- <a href="exp_sin.py">exp_sin.py</a> (Analisador Sintático): Implementa a gramática e realiza a avaliação da expressão.

### 1. **Analisador Léxico (`exp_lex.py`)**

O analisador léxico utiliza a biblioteca **PLY (Python Lex)** para reconhecer os tokens.

#### Tokens:
- `NUM`: Representa os números inteiros;
- `ADD`: Representa o operador `+`;
- `SUB`: Representa o operador `-`;
- `MUL`: Representa o operador `*`;
- `DIV`: Representa o operador `/`;
- `PO` : Representa o operador `(`;
- `PC` : Representa o operador `)`.

#### Expressões Regulares:
- `t_ADD = r'\+'`
- `t_SUB = r'\-'`
- `t_MUL = r'\*'`
- `t_DIV = r'\/'`
- `t_PO  = r'\('`
- `t_PC  = r'\)'`
- `t_DIV = r'\)'`
- `t_NUM = r'\d+'`  (Reconhece sequências de dígitos e converte-as para inteiros.)

Se um caractere inválido for encontrado, o lexer emite uma mensagem de erro e ignora o caractere.

### 2. **Analisador Sintático (`exp_sin.py`)**

Gramática:

```
T = {num, '+','-','*','/', '(', ')'}
S = ExpI
N = {Exp1, Exp11, Exp2, Exp22, Exp3}
P = {
   Exp1  -> Exp2 Exp11
   Exp11 -> ADD Exp1
   Exp11 -> SUB Exp1
   Exp11 -> ε
   Exp2  -> Exp3 Exp22
   Exp22 -> MUL Exp2
   Exp22 -> DIV Exp2
   Exp22 -> ε
   Exp3  -> PO Exp1 PC
   Exp3  -> NUM
}
```

A estrutura garante a correta prioridade das operações:
- Os parênteses têm prioridade.
- Multiplicação e divisão têm maior prioridade que adição e subtração.
- As expressões são processadas de forma recursiva, garantindo a correta avaliação dos termos.

## Como Usar 🛠️

Para executar o analisador, basta correr os seguintes comandos:

```bash
python3 exp_sin.py
```

## Exemplos e Resultados 📊

```
$ python3 exp_sin.py
2+3
Result: 5

2. +3
Invalid character:  .
Result: 5

67-(2+3*4 )
Result: 53

(9-2)*(13-4)
Result: 63

(9-2)*(13-4
Sintaxe error: Expected PC, but found EOF

2+3*2
Result: 8

2*7-5*3
Result: -1

6/2+5-1+2*10
Result: 27.0

1-1-1-1
Result: -2
```
