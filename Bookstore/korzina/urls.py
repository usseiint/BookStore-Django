from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from korzina.models import Books
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url('', ListView.as_view(queryset=Books.objects.all(),template_name="korzina/post.html"))
]