from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from mayan.apps.events import EventTypeNamespace

namespace = EventTypeNamespace(
    name='user_management', label=_('User management')
)

event_group_created = namespace.add_event_type(
    label=_('Group created'), name='group_created'
)
event_group_edited = namespace.add_event_type(
    label=_('Group edited'), name='group_edited'
)

event_user_created = namespace.add_event_type(
    label=_('User created'), name='user_created'
)
event_user_edited = namespace.add_event_type(
    label=_('User edited'), name='user_edited'
)