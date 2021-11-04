#subir na 'mão'
'''linha= ''
for coluna in colunas:
linha =linha + f'{coluna}',
print(linha[0:-1])
'''

import os 

#cadastro
def solicitar_dados():
    nome = input('Nome completo: ')
    n_da_mae=input('Nome da mãe: ')
    n_do_pai=input('Nome do pai: ')
    titulo=int(input('Numero do titulo de eleitor: '))
    dta_nascimento=int(input('Data de nascimento: '))
    votou=input('Votou na ultima eleição? (S/N)')
    dados = (nome, n_da_mae,n_do_pai, titulo, dta_nascimento,votou)
    return dados
    
def criar_base_dados(caminho):    
    colunas=['nome','titulo','n_da_mae','n_do_pai','dta_nascimento','Votou']
    #primeira vez que abrir o arquivo
    arquivo = open('caminho','w')
    linha=','.join(colunas) #união de todos elementos com o separador ',' 
    arquivo.write(linha + '\n') #writelines.([linha])
    arquivo.close()

def cadastrar_eleitor(dados,caminho):
    #modo 'a' permite adicionar no arquivo
    arquivo = open(caminho,'a')
    arquivo.write(','.join(dados) + '\n')
    arquivo.close()
    print('Eleitor cadastrado com sucesso')

caminho = 'base_eleitores.css'    
if not os.path.exists(caminho):
    criar_base_dados('base_eleitores.csv')
    
dados_eleitor = solicitar_dados()
cadastrar_eleitor(dados_eleitor,'base_eleitores.csv')





