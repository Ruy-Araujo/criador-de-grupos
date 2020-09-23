###########
# Criador de Grupos      
# Versão v0.1                  
###########

import random 
import math
import os

wd = os.getcwd()                # Bloco responsavel por apontar a pasta 
os.chdir(wd)                    # com os arquivos de entrada e saida


qnt_integrantes = int(input('Digite a quantidade de integrantes em cada grupo: '))
open_grupos = open('grupos.txt','w')

with open('nomes.txt','r') as arquivo_nomes:            # Bloco responsavel por ler o arquivo de entradada
    lista_nomes = arquivo_nomes.read().splitlines()     # e transformar cada linha em um item da lista
    random.shuffle(lista_nomes)                         #

qnt_pessoas = lista_nomes.__len__()                         
total_grupos = math.ceil( qnt_pessoas / qnt_integrantes)

def separador(lista, n):                                # Função responsavel por separar a lista com nomes em 
    inicio = 0                                          # sublistas com a aquantidade certa de pessoas
    for i in range(n):
        final = inicio + len(lista[i::n])
        yield lista[inicio:final]
        inicio = final
    
grupos = list(separador(lista_nomes,total_grupos))

for indice,lista in enumerate(grupos,start=1):          # Bloco responsavel pela gravação dos nomes no arquivo de saida
    open_grupos.write(f'#### Grupo {indice} ####\n')
    for nome in lista:
        open_grupos.write(nome+'\n')
    open_grupos.write('\n')
        
open_grupos.close()
print('Processo finalizado você ja pode fechar esta janela!')