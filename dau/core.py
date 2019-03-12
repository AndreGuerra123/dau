
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured

def tag(msg:str):
    return "{} {}{}"('[DJANGO AUTO USER]',msg,'.')

def err_set(err_msg:str):
    raise ImproperlyConfigured(tag(err_msg))

def err_cre(err_msg:str):
    raise RuntimeError(err_msg)

class DjangoAutoUser():

    def __init__(self):
        self.auto_user = getattr(settings,'DJANGO_AUTO_USER')
        self.__validate()
        
    def __is_valid(self,obj,typ:type):
        if obj and isinstance(obj,typ):
            return True
        else:
            return False

    def __validate(self):
        self.__settings_validation()
        self.__users_validation()

    def __settings_validation(self):
        if not self.__is_valid(self.auto_user,list):
            err_set('AUTO_USER settings under Django settings must be of type list but instead is of type {}'.format(str(type(self.auto_user))))

    def __users_validation(self):
        for idx, user in enumerate(self.auto_user):
            self.__is_valid_user(idx,user)

    def __is_valid_user(self,idx,user):
        if not self.__is__valid(user,dict):
            err_set('User entry at index {} in AUTO_USER settings must contain a non empty dictionary'.format(str(idx)))


    def __create_users(self):
        for idx, user in enumerate(self.auto_users):
            try:
                u = User()
                for field, value in user.items():
                    setattr(u,field,value)
                u.save()
            except Exception as error:
                err_cre('Could not create user entry at index {} in AUTO_USER settings. {}'.format(str(idx),str(error)))

