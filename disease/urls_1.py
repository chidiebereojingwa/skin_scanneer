
from django.urls import path

from . import views

app_name = 'disease'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('contact/', views.contact, name='contact'),
    # ex: /polls/5/
    path('information/', views.information, name = 'information'),

    path('help/',views.help, name ='help'),

    path('seedoctor/',views.seedoctor,name = 'seedoctor'),

    path('uploadskin/', views.uploadskin, name='uploadskin'),
    # ex: /polls/5/results/
    path('resultsskin/', views.resultsskin, name='resultsskin'),

]
