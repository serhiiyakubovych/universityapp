from django.contrib import admin
from educational_institution.models import Educational_institution, City, Educational_institution_type, Faculty, Student, Type_of_payment_for_education, Educational_direction, Educational_method

# Register your models here.
class Educational_institution_Admin(admin.ModelAdmin):
    list_filter = ['founding_date']
    search_fields = ['educational_institution_name']

admin.site.register(Educational_institution, Educational_institution_Admin)
admin.site.register(City)
admin.site.register(Educational_institution_type)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Type_of_payment_for_education)
admin.site.register(Educational_direction)
admin.site.register(Educational_method)