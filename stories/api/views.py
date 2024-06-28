from stories.models import Category, Receipe
from django.http import JsonResponse
from .serializers import CategorySerialzier, RecipeSerialzier, RecipeCreateSerialzier
from rest_framework.decorators import api_view

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
            return JsonResponse(data=serializer.data, safe=False)
        return JsonResponse(data=serializer.errors, safe=False)
    recipe_list = Receipe.objects.all()
    serializer = RecipeSerialzier(recipe_list, context={'request':request}, many=True)
    return JsonResponse(serializer.data, safe=False)