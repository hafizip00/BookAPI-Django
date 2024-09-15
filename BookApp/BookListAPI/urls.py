from django.urls import path, include
from BookListAPI import views

urlpatterns= [
    # path('books/' , views.books)
    path('books/' , views.BookList.as_view()),
    path('book/<int:pk>' , views.Book.as_view())
]