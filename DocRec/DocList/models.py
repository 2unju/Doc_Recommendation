from django.db import models

class Title(models.Model):
    _text = models.CharField(max_length=200)
    _date = models.DateTimeField('date published')
    def __str__(self):
        return self._text

class Content(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    _text = models.TextField()
    def __str__(self):
        return self._text

class DocUrl(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    _text = models.CharField(max_length=100)
    def __str__(self):
        return self._text