from rest_framework import serializers

from apps.todolist.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id','performing', 'title', 'description', 'image',
                  'is_completed', 'created_at')
        