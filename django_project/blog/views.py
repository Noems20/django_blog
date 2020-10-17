from django.shortcuts import render

posts = [
    {
        'author': 'NoeMs',
        'title': 'Blos Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Jane doe',
        'title': 'Blos Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018',
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})