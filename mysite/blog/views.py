from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

def blog_title(request):
    blogs=BlogArticles.objects.all()  #得到所有BlogArticles对象实例
    return render(request,"blog/titles.html",{"blogs":blogs}) #render（）将数据渲染到指定模板上

def blog_article(request,article_id):
   # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles,id=article_id)   #简化网页不存在的异常处理
    pub=article.publish
    return render(request,"blog/content.html",{"article":article,"publish":pub})
# Create your views here.
