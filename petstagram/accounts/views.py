from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.db.models import Count

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petstagram.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()


# def register(request):
#     return render(request, 'accounts/register-page.html')

class RegisterUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('accounts:login')


# def login(request):
#     return render(request, 'accounts/login-page.html')

class AppUserLoginView(LoginView):
    authentication_form = AppUserLoginForm
    template_name = 'accounts/login-page.html'




class AppUserLogoutView(LogoutView):
    pass

# def show_profile_details(request, pk):
#     return render(request, 'accounts/profile-details-page.html')

class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_photos = self.object.photos.order_by('-date_of_publication')
        user_pets = self.object.pets.all()

        total_likes = user_photos.aggregate(total = Count('likes'))['total']

        context['user_photos'] = user_photos
        context['user_pets'] = user_pets
        context['total_likes'] = total_likes

        return context




# def edit_profile(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile_details', kwargs={'pk': self.object.pk})


# def delete_profile(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')

class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('common:home')
