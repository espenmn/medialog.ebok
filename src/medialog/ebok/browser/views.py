from Products.Five.browser import BrowserView
from plone import api
from medialog.ebok.interfaces import IBokSettings


from urlparse import urlparse
from urllib import quote

from Acquisition import aq_inner, aq_base, aq_parent
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IBundleRegistry
from Products.CMFPlone.interfaces import IResourceRegistry
from plone.app.theming.utils import theming_policy
from plone.registry.interfaces import IRegistry
from zope import component
from zope.component import getMultiAdapter
from zope.component import getUtility
from Products.CMFPlone.resources.browser.combine import get_production_resource_directory

class CacheManifest(BrowserView):
    """ Cache Manifest file.
    Combines files from the catalog and urls added
    in the medialog control panel
    """

    def __call__(self, *args, **kw):
        self.update()
        #self.folder_path = '/'.join(self.site_url.getPhysicalPath())
        return self.manifestlist()

    def update(self):
        self.portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')
        self.site_url = self.portal_state.portal_url()
        self.registry = getUtility(IRegistry)

        self.production_path = get_production_resource_directory()

        self.diazo_production_css = None
        self.diazo_development_css = None
        self.diazo_development_js = None
        self.diazo_production_js = None
        self.themeObj = None

        # Check if its Diazo enabled
        policy = theming_policy(self.request)
        if policy.isThemeEnabled():
            self.themeObj = policy.get_theme()
            if self.themeObj:
                if hasattr(self.themeObj, 'production_css'):
                    self.diazo_production_css = self.themeObj.production_css
                    self.diazo_development_css = self.themeObj.development_css
                    self.diazo_development_js = self.themeObj.development_js
                    self.diazo_production_js = self.themeObj.production_js

    def get_resources(self):
        return self.registry.collectionOfInterface(
            IResourceRegistry, prefix="plone.resources", check=False)

    def styles(self):
        """
        Trying to get all the styles
        """
        result = [{
            'src': '%s/++plone++%s' % (
                self.site_url,
                self.production_path + '/default.css')
            },
        ]

        # Add manual added resources
        resources = self.get_resources()
        if hasattr(self.request, 'enabled_resources'):
            for resource in self.request.enabled_resources:
                if resource in resources:
                    for data in self.get_urls(resources[resource], None):
                        result.append(data)

        for bundle in self.bundles.values():
            css_path = bundle.csscompilation
            if css_path != None:
                if '++plone++' in css_path:
                    resource_path = css_path.split('++plone++')[-1]
                    resource_name, resource_filepath = resource_path.split(
                    '/', 1)
                    css_location = '%s/++plone++%s/++unique++%s/%s' % (
                        self.site_url,
                        resource_name,
                        quote(str(bundle.last_compilation)),
                        resource_filepath
                        )
                else:
                    css_location = '%s/%s?version=%s' % (
                        self.site_url,
                        bundle.csscompilation,
                        quote(str(bundle.last_compilation))
                        )
                result.append({
                    'src': css_location
                    })

        # Add diazo css
        origin = None
        if self.diazo_production_css:
            origin = self.diazo_production_css
        if origin:
            url = urlparse(origin)
            if url.netloc == '':
                # Local
                src = "%s%s" % (self.site_url, origin)
            else:
                src = "%s" % (origin)

            data = {'src': src}

            result.append(data)
        return result

    def get_scripts(self):
        result = [{
                'src': '%s/++plone++%s' % (
                    self.site_url,
                    self.production_path + '/default.js')
            },
        ]

        for bundle in self.bundles.values():
            js_path = bundle.jscompilation
            if js_path != None:
                if '++plone++' in js_path:
                    resource_path = js_path.split('++plone++')[-1]
                    resource_name, resource_filepath = resource_path.split('/', 1)
                    js_location = '%s/++plone++%s/++unique++%s/%s' % (
                        self.site_url,
                        resource_name,
                        quote(str(bundle.last_compilation)),
                        resource_filepath
                        )
                else:
                    js_location = '%s/%s?version=%s' % (
                        self.site_url,
                        bundle.csscompilation,
                        quote(str(bundle.last_compilation))
                        )
                result.append({
                        'src': js_location
                })

        # no need for logged-in resources for you
        # ...
        # Add manual added resources

        if hasattr(self.request, 'enabled_resources'):
            resources = self.get_resources()
            for resource in self.request.enabled_resources:
                if resource in resources:
                    data = resources[resource]
                    if data.js:
                        url = urlparse(data.js)
                        if url.netloc == '':
                            # Local
                            src = "%s/%s" % (self.site_url, data.js)
                        else:
                            src = "%s" % (data.js)

                        data = {
                            'src': src}
                        result.append(data)

        # Add diazo url
        origin = None
        if self.diazo_production_js:
            origin = self.diazo_production_js
        if origin:
            result.append({
                'src': '%s/%s' % (
                    self.site_url, origin)
            })

        return result


    def manifestlist(self):
        self.bundles = self.registry.collectionOfInterface(IBundleRegistry, prefix="plone.bundles", check=False)
        catalog = api.portal.get_tool(name='portal_catalog')
        manifest_base = api.portal.get_registry_record('manifest_base', interface=IBokSettings)
        manifest_on = api.portal.get_registry_record('manifest_on', interface=IBokSettings)

        if manifest_on:
            folder_path = '/'.join(self.context.getPhysicalPath())
            all_content_brains = catalog(path=folder_path, sort_on='modified', sort_order='descending')
            manifest = str(all_content_brains[0].modified)
            for brain in all_content_brains:
                manifest += "\n" + brain.getURL()
            for script in self.get_scripts():
                manifest += "\n"  + script['src']
            for style in self.styles():
                manifest += "\n"  + style['src']
            return """CACHE MANIFEST
%(manifest_base)s
#%(manifest)s


    """  % {
            'manifest': manifest,
            'manifest_base': manifest_base,
            }
        else:
            return "CACHE MANIFEST"
