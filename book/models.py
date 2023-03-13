from django.db import models
from django.urls import reverse

class BookManager(models.Manager):
    def actived (self):
        return self.filter(status = 'A')
    

class AuthorManager(models.Manager):
    def actived (self):
        return self.filter(status = True)
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birth = models.IntegerField()
    death = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='author/image')
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'Author'


    def __str__(self):
        return self.name

    objects = AuthorManager()

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book (models.Model):

    STATUS_CHOICES = (
        ('A',  "Available"),
        ('U',"Unavailable"),
        )

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255 , unique=True)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    author = models.ForeignKey(Author , on_delete=models.CASCADE, related_name='author')
    translator = models.ForeignKey(Translator , on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)
    description = models.TextField()
    pages = models.IntegerField()
    published_date = models.IntegerField()
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES)
    active_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='image')
    price = models.IntegerField()

    class Meta:
        db_table = 'Book'
        ordering = ['-active_date', '-id']
        get_latest_by = 'active_date'

    def __str__(self):
        return self.name
  
    objects = BookManager()


class Comment (models.Model):
    
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    comment_title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.full_name


class Contact(models.Model):

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'Contact Us'
        ordering = ['-created_date']


    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('Book:contact_us')


