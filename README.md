![Sojourn Scribbles logo](static/images/tplogo.png)

# Welcome to Sojourn Scribbles

## A Travel Journal Blogging website
### Sojourn Scribbles brings together solo women travelers from around the globe, offering a platform to share experiences, insights, and camaraderie.  

The responsive website allows registered users to create blog posts (journal entries) and a profile with thier bio and a photo. Users who are not registered are free to browse the posts. To make it easy to find content for you, users can filter blog posts by author or country.  

# **[Link to Live Site](https://sojourn-scribbles-b8489dc9653c.herokuapp.com/)**  

*This project is created as a final portfolio project for the Code Institude.*  

**Built by Katie Jane Coughlan**

---

# Table of Contents  

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---

# UX

## Database Planning

## UX Design

## Wireframes

##### [ Back to Top ](#table-of-contents)

# Agile Development

## Kanban Board

## User Stories

##### [ Back to Top ](#table-of-contents)

# Features Implemented

## Navbar and Footer

## Index Page

## Our Story

## My Journal

## Home

## Authentication and Profile Management

## Responsiveness

##### [ Back to Top ](#table-of-contents)

# Features Left to Implement

- xyz
- xyz

##### [ Back to Top ](#table-of-contents)

# Technology Stack

- HTML - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for event listeners on buttons
- Django - framework used to build this project
- Jinja - templating language rendering logic within html documents
- Bootstrap 5 - front end framework used for styling
- Heroku PostgreSQL - used as the database
- Balsamiq - for wireframes
- Canva - for creating assets
- Font Awesome - for social media icons
- Lucidchart - for database ER diagrams
- Gencraft - for AI images
- Pexels - for free stock images
- Google Fonts- 
- GitHub - for storing the code and for the Kanban board
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - for version control

##### [ Back to Top ](#table-of-contents)

# Testing and Validation

## Responsiveness

## Manual Testing

## Code Validation

##### [ Back to Top ](#table-of-contents)

# Known Bugs

- **There is a bug with alert message in the profiles view.**  
The error message for the PostForm is not working as expected BUT thanks to the power of Django the user still receives red error messages within the form itself.  
The ProfilesForm success message was incorrectly displaying when there was an error submitting the PostForm. To avoid confusion for the user, until the bug is resolved I have turned off that alert message.  
  
![Alert message error](/static/images/readme/ealert.png)

- xyz

##### [ Back to Top ](#table-of-contents)

# Deployment 

## Deployment Guide for the Sojourn Scribbles Website

### Deployment Steps:

#### Creating the Heroku App

- Begin by signing up or logging in to Heroku.
- In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Choose a unique name for your project, like "Travelling Scribbles".
- Select the EU region.
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

#### Setting Up Environment Variables

- Create `env.py` in the top level of the Django app.
- Import `os` in `env.py`.
- Set up necessary environment variables in `env.py`, including the secret key and database URL.
- Update `settings.py` to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".
- Migrate the models to the new database connection in the terminal.
- Configure static files and templates directories in `settings.py`.
- Add Heroku to the `ALLOWED_HOSTS` list.

#### Creating Procfile and Pushing Changes

- Create a `Procfile` in the top level directory.
- Add the command to run the project in the `Procfile`.
- Add, commit, and push the changes to GitHub.

#### Heroku Deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Make sure to resolve any deployment errors by adjusting the code as necessary.

### Forking the Repository

Forking the GitHub Repository allows you to create a copy of the original repository without affecting it. Follow these steps:

- Log in to GitHub or create an account.
- Visit the [repository link](https://github.com/katiejanecoughlan/sojourn-scribbles-V3).
- Click on "Fork" at the top of the repository.

### Creating a Clone of the Repository

Creating a clone enables you to make a local copy of the repository. Follow these steps:

- Navigate to the [Sojourn Scribbles repository](https://github.com/katiejanecoughlan/sojourn-scribbles-V3).
- Click on the <>Code button.
- Select the "HTTPS" option under the "Local" tab and copy the URL.
- Open your terminal and change the directory to your desired location.
- Use `git clone` followed by the copied repository URL.


##### [ Back to Top ](#table-of-contents)

# Resources

- [Code Institute Full Stack Development course materials](https://codeinstitute.net/) 
- [Django docs](https://www.djangoproject.com/)
- [Crispy forms docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Cloudinary docs](https://cloudinary.com/documentation/programmable_media_overview)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack overflow](https://stackoverflow.com/)
- [Dev Community](https://dev.to/)
- [Code Institude Slack](https://slack.com/)

##### [ Back to Top ](#table-of-contents)

# Credits and Acknowledgements

## Images

- The Sojourns Scribbles logo was created by me using [Canva](https://www.canva.com/)
- Profile images for the mock content were generated by AI using [gencraft](https://gencraft.com/)
- Post featured images for the mock content were taken from royalty free stock photos on [Pexels](https://www.pexels.com/)

## Code

- **Code Institute** course content for providing the knowledge and guidance to build the project
- GitHub user **TulaUnogi** for sharing a best practice README structure
- Course Facilitator **David Calikes** for his unwaving support and guidance during the process 
- Tutor **Martin McInerney** for his endless patience and support with trouble shooting issues
- Tutor **Kevin Loughrey** for his helpful SME sessions and constant support
- My mentor **Chris Quinn** for sharing his wisdom and guiding me in this project
- My fellow **cohort peers** for their support, help with trouble shooting issues and sharing the experience

## Content

##### [ Back to Top ](#table-of-contents)

