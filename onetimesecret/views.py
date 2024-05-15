from onetimesecret.models import Secret
from django.views.generic import CreateView, TemplateView
from onetimesecret.forms import SecretForm
from onetimesecret.services import generate_code
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404


class SecretCreateView(CreateView):
    model = Secret
    form_class = SecretForm

    def form_valid(self, form):
        new_secret = form.save(commit=False)
        new_secret.code = generate_code()
        new_secret.time = timezone.now()
        new_secret.days = form.cleaned_data['days']
        new_secret.time += timedelta(days=new_secret.days)
        new_secret.save()
        return render(self.request,
                      'onetimesecret/secret_created.html',
                      {'secret_code': new_secret.code})


class SecretGetView(TemplateView):
    template_name = 'onetimesecret/secret_page.html'

    def get_context_data(self, **kwargs):
        code = self.kwargs['code']
        secret_object = get_object_or_404(Secret, code=code)
        secret = secret_object.text  # Здесь используем значение поля text
        secret_object.delete()  # Удаляем секрет из базы данных
        return {'secret': secret}
