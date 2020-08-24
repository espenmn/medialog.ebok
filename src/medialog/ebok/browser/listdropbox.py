################################################################
# pp.client-plone
# (C) 2013,  ZOPYX Limited, D-72074 Tuebingen, Germany
################################################################

from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


from dropbox import dropbox
from dropbox import client
from dropbox.client import DropboxClient



class DropView(BrowserView):
    """ Dropbox view Bok.
    """
    
    app_key = ''
    app_secret = ''
    
    flow = client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    #authorize_url = flow.start()

    # Have the user sign in and authorize this token
    #authorize_url = flow.start()
    #print '1. Go to: ' + authorize_url
    #print '2. Click "Allow" (you might have to log in first)'
    #print '3. Copy the authorization code.'
    #code = raw_input("Enter the authorization code here: ").strip()

    template = ViewPageTemplateFile('book.pt')

    def __call__(self):
        import pdb; pdb.set_trace()
        metadata = DropboxClient.metadata('/bok')
        files = [content['path'].split('/')[-1] for content in metadata['contents']]
        return self.template(self.context)

InitializeClass(DropView)