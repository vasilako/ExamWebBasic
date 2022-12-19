from django.shortcuts import render, redirect

from ExamWebBasic.webcars.models import Profile, Car


def profile_check():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None
PROFILE = profile_check()

def index(request):
    if PROFILE is None:
        contex = {
            'profile':PROFILE
        }
        return render(request, 'index.html', contex)
    else:
        return redirect('catalogue')


def profile_create(request):
    contex={}
    return render(request, 'profiles/profile-create.html', contex)

def profile_details(request):
    contex={}
    return render(request, 'profiles/profile-details.html', contex)

def profile_edit(request):
    contex={}
    return render(request, 'profiles/profile-edit.html', contex)

def profile_delete(request):
    contex={}
    return render(request, 'profiles/profile-delete.html', contex)



def car_create(request):
    contex={}
    return render(request, 'cars/car-create.html', contex)

def car_details(request):
    contex={}
    return render(request, 'cars/car-details.html', contex)

def car_edit(request):
    contex={}
    return render(request, 'cars/car-edit.html', contex)

def car_delete(request):
    contex={}
    return render(request, 'cars/car-delete.html', contex)

def car_cataloge(request):

    all_cars = Car.objects.all()
    len_catalogue = len(all_cars)

    contex = {'my_cars':all_cars,
              'len_cataloge':len_catalogue,
              'profile':PROFILE
              }

    return render(request, 'core/catalogue.html', contex)
