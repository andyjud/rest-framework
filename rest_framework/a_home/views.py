from django.shortcuts import render

def home_view(request):
    return render(request, 'a_home/home.html')


def comment_view(request, id):
    return render(request, 'a_home/comment.html')
