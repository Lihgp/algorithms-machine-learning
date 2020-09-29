import pandas as pd
import sys
import numpy as np
import os
from kmeans import k_means

def read_csv(name_csv):
    df = pd.read_csv(name_csv, header=None)
    return df
   
def save(df,dfpath):
    if not os.path.isfile(dfpath):
        df.to_csv(dfpath, index = None)
    else:
        df.to_csv(dfpath, mode = 'a', index = None)

def calcula_pureza(data, qtd_grupos):
    # Exclui a coluna 'Grupo' para ser melhor manipulada a seguir
    data_temp = data.drop('Grupos', axis = 1, inplace = False)

    # Guarda o maior valor de cada linha e a soma de todos os valores de cada linha para depois calcular a pureza de cada grupo
    purezaList = []
    for index in range(0, qtd_grupos):
        max_value = data_temp.loc[index].max()
        sum_value = data_temp.loc[index].sum()
        pureza = max_value/sum_value
        purezaList.append(pureza)
    
    # Adiciona a coluna 'Pureza' no Dataframe
    data['Pureza'] = purezaList

    # Adiciona o resultado no arquivo csv
    save(data, 'resultados.csv')

# Função para montar a estrutura para podermos calcular a pureza
def montar_estrutura(df, classeList, qtd_grupos):
    # Cria o Dataframe
    data = pd.DataFrame()
    # Adiciona a coluna 'Grupo' no Df
    grupos = [x for x in range(1, qtd_grupos+1)]
    data['Grupos'] = grupos

    # Adiciona os valores nas colunas da classe
    for classe in classeList:
        valores = []
        for index in range(0, qtd_grupos):
            # Pega o valor da contagem da classe e do grupo específico para adicionar no Dataframe estruturado
            valor_contagem = df.loc[(df['Classe'] == classe) & (df['Grupo'] == index)]['Contagem'].values.tolist()
            if len(valor_contagem) == 0:
                valor_contagem = 0
            else:
                valor_contagem = valor_contagem[0]
            valores.append(valor_contagem)

        # Adiciona os valores da contagem em cada tipo da classe
        data[classe] = valores

    return data

def validar_agrupamento(df):
    # Calcula kmeans quando K=2, K=3, K=4
    for i in range(2,5):
        # Remove a última coluna, pois ela é a classe, vou utilizar ela para o algoritmo kmeans
        data_sem_classe = df.drop(df.columns [-1], axis = 1, inplace = False)

        # Chama a função para realizar o kmeans
        data = k_means(data_sem_classe,i)

        # Adiciona a coluna "Classe" de volta ao Dataframe
        data['Classe'] = df[df.columns[-1]]
        
        # Agrupa por 'Classe' e 'Grupo'
        grouped_df = data.groupby( [ "Classe", "Grupo"] )

        # Converte o objeto para Dataframe e calcula a contagem em cada grupo
        data_contagem = pd.DataFrame(grouped_df.size().reset_index(name = "Contagem"))

        # Guarda em uma variável todos os tipos de classe, removendo aquelas repetidas por estarem em mais de um grupo 
        classeList = sorted(set(data_contagem['Classe'].values.tolist()))

        # Monta uma estrutura de Dataframe para calcular a pureza
        data_estrutura = montar_estrutura(data_contagem, classeList,i)

        # Calcula a pureza
        data_pureza = calcula_pureza(data_estrutura, i)

if __name__ == '__main__':
    # Chama a função para ler um arquivo csv
    df = read_csv(sys.argv[1])

    validar_agrupamento(df)
