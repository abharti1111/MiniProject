from django.urls import path
from .views import search_result, RetrieveCriminalStuff,CreateCriminalStuff
urlpatterns = [
    path('search/',search_result, name='search'),
    path('add/',CreateCriminalStuff.as_view(), name='add'),
    
    # path('search/results/', RetrieveCriminalStuff.as_view(), name='searchresult'),


]