from django.shortcuts import render

def main_page(request):
    return render(request, 'mainpage/main_page.html')
