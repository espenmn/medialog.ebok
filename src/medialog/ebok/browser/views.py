from Products.Five.browser import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BookView(BrowserView):
    """ Cache Manifest file.
    """
 
    # template = ViewPageTemplateFile('cachelist.pt')

    def __call__(self, *args, **kw):
         
        return self.manifestlist(self.context)
        #return self.template(self.context)
        
        
    def manifestlist(self, context)
    	return """CACHE MANIFEST 
#date 4


NETWORK: 
*

CACHE:
http://k16.medialog.no/medical-english
/medical-english
http://ebok.medialog.no/++plone++production/++unique++2017-02-20T15:00:43.561263/default.css
http://ebok.medialog.no//++theme++ebooktheme/less/barceloneta-compiled.css
http://k16.medialog.no/++theme++ebooktheme/markdown.css


# FALLBACK:
# / /++theme++k16theme/offline.html

"""