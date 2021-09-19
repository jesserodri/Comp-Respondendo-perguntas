
from random import randint
cont = 0

gostos = ["gosto de aprender mais", "gosto de solucionar problemas", "gosto de observar as pessoas", "gosto de praticar minha sabedoria"]
film = ["filmes como toy story, gente grande, diversos filmes de comedia e por ai vai "]
faz = ["eu ainda nao faço muita coisa"," procuro responder as perguntas que me façam","eu respondo perguntas simples"," nao faço muita coisa mas posso lhe responder algumas coisas"]
anosVida = ["tenho pouco tempo de vida", ' meu criador me fez a pouco tempo', "meu pai está me desenvolvendo ainda, então tenho pouco tempo de vida"]
dia = ['foi muito bom', 'foi otimo', 'legalzinho até','não foi muito legal', 'foi pessimo mas obrigado por perguntar']
#pessoas = ["gosto de pessoas que são otimistas","gosto de pessoas realistas","gosto de pessoas que tem interesse em saber mais"]
bebidas= ['cerveja', "vodka", "whisky"," não tenho uma favorita", "desculpa eu não bebo"]
afirma =["não","Sim", "não tenho certeza "]
deci = ['Não sei, acho que não','Não sei, acho que sim' , 'Você quem sabe', 'Sim pode ter certeza']
negacao = ['eu não sei', ' eu sei mas nao quero falar '," não faço ideia", "não sei mas posso pesquisar"]

while True:
    cont+=1
    if cont == 1:
        print("Me faça uma pergunta Sobre mim ou algo do seu interesse !")
    else:
        print("me fala outra pergunta: ")
    perg = input("> ")


#sobre
    if 'como' and 'foi' and 'dia' in perg:
        resp = randint(0, len(dia))
        print(dia[resp])
        continue

    elif 'voce' and 'gosta de que' in perg:
        resp = randint(0, len(gostos)-1)
        print(gostos[resp])
    elif 'filme' and 'favorito' in perg:
        print(film[0])

    elif 'quais' and 'suas' and 'qualidades' in perg:
        resp = randint(0, len(faz))
        print(faz[resp])

    elif 'o que' and 'voce' and 'faz' in perg:
        resp = randint(0, len(faz))
        print(faz[resp])

    elif 'quais' and 'caracteriscas' and 'suas' in perg:
        resp = randint(0, len(faz)-1)
        print(faz[resp])

#idade

    elif 'quantos' and 'anos' and 'voce' in perg:
        resp = randint(0, len(anosVida)-1)
        print(anosVida[resp])
        continue
    elif 'quantos' and 'anos' and 'tem' in perg:
        resp = randint(0, len(anosVida) - 1)
        print(anosVida[resp])
    elif 'quantos' and 'anos' and 'vida' in perg:
        resp = randint(0, len(anosVida) - 1)
        print(anosVida[resp])

    elif 'como' in perg:
        resp = randint(0, len(negacao))
        print(negacao[resp])

    elif 'devo'and'sair' in perg:
        resp = randint(0, len(deci)-1)
        print(deci[resp])

    elif 'qual' and "bebida" in perg:
        resp = randint(0,len(bebidas)-1)
        print(bebidas[resp])

    else:
        print("desculpe ainda não tenho resposta para isso !")

    ''' 
    print("DESEJA CONTINUAR ?")
    esc = input("> ").upper()[0]
   
#Pergunta ao usuario se deseja continuar ou sair (vou deixar fora para testar o programa)
    while esc not in 'SN':
        if esc[0] in 'S':
            continue
        elif esc[0] in 'N':
            print("Volte sempre!")
            break
        
        else:
            print("tente novamente: ")
            esc = input("> ").upper()[0]
'''