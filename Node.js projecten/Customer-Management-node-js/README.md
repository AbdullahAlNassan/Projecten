Customer Management Web App



A simple customer management application built with Node.js, Express, MongoDB, and EJS.
This application allows users to manage customers by adding, editing, deleting, searching, and viewing their information.
The app also includes authentication with a login and signup system.

Features

Customer Management:

Add new customers. 
Edit existing customer details. 
Delete customers from the database. 
Search for customers by name. 
View detailed customer information. 

Authentication:


User login and signup functionality.
Passwords are securely hashed using bcrypt.

Responsive UI:


Built with Bootstrap and custom CSS for a clean, responsive design.
Light and dark mode toggle included.
File Structure

Views:


add.ejs: Form to add a new customer.
edit.ejs: Form to edit customer details.
search.ejs: Search results page.
view.ejs: Detailed view of a customer's information.
index.ejs: Homepage displaying all customers.

Components:


dark-light.ejs: Toggle for light/dark mode.
navbar.ejs: Navigation bar.
sidebar.ejs: Sidebar for easy navigation.

Public Folder:


bootstrap-icons: Icons used in the app.
css: Custom stylesheets.
img: Images used in the app.
js: Custom JavaScript files.

Routes:

allRoutes.js: Handles all customer-related operations.
addUser.js: Handles user registration.

Controllers:

userController.js: Logic for handling customer management and user authentication.

Models:


customerSchema.js: Defines the database schema for customers and users.
Technologies Used
Backend: Node.js, Express
Frontend: EJS, Bootstrap
Database: MongoDB
Authentication: bcrypt
UI Enhancements: Bootstrap Icons, Custom CSS
Installation

Clone the repository:



Visit the app in your browser at https://customer-management-nodejs.onrender.com
