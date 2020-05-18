from django.shortcuts import render
from django.views.generic import ( DetailView, 
                                TemplateView, 
                                FormView, 
                                CreateView, 
                                UpdateView, 
                                ListView,

                                )
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm
from .models import Criminal
import numpy as np
from .face_rec import encode_face,resolve_image
# Create your views here.

def search_result(request):
    if request.method == "POST":
        form = SearchForm(request.POST,request.FILES)
        if form.is_valid():
            # print(Criminal.image_data)
            all_encodings = []
            all_id = []
            for i in Criminal.objects.all():
                all_encodings.append(np.array(i.image_data))
                all_id.append(i.pk)
            # print(request.FILES['upload_image'])
            ids = resolve_image(request.FILES['upload_image'],all_encodings,all_id)
            if ids:
                return render(request,'criminal_stuff/search_image.html',{'criminal':Criminal.objects.get(pk=ids)})
            else:
                return render(request,'criminal_stuff/search_image.html',{'sorry':'someone new'})
            
    else:
        form = SearchForm()
    
    return render(request,'criminal_stuff/search_image.html',{'form':form})


class CreateCriminalStuff(LoginRequiredMixin,CreateView):
    model = Criminal
    fields = ['name', 'address', 'pin_code', 'phone_number', 'crime_category', 'crime_description',
            'image'
        ]
    template_name = 'criminal_stuff/upload_data.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.booked_at_police_station = self.request.user
        form.instance.image_data = list(encode_face(form.instance.image))
        # print(list(form.instance.image_data))
        return super().form_valid(form)

class RetrieveCriminalStuffList(ListView):
    pass

class RetrieveCriminalStuff(TemplateView):
    template_name = 'search_result'
