from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views.generic import ListView
# from django.views.generic import DetailView
# from django.views.generic import CreateView
# from django.views.generic import DeleteView
# from django.views.generic import UpdateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Book

# Create your views here.
class ListBookView(ListView):
    template_name = 'book/book_list.html'
    model         = Book

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model         = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model         = Book
    fields        = ('title', 'text', 'category')
    success_url   = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model         = Book
    success_url   = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    template_name = 'book/book_update.html'
    model         = Book
    fields        = ('title', 'text', 'category')
    success_url   = reverse_lazy('list-book')

# renderについて
# Django内部では、requestオブジェクトを受け取り、responseオブジェクトを返す。
# renderの第一引数は、request
# renderの第二引数は、表示するtemplate
# renderの第三引数は、使うデータの指定
def index_view(request):
    # object_list = Book.objects.all() 一覧表示
    object_list = Book.objects.order_by('category') # カテゴリによるソート
    return render(request, 'book/index.html', {'object_list':object_list})