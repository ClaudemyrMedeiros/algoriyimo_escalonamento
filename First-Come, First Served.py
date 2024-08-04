processos = [5,8,2,5,6]
variavel=0
item=0
print('********* Simulador  First-Come, First Served ********* ')
for processo in processos:
    variavel+=processo
    item+=1
    print(f'{item}º processo levou {variavel} segundos' )
print(f'####### Tempo médio {variavel/item} segundos ###########')

