# Entrada de Dados
print('\t***** IEEE-754 -- Conversão de Ponto-Flutuante *****')
print('Flutuante decimal para representação Hexadecimal de 32 bits e 64 bits e equivalente Binário\n\n')
n = float(input('Informe o número em Ponto Flutuante decimal: '))
precisao = int(input(
    'Precisão simples 32 bits - Precisão dupla 64 bits\n\tInforme a precisão: '))

# Definição de variável auxiliar, variável para parte inteira e para parte decimal
aux = n
if aux < 0:
    aux *= -1
num = int(aux)
decimal = aux - num

# Define variáveis conforme a precisão
if precisao == 32:
    significand = 23
    const_bias = 127
    lim_expo = 8
    qtd_bits = (precisao - 1)
else:
    significand = 52
    const_bias = 1023
    lim_expo = 11
    qtd_bits = (precisao - 1)

# Processamento
# 1º passo: Converter a parte inteira para binário
var = -1
bit_Int = []
if num >= 1:
    while num >= 1:
        x = num % 2
        bit_Int.append(x)
        num = num // 2
        var += 1
    bit_Int = bit_Int[::-1]
else:
    bit_Int = [0]
    var = 0

# 2º passo: Converter a parte decimal para binário
ListaFloat = []
bit_Dec = []
for i in range(0, (significand - var)):
    decimal *= 2
    ListaFloat.append(decimal)
    bit_Dec.append(int(ListaFloat[i]))
    if decimal >= 1:
        decimal -= 1

# 3º passo: Normalizar o binário obtido
cont = 0
L1 = []
mantissa = []
if len(bit_Int) == 1 and bit_Int[cont] == 0:
    # [44] -> se refere ao código ASCII do caracter vírgula (,)
    L1 = [','] + bit_Dec
    elementos = len(L1)
    ordenado = False
    while not ordenado:
        if L1[cont+1] == 1:
            L1[cont], L1[cont+1] = L1[cont+1], L1[cont]
            ordenado = True
        else:
            L1[cont], L1[cont+1] = L1[cont+1], L1[cont]
            ordenado = False
        cont += 1
    bias = -1 * cont
    mantissa = bit_Dec[cont:]
elif len(bit_Int) == 1 and bit_Int[cont] == 1:
    mantissa = bit_Dec
    bias = 0
else:
    # [44] -> se refere ao código ASCII do caracter vírgula (,)
    L1 = [','] + bit_Int
    L1[cont], L1[cont+1] = L1[cont+1], L1[cont]
    bias = len(L1)-2
    mantissa = bit_Int[1:] + bit_Dec

# 4º passo: converter o expoente
expoente = []
bias += const_bias
while bias >= 1:
    x = bias % 2
    expoente.append(x)
    bias = bias // 2
while len(expoente) < lim_expo:
    expoente.append(0)
expoente = expoente[::-1]

# 5º passo: verificar a quantidade de bits (obs.: se necessário completar)
if len(expoente + mantissa) < qtd_bits:
    for i in range(i+1, (i+cont+1)):
        decimal *= 2
        ListaFloat.append(decimal)
        mantissa.append(int(ListaFloat[i]))
        if decimal >= 1:
            decimal -= 1

# 6º passo: anotar os bits no gabarito
gabarito = []
if n < 0:
    gabarito = [1] + expoente + mantissa
    sinal = 1
else:
    gabarito = [0] + expoente + mantissa
    sinal = 0

# 7º passo: converter para Hexadecimal
hexa = []
cont = 3
x = 0
contador = 0
for i in range(0, precisao):
    if gabarito[i] == 1:
        x += (2 ** cont)
    cont -= 1
    if contador == 3:
        hexa.append(x)
        cont = 3
        contador = -1
        x = 0
    contador += 1

for i in range(0, len(hexa)):
    if hexa[i] == 10:
        hexa[i] = 'A'
    elif hexa[i] == 11:
        hexa[i] = 'B'
    elif hexa[i] == 12:
        hexa[i] = 'C'
    elif hexa[i] == 13:
        hexa[i] = 'D'
    elif hexa[i] == 14:
        hexa[i] = 'E'
    elif hexa[i] == 15:
        hexa[i] = 'F'
    else:
        hexa[i] = hexa[i]

# Saídas
# 8º passo: printar na tela os resultados - Sinal | Expoente | Mantissa | Gabarito | Hexadecimal
print('\nResultados - Precisão simples 32 bits\n\t Valor decimal inserido: ', aux)
print('\nBit', (precisao - 1), '\t\tBit', (precisao - 2), '-',
      (precisao - 9), '\t\t\t\tBit', (precisao - 10), '-', 0)
print('Sinal:', sinal, '\tExpoente:', ' '.join(map(str, expoente)),
      '\tMantissa:', ' '.join(map(str, mantissa)))
print('\nGabarito:', ' '.join(map(str, gabarito)))
print('Hexadecimal:', ' '.join(map(str, hexa)))
