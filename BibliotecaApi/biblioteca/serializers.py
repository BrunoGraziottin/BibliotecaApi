from rest_framework import serializers
from biblioteca.models import Livro, Categoria, Catalogo
from django.contrib.auth import get_user_model # If used custom user model

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class LivroSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Livro
        fields = ('id', 'nome', 'autor', 'categoria', 'nr_paginas')

class CatalogoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(read_only=True, many=True)

    class Meta:
        model = Catalogo
        fields = ('livros',)

class LivroCatalogoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)