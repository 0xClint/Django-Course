from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january":"Januray",
    "february":"February",
    "march":"March",
    "april":"April",
    "may": "May",
    "june":"June",
    "july":"July",
    "august":"August",
    "september":"September",
    "october":"October",
    "november":"November",
    "december":"December"
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{"months":months})

    # list_items=""
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     redirect_path = reverse("month-challenges",args=[month])
    #     list_items +=f'<li><a href="{redirect_path}" >{capitalized_month}</a></li>' 
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)



def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())

    if(month> len(months)):
        return HttpResponseNotFound("<h2>Invalid month! :(<h2>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenges",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text= monthly_challenges[month]
        return render(request,"challenges/challenge.html",{"challenge_text":challenge_text,"month":month})
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # return render_to_string("<h2>page not Found!<h2>")