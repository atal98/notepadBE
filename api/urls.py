from django.contrib import admin
from django.urls import path
from api.views import Routes, NotesAPI,NoteAPI

urlpatterns = [
    path('routes/',
         Routes.as_view(),
         name='routes'
    ),
    path('notes/',
         NotesAPI.as_view(),
         name='notes'
    ),
    path('notes/<int:pk>/',
         NoteAPI.as_view(),
         name='note'
    )
]
