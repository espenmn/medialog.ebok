# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from medialog.ebok.testing import MEDIALOG_EBOK_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.ebok is properly installed."""

    layer = MEDIALOG_EBOK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.ebok is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.ebok'))

    def test_browserlayer(self):
        """Test that IMedialogEbokLayer is registered."""
        from medialog.ebok.interfaces import (
            IMedialogEbokLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogEbokLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_EBOK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.ebok'])

    def test_product_uninstalled(self):
        """Test if medialog.ebok is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.ebok'))

    def test_browserlayer_removed(self):
        """Test that IMedialogEbokLayer is removed."""
        from medialog.ebok.interfaces import IMedialogEbokLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogEbokLayer, utils.registered_layers())
