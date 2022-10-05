from django.urls import path

#from .views import book_list, book_create, book
from .views import BookCreate, BookList

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    #path('<int:pk>', book)
]
