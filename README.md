# Requests Logger
A general purpose http request logging middleware for Django

Steps to install
----------------

1. Add the requests_logger.py into any of your existing app or create a new one.
2. Add a new entry into MIDDLEWARE_CLASSES section of settings.py

How it works
------------

It captures all http requests and outputs on console. 
It dumps captured requests into a text file after each 1000 requests.


Why use it
----------

I buit this primarily because we are using waitress web server and I needed a simple solution to log http requests. 
