from django.contrib import admin
from myfiles.models import Kurs, Student


# Register your models here.

class AdminKurs(admin.ModelAdmin):
    list_display = ['id', 'nomi']


admin.site.register(Kurs, AdminKurs)


class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'ism', 'yosh', 'yonalish', 'date']


admin.site.register(Student, AdminStudent)
