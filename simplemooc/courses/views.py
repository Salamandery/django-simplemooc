from django.shortcuts import render, get_object_or_404

from simplemooc.logging import Logger

from .models import Course
from .forms import ContactCourses

logger = Logger()
# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    
    return render(request, 'courses/index.html', context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    form = ContactCourses()
    context = {}

    if request.method == 'POST':
        form = ContactCourses(request.POST)

        if form.is_valid():
            context['is_valid'] = True

            logger.info('##### dados recebidos #####')
            logger.info(form.cleaned_data)
            
            form.send_mail(course)
            form = ContactCourses()
    
    context['form'] = form
    context['course'] = course
    
    return render(request, 'courses/details.html', context)