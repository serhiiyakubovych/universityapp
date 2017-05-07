from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.db.models import Q
from django.shortcuts import render_to_response
from educational_institution.models import Educational_institution, Type_of_payment_for_education, City,\
    Educational_direction, Student, Educational_method, Faculty, Educational_institution_type

# Create your views here.


def home(request):
    return render_to_response('home.html', {})


def cities(request):
    return render_to_response('cities.html', {'cities': City.objects.all})


def city(request, city_id=1):
    return render_to_response('city.html', {'city': City.objects.get(id=city_id)})


def educational_institution_types(request):
    return render_to_response('educational_institution_types.html',
                              {'educational_institution_types': Educational_institution_type.objects.all})


def educational_institution_type(request, educational_institution_type_id=1):
    return render_to_response('educational_institution_type.html',
                              {'educational_institution_type': Educational_institution_type.objects.get(id=educational_institution_type_id)})


def educational_directions(request):
    return render_to_response('educational_directions.html',
                              {'educational_directions': Educational_direction.objects.all})


def educational_direction(request, educational_direction_id=1):
    return render_to_response('educational_direction.html',
                              {'educational_direction': Educational_direction.objects.get(id=educational_direction_id)})


def educational_methods(request):
    return render_to_response('educational_methods.html',
                              {'educational_methods': Educational_method.objects.all})


def educational_method(request, educational_method_id=1):
    return render_to_response('educational_method.html',
                              {'educational_method': Educational_method.objects.get(id=educational_method_id)})


def faculties(request):
    return render_to_response('faculties.html', {'faculties': Faculty.objects.all})


def faculty(request, faculty_id=1):
    return render_to_response('faculty.html', {'faculty': Faculty.objects.get(id=faculty_id)})


def payment_types(request):
    return render_to_response('payment_types.html', {'payment_types': Type_of_payment_for_education.objects.all})


def payment_type(request, payment_type_id=1):
    return render_to_response('payment_type.html',
                              {'payment_type': Type_of_payment_for_education.objects.get(id=payment_type_id)})


def students(request):
    return render_to_response('students.html', {'students': Student.objects.all})


def student(request, student_id=1):
    return render_to_response('student.html', {'student': Student.objects.get(id=student_id)})


def educational_institutions(request):
    query = request.GET.get("q")
    if query:
        educational_institution_list = Educational_institution.objects.filter(
            Q(educational_institution_name__icontains=query)|
            Q(city__city_name__icontains=query)
        )
    else:
        educational_institution_list = Educational_institution.objects.all
    return render_to_response('educational_institutions.html',
                              {'educational_institutions': educational_institution_list, 'request': request})


def educational_institution(request, educational_institution_id=1):
    return render_to_response('educational_institution.html',
                              {'educational_institution': Educational_institution.objects.get(id=educational_institution_id)})
