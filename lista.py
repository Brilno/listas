produtos = [
    [1, "óleo", 7],
    [2, "arroz", 29],
   [3, "feijão", 8],
];
print(produtos);

id_procurado = 2
for produto in produtos:
    if produto[0] == id_procurado:
        print(produto);
 
 
 
for indice, produto in enumerate(produtos):
    if produto[0] == id_procurado:
        removido = produtos.pop(indice)
        print("Registro removido:", removido)
        print(produtos);
  