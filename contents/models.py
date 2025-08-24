from django.db import models

# 채널
class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)   # 채널명
    logo = models.ImageField(upload_to='channel_logos/')   # 채널 로고

    def __str__(self):
        return self.name


# 영상
class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # 직접 업로드
    video_link = models.URLField(blank=True, null=True)  # 외부 링크 (예: YouTube)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
