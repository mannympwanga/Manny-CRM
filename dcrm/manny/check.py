from django.contrib.auth.models import User

superuser = User.objects.filter(is_superuser=True).first()
print(superuser.username)
print(superuser.email)
print(superuser.password)
