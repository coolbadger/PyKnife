from django.db import models


# Create your models here.

class Host(models.Model):
    name = models.CharField(max_length=200)
    ipv4 = models.CharField(max_length=50, unique=True)
    ipv6 = models.CharField(max_length=200, null=True)
    check_date = models.DateTimeField(null=True)
    checked = models.BooleanField(default=False)
    port_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Host'


class Port(models.Model):
    port_no = models.IntegerField(unique=True)
    default_name = models.CharField(max_length=200, null=True)
    desc = models.TextField(null=True)

    class Meta:
        verbose_name = 'Port'


class Host_Port(models.Model):
    host = models.ForeignKey(Host)
    port = models.ForeignKey(Port)
    port_name = models.CharField(max_length=200, null=True)
    port_desc = models.TextField(null=True)
    check_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Host_Port'
