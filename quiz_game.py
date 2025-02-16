print("Seja bem-vindo ao quiz de computadores!")

jogando = input('Você quer jogar?').lower()

if jogando != "sim":
    quit()
    print('O jogo não iniciou nem iniciará. Até mais!')
else:
    print('Vamos iniciar o jogo!')
    
score = 0
    
pergunta1 = input('O que significa a sigla CPU? ').lower()

if pergunta1 == "unidade central de processamento":
    score += 1
    print(f'A resposta {pergunta1} está correta! E sua pontuação é {score}!')
else:
    print('Está incorreto!')
    
    
pergunta2 = input('Qual é a linguagem de programação utilizada para criar páginas da web? ').lower()

if pergunta2 == "html":
    score += 1
    print(f'A resposta {pergunta2} está correta!E sua pontuação é {score}!')
else:
    print('Está incorreto!')
    
pergunta3 = input('Qual é o sistema operacional da Apple? ').lower()

if pergunta3 == "ios":
    score += 1
    print(f'A resposta {pergunta3} está correta!E sua pontuação é {score}!')
else:
    print('Está incorreto!')
    
print(f'O jogo acabou e a sua pontuação total foi: {score}')
    

    
    
    
    
    
