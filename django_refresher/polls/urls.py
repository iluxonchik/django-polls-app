from django.urls import path
from . import views

app_name = 'polls' # namespacing urls
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: polls/26/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: polls/26/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: polls/26/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
