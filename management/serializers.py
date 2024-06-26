from rest_framework import serializers
from .models import User, Project, ProjectMember, Task, Comment
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_username', 'created_at']


class ProjectMemberSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'project_name', 'user', 'user_username', 'role']


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name')
    assigned_to_username = serializers.ReadOnlyField(source='assigned_to.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'assigned_to_username', 'project', 'project_name', 'created_at', 'due_date']

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    task_title = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'user_username', 'task', 'task_title', 'created_at']
