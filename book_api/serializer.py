from django.forms import ValidationError
from rest_framework import serializers

from book_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    # Creating additional fields that depend on additional proprieties
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    # Creating function to perform data validation on an attribute
    def validate_number_of_pages(self, value):
        if value < 50:
            raise ValidationError(
                "Books with less than 50 pages can't be added to the database")
        return value

    # Creating function to validate whole object
    def validate(self, data):
        if data['number_of_pages'] > 200 and data['quantity'] > 200:
            raise ValidationError('Too heavy for inventory')
        return data

    # Adding the description to the database
    def get_description(sef, data):
        return f"This book is called {data.title} and it is {data.number_of_pages} pages long."
