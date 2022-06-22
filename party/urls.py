"""party URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from party import views
from party.views import AddPersonView, EditPersonView, EditPartyView, AddPartyView, DeletePartyView, DeletePersonView

urlpatterns = [
    path('admin/', admin.site.urls),

    #VIEWS
    path('', views.homepage),

    path('add_party/', AddPartyView.as_view()),
    path('edit_party/<int:party_id>/', EditPartyView.as_view(), name='edit_party'),
    path('delete_party/<int:party_id>/', DeletePartyView.as_view()),
    path('parties/<int:id>', views.party_detail),
    path('parties/edit/<int:id>', views.EditPartyView.as_view),

    path('add_person/', AddPersonView.as_view()),
    path('edit_person/<int:person_id>/', EditPersonView.as_view(), name='edit_person'),
    path('delete_person/<int:person_id>/', DeletePersonView.as_view()),
    path('persons/<int:id>', views.person_detail),
    path('persons/edit/<int:id>', views.EditPersonView.as_view),

    # API
    path('api/', views.api_all_data),
    path('api/parties/', views.api_party_list),
    path('api/parties/<int:id>', views.api_party_detail),
    path('api/persons/', views.api_person_list),
    path('api/persons/<int:id>', views.api_person_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)