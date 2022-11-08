from notifications_app.models import BroadcastNotification


def notifications(request):
    all_notifications = BroadcastNotification.objects.all()
    context = {
        'notifications': all_notifications
    }
    return context
