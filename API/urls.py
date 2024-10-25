from django.urls import path
from .views import  getapi, task_list, task_detail, TaskViewSets, BookViewSets, AuthorViewSets
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('hello/', getapi, name='hello'),
    # path('task/', task_list, name='task_list'),
    # path('task/<int:pk>/', task_detail, name='task_detail')
]
router= DefaultRouter()
router.register('task', TaskViewSets, basename='task')
router.register('books', BookViewSets, basename='book')
router.register('author', AuthorViewSets, basename='author')
urlpatterns += router.urls