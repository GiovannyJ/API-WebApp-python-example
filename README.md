# API-WebApp-python-example
This is an example of how you can use python frameworks to make a web app with custom API

### TLDR
The basic operation stack for building apps like this is 
* make API -> test API -> make skeleton pages -> test API with pages -> rework API -> make pages look pretty

* APIs can be made in any language so which ever your best with just use that one. 

### Files:
* custom_API.py
    - this is a custom API proof of concept that will show you how endpoints work
* connect.py
    - this is an example of how to connect to an sql database server (as of rn its connect to one of mine)
* db_handler.py
    - this is an example of how to handle the data manipulation of an API and interact with the database
* third_party_API.py
    - this is an example of how to use a third party API
* web_app.py
    - this is a sample of a web app using flask to render pages dynamically


### The order in which to start would be

#### Creating a custom API:
*  .env -> connect.py -> db.handler.py -> custom_API.py -> IF MAKING WEB APP web_app.py

#### Using a third party API:
* third_party_API.py

### Other Frameworks for web apps in different languages
* react.js:
    * framework used to create interactive and modular pages using js (or typescript (js with types for more data safety))
    * frameworks like this can make better looking pages BUT they tend to be more heavy on resources used (lots of files will be generated) and JS can be a little overwhelming
* node.js:
    * runtime for js typically used by a lot of other frameworks 

### Other resources:
* POSTMAN: API testing application

### Related links
* https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
* https://flask.palletsprojects.com/en/3.0.x/
* https://react.dev
* https://nodejs.org/en

### My Work with APIs
* https://github.com/GiovannyJ/bookup
* https://github.com/GiovannyJ/SE-project2


### Recommended Process for your project
1. Find out what type of information you need
2. format how the data will be presented (json_templates)
3. organize database
4. create API to interact with each table in the database
5. test API in CLI
6. create pages (Skeleton pages that will be populated with data)
7. connect pages to API (GUI)
8. Make data from API on pages look pretty

I typically struggle with making ascetically pleasing pages but the gist is to create the API first so that you can serve your data and then create the pages after to reflect this data (typically it would be done concurrently but sometimes time doesnt allow for that). The most important part is that you can do CRUD operations with your data, once that can be done reliably using a simple web page then you can make the page look pretty.