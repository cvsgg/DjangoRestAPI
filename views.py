from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer
# Mostra ao usuario os dados especificos registrados no bd


class AlunosViewSet (viewsets.ModelViewSet):
    queryset = Aluno.nome.all()
    serializer_class = AlunoSerializer


class CursosViewSet (viewsets.ModelViewSet):
    queryset = Curso.codigo_curso.all()
    serializer_class = CursoSerializer
