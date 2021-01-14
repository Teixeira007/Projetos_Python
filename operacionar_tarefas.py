"""
Exercício:

Faça uma lista de 'tarefas' com as seguintes opções:

#Adicionar tarefa
#Listar tarefas
#Opção de desfazer tarefa (a cada vez que chamarmos, desfaz a última)
#Opção de refazer tarefa (a cada vez que chamarmos, refazer a última)

"""

def adicionartarefa():
    tarefaAdicionar = input('Adicionar Tarefa: ')
    listatarefas.append(tarefaAdicionar)
    
def listartarefas():
    return listatarefas
    
def desfazertarefa():
    if len(listatarefas) != 0:
        listacopia.append(listatarefas.pop())
    print(listartarefas())
    return listatarefas  

def refazertarefa(): 
    if len(listacopia) != 0: 
        listatarefas.append(listacopia.pop()) 
    print(listartarefas())
    
listacopia = []
listatarefas = [] 
#Main
loop = True
while loop:
    opcaoUsuario = int(input('1. Adicionar Tarefa\n2. Listar Tarefas\n3. Desfazer Tarefa\n4. Refazer Tarefa\n5. Sair\n'))
    if opcaoUsuario == 1:
        adicionartarefa()
    elif opcaoUsuario == 2:
        print(listartarefas())
    elif opcaoUsuario == 3:
        desfazertarefa()
    elif opcaoUsuario == 4:
        refazertarefa()
    elif opcaoUsuario == 5:
        loop = False
