
<div align="center">
  <br>
  <h1><b>Django Live Chat</b></h1>
  <strong>A real-time chat application</strong>
</div>
<br>
<table align="center" style="border-collapse:separate;">
  <tr>
    <td style="background: #344955; border-radius:20px; border: 5px solid transparent"><small>Python</small></td>
    <td style="background: #344955; border-radius:20px"><small>Django</small></td>
    <td style="background: #344955; border-radius:20px"><small>JavaScript</small></td>
    <td style="background: #344955; border-radius:20px"><small>Tailwind Css</small></td>
    <td style="background: #344955; border-radius:20px"><small>Daphne</small></td>
  </tr>
</table>

# Table of Contents
- [Introduction](#introduction)
   - [Installation](#installation)
   - [How Django Chat works](#how-django-chat-works)
- [Code and organization](#code-and-organization)
   - [The project folder: chat](#the-project-folder-chat)
   - [The App folders: core and room](#the-app-folders-core-and-room)
   - [The static folder](#the-static-folder)
   - [Templates](#templates)
   - [Requirements](#requirements)
   - [Third-party code](#third-party-code)
- [About](#about)
- [Distinctiveness and complexity](#distinctiveness-and-complexity)
<br>
 
# Introduction
This is a Django-based chat application that allows the admin to create rooms through the Django admin page and allows users to chat in real-time using WebSockets. It includes user authentication, room creation and real-time messaging.

## Installation

<details>
   <summary>1. Clone this repository</summary>

   >You can clone the repository by using this Git command in the terminal:
   >```pwsh
   >git clone <repository link>
   >```
   > It is necessary that you have installed <a href="https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/daphne/">Daphne</a>

</details>
<details>
   <summary>2. Install dependencies</summary>
   
   > Once you have navigated to the project directory install the dependencies by entering this command in the terminal:
   > ```pwsh
   > pip install -r requirements.txt
	>```

</details>
<details>
   <summary>3. Run migrations</summary>

   >\
   > To initialise the migrations use this command in the terminal:
   > ```pwsh
   > python manage.py makemigrations
   >```
   >
   > After you have entered this command run:
   > ```pwsh
   > python manage.py migrate
   >```
   > 


</details>
<details>
   <summary>4. Create a superuser</summary>
   
   > To create a superuser enter the following command in the terminal:
   > ```pwsh
   > python manage.py createsuperuser
   >```
   >After entering this command following the prompts to enter a username, email and password.
   >Once all of the above is completed you will have a superuser!
   

</details>
<details>
   <summary>4. Start the server</summary>
   
   > To start the server use this Daphne command in the terminal:
   > ```pwsh
   > daphne chat.asgi:application --port 8001
   >```
   >After this step, in another terminal enter this command to start the django development server:
   >```pwsh
   >python manage.py runserver
   >```
   

</details>
<details>
   <summary>4. Enjoy!</summary>
   
   > If you have completed all these steps you should now be able to open the TCP address in your browser and test out Django chat for yourself.

</details>

## How Django chat works

The user must create an account, if they would like to remove or  create a room they must create a superuser as demonstrated in the installation instructions. The user must then log in if they have created a superuser or sign in if they have chosen not to. After this you are able to access the "rooms" page which allows you to view all the chat rooms that are available to join.
<br>

1. **User Authentication**:
Users can sign up or log in if they have created a superuser which is shown in the [installation section](#installation) of this file. Authentication is handled through Django's built in authentication system and the log out function is handled by a custom log out function in core/views.py using the built in django logout handling. Once logged in the user is redirected to the homepage again from which they can access the chat rooms page through a link in the navbar where they can view, join and chat in a chat room of their choosing.

2. **Room Creation**:
A logged in superuser can remove or create chat rooms providing a name, through the Django admin page. Each room is assigned a unique slug (URL-friendly-identifier) for easy access

3. **Joining a Room**:
Users can join an existing room by clicking on the room's name from the "rooms" page. Once inside a room users can see the previous messages in the room and start sending new messages.

4.**Real-Time Messaging**:
The application uses <strong>Django Channels</strong> and <strong>WebSockets</strong> to enable real-time communication.
when a user sends a message, the message is broadcast to all users in the same room and the message is saved to the database for future reference. Users will also see messages appear instantly without refreshing the page.

5.**Room Management**:
Each room has a unique URL based on its slug (/rooms/room-name/). Users can also leave a room at any time by navigating away from the page.

6.**Database Structure**:
The application uses a SQLite database (by default) to store the user account and authentication details, chat rooms created and messages sent in each room linked to their respective room and user.

7.**Frontend and Backend Interaction**:
The frontend handles user interactions and displays real-time updates. The backend manages WebSocket connections, message broadcasting and database operations.
	
<br>

# Code and organization
The Django chat application has the following structure:
- It is divided into 2 apps: core and room.
- Each app folder contains a models.py, views.py and templates folder. Views imports from models.py.
- Both of the apps have db models in their respective models.py: website and dashboard
- The project does not feature any static JavaScript or Css files. Due to the use of script tags in the base.html file and the use of Tailwind Css.


Let's take a look at what each app does.
<br>

## The project folder: chat
<br>
The chat folder is the standard django application folder.
<br><br>

## The App folders: core and room

### **1. Core**
Contains the files responsible for the homepage, sign-up, log-in and log-out. It is responsible for the creation of user accounts.
### **2. Room**
Contains most of Django chat's logic. This is where the live chat feature gets handled through the use of Websockets and Python and Javascript logic to handle the storage and displaying of chats entered into a chat room. This is also where the logic for displaying and joining a chat room is stored.
<br>

## Templates
Each app counts with its own templates folder for their respective pages that they need to show. These are accessible from the login page.
<br>

## Requirements
As noted in the installation instructions, a requirements.txt file will be featured in the repository so that all dependencies can be installed accordingly.

The requirements.txt hold dependencies such as daphne.
<br>

## Third-party code
Writing the codebase required some research. Source for media such as icons are included in the code. 

# About
This project is my submission as the capstone project for CS50w from HarvardX.
More information about the CS50w requirements available at https://cs50.harvard.edu/web/2020/projects/final/capstone/
<br>

# Distinctiveness and complexity
This Django-based chat application stands out from other projects in the course due to its advanced features, real-time functionality, and use of modern web technologies. Unlike traditional Django applications that rely on HTTP requests and responses, this project uses WebSockets for real-time communication. WebSockets enable instant message delivery between users without requiring page refreshes, which is a significant departure from the synchronous nature of standard Django views. Implementing WebSockets requires Django Channels, which extends Django to handle asynchronous tasks and real-time features, adding a layer of complexity not found in simpler projects.

The project leverages asynchronous programming to handle multiple WebSocket connections simultaneously. This requires a deeper understanding of ASGI (Asynchronous Server Gateway Interface) and how it differs from the WSGI used in traditional Django applications. Additionally, the application includes a robust user authentication system, allowing users to sign up, log in, and log out. Users must be authenticated to create or join rooms, ensuring that only authorized users can participate in chats. This adds an extra layer of complexity compared to simpler projects that don’t require user authentication.
<div align="center">
  <br>
