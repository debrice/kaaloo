from django import template
from django.utils.translation import ugettext as _
from exceptions import Exception
register = template.Library()

@register.inclusion_tag('status.html')
def user_status(user, time=True):
    from timer.models import TimeRecord
    status = _('Unknow')
    time_record = None
    try:
        time_record = TimeRecord.objects.get(user=user, stop_date=None)
        status = _('Working on %s') % (time_record.title)
    except TimeRecord.DoesNotExist, e :
        status = _('On Pause')
    return {'status':status, 'time_record':time_record, 'time':time}

@register.simple_tag
def name_or_email(user, max_char=None):
    if user.first_name and user.last_name:
        value = "%s %s" % (user.first_name, user.last_name)
    else:
        value = user.email
    if max_char and len(value) > int(max_char):
        return value[:int(max_char)-3] + '...'
    return value

@register.simple_tag
def name_and_email(user, max_char=None):
    if user.first_name and user.last_name:
        value = "%s %s - %s" % (user.first_name, user.last_name, user.email)
    else:
        value = user.email
    if max_char and len(value) > int(max_char):
        return value[:int(max_char)-3] + '...'
    return value

@register.inclusion_tag('user_detail.html')
def user_detail(user):
    return {'user':user}
