## Introdução
* Algoritmo feito em python para implementar o algoritmo de validar a pureza do algoritmo K-means. 
* O código foi comentado para melhor entendimento.
* A implementação foi separada em 2 arquivos. Em um contém toda a implementação necessária do K-means(kmeans.py).
No outro contém toda a implementação necessária para o código de validação (validacao.py).

## Tecnologias utilizadas:
* Python 3.6.9
* Pandas 1.1.1

## Considerações a serem feitas antes de executar o código:
* O código considera a ÚLTIMA coluna do arquivo csv como a CLASSE.
* Desse modo, a implementação irá funcionar somente se a classe da base de dados for a última coluna.

## Executar o programa
Todos os comandos listados a seguir devem ser executados a partir da raíz do projeto.

Para executar o programa:
```
    python3 validacao.py "nome_arquivo_csv.csv"
```

"nome_arquivo_csv" = é o nome do arquivo csv que será utilizado como base. Esse arquivo deve estar dentro da pasta raíz do projeto.

Exemplo para implementar o algoritmo k-means através da base Iris que está na raíz do projeto:
```
    python3 validacao.py "iris.csv"
```

Após executar essa linha de código com exito será criado um arquivo na raíz do projeto com o nome "resultados.csv". 

## Observações:
* Nesse arquivo estará armazenado, em ORDEM, a resposta da execução quando K=2, K=3, K=4.
* No arquivo 'exemplo-execucao.png' é mostrado um exemplo de resposta ao executar esse algoritmo com a Base Iris (iris.csv).
Linha 1-3: Execução quando K=2
Linha 4-7: Execução quando K=3
Linha 8-12: Execução quando K=4