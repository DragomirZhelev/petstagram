from django.urls import path, include

from petstagram.pets import views

app_name = 'pets'

urlpatterns = [
    # path('add/', views.pets_add_view, name = 'add'),
    path('add/', views.AddPetView.as_view(), name = 'add'),

    path('<int:user_pk>/pet/<slug:pet_slug>/', include([
        # path('', views.pets_details_view, name = 'details'),
        path('', views.PetDetailsView.as_view(), name = 'details'),
        # path('edit/', views.pets_edit_view, name = 'edit'),
        path('edit/', views.EditPetView.as_view(), name = 'edit'),

        # path('delete/', views.pets_delete_view, name = 'delete'),

        path('delete/', views.DeletePetView.as_view(), name = 'delete'),
    ])),
]

