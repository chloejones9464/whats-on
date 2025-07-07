


## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)

    
2. [Features](#features)
    * [Navigation](#Navigation)
    * [Footer](#Footer)
    * [Home page](#Home-page)
    * [Other features](#Other-features)

3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Design & Planning:

### User Stories
[Here](userstories.md) you'll find the user stories for my project.

This page contains links to my user stories in my GitHub project and will have corresponding screenshots/screen recordings of the completed tasks.
### Wireframes
[Click here](wireframes.md) to view all the wireframes for this project.
### Typography
Explain font you've used for your project
### Colour Scheme
Screenshoot of the colour scheme for your project

## Features:
Explain your features on the website,(navigation, pages, links, forms.....)
### Navigation
### Footer
### Other features
## Technologies Used
HTML,
CSS,
Bootstrap,
Github,
Python,
Django,
Summernote,
AllAuth
## Testing
Important part of your README!!!
### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
Check compatability with different browsers
### Responsiveness
Screenshots of the responsivness, pick few devices (from 320px top 1200px)
### Code Validation
Validate your code HTML, CSS (all pages/files need to be validated!!!), display screenshots
### Manual Testing user stories or/and features
User Story |  Test | Pass
--- | --- | :---:
paste here you user story | what is visible to the user and what action they should perform | &check;
As a **logged-in user**, I want **to see a list of events I've created** so that **I can manage them easily** | When the user lands on the events page, they should be able to browse events they've created | 
As a **returning user**, I want **to log in** so that **I can access my saved events** | The returning user should be able to log in with ease, they will then be redirected to the events page with the option to view their saved events |
As a **new user**, I want **to register for an account** so that **I can save events I'm interested in** | Given the user has not yet signed up, they will be directed to sign up(or log in) this will then give the user access to the site and the ability to save events of their interest |
As an **event manager**, I want **to create a new event** so that **I can share it with the community** | The user must have an account under the user type of bar owner to be able to create and event. If so then they will be given a form identical to the one on the admin page to create and post their event |
As an **organizer**, I want **to edit my events details** so that **I can keep them up to date** | Given the user is a bar owner they will be able to edit the events detail on their very own 'Manage you events' page. They should see an 'Edit' button, when clicked, should allow the bar owner to edit their event (Field inputs prepopulated with the previous information) |
As an **organizer**, I want **to delete an event** so that **the event is no longer visible to the public** | As with the above user story, they will need to be on their event management page to be able to delete their events. This will show as a 'Delete' button(in red) they will then have a message pop up to ensure this is what they'd like to do. |
As a **user**, I want **to see a list of upcoming events** so that **I can find something to attend** | Given the user is logged in, they will be able to see the list of upcoming events on the home screen. |
As a **user**, I want **to filter events by date or category** so that **I can find relevant ones quickly** | Given the user is logged in, they will be able to filter the events to most recent dates and times, location of the events |
As a **user**, I want **to see details of an event** so that **I can decide if I want to go** | Given the user has clicked on the event, when viewing the event's page, then they should see the date, time and location of the event  |
As a **user**, I want **the past events not to be displayed** so that **I will not get confused about upcoming events** | Given the user is logged in, when on their saved events or the site's home page, then they will only see the events that are upcoming. The past events will have gone when the date has passed. |
As a **user**, I want **to be able to comment on events** so that **I can ask questions or give my opinion** | Given the user is logged in and has clicked on an event on the page, they will be able to comment on the event at the bottom of the page. |
As a **user**, I want **to be able to edit or delete my comments** so that **I can change the text or delete the comment** | Given the user is logged in and has created a comment. If they need to make amends to the comment made, they will be able to click on the edit button and the field will be prepopulated with the message they'd already written. There will be a delete button(in red) next to the edit button for the user to delete the comment completely. |
As a **Superuser**, I want **to be able to monitor the comments** so that **I ensure that the comments made are appropriate** | Given the user is a Superuser, they will have the ability to monitor comments and delete them if need be. This is all done on the admin page. |
As a **user**, I want **see when a comment is posted** so that **it can feed my nosy personality** | Given the user is logged in and has clicked on an event, they will be able to see the comments posted and when they were published to the site. |


## Bugs

Let's talk bug and how I've managed to fix them.

#### Connecting the view
I have a little bit of trouble with this. I tried it all, you name it!
It came down to the name of the file. I was trying to connect my events list HTML page(events_list.html) but Django wasn't looking for this file, it was looking for event_list.html. The difference being event is singular not plural! After working this out, the view was connected and I felt like I deserved a nice warm bubble bath!

#### Favicon
I love the idea of having you're own logo at the top of the browser, it's so fun and also very personal to the project. This bug caused a few grey hairs being pulled out!
The Favicon was not displaying and I kept getting an error display. I looked up on StackOverflow and found out that I needed to put the Favicon documents in the static folder in the directory. With this done, all I needed to do then was change the path. BOOM! Favicon in all it's glory.

#### Pending comment
I wanted to show the user that their comment hasn't been posted but is awaiting approval by the admin. This was tricky and needed a good bit of research. I couldn't find the specific answer, maybe I wasn't asking the right question. I then resorted to asking my newly nicknamed ChatGPT friend, Codey, to help me work this issue out. I discovered that I needed to import Q from django, and I then used a filter so that only the user was able to see their pending comment and no one else. Once approved the comment is posted. This was worthy of more than a bubble bath!!

## Deployment

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.
#### Deloying on Github
The site was deployed to Github Pages using the following method:
- Go to the Github repository.
- Navigate to the 'settings' tab.
- Using the 'select branch' dropdown menu, choose 'main'.
- Click 'save'.

## Credits
List of used resources for your website (text, images, snippets of code, projects....)
  - Code Institute
  - StackOverflow - This helped me for quite a lot of my project, it was refreshing that others had the same issues as I did.
  - ChatGPT - Saved the day when I needed to ask silly questions or solve stubborn error messages. It also created my background image and favicon.
  - Favicon
  - Django website - Made my life so much easier reading through the documentation.
  
  - Media
  
  - Acknowledgment
    - acknowledgment to mentors, peers, tutors, friends, family, facilitator (who ever contributed and helped with the project)