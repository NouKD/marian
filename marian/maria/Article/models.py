from django.db import models

# Create your models here.
class categorie(models.Model):
   
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="categorie"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.nom         

class Offre(models.Model):
    nom = models.CharField(max_length = 255)
    prix = models.FloatField
    image = models.ImageField(upload_to='images/Offre')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Offre"
        verbose_name_plural = "Offres"

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom 

class Article(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    contenue = models.TextField()
    image = models.ImageField(upload_to='images/Article')
    tag = models.ManyToManyField(Tag,related_name="Tag_Article")
    categorie = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name='Article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.nom         

 