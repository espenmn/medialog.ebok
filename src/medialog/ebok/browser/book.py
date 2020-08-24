from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BookView(BrowserView):
    """ Converter view for Bok.
    """
    template = ViewPageTemplateFile('book.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
            'convertFootnotes',
            'removeCrapFromHeadings',
            'fixHierarchies',
        )

        return self.template(self.context)

InitializeClass(BookView)



class OneChapterView(BrowserView):
    """ PDF Converter view for one chapter.
    """
    template = ViewPageTemplateFile('one_chapter.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
            'removeCrapFromHeadings',
            'convertFootnotes',
            'fixHierarchies',
        )

        return self.template(self.context)

InitializeClass(OneChapterView)

#'removeCrapFromHeadings',
