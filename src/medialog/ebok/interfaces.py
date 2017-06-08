# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from medialog.ebok import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer



from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.ebok')


class IMedialogEbokLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEbok(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )




class IBokSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'ebok',
        label=_(u'Ebok settings'),
        fields=[
             'manifest_base',
        ],
     )


        
    manifest_base = schema.Text (
    	title=_(u"Manifest base", default=u"Manifest base"),
    )
    
    
        
alsoProvides(IBokSettings, IMedialogControlpanelSettingsProvider)