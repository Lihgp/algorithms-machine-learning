## Introdução
Algoritmo feito em python para implementar o algoritmo K-means. O código foi comentado para melhor entendimento.

## Tecnologias utilizadas:
* Python 3.6.9
* Pandas 1.1.1

## Executar o programa
Todos os comandos listados a seguir devem ser executados a partir da raíz do projeto.

Para executar o programa é necessário passar 2 variáveis como argumento:
```
    python3 kmeans.py "nome_arquivo_csv.csv" numero_grupos(k)
```

"nome_arquivo_csv" = é o nome do arquivo csv que será utilizado como base. Esse arquivo deve estar dentro da pasta raíz do projeto.

numero_grupos(k) = é um número inteiro que significa a quantidade de grupos (K) que vamos utilizar.

Exemplo para implementar o algoritmo k-means através da base Iris que está na raíz do projeto:
```
    python3 kmeans.py "iris.csv" 5
```

Após executar essa linha de código com exito será criado um arquivo na raíz do projeto com o nome "kmeans_resultados.csv". 

## Observações:
* Cada linha significa um objeto.
* A última coluna deste arquivo, de nome "Grupo", é referente ao grupo em que o objeto pertence. 
* Os grupos são nomeados de 0 até K-1. Ou seja, se o valor entrado de K = 10, os grupos nomeados serão de 0 até 9.