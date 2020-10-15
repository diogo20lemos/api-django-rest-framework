from django.http import JsonResponse
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.serializer import (
    AlunoSerializer, 
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunosSerializer,
    ListaAlunosMatriculadosSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas""" 
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos""" 
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

       
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todos as Matriculas""" 
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]
       

class ListaMatriculaAluno(generics.ListAPIView):
    """Listando as matriculas de aluno""" 

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return  queryset
    serializer_class = ListaMatriculasAlunosSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando alunos e alunas matriculados em curso """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]
