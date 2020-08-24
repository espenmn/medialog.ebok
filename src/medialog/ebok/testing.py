# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.ebok


class MedialogEbokLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=medialog.ebok)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.ebok:default')


MEDIALOG_EBOK_FIXTURE = MedialogEbokLayer()


MEDIALOG_EBOK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_EBOK_FIXTURE,),
    name='MedialogEbokLayer:IntegrationTesting'
)


MEDIALOG_EBOK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_EBOK_FIXTURE,),
    name='MedialogEbokLayer:FunctionalTesting'
)


MEDIALOG_EBOK_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_EBOK_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MedialogEbokLayer:AcceptanceTesting'
)
