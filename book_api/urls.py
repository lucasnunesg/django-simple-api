from django.urls import path

from .views import BookCreate, BookDetail, BookList

urlpatterns = [
    path('', BookCreate.as_view(), name='book_create'),
    path('list/', BookList.as_view(), name='book_list'),
    path('<int:pk>', BookDetail.as_view(), name='book_details')
]
