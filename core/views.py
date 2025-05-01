from django.shortcuts import render
from django.db.models import Q
from people import models as PEOPLE_MODELS
from publications import models as PUBLICATIONS_MODELS
from projects import models as PROJECTS_MODELS
from outreach import models as OUTREACH_MODELS
from robots import models as ROBOTS_MODELS
from news import models as NEWS_MODELS
from events import models as EVENTS_MODELS
from datetime import datetime


def home(request):
    context = {
        "news": NEWS_MODELS.News.objects.all(),
        "upcoming_events": EVENTS_MODELS.Event.objects.filter(
            date_starting__gte=datetime.now()
        ),
        "past_events": EVENTS_MODELS.Event.objects.filter(
            date_starting__lte=datetime.now()
        ),
        # "msc_projects" :PROJECTS_MODELS.Project.objects.filter(category=PROJECTS_MODELS.Project.MSC)
         "projects": PROJECTS_MODELS.Project.objects.filter( category=PROJECTS_MODELS.Project.RE
        ),
        
    }

    return render(request, "core/index.html", context=context)


def about(request):
    # SEO content for the About page
    seo_data = {
        "title": "About Us | JKUAT Social Robotics Lab",
        "description": "Learn about the mission, vision, and innovative work done by the JKUAT Social Robotics Lab in AI, Robotics, and Engineering.",
        "keywords": "Social Robotics, AI, Robotics, JKUAT, Engineering, Innovation, Robotics Lab, About Us",
        "og_title": "About JKUAT Social Robotics Lab",
        "og_description": "Discover the vision and mission behind the JKUAT Social Robotics Lab and the cutting-edge research in Robotics and AI.",
        "og_image": "img/og-image-about.jpg",  # Make sure this image exists in your static folder
        "og_url": request.build_absolute_uri(),  # This will dynamically get the full URL of the page
        "twitter_title": "About JKUAT Social Robotics Lab",
        "twitter_description": "Explore the innovative research happening at the JKUAT Social Robotics Lab.",
        "twitter_image": "img/twitter-card-about.jpg",  # Make sure this image exists in your static folder
    }

    return render(request, "core/about.html", seo_data)


def admin(request):
    return render(request, "core/moderator.html")


def activities(request):
    context = {
        "news": NEWS_MODELS.News.objects.all(),
        "events": EVENTS_MODELS.Event.objects.all(),
    }
    return render(request, "core/activities.html", context=context)


def search(request):
    query = request.GET.get("q", "")
    if query:
        people = PEOPLE_MODELS.Person.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(degree__icontains=query)
            | Q(specialty__icontains=query)
            | Q(pursuing__icontains=query)
            | Q(focus_title__icontains=query)
            | Q(focus_short__icontains=query)
            | Q(focus_long__icontains=query)
            | Q(quote__icontains=query)
            | Q(category__icontains=query)
            | Q(bio__icontains=query)
        )
        publications = PUBLICATIONS_MODELS.Publication.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(external_link__icontains=query)
        )
        projects = PROJECTS_MODELS.Project.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(external_link__icontains=query)
        )
        outreach = OUTREACH_MODELS.Outreach.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(external_link__icontains=query)
        )
        robots = ROBOTS_MODELS.Robot.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(external_link__icontains=query)
        )
        news = NEWS_MODELS.News.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(external_link__icontains=query)
        )
    context = {
        "query": query,
        "people": people,
        "publications": publications,
        "projects": projects,
        "outreach": outreach,
        "robots": robots,
        "news": news,
    }
    return render(request, "core/search_results.html", context=context)
