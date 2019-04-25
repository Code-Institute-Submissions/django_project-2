# Unicorn Attractor

##### Project purpose and overview
Unicorn Attractor is a project to demonstrate my skills and understanding of a full stack web application built around Python Django and an sql/postgres backend database.  The purpose of the app is to provide a bug fixing and feature creation service for users. Users can register and sign in, then they are free to log their bugs which we will fix.  They can also suggest features which we will create depending on popularity.  Popularity is determined by upvoting a bug or feature request. Users can upvote bugs for free but to upvote a feature request we require a one time payment/purchase of the upvoting feature via Stripe.
App is live here..   [Unicorn](https://p5tracker.herokuapp.com/)

## Project

To get started the user lands on the homepage and can see all the bugs and feature requests logged.  They can use the register link to creat a free account by providing their username, password and email account details.  After that they can then sign in and begin to log bugs, log feature requests, comment on bugs/feature requests and click the thumbs up button to signify they also require a feature or a bug fix.  This upvote count will determine what we tend to most.and we promise to spend 50% of our time developing the highest upvoted feature request.  With the aid of the Stripe API users can make a one time payment enabling them to upvote feature requests.
Users can see the popularity of bugs and feature requests with the charts on the both the home page and Charts page.

## Planning

At the heart of the project is the Python Django Web Framework.  I decided to go with the latest version of Django which is version 2.2 for a few reasons, mainly because the latest versions of frameworks are evolving and improving ease of use, for example regex is no longer needed for creating dynamic url routes.  Also I follow python tutorials by Corey Schaefer who uses the latest version of python and django.

In development I used sqlite as it is baked into django and migrated to a postgres database on my live Heroku production version as Heroku makes this very easy.  
My workflow is based around the Atom editor and cmder for my command line interaction on a windows 7 machine.  I use Pipenv as my virtual environment which works very well for me.  My code is synched to github using git and everything is pushed to heroku using the heroku CLI.

For the front end I went with bootstrap 4 as it is a great framework and easy to use and provides great helper classes to cut down on CSS, ie padding and margin classses are very handy.  To represent my data with charts I decided to go with Chart JS as its quite easy to use and get working.  I decided to get my hands wet with the Django Rest framework and used that to create an API that serves the data to generate my Chart JS graphs using JQuery and Ajax. The Stripe API is integrated to enable Payments for the features upvoting functionality.

## UX Design
For the design of the app I decided to a bright blue colour scheme with other bright colours like orange, yellow and green with grey which contrast well in my opinion.  I used bootstrap 4 cards to represent the posts.  Additional css styles were add to improve the style of the UI with things like animations.  Animate CSS was also used for some animations to give a nice feel.  Its quite possible I may have been influenced by the style of a service called Monday.com as their adds constantly appear wherever I browse.  With the use of CSS variables I was able to create the core colour scheme for my UI and and also used this colour scheme in my Chart JS charts.  There is also a light sprinkling of font awesome and material icons to make things nice.  To improve things further I created a few Javascript functions to interact with certain elements, for example changing the status of badges and shortening long post titles in the list view.  All forms follow a consistant colour scheme and animation also.  All forms follow a consistant colour scheme and animation also. To make the App as responsive as possible I added media queries along with the bootstrap grid classes.  The app was tested on all screen sizes. Here is a wireframe I created to show general layout..
[Wireframe](https://wireframe.cc/zqvdjD)

## Schema / Project Structure
The django convention is to comprise a project of various apps each taking care of a unique part of a project.

Unicorn uses four apps..

* Users
* Tracker (Ticket system)
* Products
* Cart

Tracker is the heart of the application and contains the tickets which I have represented as posts.  Posts can be either bugs or features.  Post has a many to many relationship with users to enable the user > upvotes a post functionality.  The tracker model also has a comment class for creating comments on posts.

Users have a profile class which contains extra information about the user like their stripe key.  A signal is used to automatically create a user profile when a user is created.

Products contains the product table used to create the current single product which is upvoting.  For the moment this can be created in the django admin section by the superuser when the application is initialised.  Just go to root/admin and login.

Cart contains the tables order, orderItem and tramsaction

## Charts & API
The dependencies Django Rest Framework and Chart JS are required for Charts data and integration.  Both services provide very clear documenation to get up and running.  My API is set up to pull the data needed from the posts database to generate the Charts in Chart JS with the aid of Ajax and JQuery.  Currently the API is connected to the bugs and features charts, features and bug fixes progress data not yet connected.
[Django Rest Framework](https://www.django-rest-framework.org)
[Chart JS](https://www.chartjs.org/)

## Stripe API
Go to the stripe homepage and gegister for an account to get your own API keys, they also provide great documenation...[Stripe](https://stripe.com/docs/api)


### Dependencies

* Python 3.6 and above
* Django version 2.2
* HTML5
* Javascript
* Bootstrap 4
* JQuery
* Chart JS
* Django Rest Framework
* Stripe
* Pillow
* Animate CSS
* Font awesome
* Material Icons

### Installing

See below link for instructions installing and using pipenv

[Pipenv](https://pipenv.readthedocs.io/en/latest/basics/#example-pipfile-pipfile-lock)

* Install Python 3.6 on your machine
* Create Pipenv environment
* Download this repository to your local machine
* Make database migrations
* Create superuser

### Executing program

* Go to root of project in your virtual environment and open command line at this location
* then run the command..

*pipenv run python manage.py runserver*


### Testing
Minimal python unittests were ran for this project as most of the testing was done manually on a daily basis but its something I endeavour to improve on in future.  I created a few tests in tracker/tests.py.  To run them open your pipenv virtual environment and run the command *pipenv run python manage.py test*

For the front end this app was tested on many different screen sizes like laptops, tablets smartphones and is very responsive.

### Deployment
App is deployed to Heroku using git and github.
Currently having problems running with DEBUG set to False so DEBUG is set to True.

## Authors

Alan Smith  

[LinkedIn](https://www.linkedin.com/in/alanhbv/)

## Version History

* 0.1
    * Initial Release

## License

Public Licence

## Acknowledgments

Inspiration, code snippets, etc.
* [CoreyMSchafer](https://github.com/CoreyMSchafer)
* [Brad Traversy](https://www.traversymedia.com)
* [NetNinja](https://www.thenetninja.co.uk/)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [progrAmmar](https://jsfiddle.net/3bu8fxnp/9/)
* [JoinCFE](https://www.codingforentrepreneurs.com/)
* [Gerardo Valencia](https://codepen.io/grardovr/pen/rJQWLN)
