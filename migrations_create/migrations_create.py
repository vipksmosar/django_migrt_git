#!/usr/bin/env python
import re
import os
from django.core.management import call_command

import migrations_create.setting


class Migrate_creater:
    def __init__(self, app_name, model_name):
        self.app_name = app_name
        self.model_name = model_name
        self.file_path = '{}/{}/models.py'.format(migrations_create.setting.DIR_WITH_DJANGO, self.app_name)

    def __read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                file_out = file.readlines()
            return file_out
        except Exception as E:
            return E

    def __write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
                print('models write succeful')
        except Exception as E:
            return E

    def __find_field(self, field_name):
        all_file = self.__read_file()
        start_pos_list = [all_file.index(x) for x in all_file if re.search('class {}'.format(self.model_name), x)]
        if len(start_pos_list) == 0:
            raise Exception('class {} not found in the model'.format(self.model_name))
        elif len(start_pos_list) > 1:
            corr_start_pos_list = [start_pos_list.index(x) for x in start_pos_list if
                                   re.search('class {} '.format(self.model_name), all_file[x])
                                   or re.search('class {}\('.format(self.model_name), all_file[x])]
            if len(corr_start_pos_list) > 1:
                raise Exception('syntax error in file models.py with classes {}'.format(self.model_name))
            elif len(corr_start_pos_list) == 1:
                start_pos = corr_start_pos_list[0]
            elif len(corr_start_pos_list) == 0:
                raise Exception('maybe error in file models.py with classes {}'.format(self.model_name))
            else:
                raise Exception('unsupported error')
        elif len(start_pos_list) == 1:
            start_pos = start_pos_list[0]
        else:
            raise Exception('unsupported error')

        end_pos_list = [all_file.index(x) for x in all_file if re.search('class', x)]
        end_pos = start_pos + end_pos_list[1]
        model_list = all_file[start_pos:end_pos]
        field_pos_list = [model_list.index(x) for x in model_list if re.search(
            '{}.+=.+models|{}=models|{}.+=models|{}=.+models'.format(field_name, field_name, field_name, field_name),
            x)]

        field_pos = field_pos_list[0] + start_pos
        return field_pos, all_file

    def __migrate(self):
        #os.system('source {}/bin/activate'.format(setting.BASE_DIR))
        #os.system('python3 {}/manage.py makemigrations'.format(setting.DIR_WITH_DJANGO))
        #os.system('python3 {}/manage.py migrate'.format(setting.DIR_WITH_DJANGO))
        call_command('makemigrations', 'testapp', verbosity=3, interactive=False)
        call_command('migrate', 'testapp', verbosity=3, interactive=False)

    def ChangeTypeField(self, field_name, verb):
        field_pos, content = self.__find_field(field_name)
        new_content = DeleteObj.delete_model_field(content, field_pos)
        self.__write_file(new_content)
        try:
            self.__migrate()
            return 'OK'
        except Exception as E:
            raise Exception(E)

    def CreateField(self, field_name, type_field):
        pass


class DeleteObj:
    def delete_model_field(file_list, pos):
        file_list = file_list[:pos] + file_list[pos + 1:]
        content_file = ''.join(file_list)
        return content_file




