import django_setup
from lesson import models
from lesson.models import *

some_user = models.User(username='user_1', email='email@gmail.com', role='admin')
some_user.save()