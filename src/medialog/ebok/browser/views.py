from Products.Five.browser import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone import api


class CacheManifest(BrowserView):
    """ Cache Manifest file.
    """
 
    # template = ViewPageTemplateFile('cachelist.pt')

    def __call__(self, *args, **kw):
         
        return self.manifestlist(self.context)
        #return self.template(self.context)
        
        
    def manifestlist(self, context):
        catalog = api.portal.get_tool(name='portal_catalog')
        folder_path = '/'.join(context.getPhysicalPath())
        
        all_content_brains = catalog(path=folder_path, sort_on='modified', sort_order='descending')

        manifest = str(all_content_brains[0].modified)         
        for brain in all_content_brains:
            manifest += "\n"
            manifest += brain.getURL() 
            
    	return """CACHE MANIFEST 


NETWORK: 
*

CACHE:
/++theme++k16theme/markdown.css
/++theme++k16theme/barceloneta-favicon.ico
/++theme++k16theme/barceloneta-apple-touch-icon.png
/++theme++k16theme/barceloneta-apple-touch-icon-144x144-precomposed.png
/++theme++k16theme/barceloneta-apple-touch-icon-114x114-precomposed.png
/++theme++k16theme/barceloneta-apple-touch-icon-72x72-precomposed.png
/++theme++k16theme/barceloneta-apple-touch-icon-57x57-precomposed.png
/++theme++k16theme/barceloneta-apple-touch-icon-precomposed.png
          
http://k16.medialog.no//++theme++k16theme/less/barceloneta-compiled.css 
http://k16.medialog.no/++theme++ebooktheme/markdown.css

#%(manifest)s

# FALLBACK:
# / /++theme++k16theme/offline.html

"""  % {
        'manifest': manifest,
        }