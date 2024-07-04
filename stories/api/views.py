from stories.models import Category, Receipe, Tag
from django.http import JsonResponse
from .serializers import CategorySerialzier, RecipeSerialzier, RecipeCreateSerialzier, TagListSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def categories(request):
    category_list = Category.objects.all()
    serializer = CategorySerialzier(category_list, many=True)
    # category_dict = []
    # for category in category_list:
    #     category_dict.append(
    #         {
    #             "cat_id": category.id,
    #             "cat_name": category.name
    #         }
    #     )
    return JsonResponse(serializer.data, safe=False)

@api_view(http_method_names=["GET", "POST"])
def recipes(request):
    if request.method == "POST":
        serializer = RecipeSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201, safe=False)
        return JsonResponse(data=serializer.errors, status=400,  safe=False)
    recipe_list = Receipe.objects.all()
    serializer = RecipeSerialzier(recipe_list, context={'request':request}, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(http_method_names=["PUT", "PATCH"])
def recipe_update(request, id):
    # recipe = Receipe.objects.get(id=id)
    recipe = get_object_or_404(Receipe, id=id)
    if request.method == "PUT":
        serializer = RecipeCreateSerialzier(data=request.data, context={'request': request}, instance=recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201, safe=False)
        return JsonResponse(data=serializer.errors, status=400,  safe=False)
    if request.method == "PATCH":
        serializer = RecipeCreateSerialzier(data=request.data, partial=True, context={'request': request}, instance=recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201, safe=False)
        return JsonResponse(data=serializer.errors, status=400,  safe=False)
    

class RecipeListView(ListCreateAPIView):
    """
    This endpoint is for list and create
    """
    serializer_class = RecipeCreateSerialzier
    permission_classes = [AllowAny]
    queryset = Receipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeSerialzier
        return super().get_serializer_class()


    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = Receipe.objects.filter(title__icontains = keyword)
            return queryset
        return super().get_queryset()
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('keyword', openapi.IN_QUERY, description="keyword to filter name", type=openapi.TYPE_STRING)
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class RecipeRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerialzier
    permission_classes = [IsAuthenticated]
    queryset = Receipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeSerialzier
        return super().get_serializer_class()

class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()