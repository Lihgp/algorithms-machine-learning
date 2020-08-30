## Introdução
Algoritmo feito em python para calcular distância euclidiana e distância manhattan em base de dados.

## Tecnologias utilizadas:
* Python 3.6.9
* Pandas 1.1.1

## Executar o programa
Todos os comandos listados a seguir devem ser executados a partir da raíz do projeto.

Para executar o programa é necessário passar 2 variáveis como argumento:
```
    python3 distance.py "nome_arquivo_csv.csv" tipo_distancia
```

"nome_arquivo_csv" = é o nome do arquivo csv que será utilizado como base. Esse arquivo deve estar dentro da pasta raíz do projeto.

tipo_distancia = é um número inteiro que identifica se a distância será euclidiana ou manhattan. 1- Euclidiana 2- Manhattan.

Exemplo para calcular a distância euclidiana através da base Iris que está na raíz do projeto:
```
    python3 distance.py "iris.csv" 1
```

Após executar essa linha de código com exito será criado um arquivo na raíz do projeto com o nome "distancias.csv"
