from django.urls import path, include, re_path
from . import views
from django.contrib.auth import authenticate, login

# Include the app name so Django can differentiate between
# URL names between them - both blog and polls apps have 
# 'detail' view.
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('login/', views.user_login, name='login')
]