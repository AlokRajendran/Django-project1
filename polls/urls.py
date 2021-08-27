from django.urls import path
from django.views.generic.detail import DetailView
from .import views

app_name = "polls" 

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/', views.questions, name='questions'),

    path('<int:pk>/', views.Detail.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.Results.as_view(), name = 'results')
]