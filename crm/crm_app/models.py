from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

# Custom User Model
class User(AbstractUser):
    is_organizer = models.BooleanField(_("organizer"), default=False)
    is_agent = models.BooleanField(_("agent"), default=False)

# User Profile Model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("customer", "Customer"),
        ("manager", "Manager"),
        ("hr", "HR"),
    ]
    
    user = models.OneToOneField(User, verbose_name=_("User Profile"), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

# Agent Model
class Agent(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Agent"), on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, related_name='agent_organisation', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse_lazy("agents:detail-agent", kwargs={"pk": self.pk})

# Client Model
class Client(models.Model):
    name = models.CharField(max_length=240)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=240)
    date_created = models.DateTimeField(auto_now_add=True)
    organisation = models.ForeignKey(UserProfile, related_name='client_organisation', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("crm:detail-client", kwargs={"pk": self.pk})


# Calendar Event Model
class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")
    attendees = models.ManyToManyField(User, related_name="events_attending")

    def __str__(self):
        return self.title


# Document Model
class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.title


# Meeting Model
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_meetings")
    attendees = models.ManyToManyField(User, related_name="meetings_attending")
    google_meet_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


# Task Model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# HR Models
class HRFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"HR File for {self.user.username}"


class LeaveRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Leave Record for {self.user.username}"


class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Timesheet for {self.user.username} on {self.date}"


class Payslip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to="payslips/")

    def __str__(self):
        return f"Payslip for {self.user.username} on {self.date}"


class PerformanceReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    review = models.TextField()

    def __str__(self):
        return f"Performance Review for {self.user.username} on {self.date}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="expenses/", blank=True)

    def __str__(self):
        return f"Expense for {self.user.username} on {self.date}"


class PrivateNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f"Private Note for {self.user.username} on {self.date}"


class Policy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# OKR Models
class Objective(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title


class OKRTask(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="okr_tasks")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Department and Role Models
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="roles")

    def __str__(self):
        return self.name
