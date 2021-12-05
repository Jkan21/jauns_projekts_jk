from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . forms import (
    VisitForm,
    VisitorNameForm,
    CreateUserForm,
    UploadCsvForm,
)

from . models import Visit
from .csv_handler import (
    read_and_decode_csv,
    visit_csv_rows_to_db,
    create_visit_from_csv_row,

)

import random



# skats
def show_hello(request): # fukncijai ir parametrs request
    return HttpResponse('Hello, Julija!') # return ir tas ko redzes lapā


#skats
def show_html(request):
    return render(
        request,
        template_name='hello.html'
    )

#skats
def show_datetime(request):
    current_datetime = datetime.now()
    context = {
        'datetime': current_datetime,
    }

    return render(
        request,
        template_name='datetime.html',
        context=context,
    )

#skats
def show_name_first(request):
    return render(
        request,
        template_name='form.html'
    )

#skats
def show_name(request):
    if request.method == 'POST':
        first_name = request.POST['fist_name']
        last_name = request.POST['last_name']
        return HttpResponse(f'FORMU IESNIEDZA {first_name} {last_name}')

    return render(
        request,
        template_name='form.html',
    )


#skats
def university(request):
    if request.method == 'POST':
        full_name = request.POST['Full name: ']
        mathematics = request.POST['Mathematics: ']
        latvian_language = request.POST['Foreign language']
        return HttpResponse (f'FORMU IESNIEDZA {full_name} {mathematics} {latvian_language}')

    return render(
        request,
        template_name='form.html',
    )

#skats
def motivate(request):
    motivations = (
        "Failure is not fatal",
        "Uzturies motivētu cilvēku kopumā",
        "Neliec sev limitus",
        "Nepadodies Jūlija :)",
        "Labākais laiks, kad iestādīt koku, bija pirms 20 gadiem. Otrs labākais laiks ir tagad"

    )

    motivation = random.choice(motivations)
    return HttpResponse(motivation)


#skats
def add_visit(request):
    if request.method == 'POST':
        context = {
            'visitor': request.POST['visitor'],
            'date_time': request.POST['date_time'],
            'reason': request.POST['reason']
        }

        return render(
            request,
            template_name='visit.html',
            context=context,
        )

    # REnder izpildās ja ir GET metode
    return render(
        request,
        template_name='add_visit.html',
    )

#skats

def visit_new(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        context = {
            'visitor': request.POST['visitor'],
            'date_time': request.POST['date_time'],
            'reason': request.POST['reason']
        }

        return render(
            request,
            template_name='visit_new.html',
            context=context,
        )

    context = {
        'form': form,
    }
    return render(
        request,
        template_name='visit_new.html',
        context=context,
    )

#Skats majasdarbs - 21.11.2021

def filter_visits_by_visits(request):

    form = VisitorNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visitor_name = form.cleaned_data['visitor_name']
            visits = Visit.objects.filter(visitor=visitor_name)

            context = {
                'visits': visits,
            }

            return render(
                request,
                template_name='visits.html',
                context=context
           )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context
    )

def get_all_visits(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        request,
        template_name='visits.html',
        context=context
   )

def get_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)

    context = {
        'visit': visit,

    }

    return render(
        request,
        template_name='visit.html',
        context=context,
    )


def add_visit(request):
    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            # izveidojam Visit klases objekts
            visit = Visit(
                visitor=form.cleaned_data['visitor'],
                reason=form.cleaned_data['reason'],
                date_time=form.cleaned_data['date_time'],
            )

            visit.save()

            context = {
                "visit": visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )

def upload_csv_row_to_db(request):

    form = UploadCsvForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():

            decoded_csv = read_and_decode_csv(request.FILES['csv_file'])
            visit_csv_rows_to_db(decoded_csv)

            return HttpResponse('OK')

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )
