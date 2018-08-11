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

class Request(models.Model):
    district = models.CharField(
        max_length = 15,
        choices = districts,
    )
    location = models.CharField(max_length=500)
    requestee = models.CharField(max_length=100)
    requestee_phone = models.CharField(max_length=10)
    needwater = models.BooleanField()
    needfood = models.BooleanField()
    needcloth = models.BooleanField()
    needmed = models.BooleanField()
    needothers = models.CharField(max_length=500, verbose_name="Other needs", blank=True)
    status = models.BooleanField(default=False)
    supply_details = models.CharField(max_length=100)
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
