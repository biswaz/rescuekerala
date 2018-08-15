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

contrib_status_types =(
    ('new', 'New'),
    ('ful', 'Fullfilled'),
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
    needkit_util = models.BooleanField(verbose_name='Kitchen utensil')

    detailwater = models.CharField(max_length=250, verbose_name='Details for required water', blank=True)
    detailfood = models.CharField(max_length=250, verbose_name='Details for required food', blank=True)
    detailcloth = models.CharField(max_length=250, verbose_name='Details for required clothing', blank=True)
    detailmed = models.CharField(max_length=250, verbose_name='Details for required medicine', blank=True)
    detailtoilet = models.CharField(max_length=250, verbose_name='Details for required toileteries', blank=True)
    detailkit_util = models.CharField(max_length=250, verbose_name='Details for required kitchen utensil', blank=True)

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
    is_spoc = models.BooleanField(default=False, verbose_name="Is point of contact")

    def __str__(self):
        return self.name


class Contributor(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    commodities = models.TextField(verbose_name="What you can contribute. Eg: Shirts, torches etc")
    status = models.CharField(
        max_length = 10,
        choices = contrib_status_types,
        default = 'new'
    )

    def __str__(self):
        return self.name + ' ' + self.get_district_display()


class DistrictManager(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.get_district_display()

class DistrictNeed(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    needs = models.TextField(verbose_name="Items required")
    cnandpts = models.TextField(verbose_name="Contacts and collection points") #contacts and collection points

    def __str__(self):
        return self.get_district_display()

class DistrictCollection(models.Model):
    district = models.CharField(
        max_length=15,
        choices=districts
    )
    collection = models.TextField(
        verbose_name="Details of collected items"
    )
