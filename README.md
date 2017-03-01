# Django Commands Practice

### Virtual Environments

* Try to consolidate all your virtual environments into one directory

***Create Virual Environments***

* Some tutorials use the below command, wasn't able to call `manage.py` with my python 3 alias when I did this
	* `virtualenv env_name`
* This will use python 3
	* `python3 -m venv env_name`

***Start and Stop Virtual Environments***

* Starting
	* `source myvenv/bin/activate` OR `. myvenv/bin/activate`

***PIP Commands***

* After starting your virtual environment, you will have to install the dependencies you want to use in that environment.
* `pip freeze` - To see what is currently installed in the virtual environment
* Below is the example of installing django 1.8. If you leave it blank it will install the latest version(django 1.8.7)

```
(myvenv) ~$ pip install django==1.8
```

***Start Project***

* In the directory you want to hold your new django app run this command
	* `django-admin startproject project_name`

***Start Server***

* The default port is 8000
* The below code will start your server

```
python3 manage.py runserver
```

***Run Migrations / SuperUser***

* Django 1.8 allows us the migrate command to start database. 
* The default database is sqlite3

```
python3 manage.py migrate
```
* You can also run the migration and at the same time create a superuser for the admin console

```
python3 manage.py syncdb
```
* localhost 8000/admin will now have a log in page
* once logged in you will have fun CRUD access to the database

***New Apps***

* Projects can have multiple apps. Apps are used to do specific tasks
* The best apps do one thing, and one thing very well
* To start an app run in terminal

```
python3 manage.py startapp app_name
```



# Trying Django Stuff

[coding for entreprenuers Try Django](https://www.youtube.com/watch?v=yfgsklK_yFo)
[Github Code](https://github.com/codingforentrepreneurs/try-django-19)
[Github Setup Guides Repo](https://github.com/codingforentrepreneurs/Guides)

##### Try Django 1.9 Part 1

* Introduction shit, nothing learned

##### Try Django 1.9 Part 2

* Overview of CRUD app and admin panel

##### Try Django 1.9 Part 3

* Talks about youtube videos and repos with all the code and guides

##### Try Django 1.9 Part 4

* Use pip3 to install virtual environment / upgrade it
	* `pip3 install virtualenv`
	* `pip3 install virtualenv --upgrade`
* Create a virtual environment in the folder you are in
	* `virtualenv .`
* Starting your virtual environment
	* Mac = `source bin/activate`
	* Windows = `.\Scripts\activate`
* Your virtual environment name should appear inside parenthesis that is in front of your directory route in bash

```
(mydjangoapp)$
```
* Find out what packages are installed either on your computer, or current virtual environment
	* `pip3 freeze`
* Install django version 1.9
	* `pip3 install django==1.9`
* To uninstall a package or upgrade a package using pip
	* `pip3 uninstall django`
	* `pip3 install django --upgrade`
* Create a django project
	* `django-admin.py startproject trydjango19`
* cd into your project folder and run the server using manage.py
	* `python3 manage.py runserver`
	* change port = `python3 manage.py runserver 8888` 

##### Try Django 1.9 Part 5

* Right now we have a venv called trydjango, along with a folder inside there called trydjango, and another trydjango folder in that. 
	* Inside your virtual environment folder, in the same directory where `bin`, `include`, and `lib` live, change the trydjango folder name to `src`
* We have to make sure our database and django are connected the right way. 
* Run your migrations
	* `python3 manage.py migrate`
* Create a superuser
	* `python3 manage.py createsuperuser`
	* enter username
	* no need for email
	* Django 1.9 has some password validation now
* How come there is a db.sqlite3 file in the project? Where did it come from?
* Django made a sqlite3 database for us
* Open `settings.py` and look around
	* `database section`: Sqlite3 database was created by default from Django
	* `Installed Apps section`: shows us some default installed apps
		* `django.contrib.admin` - allows us to user the superuser admin page
		* `django.contrib.auth` - authentication for users 
		* `django.conf.urls` - we can use this with the `urls.py` folder
* Visit the admin page and log in with the superuser you just created
	* `python3 manage.py runserver`
	* visit `127.0.0.1:8000/admin`
	* log in and play around

##### Try Django 1.9 Part 6

* apps vs projects
	* apps are little components that build up to the project as a whole
* Create a app (part of the project)
	* `python3 manage.py startapp posts`
	* posts is the name of the app, it can be anything\
	* now a posts folder was created
* `models.py `
	* Models for MVC, how you are associating what you want with your DB
* Create a model class for use

```
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length =120)
	content = models.TextField()
	# updated will auto update 
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	# Timestamp will save and set one time
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	
	def __str__(self):
		return self.title
```
* To connect this to your project go to the `settings.py` file and add `posts` to the bottom of `Installed Apps`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]
```
* We have to make our database in sync with the project
	* `python3 manage.py makemigrations` - tells django we made changes to our models
	* `python3 manage.py migrate` - tells django to apply those changes to our database

##### Try Django 1.9 Part 7

* [Django Docs to see different Fields we can use in Models](https://docs.djangoproject.com/en/1.9/ref/models/fields/)
* Import the model from last section into admin
* Inside your `admin.py`
	* `from posts.models import Post`
	* from what model import name_of_class
	* `from .models import Post` will look at all models
	
```
from django.contrib import admin

from posts.models import Post

admin.site.register(Post)
```
* Now if you log into admin `Posts` will appear as another section

##### Try Django 1.9 Part 8

* Learn to customize the admin page
* We created a class that will represent models for posts on the admin page
* We then connect that new model to the Post model
* The other characteristics were a few of the options from the [Models documentation](https://docs.djangoproject.com/en/1.9/ref/models/fields/)

```
	from django.contrib import admin

	# Register your models here.
	from posts.models import Post

	# check out docs for Models options
	# https://docs.djangoproject.com/en/1.9/ref/models/fields/

	# create a class that will be a model for Posts in the Admin page
	class PostModelAdmin(admin.ModelAdmin):
	
		# displays other factors of the model
		list_display = ["title", "updated", "timestamp"]
		# choose which items are clickable/links
		list_display_links = ["updated"]
		# choose what parts of the list the user can edit by clicking
		list_editable = ["title"]
		# gives a default filtering box on the side
		list_filter = ["updated", "timestamp"]
		# allow us to search for specific things
		search_fields = ["title", "content"]
		
		# Connects this class to the Post model
		class Meta:
			model = Post

	# added the PostModelAdmin to the admin.site.register
	admin.site.register(Post, PostModelAdmin)
```

##### Try Django 1.9 Part 9

* CRUD
	* Create, Read, Update, Delete
	* Make new, Get, Edit, Delete
	* POST, GET, PUT/PATCH, DELETE
* `views` allow us to run all these methods 

##### Try Django 1.9 Part 10

* class based views are not talked about in this project. Do your own research after doing function based views
* function based views
* `views.py`

```
from django.http import HttpResponse
from django.shortcuts import render

def posts_home(request):

	return HttpResponse("<h1>HELLO WORLD</h1>")
```

##### Try Django 1.9 Part 11

* Request Response Cycle
* Your view will handle a request, and return a response
* urlpatterns MAP the requests to where it needs to go

##### Try Django 1.9 Part 12

* We are going to connect the view method you made two sections ago
* `urls.py`

```
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # this is a direct path
    url(r'^posts/$', "posts.views.post_home"),
]
```
* Django urls use Regex
* This example is a direct path
* We target the `app` -> `filename` -> `function name`
* You can also import the views

```
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # You can also import views
    url(r'^posts/$', views.post_home),
]
```
* This gets tricky if you have more apps with views to bring in
* Build Regex Lesson

##### Try Django 1.9 Part 13 - Build urls.py for your apps

* We want to make our urls cleaner and more organized. You can do this my having each app get their own urls file
* Create a `urls.py` file in the `posts` app
* Django looks for the first url to match the pattern
	* urlpatterns read top to bottom and left to right

```
from django.conf.urls import url
from django.contrib import admin

	# import your post from views
from . import views

urlpatterns = [
	url(r'^$', "posts.views.post_list"),
	url(r'^create/$', "posts.views.post_create"),
	url(r'^detail/$', "posts.views.post_detail"),
	url(r'^update/$', "posts.views.post_update"),
	url(r'^delete/$', "posts.views.post_delete"),
]
```
* Update your views for CRUD

```
from django.http import HttpResponse
from django.shortcuts import render

	# Create your views here.

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	return HttpResponse("<h1>Detail</h1>")

def post_list(request):
	return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
```
* Update your admin urls.py
* `include module` will allow us to include all the paths in the posts file
* Instead of using a direct view path we can use `include("posts.urls")`

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # making the post app have it's own file
    url(r'^posts/', include("posts.urls")),
]
```
* run your server and visit the `posts paths`
	* 127.0.0.1:8000/posts
	* 127.0.0.1:8000/posts/create
	* 127.0.0.1:8000/posts/update

##### Try Django 1.9 Part 14

* Start to make your view functions target their specific templates
* `settings.py -- BASE_DIR`
	* base directory where manage.py is
	* os is a python module that will solve the path issues between operating systems
	* In `DATABASES` we see `os.path.join(BASE_DIR, database) - Example of how we do not have a hardcoded filepath 
* Setting up templates
	* Go to `settings.py`
	* Scroll to `TEMPLATES`
	* Change the `DIRS` to have the base dir and templates
		* `'DIRS': [os.path.join(BASE_DIR, 'templates')],`
* Make a `templates` folder in `src`
* Create an `index.html` file in the templates file. Put something in it
* Render that index.html file when a user visits `127.0.0.1:8000/posts`
* `views.py`

```
def post_list(request):
	return render(request, "index.html",{})
```
* This still works
* The tutorial says to change the way we import and call our views in our url patterns
* `urls.py --posts`

```
from django.conf.urls import url
from django.contrib import admin
	# from posts import views

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list),
	url(r'^create/$', post_create),
	url(r'^detail/$', post_detail),
	url(r'^update/$', post_update),
	url(r'^delete/$', post_delete),
]
```
* For more practice change the name of the file in the views function to something that does not exist. Then visit the page and see the information Django gives you

##### Try Django 1.9 Part 15

* More on rendering templates in the views
* Earlier we had an empty dictionary as the last render argument. 

```
def post_list(request):
	return render(request, "index.html",{})
```
* This is because we had nothing to pass into the template.
* For more dynamic information we can pass in dictionaries

```
def post_detail(request):
	context = {
		"title": "POST_DETAIL"
	}
	return render(request, "index.html", context)

def post_list(request):
	context = {
		"title": "POST_LIST"
	}
	return render(request, "index.html", context)
```
* In the html file we use double curly brackets `{{}}` for templating.
* We will target the key to populate the value

```
<body>
	<h1>WELCOME TO THE {{ title }} VIEW</h1>
</body>
```
* Now our views.py will be more dynamic because we can utilize one template for similar purposes
* Add some user authentication and control flow to the view

```
def post_list(request):
	if request.user.is_authenticated():
		context = {
			"title": "MY USER LIST"
		}
	else:	
		context = {
			"title": "GENERAL POST LIST"
		}
	return render(request, "index.html", context)
```
* We like the first way better. Will start using query sets

##### Try Django 1.9 Part 16

* Query Sets - Querying the DB for data
* Open up your python shell related to Django
	* `python3 manage.py shell`
	* Allows us to tpye python code and work with our django project, including the DB
* Inside your Django Python Shell
* Import your models to use them
	* `>>> from posts.models import Post`
* Make a all query
	* `>>> Post.objects.all()`
* Make a filter query
	* `>>> Post.objects.filter(title="abc")`
	* `>>> Post.objects.filter(title__icontains="abc")`
* Create a new post
	* `>>> Post.objects.create(title="New Post", content="New Content")`
	* These are real time and actual instances of the class that have been entered into the Database. If we query the DB again you will see your new posts
	* `>>> Post.objects.all()`
* Assign your query set to a variable and loop through them.

```
queryset = Post.objects.all()

for obj in queryset:
	print(obj.title)
	print(obj.id)
	print(obj.pk)
```
* `id` = the unique identifier
* `pk` = the primary key
* Exit the shell and work in sublime
* import your models to the views so we can make a queryset

```
from .models import Post

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "POST LIST",
	}
	return render(request, "index.html", context)
```
* Now use templating in the html file
	* `{{}}` - used to present content onto the page
	* `{%%}` - used to create logic onto the page

```
	<h1>WELCOME TO THE {{ title }} VIEW</h1>

	{% for obj in object_list %}
	<ul>
		<li>{{obj.id}}</li>
		<li>{{obj.title}}</li>
		<li>{{obj.content}}</li>
		<li>{{obj.timestamp}}</li>
		<li>{{obj.updated}}</li>
	</ul>
	{% endfor %}
```

##### Try Django 1.9 Part 17

* In your `views.py` import `get_object_or_404` from shortcuts
	* `from django.shortcuts import render, get_object_or_404`
	* this will target a specific object
* `views.py` connect get/404 object
* use it in the post_details view function

```
from django.shortcuts import render, get_object_or_404

def post_detail(request):
	instance = get_object_or_404(Post, id=3)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)
```
* `post_detail.html` - Make a new html file in templates
* In the template create a list to house all the information from the instance

```
	<h1>{{ title }}</h1>

	<ul>
		<li>{{instance.id}}</li>
		<li>{{instance.title}}</li>
		<li>{{instance.content}}</li>
		<li>{{instance.timestamp}}</li>
		<li>{{instance.updated}}</li>
	</ul>
```

##### Try Django 1.9 Part 18

* Making your urlpatterns accept parameters to pass to the views
* `urls.py` change the detail view
	* `url(r'^detail/(?P<id>\d+)/$', post_detail),`
	* `(?P<id>\d+)/`
		* take a new parameter, with the name id, and will only accept digits
* This will pass a `keyword argument` to the views
	* In the above case it will pass to the post detail id
	* `def post_detail(request, id=None):`
	* We leave this to `NONE` because it is a keyword argument, not a standard parameter
* `views.py` alter the post detail function

```
def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)
```
* Now visit the post detail urls but follow with an id number
	* 127.0.0.1:8000/posts/detail/1
	* 127.0.0.1:8000/posts/detail/2
	* 127.0.0.1:8000/posts/detail/3
* remove `detail` from the urlpattern to make the url look nicer
	* `urls.py` = `url(r'^(?P<id>\d+)/$', post_detail),`
* Now visit the urls
	* 127.0.0.1:8000/posts/1
	* 127.0.0.1:8000/posts/2
	
***CFE Github has Guides called [Common Django URL REGEX Patterns](https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md)***
	
##### Try Django 1.9 Part 19

* Make the `titles in index.html` clickable

```
	<h1>WELCOME TO THE {{ title }} VIEW</h1>

	{% for obj in object_list %}
	<ul>
		<li>{{obj.id}}</li>
		<li><a href="/posts/{{obj.id}}">{{obj.title}}</a></li>
```
* Now the title can be clicked, and will lead to the detail viewed with the objects id number
* This is dumb, we'll make our URLS more organized and dynamic with names and namespaces
* `urls.py` add the name detail to the detail url pattern
	* `url(r'^(?P<id>\d+)/$', post_detail, name='detail'),`
	* this makes our urls more dynamic so we don't have to hard code them into our templates
* `urls.py` in the src file add a namespace
	* `url(r'^posts/', include("posts.urls", namespace='posts')),`
	* this allows us to know which urls we are targeting. 
	* Say we had multiple applications with a `detail` url. Adding a namespace to the app will let django know which url.py file to look for
	* this is only applied when we have a set of urls
* `models.py` add a function to get the absolute url
* import reverse 
	* `from django.core.urlresolvers import reverse`
	* Reverse will allow us to use something similar to the `url()` but do this inside of the model
* `models.py` Build method to pass in kwargs id

```
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id" = self.id})
```
* `index.html`: change the link to target the model get absolute url
	* `<li><a href="{{ obj.get_absolute_url }}">{{obj.title}}</a></li>`

##### Try Django 1.9 Part 20 - Model Forms

* Model Forms - build a form on a web page and it will save that data into the DB for us
* Create a `forms.py` file inside the posts project
* Import django forms and import your Post model
	* `from django import forms`
	* `from .models import Post`
* Create a class for Post form that will like to the Post Model
* We target what fields we want from the Post to show the user in the form

```
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]
```
* `views.py` import your newly made PostForm class
	* `from .forms import PostForm`
* Initialize the PostForm object in the create function.
* Save a `context` variable
* Return a render function that targets a new html file

```
from .forms import PostForm

def post_create(request):
	form = PostForm()
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
```
* Create a `post_form.html`

```
	<h1>FORMMMMM</h1>


	<form method="POST" action="">{%csrf_token%}

		{{ form.as_p }}

		<input type="submit" value="Create Post"/>
	</form>
```
* method = What type of HTTP Verb / CRUD we are performing
	* The default method for a form is `GET`
	* In this example we want to use `POST` to create the data
* Action = What url will this form be hitting
* csrf = cross site request forgery. We need security to validate data
* Django provides csrf token by default
	* `{%csrf_token%}`
* We have validation but still have to put the data into the DB
* We might do something similar to earlier such as

```
def post_create(request):
	form = PostForm()
	if request.method == "POST":
		title = request.Post.get("title")
		Post.objects.create(title=title)
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
```
* We will use `Django Forms` instead to validate against our own Models

```
def post_create(request):
	form = PostForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
```
* This will make sure the "title" and "content" containers are filled out
* Now lets save that post instance to the database

```
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
```

##### Try Django 1.9 Part 21

* Working to give user Edit Access
* The `post_update view` will look very similar to the `detail_view` combined with the `create_view`

```
def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)
```
* We will be creating an instance 
* We will be creating a form
	* The form will take in the request POST method or None
	* It will also take in another keyword argument to populate the form
		* `instance = instance` 
* Validate the form
* Create the context that will be passed to the template
* Change the url now
* `url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),`
	* Target an id that has to be a digit
	* /edit/ will lead to the update function
	* name is for organized urls
* Add a redirect functionality to create and update to exit the form
* Import `HttpResponseRedirect` in the views 
* Use it to target the Post Model Function get absolute url
	* `return HttpResponseRedirect(instance.get_absolute_url())`
	* Put this inside the form validation conditional
	
##### Try Django 1.9 Part 22 - Alert that Create or Update were Successful

* import messages in `views.py`
	* `from django.contrib import messages`
* Now use the `messages module success method`

```
def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "NOT Successfully SAVED")
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)
```
* We will also have to include an if condition in the `post_detail` template so the message can appear

```
{% if messages %}
	<ul class="messages">
		{% for message in messages %}
			<li {% if message.tags %} class="{{message.tags}}"{%endif%}>{{ message }}</li>
		{% endfor %}
	</ul>
{% endif %}
```

##### Try Django 1.9 Part 23 - Delete a Post

* Edit your `post_delete view function`

```
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect 
from .forms import PostForm
from .models import Post

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Successfully DELETED!")
	return redirect("posts:list")
```
* Import `redirect` from django.shortcuts
* target and delete the instance
* Create a message success. This isn't used because it is not in our template
* Return a reidrector to the posts:list url
* Change `posts:list in urls.py`
* Change `delete in urls.py` to take an id

```
urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^(?P<id>\d+)/delete/$', post_delete),
```

##### Try Django 1.9 Part 24 - Template Inheritance

* Create a new template called `base.html` inside templates
* This will be the `parent template` of other templates. 
	* You can have multiple parent templates
* We're going to work with the base so `delete the index.html file`
* Replace where you had `index.html` to be `base.html` in your views
* Inside the base.html we will have the index.html content wrapped in a container div and code block

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

	<div class='container'>
		{% block content %}

			<h1>WELCOME TO THE {{ title }} VIEW</h1>

			{% for obj in object_list %}
			<ul>
				<li>{{obj.id}}</li>
				<li><a href="{{ obj.get_absolute_url }}">{{obj.title}}</a></li>
				<li>{{obj.content}}</li>
				<li>{{obj.timestamp}}</li>
				<li>{{obj.updated}}</li>
			</ul>
			{% endfor %}

		{% endblock content%}

	</div>
</body>
</html>
```
* Open `post form html` and get rid of all the html boilerplate that is not the content
* Input the `extends` block on the first line

```
{% extends "base.html" %}

	{% block content %}
	<h1>FORMMMMM</h1>

	<form method="POST" action="">{%csrf_token%}

		{{ form.as_p }}

		<input type="submit" value="Create Post"/>
	</form>
	
	{% endblock content %}
```
* `{% extends "base.html" %}` - Recognize the base.html as the parent and replace anything inside the code block with the following code
* If you wanted the parent content to still appear you could throw in `{{ block.super }}` in between the extends and block content
* Add messages to the base and remove them from the other templates

```
{% if messages %}
	<div class="messages">

	<ul class="messages">
	    {% for message in messages %}
	    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{% if "html_safe" in message.tags %}{{ message|safe }}{% else %}{{ message }}{% endif %}</li>
	    {% endfor %}
	</ul>

	</div>
{% endif %}
```
* Edit title of base to make it more dynamic. Include the instance title in the browser tab
* `base.html` == `<title>{% block head_title %}TRY DJ 1.9{% endblock head_title%}</title>`
* `post_detail.html` == `{% block head_title %}{{instance.title}} | {{ block.super}}{% endblock head_title%}`
* Create a `post_list.html` template to clean our your base
	* Change the html inside the views.py
	* Remove the content from the base.html and put them in post_list.html
* Make a messages_display.html
	* copy and past the message content from base.html to the messages_display.html
* Use include syntax to run the messages_display.html content
	* `{% include "messages_display.html" %}`

##### Try Django 1.9 Part 25 - Setting Up Static Files

* `settings.py` - at the bottom you will see a link to the Django docs. Follow it
* Place the below code inside

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # "/var/www/static",
]
```
* `urls.py - tryDjango` - Let our static files be seen in development

```
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
``` 
* At the end of the `urls.py` file put an if statement to check for DEBUG
* Do not run DEBUG on true during production

```
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
* Inside terminal run `python3 manage.py collectstatic`
	* This should throw you an error right now
	* collectstatic is acting as if we had a server with all our static files in one place
* Add the path for django to search for the static files inside `settings.py`

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # "/var/www/static",
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
```
* `os.path.dirname(BASE_DIR)` will target the directory name of the base dir path and search for a folder called static cdn
* Make a folder called `static_cdn` inside our virtual environment (same folder as bin and lib)
* Make a folder called `static` inside the `src` folder. This is because of the `STATICFILES_DIRS` line
* Run the command `python3 manage.py collectstatic`
* FINALLY!!!
* Make a css folder and a `base.css` file inside of the static folder in src
* If you run the collect static command you will be sending your edits to the virtual environment static folder 
* Link the `base.css` file to the `base.html` file
* Add a `MEDIA_ROOT` by copying the `STATIC_ROOT` and create a `media_cdn` folder in the virtual environment

```
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
```
* Dynamic loading static files
* `inside base.html`

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" href="{% static "css/base.css" %}">
	<meta charset="UTF-8">
	<title>{% block head_title %}TRY DJ 1.9{% endblock head_title%}</title>
</head>
<body>

	{% include "messages_display.html" %}

	<div class='container'>
		{% block content %}

		{% endblock content%}
	</div>

<img src="{% static "img/marvel.jpg" %}" alt="">

</body>
</html>
```
* load static files on the top
* link static base.css file
* The last line is an example of how you could use this with images as well


##### Try Django 1.9 Part 26 - Implement Bootstrap

##### Try Django 1.9 Part 27

##### Try Django 1.9 Part 28

##### Try Django 1.9 Part 29

##### Try Django 1.9 Part 30

##### Try Django 1.9 Part 27

##### Try Django 1.9 Part 27










