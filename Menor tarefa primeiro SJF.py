# Menor tarefa primeiro SJF
p1= int(input('Primeiro tempo:'))
p2= int(input('Segundo tempo:'))
p3= int(input('Terceiro tempo:'))
p4= int(input('Quarto tempo:'))
p5= int(input('Quinto tempo:'))
item=0

lista=[p1,p2,p3,p4,p5]
lista_ordem=sorted(lista)
variavel=0

for processo in lista_ordem:
    variavel+=processo
    item+=1
    print(f'O {item}º  processo que leva {processo} segundos, levou {variavel} segundos para ser executado' )
print(f'####### Tempo médio {variavel/item} segundos ###########') 