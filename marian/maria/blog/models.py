from django.db import models

# Create your models here.

class Contact(models.Model):
    info = models.TextField()
    nom = models.CharField(max_length = 255)
    mail = models.EmailField()
    sujet = models.CharField(max_length = 255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.nom 

class NewsLetter(models.Model):
    mail = models.EmailField() 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="newsLetter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return str(self.mail)   

class presentation(models.Model):
    ICONES = [
        ('facebook', 'fab fa-facebook'),
        ('twitter', 'fa fa-twitter'),
        ('globe', 'fas fa-globe'),
        ('behance', 'fab fa-behance'),
    ]
    nom = models.CharField(max_length=255)
    liens = models.URLField()
    icone = models.CharField(choices=ICONES, max_length=20)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/presentation')
    titre = models.CharField(max_length=255) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="presentation"
        verbose_name_plural = "presentations"

    def __str__(self):
        return self.nom         

class message(models.Model):
    nom = models.CharField(max_length = 255)
    prenom = models.FloatField
    image = models.ImageField(upload_to='images/message')
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.nom