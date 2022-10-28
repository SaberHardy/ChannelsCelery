from django.shortcuts import render


def home(request):
    context = {
        'room_name': 'broadcast'
    }
    return render(request, 'mainApp/index.html', context)
