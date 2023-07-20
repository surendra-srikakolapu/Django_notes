***********************COMMANDS & INSTALLATION************************


---------------------------celery 4+ (windows)--------------------

pip install celery
pip install gevent

(venv) $ celery -A (project_dire_name) worker -l info -P gevent

---------------------------below versions-------------------------

pip install celery
(venv) $ python -m celery -A (project_dire_name) worker -l info


****************************************************************




























***************************DJANGO SETTING*****************************

------------------------------_ _init_ _-----------------------------


from .celery import app as celery_app

__all__ = ("celery_app",)



-----------------------------settings------------------------------


CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


***********************************************************************










**************************celery.py(in settings_dir)**********************

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project-name.settings")
app = Celery("project-name")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


**************************************************************************













**************************tasks.py(in app_dir)**********************

from celery import shared_task


@shared_task()
def sending_mail(email_address, message):

    sleep(20) 
    send_mail(
        # "Your Feedback",
        # f"\t{message}\n\nThank you!",
        # "support@example.com",
        # [email_address],
        # fail_silently=False,
    )

**************************************************************************










**************************forms.py(add delay() to form)(in app_dir)**********************

from django import forms

from appname.tasks import sending_mail


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )

**************************************************************************








**************************views.py(in app_dir)**********************

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

# from appname.forms import FeedbackForm


# class FeedbackFormView(FormView):
#     template_name = "feedback/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/success/"

#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)


# class SuccessView(TemplateView):
#     template_name = "feedback/success.html"





**************************************************************************










**************************urls.py(in app_dir)**********************

# from django.urls import path

# from appname.views import FeedbackFormView, SuccessView

# app_name = "----"

# urlpatterns = [
#     path("", FeedbackFormView.as_view(), name="feedback"),
#     path("success/", SuccessView.as_view(), name="success"),
# ]

**************************************************************************












