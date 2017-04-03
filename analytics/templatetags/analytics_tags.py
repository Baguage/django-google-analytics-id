from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def google_analytics(google_analytics_id=None):
    """ Generate google analytics code ready for inclusing to a template """
    is_disabled = getattr(settings, "DISABLE_GOOGLE_ANALYTICS", None)
    if is_disabled:
        return ""
    # If code is an option from settings, use the value of that option
    if google_analytics_id is None:
        google_analytics_id = getattr(settings, "GOOGLE_ANALYTICS_ID")
    else:
        google_analytics_id = getattr(settings, google_analytics_id, google_analytics_id)

    # https://docs.djangoproject.com/en/1.10/ref/utils/#django.utils.safestring.mark_safe
    return mark_safe("""<script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', '%s', 'auto');
      ga('send', 'pageview');

    </script>
""" % google_analytics_id)
