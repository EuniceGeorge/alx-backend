# 0x02. i18n

This project contains tasks for learning to use Flask-babel.

## Required Modules

+ Flask-Babel
+ Flask i18n tutorial
+ pytz

## Tasks To Complete
+ [x] 0. **Basic Flask app:**<br/>. 
  + First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (`<h1>`).

+ [x] 1. **Install the Babel Flask extension:**<br/>. 
  + Install the Babel Flask extension:
```
$ pip3 install flask_babel==2.0.0
```
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
     
+ [x] 2. **Get locale from request:**<br/>. 
  + Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
    
+ [x] 3. **Parametrize templates:**<br/>. 
  + Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

+ [x] 4. **Force locale with URL parameter:**<br/>. 
  + In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.
     
+ [x] 5.**Mock logging in:**<br/>. 
  + Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.
```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

