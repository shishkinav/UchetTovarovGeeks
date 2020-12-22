from rest_framework.decorators import api_view
from rest_framework.response import Response
from stockapp.api import BasicAPIRequest
from django.shortcuts import render


def index_view(request):
    return render(request, 'stockapp/index.html')

@api_view(['GET', 'POST'])
def list_view(request):
    api_r = BasicAPIRequest()
    if request.method == 'GET':
        return Response(api_r.get_products())

    elif request.method == "POST":
        return Response()


@api_view(['GET', 'POST'])
def product_view(request, slug: str):
    api_r = BasicAPIRequest()
    if request.method == 'GET':     # CRUD - read
        return Response(api_r.get_product(slug))

    elif request.method == "POST":   # CRUD - update
        return Response()

    elif request.method == "DELETE":    # CRUD - delete
        return Response()


@api_view(['GET', 'POST'])
def create_view(request):

    api_r = BasicAPIRequest()

    if request.method == 'GET':
        # TODO add form for create a product
        return Response()

    elif request.method == "POST":  # CRUD - create
        return Response(api_r.post_create_product(request))


