from django.urls import path, include

from ExamWebBasic.webcars.views import index, car_cataloge, \
    car_create, car_details, car_edit, car_delete, \
    profile_create, profile_details, profile_edit, profile_delete


urlpatterns = (
    path('', index, name ='index'),
    path('catalogue',car_cataloge, name ='catalogue'),

        path('car/', include([
            path('create/', car_create, name ='create car'),
            path('<int:pk>/details/', car_details, name ='details car'),
            path('<int:pk>/edit/',car_edit, name ='edit car'),
            path('<int:pk>/delete/',car_delete, name ='delete car'),
    ])),

        path('profile/', include([
            path('create/', profile_create, name ='create profile'),
            path('details/', profile_details, name ='details profile'),
            path('edit/', profile_edit, name ='edit profile'),
            path('delete/',profile_delete, name ='delete profile'),
        ])),

)