#################################
# Criado por Gustavo Silva      #
# Versão 1.0                    #
#################################

import random

nomes= [
'Tabata Alves Estevao dos Santos, ',
'Amanda Alves Pereira, ',
'Priscila Amano, ',
'Ruan Amaral Lemos, ',
'Victor Antônio Ferreira Fonseca, ',
'Rodrigo Augusto Aniceto Alves, ',
'Erik Augusto Teixeira Tonin ,',
'Mikael Aurio Martins de Paula da Silva, ',
'Yasmim Barbosa Vieira, ',
'Ingrid Cristinne Calou Batista, ',
'Wendell Crystecen Muria Ferreira, ',
'Lucas Damasceno de Oliveira, ',
'Ruben de Castro Rocha, ',
'Cleidson dos Santos Lima, ',
'Marcela Eduarda Biasini Borelli, ',
'Robson Ferreira Puert, ',
'Lucas Ferreira Rodrigues, ',
'Jhonata Flaubert Alves, ',
'Vinicius Freire Bispo, ',
'Carlos Gabriel Mussato de Moraes, ',
'Matheus Gabryel de Souza Santos, ',
'Cassio Giovanini de Lima, ',
'Afonso Gomes de Amorim, ',
'Gabriel Gonçalves Magalhães, ',
'Igor Guilherme da Paz Provensi, ',
'Marcelo Helton Almeida dos Santos, ',
'Gabriel Henrique Rodrigues da Silva,',
'Jose Junior Marinho da Silva, ',
'Evellyn Karoline Simões Crusat, ',
'Marcio Kavaleski Budri, ',
'Matheus Keller Streppel, ',
'Yasmin Leandra Pereira da Silva, ',
'Vinicius Leandro do Nascimento, ',
'Douglas Leonardo Thomaz Rinaldo, ',
'Miguel Lins Severich Langame Pereira, ',
'Yasmim Lira Castro, ',
'Igor Luan Teles de Souza, ',
'Leonardo Meira de Lima, ',
'Leonardo Mesquita Dalmazzo Antunes, ',
'Danilo Pagamisse Michelan, ',
'Pedro Paulo Espindola Gomes, ',
'Paulo Pedrosa dos Santos, ',
'Ruy Peral de Araujo, ',
'Paulo Pereira Fernandes Oliveira, ',
'Matheus Pessone, ',
'Beatrici Ramos Feliciano, ',
'Karen Ranny Sena Pinheiro Viana, ',
'Luis Rossi, ',
'Igor Ruiz de França, ',
'Alfredo Ryan dos Santos Padilha, ',
'Gerson Sampaio Brito, ',
'Lucas Sandrini Belarmino, ',
'Karen Santos Cunha Ávila, ',
'Alisson Santos Silva, ',
'Hires Serva de Maria Menezes, ',
'Guilherme Tadashii Ruão Takemoto, ',
'Nathan Teixeira de Simas Sussaio, ',
'Matheus Vinicius Silva de Sousa, ',
'Felipe Waddington Pereira Jeronymo, ',
'Rafael Zerbinatti, ']

random.shuffle(nomes)
for ind, smb in enumerate(nomes):
    print(smb, end='\n')
    if ind%5 == 4: 
        print('\n Grupo')
       
