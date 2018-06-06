# DishQ

Hi!

This is a demo project where I used Zomato APIs to get data of top 20 restaurants in Bengaluru.

You may need to install django on to your system before running the project. I followed https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04 to set up Django in my system.

After successfully cloning the project you just need to replace Google API key and Zomato API Key in the project with your own. The Google API can be found at the location foodie>templates in the index.html file and Zomato API can be found at urls.py in foodie folder file.  

After installing django and cloning the project, you need to do migrations using following commands in the terminal:

`python manage.py makemigrations`

`python manage.py migrate`

After successfull migrations, you may start server:

`python manage.py runserver`
