# Variáveis de estado
tentativas = 3
pontos = 0

# pergunta
perguntas = 'Quantos lados tem um triângulo?'

while tentativas > 0:
    resposta = int(input(perguntas))

    if resposta == 3:
        print('Resposta correta!')
        pontos = pontos + 1
        print(f'Pontuação: {pontos}')
        break
    else:
        print('Resposta errada...')
        tentativas = tentativas - 1
        print(f'Você tem {tentativas} tentativas...')

print(f'Pontuação: {pontos}.')