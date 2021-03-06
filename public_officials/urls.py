from django.conf.urls import url
from . import views

app_name = 'public_officials'
urlpatterns = [
    url(r'^voting-history/$', views.voting_history, name="votes"),
    url(r'^sponsored-bills/$', views.sponsored_bills, name="sponsored-bills"),
    url(r'^organization-contributions/$', views.organization_contributions, name="organization"),
    url(r'^industry-contributions/$', views.industry_contributions, name="industry"),
    url(r'^(?P<legislator_id>[0-9]+)/$', views.legislator_detail, name="detail"),
]
