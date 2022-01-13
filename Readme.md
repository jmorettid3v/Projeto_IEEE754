# IEEE-754 Standard Project

- Objective: Desevolvimento de código, a fim de criar um algoritmo que seja capaz de realizar a padronização de números em Ponto Flutuante (Nº Reais) em representação Binária e Hexadecimal de 32 bits e 64 bits, baseado no Padrão IEEE-754.

- Language used: Python
- Implementation for: 32 bits e 64 bits

## O que é o Padrão IEEE-754

O padrão IEEE-754 , recomendado pelos institutos ANSI (American National Standard Institute) e IEEE (Institute of Electrical and Eletronic Engineers), refere-se às normas a serem seguidas pelos fabricantes de computadores e construtores de compiladores de linguagens científicas, ou de bibliotecas de funções matemáticas, na utilização da aritmética binária para números de ponto flutuante. As recomendações são relativas ao armazenamento de dados numéricos, métodos de arredondamento, tratamento de casos de underflow e overflow, formas de realização das quatro operações aritméticas básicas e implementação de funções nas linguagens de programação.

## 4 elementos do Padrão IEEE-754

- O padrão pode ser implementado em valores na base 10 (decimal), como na base 2 (binária)
  - Para representar um número no Padrão IEEE-754, é necessário transformar o mesmo para sua `Forma Normal`

* ex. `Forma normalizada`: + 2.631855 10^2

- Base: 10
- Sinal: +
- Mantissa: 2.631855
- Expoente: 2

* ex. `Forma normalizada`: + 1.101 2^-2

- Base: 2
- Sinal: +
- Mantissa: 1.101
- Expoente: -2

## Padrão define 3 Precisões

- Single precision (float) - 32 bits
- Double precision (double) - 64 bits
- Double extended precision (extended)- 80 bits

## Para 32 bits:

- 1 bit - Para o `Sinal` (positivo: 0 | negativo: 1)
- 8 bits - Para o `Expoente`
- 23 bits - Para a `Mantissa` obs.: + 1 bit implícito (que estaria a esquerda do ponto decimal)
- Faixa de valores: 2^-126 até 2^127

## Para 64 bits:

- 1 bit - Para o `Sinal` (positivo: 0 | negativo: 1)
- 11 bits - Para o `Expoente`
- 52 bits - Para a `Mantissa` obs.: + 1 bit implícito (que estaria a esquerda do ponto decimal)
- Faixa de valores: 2^-1022 até 2^1023

## Implementação do Padrão IEEE-754

- Note: ex.: Produzir o Binário e o Hexadecimal no padrão IEEE-754 com precisão de 32 bits, que represente o valor `0.1`

* 1º passo: Converter a parte inteira para Binário

  - `0.1` --> Parte inteira `0` --> Em Binário `0` (continua zero)

* 2º passo: Converter a parte decimal para Binário

  - `0.1` --> Parte decimal `0.1` --> Em Binário `0. 0 "0011 ..."` (o que está entre aspas é onde a dízima periódica se inicia)

* 3º passo: Juntar as partes inteira e decimal binárias

  - Inteiro: `0`; Decimal: `0. 0 0011` --> `0. 0 0011 0011 ...`

* 4º passo: Normalizar o Binário obtido

  - `0. 0 0011 0011 ...` --> `1 . 10011 ... x 2^-4` --> Mantissa em Binário `1 0011 0011 0011 ...`

* 5º passo: Converter o expoente para Binário

  - Obs.: o padrão utiliza o método BIAS (para 32 bits, BIAS = 127)
    - Expoente: `-4`; BIAS: `127` --> BIAS `-4 + 127 = 123` --> Expoente em Binário `01111011`

* 6º passo: Anotar todos os bits no gabarito

  - Sinal | Expoente | Mantissa
  - 0 | 01111011 | 1 0011 0011 0011 ...
  - 32 bits do Gabarito: `0 01111011 10011001100110011001100`

* 7º passo: Converter o gabarito em Binário para Hexadecimal
  - Binário `0 01111011 10011001100110011001100`
  - --> `0011 1101 1100 1100 1100 1100 1100 1100`
  - --> ` 3 D C C C C C C`
  - Hexadecimal `3DCCCCCC`
