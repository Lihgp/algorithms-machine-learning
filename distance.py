import pandas as pd
import sys

def read_csv(name_csv):
    df = pd.read_csv(name_csv, header=None)
    return df
   
def write_csv(name_csv, df):
    df.to_csv(name_csv, header=None, index=None)
    
def distancia_euclidiana(v1,v2): 
    return sum([(x-y)**2 for (x,y) in zip(v1,v2)])**(0.5)

def distancia_manhattan(v1,v2):
    return sum([(x-y) for (x,y) in zip(v1,v2)])

def calculo_distancia(array, type):
    if (type=='1'):
        data = []
        for x in range(0,len(array)):
            row = []
            for y in range(0,len(array)):
                row.append(distancia_euclidiana(array[x],array[y]))
            data.append(row)
        
        # Converte lista para DataFrame
        df = pd.DataFrame(data)
        write_csv("distancias.csv", df)
        

    elif (type=='2'):
        data = []
        for x in range(0,len(array)):
            row = []
            for y in range(0,len(array)):
                row.append(distancia_manhattan(array[x],array[y]))
            data.append(row)

         # Converte lista para DataFrame
        df = pd.DataFrame(data)
        write_csv("distancias.csv", df)

    else:
        print("Tipo de distância invalida")

if __name__ == '__main__':
    # Chama a função para ler um arquivo csv
    df = read_csv(sys.argv[1])

    # Guarda em uma variável o tipo de cálculo da distância
    type_distance = sys.argv[2]

    # Converte o DataFrame para lista
    array = df.values.tolist()

    calculo_distancia(array,type_distance)


    