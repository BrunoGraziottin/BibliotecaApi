from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from biblioteca.serializers import LivroCatalogoSerializer
from biblioteca.serializers import LivroSerializer, CategoriaSerializer, CatalogoSerializer
from biblioteca.models import Livro, Categoria, Catalogo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class LivroViewSet(viewsets.ModelViewSet):
    """Listando todos os livros"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    """Listando todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CatalogoViewSet(viewsets.ModelViewSet):
    """Listando todos os livros"""
    serializer_class = CatalogoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Catalogo.objects.filter(usuario=user)
    
    def visualiza_catalogo(self, request):
        catalogo = Catalogo.objects.filter(usuario=request.user) 
        if not catalogo:
            catalogo = Catalogo.objects.create(usuario=request.user)

        serializer = CatalogoSerializer(catalogo.get())
        return Response(serializer.data)

    def add_livro(self, request):
        serializer = LivroCatalogoSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        queryset = Livro.objects.all()
        if serializer.data.get('id', ''):
            livro = get_object_or_404(queryset, pk=serializer.data.get('id'))
        else:
            return Response("Informe o id do livro")
        queryset = Catalogo.objects.all()
        catalogo = get_object_or_404(queryset, usuario=request.user)
        catalogo.livros.add(livro)

        serializer = CatalogoSerializer(catalogo)
        return Response(serializer.data)

    def remove_livro(self, request):
        serializer = LivroCatalogoSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        queryset = Livro.objects.all()
        if serializer.data.get('id', ''):
            livro = get_object_or_404(queryset, pk=serializer.data.get('id'))
        else:
            return Response("Informe o id do livro")
        queryset = Catalogo.objects.all()
        catalogo = get_object_or_404(queryset, usuario=request.user)
        catalogo.livros.remove(livro)

        serializer = CatalogoSerializer(catalogo)
        return Response(serializer.data)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]