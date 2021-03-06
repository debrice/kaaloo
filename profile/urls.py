from django.conf.urls.defaults import *

urlpatterns = patterns('profile.views',
    url(r'^login/$', 'login_view', name='login_view'),
    url(r'^logout/$', 'logout_view', name='logout_view'),
    url(r'^register/$', 'register_view', name='register_view'),
    url(r'^me/$', 'profile_view', name='profile_view'),
    url(r'^password/$', 'password_view', name='password_view'),
    url(r'^confirm/(?P<key>[0-9a-z\-]+)/$', 'register_confirm', name='register_confirm'),
    url(r'^anonymous/$', 'unconnected_view', name='unconnected_view'),
    url(r'^thank_you/$', 'thank_you_for_registering', name='thank_you_for_registering'),
    url(r'^sent/$', 'registration_sent', name='registration_sent'),
    #url(r'^accept_invitation/([\w-]+)/$', 'accept_invitation', name='profile_accept_invitation'),
)

urlpatterns += patterns('',
    url(r'^new_account/confirm/$', 'django.views.generic.simple.direct_to_template', {'template':'profile/new_account_confirm.html'}, name='profile_new_account_confirm'),
)
