from django.contrib.auth.backends import BaseBackend
from .models import student_detalis

class CustomBackend(BaseBackend):
    def authenticate(self, request, name=None, roll=None):
        try:
            student = student_detalis.objects.get(name=name, roll=roll)
            return student
        except student_detalis.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return student_detalis.objects.get(pk=user_id)
        except student_detalis.DoesNotExist:
            return None