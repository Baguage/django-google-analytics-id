Google analytics for django
===========================

This an installable django application to add your Google analytics code to your website template(s).
It is compatible with Django 1.8, 1.9 and 1.10.

Python 2.7 and python 3.5 are supported.

Installation
============

`pip install django-google-analytics-id`

add `analytics` to INSTALLED_APPS


Usage
=====

Load template tag {% load analytics_tags %}

Add {% google_analytics 'UA-123-1' %} to your base template (in <HEAD> section).

You can also pass the name of an option from setting.

GOOGLE_ANALYTICS_ID = 'UA-123-1'
{% google_analytics 'GOOGLE_ANALYTICS_ID' %}

Options
=======
DISABLE_GOOGLE_ANALYTICS, bool
If true, {% google_analytics %} will return empty string. Can be used to enable google analytics in development
and/or qa environments

Bugs and requests
=================

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/Baguage/django-google-analytics-id/issues
