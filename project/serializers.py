from rest_framework import serializers
from task.serializers import TaskSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=False)

    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'notes',
            'status',
            'creator',
            'tasks',
            'created_on',
            'updated_on',
        )
