from django.urls import path
#from .views import book_list, book_create, book
from .views import BookList

urlpatterns = [
    #path('', book_create),
    path('list/', BookList.as_view()),
    #path('<int:pk>', book)
]
