from django.http import HttpResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def home(request):
    context = {
        'room_name': 'broadcast'
    }
    return render(request, 'mainApp/index.html', context)


def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': 'Notification',
        }
    )
    return HttpResponse("Done")
