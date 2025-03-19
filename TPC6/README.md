# Avaliador de Expressões Aritméticas 🤖

## Autor 🌻
Mariana Rocha (A90817)

## Explicação 📝

Este TPC tem como objetivo desenvolver um **analisador sintático recursivo descendente** para avaliar
expressões matemáticas simples, garantindo que a ordem das operações está corretamente implementada.
O programa interpreta e avalia expressões aritméticas que envolvem números inteiros e as operações
**adição (+)**, **subtração (-)**, **multiplicação (*)** e **divisão (/)**, respeitando a prioridade dos operadores.

## Funcionalidades:

### 1. **Analisador Léxico - Reconhecimento de Tokens**
   - O lexer identifica os diferentes tokens da expressão, como números inteiros e operadores aritméticos.
   - Utiliza **expressões regulares** para reconhecer os tokens e converter os números para valores inteiros.

### 2. **Analisador Sintático**
   - O parser aplica um **analisador sintático recursivo descendente**, construindo a árvore de parse
   para avaliar corretamente a expressão.
   - A gramática utilizada assegura a correta prioridade das operações: multiplicação e divisão são
   processadas antes da adição e subtração.

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
- `DIV`: Representa o operador `/`.

#### Expressões Regulares:
- `t_ADD = r'\+'`
- `t_SUB = r'\-'`
- `t_MUL = r'\*'`
- `t_DIV = r'\/'`
- `t_NUM = r'\d+'`  (Reconhece sequências de dígitos e converte-as para inteiros.)

Se um caractere inválido for encontrado, o lexer emite uma mensagem de erro e ignora o caractere.

### 2. **Analisador Sintático (`exp_sin.py`)**

O analisador sintático utiliza a biblioteca **PLY (Python Yacc)** para reconhecer tokens.

Gramática:

```
T = {num, '+','-','*','/'}
S = ExpI
N = {ExpI, ExpS, Termo, Num}
P = {
    ExpI  -> ExpI ADD ExpS
          | ExpI SUB ExpS
          | ExpS
    ExpS  -> ExpS MUL Termo
          | ExpS DIV Termo
          | Termo
    Termo -> NUM
}
```

A estrutura garante a correta prioridade das operações:
- Multiplicação e divisão têm maior prioridade que adição e subtração.
- As expressões são processadas de forma recursiva, garantindo a correta avaliação dos termos.

### 3. **Implementação da Avaliação**

No parser, cada regra de produção é traduzida numa função que calcula o resultado:

```python
# Soma
p[0] = p[1] + p[3]

# Subtração
p[0] = p[1] - p[3]

# Multiplicação
p[0] = p[1] * p[3]

# Divisão
p[0] = p[1] / p[3]
```

Se uma expressão for válida, o resultado é impresso. Caso contrário, é exibida uma mensagem de erro sintático.

## Como Usar 🛠️

Para executar o analisador, basta correr os seguintes comandos:

```bash
python3 exp_sin.py
```

## Exemplos e Resultados 📊

Para a expressão `5 + 3 * 2`, a avaliação ocorre da seguinte forma:

1. Multiplica-se `3 * 2 = 6`
2. Soma-se `5 + 6 = 11`

Para `2 * 7 - 5 * 3`:

1. Multiplica-se `2 * 7 = 14`
2. Multiplica-se `5 * 3 = 15`
3. Subtrai-se `14 - 15 = -1`

Outro exemplo:

```
$ python3 exp_sin.py

2 + 3 * 2
Expression value:  8
Valid quote:  2 + 3 * 2

2. + 3
Caracter inválido:  .
Expression value:  5
Valid quote:  2. + 3

2 ++3
Erro sintático LexToken(ADD,'+',1,3)
Expression value:  3
Invalid sentence. Fix it and try again

2*7 - 5 *   3
Expression value:  -1
Valid quote:  2*7 - 5 *   3

6/2 + 5 - 1 + 2*10
Expression value:  27.0
Valid quote:  6/2 + 5 - 1 + 2*10
```
