from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class BlogArticles(models.Model):
    title=models.CharField(max_length=300)               #规定了字段title的属性为CharField,以及字段最大值
    author=models.ForeignKey(User,related_name="blog_posts")        #通过字段author定义了博客文章和用户之间的关系。foreignkeys是一对多
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)   #规定了BlogArticles对象显示顺序，倒序显示

    def _str_(self):
        return self.title
