from django.conf.urls.defaults import *

urlpatterns = patterns('contact.views',
    url(r'^my/$', 'contact_view', name='contact_view'),
    url(r'^add/$', 'add_contact_view', name='add_contact_view'),
    url(r'^requests/$', 'contact_requests_view', name='contact_requests_view'),
    url(r'^confirm/(?P<key>[0-9a-z\-]+)/$', 'contact_confirm_view', name='contact_confirm_view'),
    url(r'^invite/(?P<key>[0-9a-z\-]+)/$', 'invite_confirm_view', name='invite_confirm_view'),
    url(r'^added/$', 'contact_added', name='contact_added'),
    url(r'^refused/$', 'contact_refused', name='contact_refused'),
    url(r'^sent/$', 'invite_sent', name='invite_sent'),
    url(r'^detail/(?P<contact_id>\d+)/$', 'contact_detail', name='contact_detail'),
)
