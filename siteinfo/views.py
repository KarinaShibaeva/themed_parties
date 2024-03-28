from django.shortcuts import render

def main_view(request):
    context = {"page": "main"}
    return render(request, 'siteinfo/main.html', context)
