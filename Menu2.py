ProjetoIP

print(" _________________________-__________________________ ")
print("|  Autor: Sérgio Batista da Silva                    |")
print("|  e-mail: sergio.batista@dce.ufpb.br                |")
print("|  Mat: 81310048                                     |")
print("|  Bem Vindo ao colégio Alone                        |")
print("|  Data: 06/06/2016                                  |")
print("|  Descrição: Aqui você poderá fazer o Cadastro      |") 
print("|  escolar dos seus alunos no ensino fundamental     |")
print("|_________________________-__________________________|")

aluno = 0 
sr = 0 
notas = 0
n_1 = 0
n_2 = 0
n_3 = 0
salvar_diario = 0
l_Media = 0 
l_Falta = 0
salvar = " " 
  
l_Aluno = [] 
n_1 = []
n_2 = []
n_3 =[]
l_Serie = [] 
l_Falta = []  
l_Diario = [l_Aluno,n_1, n_2,n_3,l_Falta,l_Serie] 
  
#Função menu
def menu (): 
    print(" ________________۞__________________")

    print("|              MENU                 |")
    print("|   [1] Cadastrar Alunos            |")
    print("|   [2] Remover Aluno               |")
    print("|   [3] Lançar Notas                |")
    print("|   [4] Lançar faltas               |")
    print("|   [5] Listar Alunos Matriculados  |")
    print("|   [6] Ver o Diário                |")
    print("|   [x] Sair                        |")
    print("|_________________۞_________________|")
    
    opt = input("Digite a opçao desejada: ") 
    return opt 

#Função para martricular alunos.
def adicionar_matricula ():
    aluno = str(input("Digite o nome completo do aluno: "))
    aluno = aluno.upper()
    if aluno in l_Aluno:
        print("Aluno já está Matriculado")
    else:
        l_Aluno.append(aluno)
        sr = int(input("Digite a série aluno: ")) 
        l_Serie.append(sr)
        print("Aluno Matriculado")
    
    pass 

#Função para remover alunos. 
def remover_matricula (): 
    aluno = str(input("Digite o nome do aluno: "))
    aluno = aluno.upper()
    if aluno in l_Aluno:
        l_Aluno.remove(aluno) 
        print("Aluno Removido")
    else:
        print("Esse aluno não está matriculado") 
    pass 

#Função para cadastrar e listar notas. 
def lancar_notas ():
    aluno = str(input("Digite o nome do aluno: "))
    aluno = aluno.upper()
    if  aluno in l_Aluno:
        n_1 = float(input("Digite a primeira nota do aluno: "))
        n_2 = float(input("Digite a segunda nota do aluno: "))
        n_3 = float(input("Digite a terceira nota do aluno: ")) 
        l_Diario.append(n_1)
        l_Diario.append(n_2)
        l_Diario.append(n_3)
       
    else:
        print("Esse aluno não está Matriculado")
    pass 

def lancar_faltas ():
    aluno = str(input("Digite o nome do aluno: "))
    aluno = aluno.upper()
    if  aluno in l_Aluno:
        falta = (input("Digite as faltas do aluno no mês atual: ")) 
        l_Falta.append(falta)
    else:
        print("Esse Aluno Não Está Matriculado")
    pass 
      
def listar_alunos (): 
    print("Alunos Matriculados", l_Aluno) 
    pass 
  
def lediario (): 
    print(l_Diario) 
    pass 

def salva_diario (): 
    salvar = input("Deseja salvar o diario: ")
    if salvar == "sim": 
        print("O diario foi Salvo com sucesso!") 
    else:
        print("Diario não Salvo")
    pass 
  
opcao = menu() 
while opcao != "x": 
    if opcao == "1": 
        adicionar_matricula() 
    elif opcao == "2":  
        remover_matricula() 
    elif opcao == "3":  
        lancar_notas() 
    elif opcao == "4":  
        lancar_faltas() 
    elif opcao == "5":  
        listar_alunos() 
    elif opcao == "6":
        lediario()
 
    opcao = menu() 
  
salva_diario()
