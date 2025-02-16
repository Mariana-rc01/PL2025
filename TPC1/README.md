# TPC1: Somador on/off ➕

## Autor 🌻
Mariana Rocha (A90817)

## Explicação 📋

Este programa, **somadorONOFF**, recebe uma linha de texto da entrada e adiciona todos os números inteiros encontrados enquanto o estado estiver ativado (*on*). Se em alguma parte do texto surgir a palavra "off" (com quaisquer variações de maiúsculas e minúsculas), o programa desativa a soma. Quando o "on" surge novamente, a soma é reiniciada. Sempre que for detetado um "=", o programa exibe o valor atual da soma. O procedimento repete-se até que o utilizador insira uma linha vazia.

### Raciocínio 🧩

O programa começa por criar as seguintes variáveis: 

- `sum`, que armazena o total da soma, iniciado em 0. 
- `state`, que mostra se o programa está ativo ou inativo, iniciado como *True* (ativo). 
- `numberS`, que guarda temporariamente o número encontrado no texto. 

Em seguida, lê a entrada do utilizador e analisa cada caractere da linha. Se o estado estiver *on*, cada dígito identificado é guardado no `numberS` e ao encontrar um caractere que não é um número, o conteúdo de `numberS` é convertido para inteiro (através de um cast) e é adicionado ao total (`sum`). Se a palavra "off" for detectada, o estado muda para *False*, interrompendo a soma até que "on" seja identificado novamente. Se surgir "=", o programa exibe a soma atual. 

### Como executar 🛠️

Caso pretenda testar diretamente no teclado, execute o programa:

1. No terminal, execute: 
<pre>
$ python3 <a href="somadorONOFF.py">somadorONOFF.py</a>
</pre>
2. Escreva uma linha com números e as palavras "on" e "off" para controlar a soma.  
3. Os números são somados enquanto o estado estiver *on*.  
4. Escreva "=" para ver o total atual.  
5. Use "off" para parar a soma e "on" para retomá-la.  
6. Para sair, pressione CTRL+D.

Caso queira usar um ficheiro para testar o programa:

1. No terminal, execute:
<pre>
$ python3 <a href="somadorONOFF.py">somadorONOFF.py</a> < <a href="teste.txt">teste.txt</a>
</pre>

### Exemplos e Resultados 📊

Nos ficheiros <a href="resultado.txt">resultado.txt</a> e <a href="resultado1.txt">resultado1.txt</a> pode visualizar o output dos ficheiros <a href="teste.txt">teste.txt</a> e <a href="teste1.txt">teste1.txt</a>, respetivamente.

Entrada:  
```
12 abc 34 off 5 on 6 =
```  
Saída:  
```
Soma = 52
```  
A soma para no "off", ignora o 5, retoma no "on" e adiciona o 6.
