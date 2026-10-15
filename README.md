# Morse Code Converter

Um conversor de linha de comando desenvolvido em Python para transformar texto em código Morse e decodificar sequências Morse de volta para texto.

O projeto utiliza um dicionário de correspondência entre caracteres e seus sinais Morse e permite fazer conversões diretamente pelo terminal.

## Funcionalidades

- Converter texto para código Morse.
- Converter código Morse para texto.
- Reconhecer letras, números e sinais de pontuação definidos no dicionário do projeto.
- Realizar várias conversões durante a mesma execução, sem precisar reiniciar o programa.

## Tecnologias

- **Python 3**
- Módulos nativos do Python; não são necessárias bibliotecas externas.

## Estrutura do projeto

```text
Morse-Code-Converter/
├── main.py        # Interface de linha de comando e lógica de conversão
└── morse_dict.py  # Dicionário de caracteres e seus códigos Morse
```

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/FellipeO/Morse-Code-Converter.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd Morse-Code-Converter
   ```

3. Execute o programa com Python 3:

   ```bash
   python main.py
   ```

   Em alguns sistemas, pode ser necessário usar `python3 main.py`.

## Exemplos de uso

### Texto para código Morse

Digite um texto quando o programa solicitar a entrada:

```text
Word: HELLO WORLD
```

Resultado esperado:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Código Morse para texto

Digite uma sequência Morse usando espaços entre os sinais de cada letra e `/` para separar palavras:

```text
Word: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Resultado:

```text
HELLO WORLD
```

Para encerrar o programa, digite `!`.

## Caracteres suportados

O dicionário inclui letras de **A a Z**, números de **0 a 9** e sinais de pontuação como ponto, vírgula, interrogação, exclamação, parênteses e outros símbolos definidos em `morse_dict.py`. A entrada textual é convertida para maiúsculas antes do processamento.

## Objetivo do projeto

Este projeto é um exercício prático de Python que trabalha com dicionários, conversão de dados, manipulação de strings, laços de repetição e entrada e saída pelo terminal.

## Autor

**Fellipe de Oliveira**  
[GitHub: FellipeO](https://github.com/FellipeO)
