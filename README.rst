Google analytics for django
===========================

This an installable django application to add your Google analytics code to your website template(s).
It is compatible with Django 1.8, 1.9 and 1.10.

Installation
============

`pip install django-google-analytics-id`

add `analytics` to INSTALLED_APPS


Usage
=====

Add {% google_analytics 'UA-123-1' %} to your base template (in <HEAD> section).

You can also pass the name of an option from setting.

GOOGLE_ANALYTICS_ID = 'UA-123-1'
{% google_analytics 'GOOGLE_ANALYTICS_ID' %}

Options
=======
GOOGLE_ANALYTICS_CODES, dict

Example:
GOOGLE_ANALYTICS_CODES = {"portal": "UA-123-1", "admin": "UA-123-2"}

DISABLE_GOOGLE_ANALYTICS, bool
If true, {% google_analytics %} will return empty string. Can be used to enable google analytics in development
and/or qa environments