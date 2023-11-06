from django.shortcuts import render
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import pdfkit
from django.template.loader import get_template
import io
from db.models import Experience,Client,Certificates,Community,Education,Hobbies,Internships,Languages,Skills,Training
from db.models import *
from django.urls import reverse
from django.urls import resolve
from django.views import View
from xhtml2pdf import pisa
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def data_collect():

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
    return cv



# Opens up page as PDF
class engViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('engcv.html', data_collect())
        return HttpResponse(pdf, content_type='application/pdf')
class arViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('arcv.html', data_collect())
        return HttpResponse(pdf, content_type='application/pdf')
class frViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('frcv.html', data_collect())
        return HttpResponse(pdf, content_type='application/pdf')

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


