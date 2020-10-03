from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework import response, status
from rest_framework.response import Response



class PostView(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    def create(self, request):
        # serializing the categories_assigned to meet the requirements in
        # the serializer
        ids = request.data["categories_assigned"]
        new_category_assigned = []
        for i in request.data["categories_assigned"]:
            obj = models.Category.objects.get(id=i)
            body = {}
            body["id"] = obj.id
            body["name"] = obj.name           
            new_category_assigned.append(body)
        request.data["categories_assigned"] = new_category_assigned

        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            obj = models.Post.objects.create(title=request.data["title"], body=request.data["body"])
            obj.categories_assigned.set(ids)
            obj.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerilizer
    queryset = models.Category.objects.all()


    def update(self, request, pk, partial=False):
        # partial will be true if if its a patch request
        # partail should be given a default value False...so if its a PUT Request
        # then it will say unexpected keyword argument partial
        # so when its a put request it sends the partial to true
        # for PUT it sends nothing..so have to put the partial default value to False
        # bases on the True and False Value of partial u can perform patch and put
        # operation performing a if else statment...
        # for put all the values should be reset and for patch only the sent value should
        # be updated
        # for both put and patch pk which is sent
        print(request)
        print(pk)
        print(partial)
        serializer = serializers.CategorySerilizer(models.Category.objects.get(pk=pk),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

