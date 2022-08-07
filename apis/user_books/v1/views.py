from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apis.user_books.v1.serializer import ReadlingBookReadOnlySerializer, ReadingBookWOSerializer
from modules.pagination import get_paginated_response
from services.BookService import BookService
from services.ReadingBookService import MyBookService


class MyReadingViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    book_service = BookService()
    reading_book_service = MyBookService()

    def list(self, request, *args, **kwargs):
        params = request.GET
        is_reading = request.GET.get('is_reading', None)
        is_deleted = request.GET.get('is_deleted', None)
        filter = {}
        if is_reading:
            filter['is_reading'] = False
            if is_reading == 'true':
                filter['is_reading'] = True

        if is_deleted:
            filter['is_deleted'] = False
            if is_deleted == 'true':
                filter['is_deleted'] = True

        qs = self.reading_book_service.get_mybook_list(user=request.user, data=filter)
        return get_paginated_response(
            pagination_class=PageNumberPagination,
            serializer_class=ReadlingBookReadOnlySerializer,
            queryset=qs,
            request=request,
            view=self
        )

    def create(self, request):
        serializer = ReadingBookWOSerializer(data=request.data,
                                             context={'user': request.user,
                                                      'book_service': self.book_service,
                                                      'reading_book_service': self.reading_book_service})
        if serializer.is_valid():
            data = serializer.create(serializer.data)
            return Response({
                'success': True,
                'message': 'this book has been added to your reading list successfully',
                'data': ReadlingBookReadOnlySerializer(data).data
            })

        return Response(serializer.errors)

    def retrieve(self, request, reading_book_id):
        qs = self.reading_book_service.get_book(request.user, reading_book_id)
        if not qs:
            return Response({
                'message': 'No Reading Book found with this id'
            })
        serializer = ReadlingBookReadOnlySerializer(qs.first())
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, reading_book_id):
        serializer = ReadingBookWOSerializer(data=request.data,
                                             context={'user': request.user,
                                                      'book_service': self.book_service,
                                                      'reading_book_service': self.reading_book_service,
                                                      'reading_book_id':reading_book_id})

        if serializer.is_valid():
            data = serializer.update(serializer.data)
            return Response({
                'success': True,
                'message': 'reading book has been Updated',
                'data': ReadlingBookReadOnlySerializer(data).data
            })

        return Response(serializer.errors)
