from django.urls import path
from . import views

app_name = 'polls' # namespacing urls
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: polls/26/
    path('<int:pk>/', views.DeatilView.as_view(), name='detail'),
    # ex: polls/26/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: polls/26/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
