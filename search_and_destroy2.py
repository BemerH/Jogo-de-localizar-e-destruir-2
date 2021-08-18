import random

campo_tamanho = 4 #Global

def colocandoBola(campo):
    #campo_tamanho = 5 Global
    
    tem_bola = False
    
    campo_linha_X = 0
    campo_coluna_X = 0
    
    for i in range(campo_tamanho):
        for j in range(campo_tamanho):
            if campo[i][j] == 'O':
                tem_bola = True
            elif campo[i][j] == 'X':
                campo_linha_X = i
                campo_coluna_X = j
                
    if tem_bola == False:
        while True:
            campo_linha_O = random.randint(0,campo_tamanho-1)
            campo_coluna_O = random.randint(0,campo_tamanho-1)
            
            if campo_linha_O != campo_linha_X or campo_coluna_O != campo_coluna_X:
                campo[campo_linha_O][campo_coluna_O] = 'O'
                break

def campoJogo(campo):
    
    #campo_tamanho = 5 Global
    
    for i in range(campo_tamanho):
        for j in range(campo_tamanho):
            print(campo[i][j], end = '')
            if j != campo_tamanho-1:
                print(' - ', end = '')
        print()
        
def preenchendoCampo(campo):
    
    #campo_tamanho = 4 Global
    
    while True:
        
        campo_linha_X = random.randint(0,campo_tamanho-1)
        campo_coluna_X = random.randint(0,campo_tamanho-1)
        campo_linha_O = random.randint(0,campo_tamanho-1)
        campo_coluna_O = random.randint(0,campo_tamanho-1)
        
        if campo_linha_X != campo_coluna_X or campo_coluna_X != campo_coluna_O:
            campo[campo_linha_X][campo_coluna_X] = 'X'
            campo[campo_linha_O][campo_coluna_O] = 'O'
            break

"--------------------------------------------------"      
          
def controleJogo(entrada,campo):
    linha_coluna = [0,0]
    
    auxControleJogo(campo,linha_coluna)
    
    if entrada == 'W':
        moveUp(campo,linha_coluna)
    elif entrada == 'S':
        moveDown(campo,linha_coluna)
    elif entrada == 'A': 
        moveLeft(campo,linha_coluna)
    elif entrada == 'D':
        moveRight(campo,linha_coluna)
          
def auxControleJogo(campo,linha_coluna):
    #campo_tamanho = 5 Global
    
    for i in range(campo_tamanho):
        for j in range(campo_tamanho):
            if campo[i][j] == 'X':
                linha_coluna[0] = i
                linha_coluna[1] = j
                campo[i][j] = ''

"--------------------------------------------------"

def moveUp(campo,linha_coluna):
    auxMoves(campo,linha_coluna,0,0,1,0)
    #Feito VVV . Percebi que poderia usar uma função
    #economizei 12 linhas de codigo
    """
    if linha_coluna[0] != 0:
        campo[linha_coluna[0]-1][linha_coluna[1]] = 'X'
    else:
        campo[linha_coluna[0]][linha_coluna[1]] = 'X'
    """
def moveDown(campo,linha_coluna):
    auxMoves(campo,linha_coluna,0,4,-1,0)
    
def moveLeft(campo,linha_coluna):
    auxMoves(campo,linha_coluna,1,0,0,1)
   
def moveRight(campo,linha_coluna):
    auxMoves(campo,linha_coluna,1,4,0,-1)

def auxMoves(campo,linha_coluna,linha_ou_coluna,fim_tabela,move_up_down,move_left_right):

    if linha_coluna[linha_ou_coluna] != fim_tabela:
        campo[linha_coluna[0] - move_up_down][linha_coluna[1] - move_left_right] = 'X'
    else:
        campo[linha_coluna[0]][linha_coluna[1]] = 'X'
        
"--------------------------------------------------"

campo = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
preenchendoCampo(campo)

while True:
    colocandoBola(campo)
    
    campoJogo(campo)
    
    entrada = input('Type W,A,S,D:')
    
    if(entrada == '0'):
        break
    elif entrada == 'W' or entrada == 'A' or entrada == 'S' or entrada == 'D':
        controleJogo(entrada,campo)
    else:
        print("Are u kidding me? Type correctly please")