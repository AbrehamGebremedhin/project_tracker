from rest_framework import serializers
from task.serializers import TaskSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        total = 0
        completed = 0
        for task in instance.tasks.all():
            total += 1
            if task.status:
                completed += 1

        if completed == 0:
            data['Completed_Percentage'] = 0
        else:
            data['Completed_Percentage'] = (completed / total) * 100
        return data

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
