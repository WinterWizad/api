from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework import generics #for built-in api template view

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView #for customized API VIEW
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    def delete(request,self,*args,**kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer 
    lookup_field="pk"   

class BlogPostList(APIView):
    def get(self,request,format=None):
        #get the title from the query parameters (if none, default to empty string)
        title=BlogPost.objects.all(title="")

        if title:
            # filter the queryset based on the title
            blog_posts=BlogPost.objects.filter(title_icontains=title)
        else:
            #If no title, give all blogposts
            blog_posts=BlogPost.objects.all()    

        serializer=BlogPostSerializer(blog_posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)     