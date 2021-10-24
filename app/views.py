from django.forms import formsets
from django.views.generic import ListView, TemplateView
from .models import Bird
from .forms import BirdFormSet
from django.urls import reverse_lazy
from django.shortcuts import redirect


class BirdListView(ListView):
    model = Bird
    template_name = "bird_list.html"


class BirdAddView(TemplateView):
    template_name = "app/add_bird.html"

    # untuk GET request
    def get(self, *args, **kwargs):
        # tanpa parameter akan muncul semua dari DB. Mulai kosong (none)
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})

    # untuk POST request
    def post(self, *args, **kwargs):
        # instance untuk tampung data post
        formset = BirdFormSet(data=self.request.POST)

        # jika valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("app:bird_list"))
        
        return self.render_to_response({'bird_formset': formset})
