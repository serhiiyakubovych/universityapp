from django.db import models

# Create your models here.
class City(models.Model):
    class Meta:
        db_table = "city"

    city_name = models.CharField(max_length=100, verbose_name="City name")
    population = models.IntegerField(blank=True, null=True, verbose_name="Population")

    def __str__(self):
        return "%s" % self.city_name


class Educational_institution_type(models.Model):
    class Meta:
        db_table = "educational_institution_type"

    educational_institution_type = models.CharField(max_length=100, verbose_name="Type of Educational institution")

    def __str__(self):
        return "%s" % self.educational_institution_type


class Type_of_payment_for_education(models.Model):
    class Meta:
        db_table = "type_of_payment_for_education"

    type_of_payment_for_education = models.CharField(max_length=100, verbose_name="Type of payment for education")

    def __str__(self):
        return "%s" % self.type_of_payment_for_education


class Educational_direction(models.Model):
    class Meta:
        db_table = "educational_direction"

    educational_direction_name = models.CharField(max_length=100, verbose_name="Educational direction name")

    def __str__(self):
        return "%s" % self.educational_direction_name


class Educational_method(models.Model):
    class Meta:
        db_table = "educational_method"

    educational_method_name = models.CharField(max_length=100, verbose_name="Educational method name")

    def __str__(self):
        return "%s" % self.educational_method_name


class Educational_institution(models.Model):
    class Meta:
        db_table = "educational_institution"

    educational_institution_name = models.CharField(max_length=100, verbose_name="Name of the educational institution")
    accreditation_level = models.IntegerField(blank=True, null=True, verbose_name="Accreditation level")
    license_for_educational_activity = models.TextField(blank=True, null=True, default="",
                                                        verbose_name="License for educational activity")
    founding_date = models.DateField(blank=True, null=True, verbose_name="Founding date")
    city = models.ForeignKey(City, blank=True, null=True, verbose_name="City")
    type = models.ForeignKey(Educational_institution_type, blank=True, null=True, verbose_name="Type")
    type_of_payment_for_education = models.ManyToManyField(
        Type_of_payment_for_education,
        blank=True,
        related_name="payment_type",
        verbose_name="Type of payment for education"
    )
    educational_direction = models.ManyToManyField(
        Educational_direction,
        blank=True,
        related_name="educational_direction",
        verbose_name="Educational direction"
    )
    educational_method = models.ManyToManyField(
        Educational_method,
        blank=True,
        related_name="educational_method",
        verbose_name="Educational method"
    )

    def __str__(self):
        return "%s (%s)" % (self.educational_institution_name, self.city)


class Faculty(models.Model):
    class Meta:
        db_table = "faculty"

    faculty_name = models.CharField(max_length=100, verbose_name="Faculty name")
    educational_institution = models.ForeignKey(Educational_institution, blank=True, null=True,
                                                verbose_name="Educational institution")

    def __str__(self):
        return "%s (%s)" % (self.faculty_name, self.educational_institution)


class Student(models.Model):
    class Meta:
        db_table = "student"

    student_name = models.CharField(max_length=100, verbose_name="Student name")
    average_mark = models.FloatField(blank=True, null=True, verbose_name="Average mark")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth date")
    city = models.ForeignKey(City, blank=True, null=True, verbose_name="City")
    faculty = models.ManyToManyField(Faculty, blank=True, verbose_name="Faculty")

    def __str__(self):
        return "%s" % self.student_name
