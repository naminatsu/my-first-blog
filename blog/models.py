# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):　#オブジェクト
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)　#他のモデルへのリンク
    title = models.CharField(max_length=200)　#文字数制限テキスト　MAX200文字で設定
    text = models.TextField()　#制限なしテキスト
    created_date = models.DateTimeField(default=timezone.now) #日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True) #日付と時間のフィールド

    def publish(self):　#ブログ公開メソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title　#タイトルを返す