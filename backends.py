#file: si_dk/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#Cek email address
def is_email(text):
	try:
		validate_email(text)
		return True
	except ValidationError:
		return False

#Our custom Auth Backend
class AuthPlus(ModelBackend):
	def authenticate(self, **credentials):
		if 'username' in credentials:
			username = credentials.get('username')

			#Email login
			if is_email(username):
				try:
					user = AkunPerusahaan.objects.get(email=username)
					if user.check_password(credentials.get('password')):
						return user
				except AkunPerusahaan.DoesNotExist:
					return None

			#Normal username login
			else:
				return super(AuthPlus, self).authenticate(**credentials)
