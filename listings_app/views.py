from django.shortcuts import render
from .models import Listing 
from .choices import state_choices,price_choices,bedroom_choices

# Create your views here.

def index(request):
        query_set = Listing.objects.order_by('-list_date')
        print(query_set,1)
        if 'keyword' in request.GET : 
            keyword = request.GET['keyword']
            if keyword:
                query_set = query_set.filter(description__icontains = keyword)
            
        if 'city' in request.GET : 
            city = request.GET['city']
            if city:
                query_set = query_set.filter(city__iexact = city)

            print(query_set,city)
            
        if 'state' in request.GET : 
            state = request.GET['state']
            if state:
                query_set = query_set.filter(state__iexact = state)
            print(query_set,state)
        if 'bedroom' in request.GET : 
            bedroom = request.GET['bedroom']
            if bedroom:
                query_set = query_set.filter(bedrooms__lte = bedroom)
            print(query_set,bedroom)
        if 'maxprice' in request.GET : 
            maxprice = request.GET['maxprice']
            if maxprice:
                query_set = query_set.filter(price__lte = maxprice)      
            print(query_set,maxprice)

        context ={ 'listings' : query_set, 
                    'state_choices': state_choices,
                    'bedroom_choices' :bedroom_choices,
                    'price_choices' : price_choices,
                    'values' : request.GET,
        }
        print(query_set)
        
        return render(request, 'listings\index.html', context)

