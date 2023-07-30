from django.shortcuts import render
from .models import ProGandlavedu
from .models import Profriends

# Create your views here.
def index(request):

    giri1=Profriends()
    giri1.img='paddy1.jpg'
    giri1.name='PADDY'
    giri1.desc='THESE PRODUCTS ARE HEAVILY PRODUCED IN gANDLVEDU VILAGE AND IT IS ONE OF MAJOR CROPS..Most of the farmers are depend on these crops and these are very needy for both development of the country..'
    giri1.acres='nearly 250 acres yearly'

    giri2=Profriends()
    giri2.img='cotton.jpg'
    giri2.name='COTTON'
    giri2.desc='THESE PRODUCTS ARE HEAVILY PRODUCED IN gANDLVEDU VILAGE AND IT IS ONE OF MAJOR CROPS..Most of the farmers are depend on these crops and these are very needy for both development of the country..'
    giri2.acres='nearly 300 acres yearly'

    giri3=Profriends()
    giri3.img='tobacco2.jpg'
    giri3.name='TOBACCO'
    giri3.desc='THESE PRODUCTS ARE HEAVILY  FINANCIALLY VERY BENEFICIARY PRODUCED IN gANDLVEDU VILAGE AND IT IS ONE OF MAJOR CROPS..Most of the farmers are depend on these crops and these are very needy for both development of the country..'
    giri3.acres='nearly 700 acres yearly'


    sri1=ProGandlavedu()
    sri1.img='students2.jpg'
    sri1.name='students'
    sri1.desc='studying in various cities and towns'
    sri1.members='200'
    sri1.age='below the age 23'

    sri2=ProGandlavedu()
    sri2.img='job.jpg'
    sri2.name='job holders'
    sri2.desc='working in various companies and departments'
    sri2.members='250'
    sri2.age='above age 23 and below age 45'

    sri3=ProGandlavedu()
    sri3.img='agric.jpg'
    sri3.name='men and women'
    sri3.desc='Men and women working in fields and various departments'
    sri3.members='450'
    sri3.age='above the age 45'

    
    
    giris=[giri1,giri2,giri3]
    sris=[sri1,sri2,sri3]
    
    return render(request,'index.html',{'giris':giris,'sris':sris})
