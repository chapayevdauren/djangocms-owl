# djangocms-owl
**djangocms-owl** is a plugin for [Djangocms](https://github.com/divio/django-cms) that implements the JavaScript carousel library [Owl Carousel](http://owlgraphic.com/owlcarousel/). Version 1 of Owl Carousel is supported.

## Dependencies
* Djangocms>=3.0
* Django>=1.6

## Installation
Install Djangocms-owl from Pypi  
```
pip install djangocms-owl
```
Add Djangocms_owl to INSTALLED_APPS  
```
INSTALLED_APPS = (
    ...
    'djangocms_owl',  
    ...
)
```

**Owl Carousel** has a dependency on JQuery [Docs](http://owlcarousel.owlgraphic.com/docs/started-installation.html) that is not currently included within this package. Add a copy will need adding to a template such as the base.html

```html
<script src="jquery.min.js"></script>
```

## Configuration
CSS classes can be added to the plugin via a select box by using the **DJANGOCMS_OWL_STYLES** settings tuple.

```python
DJANGOCMS_OWL_STYLES = (
    ('style1', 'Style 1'),
    ('style2', 'Style 2'),
)
```

djangocms_owl/default.html is rendered by default. The user can select custom templates if the following tuple is set as the example below demonstrates. 
```python
DJANGOCMS_OWL_TEMPLATES = (
    ('template1', 'Template 1'),
    ('template2', 'Template 2'),
)
```

## Todo
* Add settings to disable inclusion of CSS
* Add settings to disable inclusion of JS
* Add support for owl carousel 2
* Expand on the included Owl Carousel configuration options

