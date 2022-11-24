from django.db import models

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='img/%Y/%m/%d/')
    mail = models.EmailField(default=None)          #default=None - База данных не терпит пустых ячеек,
                                                    #здесь мы указали, что по умолчанию в этом стобце - пустая строка
    program = models.TextField()

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    description = models.CharField(max_length=100)

class Employees(models.Model):
    name = models.CharField(max_length=100)
    foto = models.ImageField()
    position = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=100)
    foto = models.ImageField()
    author = models.ForeignKey(Employees, on_delete=models.CASCADE)
    created_by = models.DateTimeField(auto_now_add=True)
















