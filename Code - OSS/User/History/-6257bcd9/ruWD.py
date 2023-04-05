# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminappFaculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_faculty'


class AdminappGroup(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(AdminappFaculty, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_group'


class AdminappKafedra(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_kafedra'


class AdminappStudent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(AdminappGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_student'


class AdminappSubject(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_subject'


class AdminappTeacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.CharField(max_length=100)
    kafedra = models.ForeignKey(AdminappKafedra, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(AdminappFaculty, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_teacher'


class AuthUser(models.Model):
    password = models.TextField(blank=True, null=True)
    last_login = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_superuser = models.TextField(blank=True, null=True)  # This field type is a guess.
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    is_staff = models.BinaryField(blank=True, null=True)
    is_active = models.BinaryField(blank=True, null=True)
    date_joined = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'