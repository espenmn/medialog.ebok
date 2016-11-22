from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory



_ = MessageFactory('medialog.ebok')


class ICaptchaBehavior(form.Schema):
    something = schema.TextLine(
        title = _("h", default=u"h"),
        required = False,
        description = _("helps",
                      default="Dont be a "),
    )
   
alsoProvides(ICaptchaBehavior, IFormFieldProvider)


