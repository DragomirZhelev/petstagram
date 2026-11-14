from django.shortcuts import render, redirect, get_object_or_404
from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm


# Create your views here.
def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        form.save_m2m()
        return redirect('common:home')

    context = {'form': form}

    return render(request, 'photos/photo-add-page.html', context)

def photo_details_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    likes = photo.likes.all()
    comments = photo.comments.all()

    is_liked_by_user = False

    if request.user.is_authenticated:
        is_liked_by_user = photo.likes.filter(user = request.user).exists()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'is_liked_by_user': is_liked_by_user,
    }

    return render(request, 'photos/photo-details-page.html', context)



def photo_edit_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)

    if form.is_valid():
        form.save()
        return redirect('photos:details', photo.pk)

    context = {'form': form,
               'photo': photo}

    return render(request, 'photos/photo-edit-page.html', context)

def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('common:home')

