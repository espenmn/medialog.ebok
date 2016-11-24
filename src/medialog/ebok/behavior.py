#from zope import schema
from zope.interface import Interface
#from plone.directives import form
#from plone.autoform.interfaces import IFormFieldProvider
#from zope.interface import alsoProvides
#from zope.i18nmessageid import MessageFactory
#from zope.interface import implements
#from pp.client.plone.interfaces import IPPContent 


#_ = MessageFactory('medialog.ebok')


class IBokBehavior(Interface):
    """Mark item for pdf-template"""
    pass
    
#    something = schema.TextLine(
#        title = _("h", default=u"h"),
#        required = False,
#        description = _("helps",
#                      default="Dont be a "),
#    )
#   
#alsoProvides(IBokBehavior, IFormFieldProvider)


