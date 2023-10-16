from rest_framework import serializers
from task.serializers import TaskSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'notes',
            'status',
            'creator',
            'end_time',
            'tasks',
            'created_on',
            'updated_on',
        )
