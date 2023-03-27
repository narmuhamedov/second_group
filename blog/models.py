from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CommentBlog(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    blog_comment = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment_object')
    text = models.TextField()
    rate = models.CharField(max_length=100, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True)