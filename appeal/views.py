from django.http import HttpResponse
from django.shortcuts import render

from appeal.forms import AppealForm

def appeal_view(request):
    context = {"page":"notification_message"}
    return render(request, 'message/notification_message.html', context)

def submit_appeal(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'message/notification_message.html')
    else:
        form = AppealForm()
    return render(request, 'appeal/appeal.html', {'form':form})