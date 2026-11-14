from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetDeleteForm
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
# def pets_add_view(request):
#     form = PetForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('common:home')
#
#     context = {'form': form}
#
#     return render(request, 'pets/pet-add-page.html', context)

class AddPetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile_details', kwargs={'pk': self.request.user.pk},)


# def pets_details_view(request, username, pet_slug):
#
#     pet = get_object_or_404(Pet, slug=pet_slug)
#     comment_form = CommentForm()
#
#     context = {'pet': pet,
#                'all_photos': pet.tagged_pets.all(),
#                'comment_form': comment_form}
#
#     return render(request, 'pets/pet-details-page.html', context)

class PetDetailsView(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_queryset(self):
        return super().get_queryset().filter(user_id = self.kwargs['user_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.tagged_pets.all()
        context['comment_form'] = CommentForm()
        return context



#
# def pets_edit_view(request, username, pet_slug):
#     pet = get_object_or_404(Pet, slug=pet_slug)
#     if request.method == 'GET':
#         form = PetForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetForm(request.POST, request.FILES, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pets:details', username, pet_slug)
#     context = {'form': form}
#
#     return render(request, 'pets/pet-edit-page.html', context)

class EditPetView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy('pets:details', kwargs={'user_pk': self.kwargs['user_pk'],
                                                            'pet_slug': self.kwargs['pet_slug']})



# def pets_delete_view(request, username, pet_slug):
#     pet = get_object_or_404(Pet, slug=pet_slug)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('common:home')
#     form = PetDeleteForm(initial=pet.__dict__)
#     context = {'form': form}
#
#     return render(request, 'pets/pet-delete-page.html', context)


class DeletePetView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('common:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = PetDeleteForm(instance=self.object)

        return context


