from django.shortcuts import render

def project_page(request):
    if request.method == 'GET':
        return render(request, 'project_page.html')
