from django.urls import path
from task.view.section import SectionAPIView
from task.view.objective import ObjectiveAPIView

app_name = 'task'

urlpatterns = [
    path('section/<int:pk>/', SectionAPIView.as_view(), name='section'),
    path('section/', SectionAPIView.as_view(), name='section'),
    path('objective/<int:pk>/', ObjectiveAPIView.as_view(), name='objective'),
    path('objective/', ObjectiveAPIView.as_view(), name='objective')
]
