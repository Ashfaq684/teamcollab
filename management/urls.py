from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'projectmembers', ProjectMemberViewSet)
router.register(r'projects/(?P<project_id>\d+)/tasks', TaskViewSet, basename='project-tasks')
router.register(r'tasks', TaskViewSet)
router.register(r'tasks/(?P<task_id>\d+)/comments', CommentViewSet, basename='task-comments')
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
