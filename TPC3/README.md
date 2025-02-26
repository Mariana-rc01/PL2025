# Conversor de Markdown para HTML 🔁

## Autor 🌻  
Mariana Rocha (A90817)

## Explicação 📋

Este TPC tem como objetivo fornecer uma ferramenta que converte um ficheiro Markdown para HTML. O Markdown é uma linguagem de marcação simples, usada para formatação de texto. O programa lê um ficheiro em formato Markdown e converte os elementos de formatação para as correspondentes tags HTML, o que facilita a exibição do conteúdo.

## Funcionalidades:

### 1. **Conversão de Cabeçalhos**
   - O programa identifica cabeçalhos no formato Markdown, que utilizam o símbolo `#` para marcar títulos (por exemplo, `# Título` para o cabeçalho nível 1, `## Subtítulo` para nível 2, etc.).
   - O número de `#` determina o nível do cabeçalho, e o texto após os `#` é extraído e convertido numa tag `<h1>`, `<h2>`, `<h3>`, ..., dependendo da quantidade de `#`. O limite máximo de cabeçalhos é de 6 (`<h1>` a `<h6>`).

### 2. **Conversão de Negrito e Itálico**
   - O código deteta texto que está em **negrito** (formatado como `**texto**` ou `__texto__`) e converte-o para a tag HTML `<b>`.
   - Texto em *itálico* (formatado como `*texto*` ou `_texto_`) é convertido para a tag HTML `<i>`.

### 3. **Conversão de Listas Numeradas**
   - O programa identifica listas numeradas no formato Markdown (como `1. Item 1`, `2. Item 2`, etc.) e converte-as para uma lista ordenada em HTML (`<ol>` e `<li>`).

### 4. **Conversão de Links e Imagens**
   - Links no formato Markdown, como `[Texto do Link](http://example.com)`, são convertidos para a tag HTML `<a href="http://example.com">Texto do Link</a>`.
   - Imagens no formato Markdown, como `![Texto Alternativo](http://example.com/imagem.jpg)`, são convertidas para a tag HTML `<img src="http://example.com/imagem.jpg" alt="Texto Alternativo"/>`.

## Raciocínio 🧩

### Estrutura do TPC

Contém um único ficheiro responsável por realizar a conversão do Markdown para HTML.

- **`conversor.py`**: O ficheiro Python contém toda a lógica necessária para:
   - Ler o conteúdo de um ficheiro Markdown.
   - Aplicar expressões regulares para identificar os padrões de Markdown, como cabeçalhos, negritos, itálicos, listas numeradas e links/imagens.
   - Substituir esses padrões pelos elementos HTML correspondentes.
   - Gravar o conteúdo convertido num novo ficheiro HTML.

### Função Principal

- **Função `conversor(file)`**:

   A função `conversor` recebe o nome de um ficheiro Markdown como parâmetro e executa as seguintes tarefas:
   1. **Leitura do ficheiro**: Abre e lê o conteúdo do ficheiro Markdown fornecido.
   2. **Aplicação de expressões regulares**: Utiliza expressões regulares para identificar e capturar os elementos Markdown (cabeçalhos, negrito, itálico, listas, links e imagens).
   3. **Substituição de elementos**: Para cada tipo de formato Markdown detetado, realiza a substituição pela correspondente tag HTML.
   4. **Gravação do ficheiro HTML**: O conteúdo convertido é gravado num novo ficheiro chamado `output.html`.

## Expressões Regulares (Regex)

Aqui está uma explicação das expressões regulares utilizadas para identificar e capturar os diferentes padrões de Markdown:

### 1. **Cabeçalhos:** `^(#+)\s*(.*)`

   - A expressão `^(#+)\s*(.*)` é usada para capturar os cabeçalhos Markdown. O símbolo `#` é utilizado para definir os níveis dos cabeçalhos (`#` para `<h1>`, `##` para `<h2>`, etc.).
   - O número de `#` determina o nível do cabeçalho. A parte `(.*)` captura o texto do título após os `#`.
   - O código usa o número de `#` para gerar a tag HTML correspondente, até um máximo de 6 níveis de cabeçalhos.

### 2. **Negrito e Itálico:** `(\*{1,2}|\_{1,2})(.*?)\1`

   - A expressão `(\*{1,2}|\_{1,2})(.*?)\1` captura textos em **negrito** (usando `**texto**` ou `__texto__`) e **itálico** (usando `*texto*` ou `_texto_`).
   - O grupo `(\*{1,2}|\_{1,2})` captura os símbolos de asterisco ou sublinhado (que podem ser 1 ou 2), e o grupo `(.*?)` captura o texto formatado.
   - Dependendo do número de asteriscos ou sublinhados, o texto será envolvido na tag HTML apropriada (`<b>` para negrito e `<i>` para itálico).

### 3. **Links e Imagens:** `( |!)\[(.*?)\]\((.*?)\)`

   - Esta expressão é responsável por capturar links e imagens.
   - Para **links**, o padrão `[Texto](URL)` é convertido em `<a href="URL">Texto</a>`.
   - Para **imagens**, o padrão `![Texto Alternativo](URL)` é convertido em `<img src="URL" alt="Texto Alternativo"/>`.

### 4. **Listas Numeradas:** `^(\d+\.)\s(.*)`

   - A expressão `^(\d+\.)\s(.*)` deteta listas numeradas no formato Markdown (`1. item`, `2. item`, etc.).
   - O número antes do ponto (`\d+\.`) é capturado para determinar a ordem dos itens da lista. O texto após o ponto (`(.*)`) é o conteúdo de cada item da lista.
   - O código converte esses itens em tags `<ol><li>item</li></ol>`.

## Como Usar 🛠️

### Execução

Abra o terminal e execute o seguinte comando:
   
```bash
python conversor.py <input_file> <output_file>
```

Substitua `<input_file>` pelo caminho do ficheiro Markdown que deseja converter e <output_file> pelo caminho do ficheiro HTML que deseja ficar guardada a conversão.

## Exemplos e Resultados 📊

Pode-se verificar os resultados deste tpc, com o input <a href="teste.md">teste.md</a>, temos o ficheiro <a href="output.html">output.html</a>.
