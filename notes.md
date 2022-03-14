## Python Django: dev to deployment - Notes

### Setup
#### Create a virtual environment
`python3 -m venv udemy`

#### Activate a virtual environment
`source ./venv/bin/activate`

#### Install Django
`pip install django`

#### Create a Django app
`python manage.py startapp pages`




## Notes
- `templates` folder: contains html templates, per app

- statics settings:
	STATICFILES_DIRS = [os.path.join(BASE_DIR, "btre/static")]
	STATIC_ROOT = os.path.join(BASE_DIR, "static")
	STATIC_URL = '/static/'

- media settings
	MEDIA_ROOT = os.path.join(BASE_DIR, "media")
	MEDIA_URL = "/media/"

- collectstatic django command

- Remember to inlcude urls of apps in the main urls.py
	urlpatterns = [
    ...
    path("", include("pages.urls")),
    ...
    ]

- static urls
	urlpatterns = [
		...
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


- Register models in Admin pages
	admin.site.register(Listing)

- in a view:
	context = {"listings": listings}
	return render(request, "my_page.html" context)

	then we can access "listings" in template like this:
	{{ listings }}

- Match a web form to a url function:
	<form action="{% url 'login' %}" method="POST ">
	Use {% csrf_token %} in the form, for cross-site forgery

- Authentication: use `auth.authenticate` and `auth.login` functions 


### DEPLOYMENT:
- Get a remote environment (e.g. from DigitalOcean)
- Set it up (user, ssh keys, postgres, git, clone code)
- Set secrets to local_settings.py
- migrate, collectstatic: as we do in a docker-compose
- configure gunicorn and nginx

Instructions: https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71

### DB Administer
`sudo -i -u postgres`

`postgres@user:~$ psql`

`ALTER USER postgres PASSWORD '12345';`



### Credentials
Superuser: gmak/1234

User: test/testme123!

postgres password: 12345


### Known Issues
* Fix messages FE