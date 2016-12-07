from django.contrib import messages
from django.views.generic import FormView

from .forms import TestForm


class TestFormView(FormView):
    form_class = TestForm
    template_name = 'test.html'
    success_url = '/'

    def form_valid(self, form):
        for field in form.fields:
            for choice, date_list in form.cleaned_data[field]:
                msg = '%s - %s : ' % (field, choice)
                messages.success(self.request, msg + ', '.join(
                    d.strftime('%Y/%m/%d') for d in date_list))
        return super().form_valid(form)
