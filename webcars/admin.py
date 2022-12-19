from django.contrib import admin

from ExamWebBasic.webcars.models import Profile, Car


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
