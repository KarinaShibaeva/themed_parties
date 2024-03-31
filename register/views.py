import uuid

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.views import View

from register.forms import UserRegistrationForm
from register.models import EmailConfirmation


class RegisterUserView(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            email_confirmation = EmailConfirmation(user=user)
            email_confirmation.save()

            token = urlsafe_base64_encode(force_bytes(email_confirmation.token))
            confirmation_url = f'http://yourwebsite.com/confirm_email/{token}/'
            subject = 'Подтверждение регистрации'
            message = render_to_string('register/confirmation.html', {'confirmation_url': confirmation_url})
            send_mail(subject, message, 'noreply@yourwebsite.com', [user.email])

            return HttpResponse('Пожалуйста, проверьте вашу почту для подтверждения регистрации.')
        return HttpResponseBadRequest('Invalid form data')

class ConfirmEmailView(View):
    def get(self, request, token):
        try:
            token = uuid.UUID(urlsafe_base64_decode(token))
            confirmation = EmailConfirmation.objects.get(token=token)
            user = confirmation.user
            user.is_active = True
            user.save()
            confirmation.delete()
            return HttpResponse('Ваш аккаунт успешно подтвержден.')
        except EmailConfirmation.DoesNotExist:
            return HttpResponseBadRequest('Invalid confirmation link.')