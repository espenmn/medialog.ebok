from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BookView(BrowserView):
    """ Converter view for Bok.
    """

    template = ViewPageTemplateFile('book.pt')

    def __call__(self, *args, **kw):
        return self.template(self.context)

InitializeClass(BookView)

