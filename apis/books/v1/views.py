from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apis.books.v1.serializer import BookReadOnlySerializer, BookWOSerializer
from modules.errors import ERRORS
from modules.pagination import get_paginated_response
from services.BookService import BookService


class BookViewSet(viewsets.GenericViewSet):
    """
        this viewsets is for the books
        list out all the books, add book, retrieve books
    """
    permission_classes = ()
    authentication_classes = ()
    book_service = BookService()

    def list(self, request):
        queryset = self.book_service.list_book()
        return get_paginated_response(
            pagination_class=PageNumberPagination,
            serializer_class=BookReadOnlySerializer,
            queryset=queryset,
            request=request,
            view=self
        )

    def retrieve(self, request, book_id):
        qs = self.book_service.get_book(book_id)

        if not qs:
            return Response({
                'message': ERRORS['NO_BOOK']
            })

        serializer = BookReadOnlySerializer(qs.first())
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):

        data = request.data
        serializer = BookWOSerializer(data=data,
                                      context={'request': request, 'service': self.book_service})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.data)
            return Response(
                {
                    'success': True,
                    'message': "New Book Added",
                    'data': serializer.data

                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)
