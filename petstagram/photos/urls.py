from django.urls import path, include

from petstagram.photos import views


app_name = 'photos'
urlpatterns = [
    path('add/', views.photo_add_page, name='add_page'),

    path('<int:pk>/', include([
        path('', views.photo_details_view, name='details'),
        path('edit/', views.photo_edit_view, name='edit'),

        path('delete/', views.delete_photo, name='delete'),
    ])),
]