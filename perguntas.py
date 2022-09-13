print('texto explicativo')
perguntas = {
    'pergunta 1':{
        'pergunta': 'quantos é 2+2? ',
        'respostas' : {'a':'1', 'b' : '4', 'c': '6'},
        'respostacorreta': 'b',
    },
    'pergunta 2':{
        'pergunta': 'quanto é 3*2?',
        'respostas': {'a':'4', 'b':'10', 'c':'6'},
        'respostacorreta' : 'c',
    },
    

}
print()
respostaCerta = 0
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    print('respostas:')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    respostaUsuario = input('sua resposta: ')

    #print(f'Você escolheu {respostaUsuario}')

    if respostaUsuario == pv['respostacorreta']:
        print('parabéns você acertou')
        respostaCerta += 1
    else:
         print('você errou')

    print()
qtd = len(perguntas)
acerto = respostaCerta / qtd * 100

print(f'você acertou {respostaCerta} respostas')
print(f'sua porcetagem de acerto foi de {acerto}%')
