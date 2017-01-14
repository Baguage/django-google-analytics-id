from django.conf import settings
from django.test.testcases import TestCase
from django.test.utils import override_settings

from analytics.templatetags.analytics_tags import google_analytics


class GoogleAnalyticsTest(TestCase):
    def test_google_analytics_id(self):
        # No DISABLE_GOOGLE_ANALYTICS option defined
        self.assertFalse(hasattr(settings, "DISABLE_GOOGLE_ANALYTICS"))
        code = google_analytics("UA-123-1")
        # Make sure the code is not autoescaped
        self.assertIn("<script>", code)
        self.assertIn("UA-123-1", code)

    @override_settings(CODE="UA-123-2")
    def test_settings(self):
        # No DISABLE_GOOGLE_ANALYTICS option defined
        self.assertFalse(hasattr(settings, "DISABLE_GOOGLE_ANALYTICS"))
        code = google_analytics("CODE")
        # Make sure the code is not autoescaped
        self.assertIn("<script>", code)
        self.assertIn("UA-123-2", code)

    @override_settings(DISABLE_GOOGLE_ANALYTICS=False)
    def test_enabled_1(self):
        code = google_analytics("UA-123-1")
        # Make sure the code is not autoescaped
        self.assertIn("<script>", code)
        self.assertIn("UA-123-1", code)

    @override_settings(DISABLE_GOOGLE_ANALYTICS=False, CODE="UA-123-2")
    def test_enabled_2(self):
        code = google_analytics("CODE")
        # Make sure the code is not autoescaped
        self.assertIn("<script>", code)
        self.assertNotIn("CODE", code)
        self.assertNotIn("code", code)
        self.assertIn("UA-123-2", code)

    @override_settings(DISABLE_GOOGLE_ANALYTICS=True)
    def test_disabled_1(self):
        code = google_analytics("UA-123-1")
        self.assertEqual(code, "")

    @override_settings(DISABLE_GOOGLE_ANALYTICS=True, CODE="UA-123-2")
    def test_disabled_2(self):
        code = google_analytics("CODE")
        self.assertEqual(code, "")
