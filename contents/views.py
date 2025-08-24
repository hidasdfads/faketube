from django.shortcuts import render, get_object_or_404
from .models import Channel

def home(request, channel_id=None):
    channels = Channel.objects.all().order_by("id")
    if not channels:
        return render(request, "home.html", {"channels": [], "channel": None, "videos": []})

    # 특정 채널 없으면 첫 채널 선택
    if channel_id:
        channel = get_object_or_404(Channel, id=channel_id)
    else:
        channel = channels.first()

    videos = channel.videos.all()

    # 순환 버튼용
    current_index = list(channels).index(channel)
    prev_channel = channels[(current_index - 1) % len(channels)]
    next_channel = channels[(current_index + 1) % len(channels)]

    return render(request, "home.html", {
        "channels": channels,
        "channel": channel,
        "videos": videos,
        "prev_channel": prev_channel,
        "next_channel": next_channel,
    })
