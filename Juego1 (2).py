from random import sample
linea1=[];linea2=[];linea3=[];linea4=[];linea5=[];linea6=[];linea7=[];linea8=[]
lista=['cN','cB','aN','aB','tN','tB','raN','raB','ryN','ryB','  ']
for i in range(8):
    linea1=sample(lista,k=8)
    linea2=sample(lista,k=8)
    linea3=sample(lista,k=8)
    linea4=sample(lista,k=8)
    linea5=sample(lista,k=8)
    linea6=sample(lista,k=8)
    linea7=sample(lista,k=8)
    linea8=sample(lista,k=8)
    print(linea1)
    print(linea2)
    print(linea3)
    print(linea4)
    print(linea5)
    print(linea6)
    print(linea7)
    print(linea8)
    break

 piezas = ["Kw", "Qw", "Rw", "Rw", "Bw", "Bw",
              "Nw", "Nw", "Pw", "Pw", "Pw", "Pw",
              "Pw", "Pw", "Pw", "Pw",
              "Kb", "Qb", "Rb", "Rb", "Bb", "Bb",
              "Nb", "Nb", "Pb", "Pb", "Pb", "Pb",
              "Pb", "Pb", "Pb", "Pb"]
    tablero = ["__" for x in range(64)]
    
    # Generar una seleccion de piezas al azar.
    max = randint(1, len(piezas))
    seleccion = sample(piezas, max)

    for pieza in seleccion:
        # Tomamos una pieza
        while True:
           # Buscamos al azar una casilla vacia
           indice = randint(0, len(tablero) - 1)
           if tablero[indice] == "__":
               # Encontramos una casilla vacia; poblarla y salir
               tablero[indice] = pieza
               break

    # Impresion
    for fila in range(8):
        for columna in range(8):
            print(tablero[fila * 8 + columna], end = " ")
        print() 
        
