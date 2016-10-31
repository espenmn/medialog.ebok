from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

#from collective.z3cform.colorpicker import fields
#from collective.z3cform.colorpicker.fields import ColorAlpha

from collective.z3cform.colorpicker.colorpicker import IColorpickerWidget


class IColorBehavior(form.Schema):
    """Example color picker form"""
    
    form.widget(
            color=IColorpickerWidget,
    )

    color = schema.TextLine(
        title=u"Color",
        description=u"",
        required=False,
        default=u"#6298c9")

alsoProvides(IColorBehavior, IFormFieldProvider)