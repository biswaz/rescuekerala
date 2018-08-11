from django.db import models

districts = (
    ('tvm','Thiruvananthapuram'),
    ('ptm','Pathanamthitta'),
    ('alp','Alappuzha'),
    ('ktm','Kottayam'),
    ('idk','Idukki'),
    ('mpm','Malappuram'),
    ('koz','Kozhikode'),
    ('wnd','Wayanad'),
    ('knr','Kannur'),
    ('ksr','Kasaragod'),
    ('pkd','Palakkad'),
    ('tcr','Thrissur'),
    ('ekm','Ernakulam'),
    ('kol','Kollam'),
)

status_types =(
    ('new', 'New'),
    ('pro', 'In progess'),
    ('sup', 'Supplied'),
)

class Request(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    location = models.CharField(max_length=500)
    requestee = models.CharField(max_length=100)
    requestee_phone = models.CharField(max_length=10)
    needwater = models.BooleanField(verbose_name='Water')
    needfood = models.BooleanField(verbose_name='Food')
    needcloth = models.BooleanField(verbose_name='Clothing')
    needmed = models.BooleanField(verbose_name='Medicine')
    needtoilet = models.BooleanField(verbose_name='Toileteries')
    needkit_util = models.BooleanField(verbose_name='Kitchen utencil')
    needothers = models.CharField(max_length=500, verbose_name="Other needs", blank=True)
    status = models.CharField(
        max_length = 10,
        choices = status_types,
        default = 'new'
    )
    supply_details = models.CharField(max_length=100, blank=True)
    dateadded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district + ' ' + self.location

class Volunteer(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    organisation = models.CharField(max_length=250)
    address = models.TextField()
    is_spoc = models.BooleanField(default=False)

    def __str__(self):
        return self.name
