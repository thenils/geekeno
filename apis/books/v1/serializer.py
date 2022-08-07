from rest_framework import serializers

from books.models import Books


class BookReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookWOSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=135)
    author = serializers.CharField(max_length=135)

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data['name']
        author = validated_data['author']

        books = self.context['service']

        book = books.create_book(name=name, author=author)

        return book
