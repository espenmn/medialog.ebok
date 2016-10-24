# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from medialog.ebok.testing import MEDIALOG_EBOK_INTEGRATION_TESTING  # noqa
from medialog.ebok.interfaces import IEbok

import unittest2 as unittest


class EbokIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_EBOK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Ebok')
        schema = fti.lookupSchema()
        self.assertEqual(IEbok, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Ebok')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Ebok')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IEbok.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Ebok', 'Ebok')
        self.assertTrue(
            IEbok.providedBy(self.portal['Ebok'])
        )
