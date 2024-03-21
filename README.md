# Coder Academy T2A2 Assessment
 API Webserver
## Links
* [GitHub](https://github.com/jquizo/T2A2-Assessment)
* [Trello](https://trello.com/b/qKQo7VGH/t2a2-web-api-assessment)

* [R5 - Endpoints](#r5)
* [R6 - ERD](#r6)
* [R7 - Third party services](#r7)
* [R8 - Models + relationships](#r8)
* [References](#references)
## R1 – Identification of the problem
The app aims to provide users with an easy-to-use note taking app, for jotting down personal notes and thoughts that may come to mind. Sometimes it is easier to have a browser tab open you can switch to, instead of using your phone/tablet to jot down notes, thoughts or other content. Notes input into this app has a date of creation attached to it, and users can add an added category (any string) to the note. The category tag is optional, and will be marked as uncategorized if this is left out.
## R2 - Why is it a problem that needs solving?
In some circumstances, it may be easier to just switch to a new browser tab, or keep the app open in another tab instead of using your phone/tablet to jot down notes. It makes it easier to jot down notes/thoughts as they come, and provides a simple solution to document and organise notes and may make a user’s workflow faster.
## R3 - Why have you chosen this database system. What are the drawbacks compared to others?
I have chosen PostgreSQL as the database system for this app, as it is a relational database system and is very useful for storing structured and organized data between entities, as in the case with this app, the relationships between users, notes and categories. 
While PostgreSQL has many advantages, compared to a NoSQL database system like MongoDB, it has less flexibility. MongoDB is more flexible in its data structures as you can quickly change requirements, schemas and is has more advantages for apps that have frequent requirement changes. Being able to store JSON is also more advantageous for apps where the data structure/schema has not yet been defined, as relational databases usually require planning the data tables, schemas and models.
I have chosen PostgreSQL as it supports SQL, and SQL is a query language we have been learning in term 2 in Coder Academy and thus am more familiar with. As the schema and data tables for this app has already been determined, and PostgreSQL has better data integrity, PostgreSQL was the more suitable choice.
## R4 - Identify and discuss the key functionalities and benefits of an ORM
An ORM (Object-relational mapping) is a tool for helping developers work with databases using object-oriented programming concepts, rather than using SQL statements. It maps object-oriented languages to relational database structures. Benefits of an ORM include  (OpenAI, 2022 GPT-3.5)
1.	Simplifies interaction with databases – ORM’s allow developers to interact with the database using object-oriented programming concepts, such as classes and objects. This can improve workflow and productivity.
2.	Reduces repetitive code – ORM’s generate SQL statements, which saves developers from writing repetitive SQL statements for database operations
3.	Improves relationship management – ORM’s simplifies the management of relationships between tables in a database, for example using foreign keys to link different tables.
4.	Improves security – ORM’s improve security by sanitizing input data, which can prevent cyber-attacks such as SQL injections, which are malicious user inputs that can allow users to perform unauthorized actions such as modifying tables.
## <a id="r5"></a> R5 - Document all endpoints for your API
## `/`

**Description** – Serves as the home page of the app. If the user is logged in, allows them to view and add notes
### HTTP Methods
- **GET**: Renders the home template created with HTML and Jinja
- **POST**: Processes the submitted note data and adds it to the database.
### Request Body (if request == POST)
- `note (string)`: The note the user wants to add. Limited to 5,000 characters
- `category (string, optional)`: Optional. This is the category of the note, limited to 255 characters. If left blank, will be labelled as uncategorized
### Returns
- If the note is successfully added to the database, the user is redirected to the home page with a success flash message.
- If the note is too short, an error flash message is displayed.
- If the category is provided and added to the note, it is displayed alongside the note.

## `/login`

**Description** – For handling user authentication by validating email and password against the database. If email and password are valid (password is checked with the hash stored in database) then the user is logged in and then redirected to the homepage, if not then error messages are shown using flask message flashing.  

### HTTP Methods
- **GET**: Renders the login template created using HTML + jinja
- **POST**: Processes the login form data and attempts to authenticate the user.
### Request Body (POST Method)
- `email` (string): The email address of the user.
•	Email must be greater than 1 character
- `password` (string): The password of the user.
•	Minimum 5 characters – no restrictions on alphabetical/numerical characters
### Returns
- If the authentication is successful, the user is redirected to the home page with a success flash message.
- If the email does not exist in the database, an error flash message is shown that indicates that the email does not exist.
- If the password entered does not match the hashed password stored in the database, an error flash message is displayed indicating an incorrect password.

## `/logout`

**Description** – Logs out the logged in user and redirects to the login page

### HTTP Methods
- **GET**: Logs out the current user and redirects to the login page
Returns
Redirects user to this route @auth.route(‘/login’)

### `/register`
**Description** – For handling user registration. Creates new user accounts using a valid email address, first name and a password. Validates input data, otherwise a flash error message will be shown. Existing email addresses are also checked against the database to ensure no duplicate registrations on the same email. Once registration is successful, the user is logged in and redirected to the home page.

### HTTP Methods
- GET: Renders the registration page created using HTML + Jinja
- POST: Processes the registration form data and creates an account.
### Request Body (POST Method)
- `email` (string): The email address of the user.
•	Email must be greater than 1 character
- `firstName` (string): The first name of the user.
•	Name must be greater than 1 character
- `password1` (string): The password entered by the user.
•	Minimum 5 characters – no restrictions on alphabetical/numerical characters
- `password2` (string): Confirms of the password entered by the user.
### Returns
- If the registration is successful, the user is redirected to the home page with a success flash message.
- If the email address is already registered, an error flash message is displayed.
-If an input data is invalid, an error message with the appropriate error message is shown.
- If any of the input data is invalid or does not meet the specified requirements, corresponding error flash messages are displayed.

### `/delete-note`

**Description** - Deletes a note from the database. This is done using a function in the index.js file in the static folder.
### HTTP Methods
- POST: If the user attached to the note matches the user that is logged in, it deletes the note from the database.
### Request Body (POST Method)
`noteId`(integer): JSON object that contains the ID of the note to be deleted.
### Returns 
Returns an empty JSON response, and a flash message to indicate it was successful and there is no additional data to return. 


## <a id="r6"></a>R6 - Entity Relationship Diagram

## <a id="r7"></a>R7 - Detail any third-party services used by the app
### Flask 
* Flask is a web framework for Python, and provides tools, features and libraries for quickly building web applications. It can improve developer’s workflow by helping users to build web applications faster. (https://flask.palletsprojects.com/en/3.0.x/)
### Usage in the app 
* Routing – Creating routes and view functions
* Templating – Render the front end using Jinja templates
* Flash – For displaying success and error messages – (https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/)
* User Authentication and validation
* URL redirections
---
### Flask-Login 
* Flask-Login is a user-session management extension for flask. It is for handling common user tasks such as logging in, logging out, saving user sessions and authentication.
(https://flask-login.readthedocs.io/en/latest/)
### Usage in app
* @login_required decorator for protecting routes that need logging in
* Login/Logout handling 
---
### Werkzeug
* Werkzeug is a WSGI (Web Server Gateway Interface) web application library for Python. It provides developers with collections of tools and utilities for building web applications and frameworks faster.
(https://werkzeug.palletsprojects.com/en/2.3.x/utils/)
### Usage in app
* Generate_password_hash for hashing user passwords before storing them in the databases
* Check_password_hash for verifying user passwords stored in the databases.
---
### SQLAlchemy
* SQLAlchemy is an open source Python SQL tool with an ORM toolkit, that provides ways for developers to interact with databases. Being an Object relational mapper, it allows developers to interact with databases using Python instead of SQL queries
https://www.sqlalchemy.org/
### Usage in app
* Defining the database models (User, Note, Category) using Python classes

## <a id="r8"></a>R8 - Describe your projects models in terms of the relationships they have with each other

### User model
```
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
```
This model represents the user and has the following attributes:
* `id`: Unique ID of the user.
* `email`: Email address of the user.
* `password`: password of the user.
* `first_name`: First name of the user.
#### One-to-Many Relationship (User to Note):
* Each user can have multiple notes (One-to-Many).
* In the `User` model, the `notes` attribute establishes this relationship, indicating that each user can have multiple notes.
* The `user_id` attribute in the `Note` model serves as the foreign key to reference the user.
### Note model
```
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # Establishing a relationship with the Category model
    category = db.relationship('Category', backref='notes', lazy=True)
```
This model represents the users notes and has the following attributes
* `id`: Unique identifier for the note.
* `data`: Content of the note.
* `date`: Timestamp indicating when the note was created.
* `user_id`: ID of the user who created the note (has a foreign key relationship with the User model).
* `category_id`: ID of the category associated with the note (has a foreign key relationship with the category)

#### Many-to-One Relationship (Note to User and Note to Category):
*   Each note belongs to one user and one category (Many-to-One).
*   In the Note model:
    *   The user_id attribute (foreign key) references the user who created the note.
    * The category_id attribute references the category to which the note belongs to
### Category model
```
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)

    # Establishing a relationship with the Note model
    note_refs = db.relationship('Note', backref='category_ref', lazy=True)
```
This model represents a category that can be attached to a note (optional) and has the following attributes

* `id`: Unique id for the category.
* `description`: Description of the category.

#### One-to-Many Relationship (Category to Note):
*   Each category can have multiple notes (One-to-Many).
* In the Category model, the note_refs attribute establishes this relationship, indicating that each category can have multiple notes.
* The category_id attribute in the Note model is the foreign key to reference the corresponding category.

## R9 - Discuss the database relations to be implemented in your application
In this application, the database has three main tables, User, Note and Category. The following are the database relationships to be implemented

### User to note relation
*  Each user can have multiple notes
* Each note belongs only to a single user
* This relationship is a one-to-many relationship, as one user can have many notes
### Note to category relation
* A note can optionally belong to one category
* Each category can have many notes attached to it
* This relationship is a one-to-many relationship, as one category can have many notes, but each note belongs to one category only

## R10 - Describe the way tasks are allocated and tracked in your project

I used Trello to keep track of my tasks. [Link to trello board](https://trello.com/b/qKQo7VGH/t2a2-web-api-assessment)

Before starting the app, I would research online on how similar apps were built. First looking at the file structure, then deciding what routes/views I would need and then creating the models.

I decided to use Bootstrap to simplify the frontend development so I could focus on the routes/functions 

Once I had a rough idea of the routes/views I used a Trello board to input the tasks I would need to complete. I made a card for each route/view and each model. 

The method of making a card for each route and model allowed me to make the tasks look smaller, which made it easier for me to start work and make progress. It also allowed me to focus on each individual tasks better.


I had three main columns to track my progress, `To Do's`, `Doing`, & `Completed`. Inputting the individual cards in the To do's with some information and an estimate of the due date, and putting the cards I was working on in the Doing column and finally putting them in the completed column once I was done.

# <a id="references"></a>References
I acknowledge the use of ChatGPT (chat.openai.com) to help produce this application. The prompts used include 

* (ChatGPT, OpenAI, 20th March 2024, Prompt: "What are the benefits of an ORM?" )

* (ChatGPT, OpenAI, 17th March 2024, Prompt: "Could you help me create an ERD for an app that has three tables, user, note and category?" )

