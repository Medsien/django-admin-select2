# django3-admin-select2

Enable select2 for Django3 admin `select` inputs.

Automatically applies to all `select`s, excluding filtered selects (e.g. `auth.User.groups`).

Tested with Python 3.6 and Django 3.1.8.

## Installation

```shell
pip install django3-admin-select2
```

Update `settings.py`:

```python
INSTALLED_APPS = [
    ...
    # must go before django.contrib.admin
    'django3_admin_select2',
    ...
]
```

## How it works

This app adds an overriding template for `admin/base_site.html`, adding the required css and js to `extrahead` and `footer` blocks respectively.

Note that Django admin's [builtin Select2](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields) only applies to `ForeignKey` and `ManyToManyField`.

## Credits

This project was forked from [mgd020/django-admin-select2](https://github.com/mgd020/django-admin-select2).
