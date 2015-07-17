djangocms-owl
=============

**djangocms-owl** is a reuseable plugin for `django-cms`_ that
implements the JavaScript carousel library `Owl Carousel`_. Version 1 of
Owl Carousel is supported.

Dependencies
------------

-  Djangocms>=3.0
-  Django>=1.6

Installation
------------

Install Djangocms-owl from Pypi.

::

    pip install djangocms-owl

Add Djangocms\_owl to INSTALLED\_APPS

::

    INSTALLED_APPS = (
        ...
        'djangocms_owl',
        ...
    )

Django 1.6 and/or South users will need to add the following to ensure
migration compatibility.

::

    SOUTH_MIGRATION_MODULES = {
        ...
        'djangocms_owl': 'djangocms_owl.south_migrations',
        ...
    }

**Owl Carousel** has a dependency on JQuery `Docs`_ that is not
currently included within this package. Add a copy will need adding to a
template such as the base.html.

.. code:: html

    <script src="jquery.min.js"></script>

Configuration
-------------

CSS classes can be added to the plugin via a select box by using the
**DJANGOCMS\_OWL\_STYLES** settings tuple.

.. code:: python

    DJANGOCMS_OWL_STYLES = (
        ('style1', 'Style 1'),
        ('style2', 'Style 2'),
    )

djangocms\_owl/default.html is rendered by default. The user can select
custom templates if the following tuple is set as the example below
demonstrates.

.. code:: python

    DJANGOCMS_OWL_TEMPLATES = (
        ('template1', 'Template 1'),
        ('template2', 'Template 2'),
    )


Restrict the plugins available to Owl Carousel

.. code:: python

    DJANGOCMS_OWL_CHILD_CLASSES = (
        'PicturePlugin',
    )


Todo
----

-  Add settings to disable inclusion of CSS
-  Add settings to disable inclusion of JS
-  Add support for owl carousel 2
-  Expand on the included Owl Carousel configuration options

Inspiration
-----------

-  `cmsplugin-filer`_

Contributions
-------------

-  Lee Solway

History
-------
**Django 1.8 render template bug fix. 0.1.4** (2015-07-17)

**Bug Fix. 0.1.3** (2015-07-06)

**0.1.2** (2015-07-06)

- Converted README.md to README.rst
- Added AppConf
- Added DJANGOCMS_CHILD_CLASSES configuration option
- Updated the initial Django migration dependency to CMS 0001 initial

**Documentation updates. 0.1.1** (2015-07-05)

**First release on PyPI. 0.1.0** (2015-07-03)

.. _django-cms: https://github.com/divio/django-cms
.. _Owl Carousel: http://owlgraphic.com/owlcarousel/
.. _Docs: http://owlcarousel.owlgraphic.com/docs/started-installation.html
.. _cmsplugin-filer: https://github.com/stefanfoulis/cmsplugin-filer
