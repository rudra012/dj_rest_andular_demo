# dj_rest_andular_demo

Reference: 

http://gregblogs.com/how-the-do-i-build-a-django-django-rest-framework-angular-1-1-x-and-webpack-project/

Run your Django server using dev settings.

manage.py runserver --settings=mysite.settings.dev
  
Initialize your NPM package. From within mysite/frontend/, run
**$ npm init --yes**  

Install dev dependencies.
npm install --save-dev eslint eslint-loader  

Install general dependencies.
npm install --save eslint eslint-loader angular angular-resource angular-route json-loader mustache-loader lodash

**Create an Angular entry-point, declare initial dependencies, declare initial globals.**

create mysite/frontend/app/app.js, 
app.js is where Webpack will look for modules to bundle together. 

create mysite/frontend/config/eslint.json

**Configure Webpack.**
Now that we've laid out most of our app dependencies, we can build our Webpack config file. 
Webpack will consolidate all of our dependencies, as well as app-specific modules we build, 
into one file,a bundle.

create mysite/frontend/webpack.config.js

In order to have Webpack bundle our static dependencies together, 
we need to tell it where to look for those dependencies,
which dependencies to process and how to manage them prior to bundling.

**Tell Django to load app.**

In mysite/backend/mysite/mysite/urls.py add the following in the urlpatterns list

# Web App Entry
url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='index'),  


**Create the Angular app base template.**

create mysite/frontend/app/index.html

{% load staticfiles %}
<!DOCTYPE html>  
<html ng-app="myApp">  
  <head>
    <title>My Site</title>
    <script src="{% static 'dist/js/bundle.js' %}"></script>
  </head>
  <body>
  </body>
</html>  

