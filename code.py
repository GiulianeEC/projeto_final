#cadastro
def cadastro():
    nome = input('Nome completo: ')
    n_da_mae=input('Nome da mãe: ')
    n_do_pai=input('Nome do pai: ')
    titulo=int(input('Numero do titulo de eleitor: '))
    dta_nascimento=int(input('Data de nascimento: '))
    votou=input('Votou na ultima eleição? (S/N)')
    
def criar_base_dados(caminho):    
    colunas=['nome','titulo','n_da_mae','n_do_pai','dta_nascimento','Votou']
    #primeira vez que abrir o arquivo
    arquivo = open('base_eleitores.csv','w')
    linha=','.join(colunas)
    arquivo.write(linha + '\n')
    arquivo.close()

#subir na 'mão'
'''linha= ''
for coluna in colunas:
    linha =linha + f'{coluna}',
    print(linha[0:-1])
    '''

criar_base_dados('base_eleitores.csv')

if __name__ == '__main__':
    cadastro()


