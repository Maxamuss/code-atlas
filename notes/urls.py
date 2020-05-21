from django.urls import path

from . import views, api


urlpatterns = [
    path('', views.NotesView.as_view(), name='notes'),
    path('mode/edit/', views.NotesEditModeView.as_view(), name='notes_edit_mode'),
    path('mode/tags/', views.NotesTagModeView.as_view(), name='notes_tag_mode'),
    path('create/', views.CreateNoteView.as_view(), name='create_note'),
    path('create/clone/<pk>/', views.CloneNoteView.as_view(), name='clone_note'),
    path('view/<pk>/', views.ViewNoteView.as_view(), name='view_note'),
    path('edit/<pk>/', views.EditNoteView.as_view(), name='edit_note'),
    path('delete/<pk>/', views.DeleteNoteView.as_view(), name='delete_note'),
    # API views
    # path('api/', api.NotesListView.as_view()),
    path('api/public/', api.NotesMakePublicView.as_view()),
    path('api/private/', api.NotesMakePrivateView.as_view()),
    path('api/tags/', api.NotesAddTagsView.as_view()),
    path('api/delete/', api.NotesDeleteView.as_view()),
]