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

.. code:: python

    pip install djangocms-owl

Add Djangocms\_owl to INSTALLED\_APPS

.. code:: python

    INSTALLED_APPS = (
        ...
        'djangocms_owl',
        ...
    )

Django 1.6 and/or South users will need to add the following to ensure
migration compatibility.

.. code:: python

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

Include or exclude static files

.. code:: python

    DJANGOCMS_OWL_INCLUDE_CSS = True
    DJANGOCMS_OWL_INCLUDE_JS_OWL = True
    DJANGOCMS_OWL_INCLUDE_JS_JQUERY = True

Set the CMS module name in the available plugin list. The default is Generic.

.. code:: python

    DJANGOCMS_OWL_MODULE = _('Generic')

Templates
---------

base.html includes all the JavaScript and CSS needed to run the carousel, but it does not render the HTML.
Custom templates can extend base.html as long as they define a plugin block containing the html and plugin render code as show in the below example.

.. code:: html

    {% extends 'djangocms_owl/base.html' %}
    {% load cms_tags %}

    {% block plugin %}
      <div class="owl-carousel-plugin plugin{% if style %} {{ style }}{% endif %}" id="plugin-{{ instance.pk }}">
        <div class="row">
          <div class="small-12 columns">
            <div class="slider">
              {% for plugin in instance.child_plugin_instances %}
                <div class="item">
                  {% render_plugin plugin %}
                </div>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    {% endblock plugin %}

Todo
----

- Add support for owl carousel 2
- Expand on the included Owl Carousel configuration options
- Create abstract base models that can be overridden

Inspiration
-----------

-  `cmsplugin-filer`_

Contributions
-------------

-  Lee Solway

History
-------
**0.1.6** (2015-08-05)

- Added a JSON field override to allow for custom options
- Added support for custom CMS module names

**0.1.5** (2015-07-22)

- Static files included from bower
- Included jQuery
- Included v2 of Owl Carousel of later user
- Added settings to include/include jquery, owlcarousel.js and owl*.css files
- Re-added select_template with Django 1.8 support
- Separated the template to include a base to facilitate custom template creation - e.g. extend base.html

**0.1.4** (2015-07-17)

- render template bug fix with Django 1.8 (removed select_template)

**0.1.3** (2015-07-06)

- Critical bug fix

**0.1.2** (2015-07-06)

- Converted README.md to README.rst
- Added AppConf
- Added DJANGOCMS_CHILD_CLASSES configuration option
- Updated the initial Django migration dependency to CMS 0001 initial

**0.1.1** (2015-07-05)

- Documentation updates

**0.1.0** (2015-07-03)

- First release on PyPI


.. _django-cms: https://github.com/divio/django-cms
.. _Owl Carousel: http://owlgraphic.com/owlcarousel/
.. _Docs: http://owlcarousel.owlgraphic.com/docs/started-installation.html
.. _cmsplugin-filer: https://github.com/stefanfoulis/cmsplugin-filer
