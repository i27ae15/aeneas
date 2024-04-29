from django.urls import path
from task.view.section import SectionAPIView

app_name = 'task'

urlpatterns = [
    path('section/<int:pk>/', SectionAPIView.as_view(), name='section'),
    path('section/', SectionAPIView.as_view(), name='section')
]
