from django.urls import path, include
from . import views


app_name = 'mysite'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:question_id>/", views.detail, name='detail'),
    path("create/<int:question_id>/", views.create, name='create'),
    path("question_create/", views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]