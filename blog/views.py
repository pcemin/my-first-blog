from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
me = User.objects.get(username='piero')



def post_list(request):
	articoli=Post.objects.filter(author=me)

	return render(request, 'blog/post_list.html', {'posts':articoli})
