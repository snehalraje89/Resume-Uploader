from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='Home_page'),
    path('<int:pk>',views.CandidateView.as_view(),name='candidate_page')
]