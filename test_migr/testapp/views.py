from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework import permissions

from migrations_create.migrations_create import Migrate_creater
from django.core.management import call_command

from .models import Salary, Employee, Test
from .serializers import UserSerializer, GroupSerializer

import sys

def index(request):
    print('1')
    try:
        #call_command('makemigrations', 'testapp', verbosity=3, interactive=False)
        #call_command('migrate', 'testapp', verbosity=3, interactive=False)
        migrate = Migrate_creater('testapp', 'Salary')
        migrate.ChangeTypeField('back_name2', 'del')
    except Exception as E:
        raise(E)
    print('2')
    num_employees = Employee.objects.all().count()
    num_salary = Salary.objects.all().count()

    #call_command('migrate', 'testapp', verbosity=3, interactive=False)


    return render(
        request,
        'index.html',
        context={'num_employees': num_employees, 'num_salary': num_salary}
    )


class SalaryListView(generic.ListView):
    model = Salary
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SalaryListView, self).get_context_data(**kwargs)
        context['some_data'] = 'Some Data'
        assert isinstance(context, object)
        return context

class SalaryDetailView(generic.DetailView):
    model = Salary


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


#class Migrate_test(viewsets.ModelViewSet):
 #   from django.core.management import call_command
  #  call_command('makemigrations', 'testapp', verbosity=3, interactive=False)