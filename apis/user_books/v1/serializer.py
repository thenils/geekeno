from rest_framework import serializers

from apis.books.v1.serializer import BookReadOnlySerializer
from users.models import MyBooks


class ReadlingBookReadOnlySerializer(serializers.ModelSerializer):
    book = BookReadOnlySerializer(read_only=True)

    class Meta:
        model = MyBooks
        fields = '__all__'


class ReadingBookWOSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(required=False)
    is_deleted = serializers.BooleanField(required=False)
    is_reading = serializers.BooleanField(required=False)
    add_book = serializers.BooleanField(required=False)
    book_name = serializers.CharField(max_length=135, required=False)
    author_name = serializers.CharField(max_length=135, required=False)

    def create(self, validated_data):

        book_service = self.context['book_service']
        reading_book_service = self.context['reading_book_service']
        user = self.context['user']

        book = None

        if 'book_id' in validated_data:
            book = book_service.get_book(int(validated_data['book_id']))
            if not book:
                raise serializers.ValidationError({'filed': 'book', 'message': 'book not found!'})

            book = book[0]

        if not book and 'add_book' in validated_data:
            if not 'book_name' in validated_data or not 'author_name' in validated_data:
                raise serializers.ValidationError({
                    'book name and author name is required to add book'
                })
            book_name = validated_data['book_name']
            author_name = validated_data['author_name']

            book = book_service.create_book(book_name, author_name)

        if reading_book_service.book_exists(user, book):
            raise serializers.ValidationError('this book is already exist in you reading list')

        reading_book = reading_book_service.add_book_to_read_list(user, book)

        return reading_book

    def update(self, validated_data):
        reading_book_service = self.context['reading_book_service']
        user = self.context['user']
        reading_book_id = self.context['reading_book_id']

        data = {}
        if 'is_reading' in validated_data:
            data['is_reading'] = validated_data['is_reading']
        if 'is_deleted' in validated_data:
            data['is_deleted'] = validated_data['is_deleted']

        if not data:
            raise serializers.ValidationError({'nothing has to update'})

        return reading_book_service.update_reading_book(user, reading_book_id, data)


