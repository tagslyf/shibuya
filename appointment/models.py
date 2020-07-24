from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='patient_user')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Doctor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL, related_name='appointment_doctor')
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    comments = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
