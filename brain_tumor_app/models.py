from django.db import models

# Create your models here.
class agent_details(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    street = models.CharField(max_length=20, default='SOME STRING')
    hname = models.CharField(max_length=20, default='SOME STRING')
    district = models.CharField(max_length=50, default='SOME STRING')
    state = models.CharField(max_length=20, default='SOME STRING')
    pincode = models.CharField(max_length=20, default='SOME STRING')
    country = models.CharField(max_length=20, default='SOME STRING')

    email = models.EmailField()
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    license_num = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='SOME STRING')

class client_details(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    street = models.CharField(max_length=20, default='SOME STRING')
    hname = models.CharField(max_length=20, default='SOME STRING')
    district = models.CharField(max_length=50, default='SOME STRING')
    state = models.CharField(max_length=20, default='SOME STRING')
    pincode = models.CharField(max_length=20, default='SOME STRING')
    country = models.CharField(max_length=20, default='SOME STRING')

    email = models.EmailField()
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='SOME STRING')

class policy_details(models.Model):
    insurance_id = models.CharField(max_length=100)
    date_of_insurance = models.DateField()
    client_id = models.CharField(max_length=100)
    agent_id = models.CharField(max_length=20)

class request(models.Model):
    request_id = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    response = models.CharField(max_length=100)
    insurance_id = models.CharField(max_length=100)
    date_of_insurance = models.DateField()

    reason = models.CharField(max_length=20)

class office_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class add_insurance_details(models.Model):
    uid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100)
    aname = models.CharField(max_length=100)
    date = models.DateField()
    license_num = models.CharField(max_length=100)

class add_claim_details(models.Model):
    Inid = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100)
    image = models.FileField(default='SOME STRING')

class forward_claim_details(models.Model):
    Inid = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100)
    image = models.FileField(default='SOME STRING')


class response(models.Model):
    uid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=100)


