from django.shortcuts import render

posts = [
    {
        'author': "Corey MS",
        'title': 'blog1',
        'content': 'blog1_content',
        'date': '12-18-2000',
    },
    {
        'author': "Jane Doe",
        'title': 'blog2',
        'content': 'blog2_content',
        'date': '11-12-2001',
    },
]

def home(request):
    context = {
        'posts': posts,
        'title': 'blogPage',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

