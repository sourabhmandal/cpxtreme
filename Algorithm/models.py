from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class GROUP_TITLE(models.Model):
    meta_title = models.CharField(max_length=100, default='')
    title_no = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.title_no) + '. ' + self.meta_title)

class POST(models.Model):
    #titleOpt = groupTitle.objects.all()
    #print(titleOpt)
    meta_title_no = models.IntegerField(default=0)
    sub_title_no = models.FloatField()
    youtube_link = models.CharField(max_length=5000, default='')
    title = models.CharField(max_length=100)
    body = RichTextField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default='')

    def __str__(self):
        return (str(self.sub_title_no) + " - " + self.title)
