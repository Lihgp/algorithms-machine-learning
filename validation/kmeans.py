import pandas as pd
import numpy as np

def distancia_euclidiana(v1,v2):
    return sum([(x-y)**2 for (x,y) in zip(v1,v2)])**(0.5)

def calculo_distancia(array_dados, array_centroides):
    data = []
    for x in range(len(array_dados)):
        row = []
        for y in range(len(array_centroides)):
            row.append(distancia_euclidiana(array_dados[x],array_centroides[y]))
        data.append(row)
    return pd.DataFrame(data)

def k_means(data, k):
    # Escolhe aleatoriamente os centroides
    centroides = data.sample(k)

    #DataFrame para armazenar os centroides antigos
    antigos_centroides = pd.DataFrame()

    #DataFrame para armazenar as distâncias
    distancias = pd.DataFrame()
    max = 0

    while not antigos_centroides.equals(centroides) or max > 100:
        # Converte os DataFrame para array para ser trabalhado mais facilmente
        array_dados = data.values.tolist()
        array_centroides = centroides.values.tolist()

        # Calcula as distâncias entre os objetos e os centroides e armazena em um DataFrame
        distancias = calculo_distancia(array_dados, array_centroides)
        
        # Cria uma nova coluna no DataFrame para armazenar em qual grupo o objeto pertence
        data['Grupo'] = distancias.idxmin(axis=1)
        antigos_centroides = centroides

        centroides = pd.DataFrame()
        
        # Calcula os novos centroides
        novos_centroides = data.groupby('Grupo').agg(np.mean)

        #Armazena os novos centroides na variável que está sendo utilizada
        centroides[novos_centroides.columns] = novos_centroides[novos_centroides.columns]
        max+=1

    return data
