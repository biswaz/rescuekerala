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
        verbose_name='Districts - ജില്ല'
    )
    location = models.CharField(max_length=500,verbose_name='Location - സ്ഥലം')
    requestee = models.CharField(max_length=100,verbose_name='Requestee - അപേക്ഷകന്‍റെ പേര്')
    requestee_phone = models.CharField(max_length=10,verbose_name='Requestee Phone - അപേക്ഷകന്‍റെ ഫോണ്‍ നമ്പര്‍')

    needwater = models.BooleanField(verbose_name='Water - വെള്ളം')
    needfood = models.BooleanField(verbose_name='Food - ഭക്ഷണം')
    needcloth = models.BooleanField(verbose_name='Clothing - വസ്ത്രം')
    needmed = models.BooleanField(verbose_name='Medicine - മരുന്നുകള്‍')
    needtoilet = models.BooleanField(verbose_name='Toiletries - ശുചീകരണ സാമഗ്രികള്‍ ')
    needkit_util = models.BooleanField(verbose_name='Kitchen utensil - അടുക്കള സാമഗ്രികള്‍')

    detailwater = models.CharField(max_length=250, verbose_name='Details for required water - ആവശ്യമായ വെള്ളത്തിന്‍റെ വിവരങ്ങള്‍', blank=True)
    detailfood = models.CharField(max_length=250, verbose_name='Details for required food - ആവശ്യമായ ഭക്ഷണത്തിന്‍റെ വിവരങ്ങള്‍', blank=True)
    detailcloth = models.CharField(max_length=250, verbose_name='Details for required clothing - ആവശ്യമായ വസ്ത്രത്തിന്‍റെ വിവരങ്ങള്‍', blank=True)
    detailmed = models.CharField(max_length=250, verbose_name='Details for required medicine - ആവശ്യമായ മരുന്നിന്‍റെ  വിവരങ്ങള്‍', blank=True)
    detailtoilet = models.CharField(max_length=250, verbose_name='Details for required toiletries - ആവശ്യമായ  ശുചീകരണ സാമഗ്രികള്‍', blank=True)
    detailkit_util = models.CharField(max_length=250, verbose_name='Details for required kitchen utensil - ആവശ്യമായ അടുക്കള സാമഗ്രികള്‍', blank=True)

    needothers = models.CharField(max_length=500, verbose_name="Other needs - മറ്റു ആവശ്യങ്ങള്‍", blank=True)
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
    organisation = models.CharField(max_length=250, verbose_name="Organization (സംഘടന) / College")
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
    commodities = models.TextField(verbose_name="What you can contribute. ( സംഭാവന ചെയ്യാന്‍ ഉദ്ദേശിക്കുന്ന സാധനങ്ങള്‍ ) -- Eg: Shirts, torches etc ")
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
