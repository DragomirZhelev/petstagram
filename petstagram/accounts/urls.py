from django.urls import path, include

from petstagram.accounts import views


app_name = 'accounts'
urlpatterns = [
    # path('register/', views.register, name='register'),

    path('register/', views.RegisterUserView.as_view(), name='register'),

    # path('login/', views.login, name='login'),

    path('login/', views.AppUserLoginView.as_view(), name='login'),

    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', include([

        path('', views.ProfileDetailsView.as_view(), name='profile_details'),
        # path('edit/', views.edit_profile, name='profile_edit'),

        path('edit/', views.ProfileEditView.as_view(), name='profile_edit'),

        # path('delete/', views.delete_profile, name='profile_delete'),

        path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    ])),
]

