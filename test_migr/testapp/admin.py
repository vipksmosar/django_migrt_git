from django.contrib import admin

# Register your models here.


from .models import Employee, Salary

#admin.site.register(Employee)
#admin.site.register(Salary)
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'issued', 'employee', 'id')#, 'back_name2')
    list_filter = ('issued', 'employee')

#admin.site.register(Salary, SalaryAdmin)

@admin.register(Employee)
class EmployeeAdmin (admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'back_name')
    list_filter = ('last_name',)