def crearMatrizC(filas,columnas): #relleno con ceros (en blanco)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            matriz[f].append("0")
    return matriz

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

def ganoX(matriz):
    
    ganooX = False
    
    if(matriz[0][0]=="X")and(matriz[0][1]=="X")and(matriz[0][2]=="X"):
        ganooX = True
    elif(matriz[0][0]=="X")and(matriz[1][1]=="X")and(matriz[2][2]=="X"):
        ganooX = True
    elif(matriz[0][0]=="X")and(matriz[1][0]=="X")and(matriz[2][0]=="X"):
        ganooX = True
    elif(matriz[0][1]=="X")and(matriz[1][1]=="X")and(matriz[2][1]=="X"):
        ganooX = True
    elif(matriz[0][2]=="X")and(matriz[1][2]=="X")and(matriz[2][2]=="X"):
        ganooX = True
    elif(matriz[0][1]=="X")and(matriz[1][1]=="X")and(matriz[2][1]=="X"):
        ganooX = True
    elif(matriz[0][2]=="X")and(matriz[1][2]=="X")and(matriz[2][2]=="X"):
        ganooX = True
    elif(matriz[0][2]=="X")and(matriz[1][1]=="X")and(matriz[2][0]=="X"):
        ganooX = True
    return ganooX

def ganoO(matriz):
    
    ganooO = False
    
    if(matriz[0][0]=="O")and(matriz[0][1]=="O")and(matriz[0][2]=="O"):
        ganooO = True
    elif(matriz[0][0]=="O")and(matriz[1][1]=="O")and(matriz[2][2]=="O"):
        ganooO = True
    elif(matriz[0][0]=="O")and(matriz[1][0]=="O")and(matriz[2][0]=="O"):
        ganooO = True
    elif(matriz[0][1]=="O")and(matriz[1][1]=="O")and(matriz[2][1]=="O"):
        ganooO = True
    elif(matriz[0][2]=="O")and(matriz[1][2]=="O")and(matriz[2][2]=="O"):
        ganooO = True
    elif(matriz[0][1]=="O")and(matriz[1][1]=="O")and(matriz[2][1]=="O"):
        ganooO = True
    elif(matriz[0][2]=="O")and(matriz[1][2]=="O")and(matriz[2][2]=="O"):
        ganooO = True
    elif(matriz[0][2]=="O")and(matriz[1][1]=="O")and(matriz[2][0]=="O"):
        ganooO = True
    return ganooO

def validacionMov(matriz, a, pos):
    valido = True
    if(matriz[pos[0]][pos[1]]=="X")or(matriz[pos[0]][pos[1]]=="O"):
        valido = False
    return valido

def sumarX(matriz,pos):
    matriz[pos[0]][pos[1]] = "X"

def sumarO(matriz,pos):
    matriz[pos[0]][pos[1]] = "O"

def jugarr():
    ttt = crearMatrizC(3,3)

    i = 1
    ganooX = False
    ganooO = False
    a = "X"
    pos = [0,0]
    mostrarMatrizEnc(ttt)
    while(i<9)and(ganooX!=True)and(ganooO!=True):
        if(i%2)==0:
            print("Turno de las X...")
            a = "X"
        else:
            print("Turno de los O...")
            a = "O"
            
        pos[0] = int(input("Ingrese la fila que desea marcar: "))-1
        pos[1] = int(input("Ingrese la columna que desea marcar: "))-1
        
        valido = validacionMov(ttt,a,pos)
        
        if(valido!=True):
            while(valido==False):
                print(f"La posicion indicada es invalida, ingrese una nueva posicion valida para {a}: ")
                mostrarMatrizEnc(ttt)
                pos[0] = int(input("Ingrese la fila que desea marcar: "))-1
                pos[1] = int(input("Ingrese la columna que desea marcar: "))-1
                valido = validacionMov(ttt,a,pos)
        
        if(a == "X"):
            sumarX(ttt,pos)
            ganooX = ganoX(ttt)
        else:
            sumarO(ttt,pos)
            ganooO = ganoO(ttt)
        
            
        mostrarMatrizEnc(ttt)
        
        i=i+1
    
    print("Ganaste Felicitaciones!")
    
jugarr()
j = int(input("Desea volver a jugar? Ingrese 1 si desea volver a jugar y 2 si desea terminar el juego: "))
while(j==1):
    jugarr()
    j = int(input("Desea volver a jugar? Ingrese 1 si desea volver a jugar y 2 si desea terminar el juego: "))
    
print("Gracias por jugar vuelva prontosss!")
    

