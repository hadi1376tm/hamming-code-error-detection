from random import randint
from math import log2

def binary(x, maxPower2):
    return ('{0:0' + str(maxPower2) + 'b}').format(x)

def hazardChannel(data):
    randI = randint(0, len(data) - 1)
    toss = '0' if data[randI] == '1' else '1'
    data = data[:randI] + toss + data[randI+1:]
    return data


def hammingGenerate(raw):
    encoded = []
    encodedIndex = 0
    rawIndex = 0
    powerIndex = 0
    while True:
        if encodedIndex == (2 ** powerIndex) - 1:
            encoded.append('.')
            encodedIndex += 1
            powerIndex += 1
        elif rawIndex < len(raw):
            encoded.append(raw[rawIndex])
            encodedIndex += 1
            rawIndex += 1        
        else:
            break

    maxPower2 = int(log2(len(encoded))) + 1

    for i in range(0, maxPower2):
        evenParity = 0
        for j in range(0, len(encoded)):
            if (binary(j + 1, maxPower2)[-(i+1)] == '1') and encoded[j] == '1':
                evenParity += 1
        if evenParity % 2 == 1:
            encoded[2 ** i - 1] = '1'
        else:
            encoded[2 ** i - 1] = '0'
    return ''.join(encoded)

def decodeData(encoded):
    
    encoded = list(encoded)
    maxPower2 = int(log2(len(encoded))) + 1
    for i in range(0, maxPower2):
        encoded[2 ** i - 1] = '.'
    
    decoded = []
    for ch in encoded:
        if ch != '.':
            decoded.append(ch)
    return ''.join(decoded)

def hammingDetectCorrect(encoded):
    maxPower2 = int(log2(len(encoded))) + 1
    detector = ''
    encoded = list(encoded)
    for i in range(0, maxPower2):
        evenParity = 0
        for j in range(0, len(encoded)):
            if (binary(j + 1, maxPower2)[-(i+1)] == '1') and encoded[j] == '1':
                evenParity += 1
        if evenParity % 2 == 1:
            detector = '1' + detector
        else:
            detector = '0' + detector
    errorAt = int(detector, base=2) - 1
    if errorAt >= 0:
        print('Error at =>   ', errorAt)
        encoded[errorAt] = '1' if encoded[errorAt] == '0' else '0'
    else:
        print('No error')
    
    return ''.join(encoded)



def hamming(inp):
    print('Raw =>        ', inp)
    encoded = hammingGenerate(inp)
    print('Encoded =>    ', encoded)
    tranfered = hazardChannel(encoded)
    print('Transfered => ', tranfered)
    corrected = hammingDetectCorrect(tranfered)
    print('Decoded:      ', corrected)
    decoded = decodeData(corrected)
    print('Recieved:     ', decoded)

inputs = [
    '1010011',
    '1100111',
    '1011001',
]
for inp in inputs:
    print('===============================')
    hamming(inp)    