from django.db import models

# Create your models here.
class NAV_ITEM(models.Model):
    tab_Name = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=100, default='')
    link_no = models.IntegerField(default=1)

    def __str__(self):
        return (str(self.link_no) + ". " + self.tab_Name)