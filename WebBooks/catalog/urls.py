from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('authors_add', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('mybooks', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
]