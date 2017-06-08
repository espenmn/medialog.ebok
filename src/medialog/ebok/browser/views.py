from Products.Five.browser import BrowserView
from medialog.ebok.interfaces import IBokSettings
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
        manifest_base =api.portal.get_registry_record('manifest_base', interface=IBokSettings)
        folder_path = '/'.join(context.getPhysicalPath())
        
        all_content_brains = catalog(path=folder_path, sort_on='modified', sort_order='descending')

        manifest = str(all_content_brains[0].modified)         
        for brain in all_content_brains:
            manifest += "\n"
            manifest += brain.getURL() 
            
    	return """CACHE MANIFEST 
%(manifest_base)s
#%(manifest)s



"""  % {
        'manifest': manifest,
        'manifest_base': manifest_base,    
        }
