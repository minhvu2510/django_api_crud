from django.test import TestCase
from django.contrib.auth.models import User
u = User.objects.create_user(username='haki')
print (u)
u.has_perm('auth.change_user')
print (u.has_perm('auth.change_user'))
# Create your tests here.
