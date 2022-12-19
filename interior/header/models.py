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

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

class Services(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Employees(models.Model):
    name = models.CharField(max_length=100)
    foto = models.ImageField()
    position = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class News(models.Model):
    title = models.CharField(max_length=100)
    foto = models.ImageField()
    author = models.ForeignKey(Employees, on_delete=models.CASCADE)
    created_by = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
















