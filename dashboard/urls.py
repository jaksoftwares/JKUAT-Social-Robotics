# urls.py
from django.urls import path
from . import views
from .views import dashboard, delete_event, delete_publication, delete_robot
app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='siteadmin'),
    # path('edit-person/<slug:person_slug>/', views.edit_person, name='edit_person'),
    path('edit-person/<slug:slug>/', views.edit_person, name='edit_person'),
    path('delete_person/<slug:slug>/', views.delete_person, name='delete_person'),
    path('edit_form/<slug:slug>/', views.get_edit_form, name='get_edit_form'),
    path('delete-event/<int:event_id>/', delete_event, name='delete_event'),
    path('delete-publication/<int:publication_id>/', delete_publication, name='delete_publication'),
    path('delete-robot/<int:robot_id>/', delete_robot, name='delete_robot')
]
