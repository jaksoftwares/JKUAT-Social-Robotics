
# import logging
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseServerError, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect, render
from dashboard.forms import PersonForm
from people.models import Person
from news.models import News
from events.models import Event
from publications.models import Publication
from robots.models import Robot

@login_required
def dashboard(request):
    # Fetch all people
    people = Person.objects.all()  

    # Fetch all news
    news_list = News.objects.all().order_by('-date_published')  

    # Fetch all events
    events = Event.objects.all().order_by('-date_starting')

    # Fetch all publications
    publications = Publication.objects.all().order_by('-created_at')
    
    # Fetch all Robots
    robot = Robot.objects.all().order_by('-title')


    context = {
        'people': people,
        'news_list': news_list,
        'events': events,
        'publications': publications,
        'robot': robot
    }
    
    return render(request, 'dashboard/siteadmin.html', context)

def get_edit_form(request, slug):
    person = get_object_or_404(Person, slug=slug)
    form = PersonForm(instance=person)
    
    # Render the form to HTML (only the form fields)
    form_html = render_to_string('dashboard/edit_form_fields.html', {'form': form})
    
    return JsonResponse({'form_html': form_html})

# logger = logging.getLogger(__name__)

def edit_person(request, slug):
    # Fetch the person object using the slug
    person = get_object_or_404(Person, slug=slug)
    
    # Return the person data as JSON
    person_data = {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "degree": person.degree,
        "specialty": person.specialty,
        "pursuing": person.pursuing,
        "focus_title": person.focus_title,
        "focus_short": person.focus_short,
        "focus_long": person.focus_long,
        "quote": person.quote,
        "bio": person.bio,
        "linked_in_link": person.linked_in_link,
        "personal_website_link": person.personal_website_link,
        "slug": person.slug,
    }
    return JsonResponse(person_data)

# def edit_person(request, slug):
#     person = get_object_or_404(Person, slug=slug)
    
#     if request.method == "POST":
#         form = PersonForm(request.POST, request.FILES, instance=person)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True, 'message': 'Person updated successfully'})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors})
    
    # Optionally handle GET requests if needed
    # return JsonResponse({'success': False, 'message': 'Invalid method'})

def delete_person(request, slug):
    person = get_object_or_404(Person, slug=slug)
    person.delete()
    return redirect('dashboard')  # Redirect to dashboard after successful delete

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('dashboard:dashboard')

def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    publication.delete()
    return redirect('dashboard:dashboard')

def delete_robot(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    robot.delete()
    return redirect('dashboard:dashboard')


