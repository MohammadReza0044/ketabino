from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book (models.Model):

    Available = "Available"
    Unavailable = "Unavailable"
 
    STATUS_CHOICES = (
        (Available,  "Available"),
        (Unavailable,"Unavailable"),
        )

    name = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)
    translator = models.ForeignKey(Translator , on_delete=models.CASCADE)
    code = models.IntegerField()
    description = models.TextField()
    pages = models.IntegerField()
    published_date = models.DateField()
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES)
    price = models.IntegerField()

    class Meta:
        db_table = 'Book'


    def __str__(self):
        return self.name



class Comment (models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.full_name

