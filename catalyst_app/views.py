from .models import UploadedFile
from django.views.generic import CreateView, ListView
from .forms import UploadForms
from django.urls import reverse_lazy


class UploadList(ListView):
    model = UploadedFile
    context_object_name = "i"
    template_name = "h1.html"


class UploadCreate(CreateView):
    model = UploadedFile
    form_class = UploadForms
    template_name = "h2.html"
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        # Save the uploaded file
        uploaded_file = form.save(commit=False)
        uploaded_file.file = form.cleaned_data['file']
        uploaded_file.save()

        return super().form_valid(form)
