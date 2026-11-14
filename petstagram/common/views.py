from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.shortcuts import resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Comment
from petstagram.common.models import Like
from petstagram.photos.models import Photo
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page_view(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET or None)

    if search_form.is_valid() and search_form.cleaned_data['pet_name']:
        all_photos = all_photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
        ).distinct()



    photos_per_page = 1
    paginator = Paginator(all_photos, photos_per_page)
    page = request.GET.get('page')

    try:
        all_photos = paginator.page(page)
    except PageNotAnInteger:
        all_photos = paginator.page(1)
    except EmptyPage:
        all_photos = paginator.page(paginator.num_pages)

    context = {
        'all_photos': all_photos,
        "comment_form": comment_form,
        "search_form": search_form,
    }

    return render(request, 'common/home-page.html', context = context)

class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')


        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name).distinct()

        return queryset




@login_required
def like_functionality(request, photo_id):
    liked_object = Like.objects.filter(to_photo_id = photo_id, user = request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(to_photo_id = photo_id, user = request.user,)

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    link = f'{request.META["HTTP_HOST"]}{resolve_url("photos:details", photo_id)}'
    copy(link)

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

@login_required()
def add_comment(request, photo_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        photo = Photo.objects.get(pk = photo_id)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


