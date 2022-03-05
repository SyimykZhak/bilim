from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email", blank=True, null=True)
    addres = models.TextField("Адрес", max_length=5000)
    telephone = models.CharField("Телефон", max_length=15)
    description = models.CharField("Описание",max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратный связь"
        verbose_name_plural = "Обратные связи"