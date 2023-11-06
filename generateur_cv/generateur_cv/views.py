from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import pdfkit
from django.template.loader import get_template
import io
from db.models import Experience,Client,Certificates,Community,Education,Hobbies,Internships,Languages,Skills,Training
from db.models import *
from app import views
from django.views import *
from django.views import View
from xhtml2pdf import pisa
from datetime import date
from app.views import landing
def ba3dou(request):
    return redirect('formp0.html')
def landing(request):
    Client.objects.all().delete()
    Education.objects.all().delete()
    Training.objects.all().delete()
    Experience.objects.all().delete()
    Skills.objects.all().delete()
    Languages.objects.all().delete()
    Hobbies.objects.all().delete()
    Internships.objects.all().delete()
    Community.objects.all().delete()
    Certificates.objects.all().delete()
    return render(request,'formp0.html')
def eng1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        adress = request.POST.get("adress")
        postal = request.POST.get("poste")
        town = request.POST.get("town")
        phone = request.POST.get("phone")
        mail = request.POST.get("mail")
        picture = request.POST.get("profile_photo")
        donnees = Client(name=name,adress=adress,postal=postal,town=town,phone=phone,mail=mail,picture=picture)
        donnees.save()
        return redirect('engformp2.html')
    return render(request,'engformp1.html')



def eng2(request):
    if request.method == "POST":

        nationality = request.POST.get("nat")
        date_of_birth = request.POST.get("date")
        link = request.POST.get("site")
        license = request.POST.get("licence")
        profile = request.POST.get("story")

        Client.objects.update(nationality=nationality,date_of_birth=date_of_birth,link=link,license=license,profile=profile)
        return redirect('engformp3.html')
    return render(request,'engformp2.html')



def eng3(request):
    return render(request,'engformp3.html')



def eng4(request):
    if request.method == "POST":
        degree = request.POST.get("degree")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if  request.POST.get("noend")==False:
            end = request.POST.get("end")
        else:
            end = date.today()
        description = request.POST.get("description")
        donnees = Education(degree=degree, establishment=establishment, town=town, start=start,end=end,description=description)
        donnees.save()
        return redirect('engformp4.html')
    return render(request,'engformp4.html')



def eng5(request):
    if request.method == "POST":
        training = request.POST.get("training")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend") == False:
            end = request.POST.get("end")
        else:
            end = date.today()
        description = request.POST.get("description")
        donnees = Training(training=training, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('engformp5.html')
    return render(request,'engformp5.html')


def eng6(request):
    if request.method == "POST":
        experience = request.POST.get("exp")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend") == False:
            end = request.POST.get("end")
        else:
            end = date.today()
        description = request.POST.get("description")
        donnees = Experience(experience=experience, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('engformp6.html')
    return render(request,'engformp6.html')




def eng7(request):
    if request.method == "POST":
        skill = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Skills(skill = skill, level = level)
        donnees.save()
        return redirect('engformp7.html')
    return render(request,'engformp7.html')



def eng8(request):
    if request.method == "POST":
        language = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Languages(language = language,level = level)
        donnees.save()
        return redirect('engformp8.html')
    return render(request,'engformp8.html')



def eng9(request):
    if request.method == "POST":
        hobbies = request.POST.get("skill")
        donnees = Hobbies(hobbies=hobbies)
        donnees.save()
        return redirect('engformp9.html')
    return render(request,'engformp9.html')


def eng10(request):
    if request.method == "POST":
        internship = request.POST.get("int")
        employer = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend") == False:
            end = request.POST.get("end")
        else:
            end = date.today()
        description = request.POST.get("description")
        donnees = Internships(internship=internship, employer=employer, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('engformp10.html')
    return render(request,'engformp10.html')



def eng11(request):
    if request.method == "POST":
        experience = request.POST.get("ex")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend") == False:
            end = request.POST.get("end")
        else:
            end = date.today()
        description = request.POST.get("description")
        donnees = Community(experience=experience, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('engformp11.html')
    return render(request,'engformp11.html')


def eng12(request):
    if request.method == "POST":
        certificate = request.POST.get("certificate")
        description = request.POST.get("description")
        if request.POST.get("noend")==False:
            period = request.POST.get("months")+'months'+request.POST.get("days")+'days'
            donnees = Certificates(certificate=certificate, period=period, description=description)
            donnees.save()
            return redirect('engformp12.html')
    return render(request,'engformp12.html')






def ar1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        adress = request.POST.get("adress")
        postal = request.POST.get("poste")
        town = request.POST.get("town")
        phone = request.POST.get("phone")
        mail = request.POST.get("mail")
        picture = request.POST.get("profile_photo")
        donnees = Client(name=name,adress=adress,postal=postal,town=town,phone=phone,mail=mail,picture=picture)
        donnees.save()
        return redirect('arformp2.html')
    return render(request,'arformp1.html')
def ar2(request):
    if request.method == "POST":

        nationality = request.POST.get("nat")
        date_of_birth = request.POST.get("date")
        link = request.POST.get("site")
        license = request.POST.get("licence")
        profile = request.POST.get("story")

        Client.objects.update(nationality=nationality,date_of_birth=date_of_birth,link=link,license=license,profile=profile)
        return redirect('arformp3.html')
    return render(request,'arformp2.html')
def ar3(request):
    return render(request,'arformp3.html')
def ar4(request):
    if request.method == "POST":
        degree = request.POST.get("degree")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end=Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Education(degree=degree, establishment=establishment, town=town, start=start,end=end,description=description)
        donnees.save()
        return redirect('arformp4.html')
    return render(request,'arformp4.html')
def ar5(request):
    if request.method == "POST":
        training = request.POST.get("training")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Training(training=training, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('arformp5.html')
    return render(request,'arformp5.html')
def ar6(request):
    if request.method == "POST":
        experience = request.POST.get("exp")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Experience(experience=experience, employer=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('arformp6.html')
    return render(request,'arformp6.html')
def ar7(request):
    if request.method == "POST":
        skill = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Skills(language = skill,level = level)
        donnees.save()
        return redirect('arformp7.html')
    return render(request,'arformp7.html')
def ar8(request):
    if request.method == "POST":
        language = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Languages(language = skill,level = level)
        donnees.save()
        return redirect('arformp8.html')
    return render(request,'arformp8.html')
def ar9(request):
    if request.method == "POST":
        hobbies = request.POST.get("skill")
        donnees = Hobbies(hobbies=hobbies)
        donnees.save()
        return redirect('arformp10.html')
    return render(request,'arformp9.html')
def ar10(request):
    if request.method == "POST":
        internship = request.POST.get("int")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Internships(internship=internship, employer=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('arformp11.html')
    return render(request,'arformp10.html')
def ar11(request):
    if request.method == "POST":
        experience = request.POST.get("ex")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = None
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Community(experience=experience, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('arformp11.html')
    return render(request,'arformp11.html')
def ar12(request):
    if request.method == "POST":
        certificate = request.POST.get("certificate")
        description = request.POST.get("description")
        if request.POST.get("noend"):
            period = None
        else:
            period = request.POST.get("months")+'months'+request.POST.get("days")+'days'
            donnees = Certificates(certificate=certificate, period=period, description=description)
            donnees.save()
            return redirect('arformp12.html')
    return render(request,'arformp12.html')

def fr1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        adress = request.POST.get("adress")
        postal = request.POST.get("poste")
        town = request.POST.get("town")
        phone = request.POST.get("phone")
        mail = request.POST.get("mail")
        picture = request.POST.get("profile_photo")
        donnees = Client(name=name,adress=adress,postal=postal,town=town,phone=phone,mail=mail,picture=picture)
        donnees.save()
        return redirect('frformp2.html')
    return render(request,'frformp1.html')
def fr2(request):
    if request.method == "POST":

        nationality = request.POST.get("nat")
        date_of_birth = request.POST.get("date")
        link = request.POST.get("site")
        license = request.POST.get("licence")
        profile = request.POST.get("story")

        Client.objects.update(nationality=nationality,date_of_birth=date_of_birth,link=link,license=license,profile=profile)
        return redirect('frformp3.html')
    return render(request,'frformp2.html')
def fr3(request):
    return render(request,'frformp3.html')
def fr4(request):
    if request.method == "POST":
        degree = request.POST.get("degree")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end=Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Education(degree=degree, establishment=establishment, town=town, start=start,end=end,description=description)
        donnees.save()
        return redirect('frformp4.html')
    return render(request,'frformp4.html')
def fr5(request):
    if request.method == "POST":
        training = request.POST.get("training")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Training(training=training, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('frformp5.html')
    return render(request,'frformp5.html')
def fr6(request):
    if request.method == "POST":
        experience = request.POST.get("exp")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Experience(experience=experience, employer=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('frformp6.html')
    return render(request,'frformp6.html')
def fr7(request):
    if request.method == "POST":
        skill = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Skills(language = skill,level = level)
        donnees.save()
        return redirect('frformp7.html')
    return render(request,'frformp7.html')
def fr8(request):
    if request.method == "POST":
        language = request.POST.get("skill")
        level = request.POST.get("level")
        donnees = Languages(language = skill,level = level)
        donnees.save()
        return redirect('frformp8.html')
    return render(request,'frformp8.html')
def fr9(request):
    if request.method == "POST":
        hobbies = request.POST.get("skill")
        donnees = Hobbies(hobbies=hobbies)
        donnees.save()
        return redirect('frformp10.html')
    return render(request,'frformp9.html')
def fr10(request):
    if request.method == "POST":
        internship = request.POST.get("int")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = Null
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Internships(internship=internship, employer=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('frformp11.html')
    return render(request,'frformp10.html')
def fr11(request):
    if request.method == "POST":
        experience = request.POST.get("ex")
        establishment = request.POST.get("establishment")
        town = request.POST.get("town")
        start = request.POST.get("start")
        if request.POST.get("noend"):
            end = None
        else:
            end = request.POST.get("end")
        description = request.POST.get("description")
        donnees = Community(experience=experience, establishment=establishment, town=town, start=start, end=end,
                            description=description)
        donnees.save()
        return redirect('frformp11.html')
    return render(request,'frformp11.html')
def fr12(request):
    if request.method == "POST":
        certificate = request.POST.get("certificate")
        description = request.POST.get("description")
        if request.POST.get("noend"):
            period = None
        else:
            period = request.POST.get("months")+'months'+request.POST.get("days")+'days'
            donnees = Certificates(certificate=certificate, period=period, description=description)
            donnees.save()
            return redirect('frformp12.html')
    return render(request,'frformp12.html')






def engcv(request):
    cl = Client.objects.all()
    h = Hobbies.objects.all()
    s = Skills.objects.all()
    t = Training.objects.all()
    c = Certificates.objects.all()
    e = Education.objects.all()
    com = Community.objects.all()
    exp = Experience.objects.all()
    int = Internships.objects.all()
    l = Languages.objects.all()
    cv = {
        't' : t,
        'cl': cl,
        'c': c,
        'e': e,
        'com': com,
        'exp': exp,
        'int': int,
        'l': l,
        'h': h,
    }

    return render(request,'engcv.html',cv)
def arcv(request):
    cls = Client.objects.all()

    for i in cls:
        cl = i

    h = Hobbies.objects.all()
    s = Skills.objects.all()
    t = Training.objects.all()
    c = Certificate.objects.all()
    e = Education.objects.all()
    com = Community.objects.all()
    exp = Experience.objects.all()
    int = Internships.objects.all()
    l = Languages.objects.all()
    cv = {
        't' : t,
        'cl': cl,
        'c': c,
        'e': e,
        'com': com,
        'exp': exp,
        'int': int,
        'l': l,
        'h': h,
    }
    return render(request,'arcv.html',cv)
def frcv(request):
    cls = Client.objects.all()
    for i in cls:
        cl = i
    h = Hobbies.objects.all()
    s = Skills.objects.all()
    t = Training.objects.all()
    c = Certificate.objects.all()
    e = Education.objects.all()
    com = Community.objects.all()
    exp = Experience.objects.all()
    int = Internships.objects.all()
    l = Languages.objects.all()
    cv = {
        't' : t,
        'cl': cl,
        'c': c,
        'e': e,
        'com': com,
        'exp': exp,
        'int': int,
        'l': l,
        'h': h,
    }
    return render(request,'frcv.html',cv)
