from django.urls import path
from task.view.section import SectionAPIView
from task.view.objective import ObjectiveAPIView
from task.view.task import TaskeAPIView

app_name = 'task'

urlpatterns = [
    path(
        'section/<int:section_pk>/',
        SectionAPIView.as_view(),
        name='section'
         ),
    path('section/',
         SectionAPIView.as_view(),
         name='section'
         ),
    path(
        'section/<int:section_pk>/objective/<int:objective_pk>/',
        ObjectiveAPIView.as_view(),
        name='objective'
        ),
    path(
        'section/<int:section_pk>/objective/',
        ObjectiveAPIView.as_view(),
        name='objective'
         ),
    path(
        'section/<int:section_pk>/objective/<int:objective_pk>/task/',
        TaskeAPIView.as_view(),
        name='task'
        ),
    path(
        'section/<int:section_pk>/objective/<int:objective_pk>/task/<int:task_pk>/',
        TaskeAPIView.as_view(),
        name='task'
        )
]
