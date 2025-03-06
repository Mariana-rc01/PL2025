# Analisador Léxico 🔍

## Autor 🌻
Mariana Rocha (A90817)

## Explicação 📋

Este TPC tem como objetivo fornecer uma ferramenta que analisa querys SPARQL e gera uma lista de tokens.
O programa lê um ficheiro de query SPARQL e divide o código em tokens.

## Funcionalidades:

### 1. **Analisador Léxico (Lexer)**
   - O programa converte uma query numa sequência de tokens reconhecidos, como `SELECT`, `WHERE`, `LIMIT`,
   e outros elementos específicos da linguagem.
   - Este trata de expressões e elementos como variáveis, strings, números e comentários.

### 2. **Dois Métodos de Implementação**
   O código contém duas versões para o analisador léxico, ambas com a mesma função final, mas
   implementadas de maneiras diferentes.

   #### Versão 1: Usando Expressões Regulares (Regex)
   - Usa o módulo `re` para identificar os padrões de tokens com base em expressões regulares.
   - Mais flexível para modificações simples, mas pode ser mais difícil de manter com padrões mais complexos.

   #### Versão 2: Usando `ply` (Python Lex-Yacc)
   - Usa o módulo `ply.lex`, que é uma implementação do analisador léxico baseada na ferramenta Lex.
   - Permite uma implementação mais robusta e escalável, com uma sintaxe mais clara para a definição
   dos tokens e erros.

## Raciocínio 🧩

### Estrutura do TPC

Este TPC contém dois ficheiros, independentes, responsáveis por realizar a tokenização de uma query em SPARQL.

- **`query_lex1.py`**: Implementa o analisador léxico utilizando expressões regulares (`re`), que
dividem a query em tokens correspondentes aos elementos da query.
- **`query_lex2.py`**: Utiliza o módulo `ply.lex` para criar o analisador léxico. Este possui uma
abordagem mais estruturada e robusta para identificar e processar os tokens.

### Função Principal

- **Função `tokenize(input_string)` (Versão 1)**:
   A função recebe uma string que contem uma query SPARQL e usa expressões regulares para identificar
   os diferentes tipos de tokens, como:
   - Comandos (`SELECT`, `WHERE`, `LIMIT`)
   - Variáveis (`?nome`)
   - Prefixos (`foaf:name`)
   - Strings
   - Comentários
   - E outros

   Ao final, devolve uma lista com todos os tokens identificados.

- **Função `t_*` (Versão 2)**:
   A versão utilizando `ply` segue uma estrutura de funções pré-definidas (`t_*`), onde cada função
   é responsável por identificar um tipo específico de token. A vantagem é a clareza e a organização do código.

## Expressões Regulares (Regex)

### 1. **`SELECT`**: `r'\bselect\b'`

O padrão `\b` é um delimitador de palavra, que assegura que "select" seja reconhecido como uma palavra
inteira. O `\b` antes e depois de "select" impede que ele seja confundido com palavras que contêm "select", como "selects".

### 2. **`WHERE`**: `r'\bwhere\b'`

Semelhante à expressão anterior, `\b` indica que "where" deve ser tratado como uma palavra inteira,
evitando que seja confundido com palavras como "whereabouts".

### 3. **`LIMIT`**: `r'\bLIMIT\b'`

A expressão `\bLIMIT\b` garante que a palavra "LIMIT" seja reconhecida separada de outras palavras.

### 4. **`NUM`**: `r'\b\d+\b'`

O padrão `\d+` corresponde a um ou mais dígitos (0-9), e `\b` assegura que o número seja isolado
como uma palavra completa.

### 5. **`VARIABLE`**: `r'\?[a-z|A-Z]+'`

O símbolo `?` indica que a variável começa com "?", seguido por um ou mais caracteres alfabéticos
(tanto minúsculos quanto maiúsculos). A parte `[a-z|A-Z]+` descreve os caracteres válidos da variável.

### 6. **`NAME`**: `r'([a-zA-Z0-9_]+:)?[a-zA-Z0-9_]+'`

Este padrão captura nomes de variáveis. A parte `([a-zA-Z0-9_]+:)?` é opcional e permite prefixos
(como em `foaf:name`), e a parte `[a-zA-Z0-9_]+` captura o nome da variável.

### 7. **`DOT`**: `r'\.'`

O padrão `\.` corresponde literalmente ao ponto (`.`) em uma consulta SPARQL, sendo útil para indicar
separação de elementos.

### 8. **`TAG`**: `r'@\w+'`

O padrão `@\w+` corresponde a uma tag no formato de "@" seguida de uma sequência de caracteres
alfanuméricos ou de sublinhado (`_`). Isso é usado para capturar tags como `@en`.

### 9. **`STRING`**: `r'"[^"]*"'`

A expressão `"[^\"]*"` captura uma string delimitada por aspas duplas. O `[^"]*` significa que qualquer
coisa entre as aspas, exceto outra aspa dupla, será capturada como parte da string.

### 10. **`POPEN`**: `r'{'`

O padrão `\{` captura um caractere de abertura de chave `{`, usado para abrir uma expressão ou um
bloco de dados.

### 11. **`PCLOSE`**: `r'}'`

O padrão `\}` captura um caractere de fechamento de chave `}`, usado para fechar expressões ou blocos
de dados.`

### 12. **`COMMENT`**: `r'^#(.*)'`

Esta expressão regular captura um comentário que começa com `#` e segue até o final da linha. O padrão
`^#(.*)` diz que deve começar com `#` e pode ter qualquer conteúdo após ele até o final da linha.

### 13. **`NEWLINE`**: `r'\n'`

O padrão `\n` corresponde a uma nova linha. Ele é usado para identificar quebras de linha no texto.

### 14. **`SKIP`**: `r'[ \t]+'`

O padrão `[ \t]+` captura espaços em branco e tabs. Esse token é ignorado durante o processo de análise,
pois não afeta a estrutura da consulta.

### 15. **`ERROR`**: `r'.'`

O padrão `.` captura qualquer caractere individual que não tenha sido reconhecido como parte de
outros tokens. Isso é usado para identificar caracteres inválidos no código.

## Como Usar 🛠️

1. **Versão 1 - Uso de Expressões Regulares:**
   - Para correr o código com a versão 1, basta executar:
   ```bash
   python3 query_lex1.py <ficheiro.sparql>
   ```
   O resultado será uma lista de tokens que será mostrada no terminal e também escrita em `resolution1.txt`.

2. **Versão 2 - Uso de `ply.lex`:**
   - Para correr o código com a versão 2, basta executar:
   ```bash
   python3 query_lex2.py <ficheiro.sparql>
   ```
   O resultado será uma lista de tokens que será mostrada no terminal e também escrita em `resolution2.txt`.

## Exemplos e Resultados 📊

Pode-se verificar os resultados deste TPC, com o input <a href="teste.sparql">teste.sparql</a>,
com o ficheiro <a href="resolution1.txt">resolution1.txt</a> gerado pela primeira versão e com
<a href="resolution2.txt">resolution2.txt</a> gerado pela segunda versão.
