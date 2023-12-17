from django.urls import path
from . import views

urlpatterns = [
    # function-based view
    path('', views.index_view, name='index'),
    # path('logout/', views.logout_view, name='logout'),
    # class-based view
    path('book', views.ListBookView.as_view(), name='list-book'),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'),
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
]
