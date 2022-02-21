# BibliotecaApi

Para executar o projeto é necessário criar uma virtual env com o django rest framework e criar um superuser

Para realizar a autenticação entrar no /admin realizar o login com o superuser e criar um novo usuário, passar as credenciais de autenticação no header Authorization.
O projeto usa o Basic Authorization

Endpoints:
/livros - aceita os metodos get para trazer a lista de livros e post para inserir um novo livro, também é possivel acessar um unico livro passando o id do livro "/livros/id"
Para inserir um novo livro usar o formato
{
    "nome":"Nome Exemplo",
    "autor":"Autor Exemplo",
    "categoria":"1", //id da categoria
    "nr_paginas":"100"
}
/categorias - aceita os metodos get para trazer a lista de categorias e post para inserir uma nova categoria, também é possivel acessar uma unica categoria passando o id da categoria "/categorias/id"
Para inserir uma nova categoria usar o formato
{
    "nome":"Exemplo"
}
/catalogo - Aceita o metodo get para trazer o catalogo de livros do usuario autenticado
/catalogo/addlivro - aceita o metodo POST, adiciona um novo livro no catalogo do usuario autenticado
{
    "id":"1" //id do livro
}
/catalogo/removelivro - aceita o metodo POST, remove um livro do catalogo do usuario autenticado
{
    "id":"1" //id do livro
}
