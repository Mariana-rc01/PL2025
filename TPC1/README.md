# TPC1: Somador on/off

## Autor
Mariana Rocha (A90817)

## Explicação

Este programa, **somadorONOFF**, recebe uma linha de texto da entrada e adiciona todos os números inteiros encontrados enquanto o estado estiver ativado (*on*). Se em alguma parte do texto surgir a palavra "off" (com quaisquer variações de maiúsculas e minúsculas), o programa desativa a soma. Quando o "on" surge novamente, a soma é reiniciada. Sempre que for detetado um "=", o programa exibe o valor atual da soma. O procedimento repete-se até que o utilizador insira uma linha vazia.

### Raciocínio:

O programa começa por criar as seguintes variáveis: 

- `sum`, que armazena o total da soma, iniciado em 0. 
- `state`, que mostra se o programa está ativo ou inativo, iniciado como *True* (ativo). 
- `numberS`, que guarda temporariamente o número encontrado no texto. 

Em seguida, lê a entrada do utilizador e analisa cada caractere da linha. Se o estado estiver *on*, cada dígito identificado é guardado no `numberS` e ao encontrar um caractere que não é um número, o conteúdo de `numberS` é convertido para inteiro (através de um cast) e é adicionado ao total (`sum`). Se a palavra "off" for detectada, o estado muda para *False*, interrompendo a soma até que "on" seja identificado novamente. Se surgir "=", o programa exibe a soma atual. 

### Testar o programa: 

1. No terminal, execute: `python3 somadorONOFF.py`.  
2. Escreva uma linha com números e as palavras "on" e "off" para controlar a soma.  
3. Os números são somados enquanto o estado estiver *on*.  
4. Escreva "=" para ver o total atual.  
5. Use "off" para parar a soma e "on" para retomá-la.  
6. Para sair, carrege Enter sem escrever nada.

**Exemplo:**  

Entrada:  
```
12 abc 34 off 5 on 6 =
```  
Saída:  
```
Soma = 52
```  
A soma para no "off", ignora o 5, retoma no "on" e adiciona o 6.
