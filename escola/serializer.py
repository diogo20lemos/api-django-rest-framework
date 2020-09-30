from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunosSerializer(serializers.ModelSerializer):
    class meta:
        model = Aluno 
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

        
class CursoSerializer(serializers.ModelSerializer):
    class meta:
        model = Curso 
        fields = '__all__'
        