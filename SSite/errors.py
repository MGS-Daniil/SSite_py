from django.shortcuts import render, redirect


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)

