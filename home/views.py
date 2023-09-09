from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    services = ['UI/UX Design', 'Development', 'Data Science', 'Business', 'Financial', 'Marketing', 'Design']
    in_brand = ['brand-01.png', 'brand-02.png', 'brand-03.png', 'brand-04.png', 'brand-05.png', 'brand-06.png']
    return render(request, 'index.html', context={'services': services, 'brands': in_brand})


def courses(request):
    menus = ['All Courses', 'Collections', 'Wishlist', 'Archived']
    posts = [
        {
            'title': 'Finance Series: Learn to Budget and Calculate your Net Worth.',
            'author': 'Jason Williams',
            'tag': 'Science',
            'image': {
                'blog': 'courses-01.jpg',
                'auth': 'author-04.jpg'
            },
            'average': 72
        },
        {
            'title': 'Build Brand Into Marketing: Tackling the New Marketing Landscape',
            'author': 'Pamela Foster',
            'tag': 'UX Design',
            'image': {
                'blog': 'courses-05.jpg',
                'auth': 'author-05.jpg'
            },
            'average': 38
        },
        {
            'title': 'Create Amazing Color Schemes for Your UX Design Projects',
            'author': 'Patricia Collins',
            'tag': 'Business',
            'image': {
                'blog': 'courses-02.jpg',
                'auth': 'author-02.jpg'
            },
            'average': 87
        }
    ]
    return render(request, 'courses.html', context={'menus': menus, 'posts': posts})


def blogs(request):
    posts = [
        {
            'title': 'Data Science and Machine Learning with Python - Hands On!',
            'author': 'Jason Williams',
            'tag': 'Science',
            'image': {
                'blog': 'blog-01.jpg',
                'auth': 'author-01.jpg'
            }
        },
        {
            'title': 'Create Amazing Color Schemes for Your UX Design Projects',
            'author': 'Pamela Foster',
            'tag': 'UX Design',
            'image': {
                'blog': 'blog-02.jpg',
                'auth': 'author-02.jpg'
            }
        },
        {
            'title': 'Culture & Leadership: Strategies for a Successful Business',
            'author': 'Patricia Collins',
            'tag': 'Business',
            'image': {
                'blog': 'blog-03.jpg',
                'auth': 'author-03.jpg'
            }
        }
    ]
    return render(request, 'blogs.html', context={'posts': posts})


def contact(request):
    email = 'contact@example.com'
    phone = '+880 1316-440504'
    office = 'Dhaka-1206 Bangladesh'
    return render(request, 'contact.html', context={'email': email, 'mobile': phone, 'office': office})
