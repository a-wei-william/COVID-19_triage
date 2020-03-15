

from django.urls import path
from . import views


app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/next/', views.next, name='next'),
    path('advice/<int:opt>', views.advice, name='advice'),
]

"""
    path('low_risk/', views.low_risk, name='low_risk'),
    path('phone_call/', views.phone_call, name='phone_call'),
    path('hospital_admission/', views.hospital_admission, name='hospital_admission'),
"""