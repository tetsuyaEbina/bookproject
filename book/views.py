from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
from .models import Book, Review

# Create your views here.
# codeは左側から実行される為、順番も留意する
class ListBookView(LoginRequiredMixin, ListView):
    template_name = 'book/book_list.html'
    model         = Book

class DetailBookView(LoginRequiredMixin, DetailView):
    template_name = 'book/book_detail.html'
    model         = Book

class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = 'book/book_create.html'
    model         = Book
    fields        = ('title', 'text', 'category', 'thumbnail')
    success_url   = reverse_lazy('list-book')

class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model         = Book
    success_url   = reverse_lazy('list-book')

class UpdateBookView(LoginRequiredMixin, UpdateView):
    template_name = 'book/book_update.html'
    model         = Book
    fields        = ('title', 'text', 'category', 'thumbnail')
    success_url   = reverse_lazy('list-book')

class CreateReviewView(LoginRequiredMixin, CreateView):
    model         = Review
    fields        = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'
    # CreateViewのget_context_dataを上書きする
    def get_context_data(self, **kwargs):
        context         = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk':self.object.book.id})

# renderについて
# Django内部では、requestオブジェクトを受け取り、responseオブジェクトを返す。
# renderの第一引数は、request
# renderの第二引数は、表示するtemplate
# renderの第三引数は、使うデータの指定
def index_view(request):
    # object_list = Book.objects.all() 一覧表示
    object_list = Book.objects.order_by('category') # カテゴリによるソート
    return render(request, 'book/index.html', {'object_list':object_list})
