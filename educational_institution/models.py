from django.db import models

# Create your models here.
class City(models.Model):
    class Meta:
        db_table = "city"

    city_name = models.CharField(max_length=100)
    population = models.IntegerField()


class Educational_institution_type(models.Model):
    class Meta:
        db_table = "educational_institution_type"

    educational_institution_type = models.CharField(max_length=100)


class Educational_institution(models.Model):
    class Meta:
        db_table = "educational_institution"

    educational_institution_name = models.CharField(max_length=100)
    accreditation_level = models.IntegerField()
    license_for_educational_activity = models.TextField(blank=True, null=True, default="")
    founding_date = models.DateField()
    city = models.ForeignKey(City, null=True)
    type = models.ForeignKey(Educational_institution_type, null=True)


class Faculty(models.Model):
    class Meta:
        db_table = "faculty"

    faculty_name = models.CharField(max_length=100)
    educational_institution = models.ForeignKey(Educational_institution, null=True)


class Student(models.Model):
    class Meta:
        db_table = "student"

    student_name = models.CharField(max_length=100)
    average_mark = models.FloatField()
    birth_date = models.DateField()
    city = models.ForeignKey(City, null=True)
    faculty = models.ManyToManyField(Faculty)


class Type_of_payment_for_education(models.Model):
    class Meta:
        db_table = "type_of_payment_for_education"

    type_of_payment_for_education = models.CharField(max_length=100)
    educational_institution = models.ManyToManyField(Educational_institution)


class Educational_direction(models.Model):
    class Meta:
        db_table = "educational_direction"

    educational_direction_name = models.CharField(max_length=100)
    educational_institution = models.ManyToManyField(Educational_institution)


class Educational_method(models.Model):
    class Meta:
        db_table = "educational_method"

    educational_method_name = models.CharField(max_length=100)
    educational_institution = models.ManyToManyField(Educational_institution)