


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
For this project I chose the fonts Schoolbell and Henny Penny. I found these fonts really fun and eye catching. They give the project a relaxed and fun look.
### Colour Scheme
I used the page's Eye Dropper extention to find a color that I could bounce off.

<details>
<summary>Eye Dropper screenshot</summary>

![Eye Dropper screenshot](assets/documentation/webpage-eyedropper.webp)
</details>

<br>

Then from that selection I used Colorspace to create a palette for my site.

<details>
<summary>Colorspace</summary>

![Colorspace](assets/documentation/colorspace.webp)
</details>

## Features:

### Navigation
I've kept the design on this website very. VERY simple. The reason for this came from a little market research(a chat with my co-workers at my current job). They had said that people tend to lose interest in events website because they are usually overloaded with useless navigation links and pages.
This is as simple and easy to use as I could possibly make it. <br> The navigation consists of 3 buttons(not including the logo, leading back to the home screen). The 'Home' button takes the user to the events list page, with all the upcoming events in the area. The 'My Events' button takes the user to their saved events, or for the organiser (Bars) they will be redirected to the event's that they've created.
### Footer
The footer is a simple sentence that tells the user the company that's created the website.
### Other features
There are many different features on this website that offer a diverse experience for users.

#### User Types
The site has a sign up page allowing the user to choose the type of user they are e.g 'Public' or 'Bar/Pub'. This separates the views that each of the user types can see.
<br>
The public can only like/save and view the events, whereas the Bar/Pub user type can create/delete/edit their own events for the public to see.

#### Commenting
This is a feature that I really wanted to include in the site. It gives the chance for the public to express how they feel about the event and share their opinions to others. This is controlled by the Superuser, they will have the final say on whether the comment can be posted or deleted.

#### The like button(heart)
I've added this feature for the public to like and saved the events on their own personal page. They can also unlike the event and this will remove the event from their 'My Events' page.

#### Filtering
The option to filter through the events adds definition to the site, allowing the user to search for specific dates and locations(Bars/Pubs).

## Technologies Used
HTML,
CSS,
Bootstrap,
Github,
Python,
Django,
Summernote,
AllAuth,
Cloudinary
## Testing
THE most important part of this project, and I still have a love/hate relationship with! <br> Here we go!!
<br>

#### Superuser access
<details>

<summary>Superuser access credentials here!</summary>
Username: codeinstitute <br>
Password: Helloworld!
</details>

### Google's Lighthouse Performance

<details>
<summary>Mobile</summary>

![Mobile Lighthouse Performance]()
</details>

<details>
<summary>Desktop</summary>

![Desktop Lighthouse Performance]()
</details>

### Browser Compatibility

<details>
<summary>Chrome</summary>

![Chrome](assets/documentation/chrome-browser.webp)
</details>

<details>
<summary>Internet Explorer</summary>

![Internet Explorer](assets/documentation/internet-explorer-browser.webp)
</details>

<details>
<summary>Safari</summary>

![Safari](assets/documentation/safari-browser.webp)
</details>

<details>
<summary>Firefox</summary>

![Firefox](assets/documentation/firefox-browser.webp)
</details>

<details>
<summary>Opera</summary>

![Opera](assets/documentation/opera-browser.webp)
</details>

### Responsiveness
I've displayed the responsiveness of this site in my [user stories](userstories.md), head over to see them!
### Code Validation


<details>
<summary>Logged in event list page</summary>

![Logged in event list page](assets/documentation/event_list_loggedin-validation.webp)
</details>

<details>
<summary>Logged out event list page</summary>

![Logged out event list page](assets/documentation/event-list-not-loggedin-%20validation.webp)
</details>

<details>
<summary>Logged in(bar) event list page</summary>

![Logged in(bar) event list page](assets/documentation/event-list-loggedin-bar-validation.webp)
</details>

<details>
<summary>Log in page</summary>

![Log in page](assets/documentation/login-validation.webp)
</details>

<details>
<summary>Log out page</summary>

![Log out page](assets/documentation/logout-validation.webp)
</details>

<details>
<summary>Sign up page</summary>

![Sign up page](assets/documentation/signup-validation.webp)
</details>

<details>
<summary>Event detail page</summary>

![Event detail page](assets/documentation/event-detail-validation.webp)
</details>

<details>
<summary>My events(Bar) page</summary>

![My events(Bar) page](assets/documentation/my-events-bar-validation.webp)
</details>

<details>
<summary>My events(Public) page</summary>

![My events(Public) page](assets/documentation/my-events-public-validation.webp)
</details>

<details>
<summary>CSS</summary>

![CSS](assets/documentation/css-validator.webp)
</details>

### CI Python Linter

<details>
<summary>admin.py</summary>

![admin.py linter](assets/documentation/admin.py-linter.webp)
</details>

<details>
<summary>apps.py</summary>

![apps.py linter](assets/documentation/apps.py-linter.webp)
</details>

<details>
<summary>forms.py</summary>

![forms.py linter](assets/documentation/forms.py-linter.webp)
</details>

<details>
<summary>models.py</summary>

![models.py linter](assets/documentation/models.py-linter.webp)
</details>

<details>
<summary>settings.py</summary>

![settings.py  linter](assets/documentation/settings.py-linter.webp)
</details>

<details>
<summary>signals.py</summary>

![signals.py linter](assets/documentation/signals.py-linter.webp)
</details>

<details>
<summary>urls.py</summary>

![urls.py linter](assets/documentation/urls.py-linter.webp)
</details>

<details>
<summary>urls.py project-level</summary>

![urls.py project-level linter](assets/documentation/urls.py-project-level-linter.webp)
</details>

<details>
<summary>views.py</summary>

![views.py linter](assets/documentation/views.py-linter.webp)
</details>

### Manual Testing user stories or/and features
User Story |  Test | Pass
--- | --- | :---:
As a **logged-in user**, I want **to see a list of events I've created** so that **I can manage them easily** | When the user lands on the events page, they should be able to browse events they've created | &check;
As a **returning user**, I want **to log in** so that **I can access my saved events** | The returning user should be able to log in with ease, they will then be redirected to the events page with the option to view their saved events |&check;
As a **new user**, I want **to register for an account** so that **I can save events I'm interested in** | Given the user has not yet signed up, they will be directed to sign up(or log in) this will then give the user access to the site and the ability to save events of their interest |&check;
As an **event manager**, I want **to create a new event** so that **I can share it with the community** | The user must have an account under the user type of bar owner to be able to create and event. If so then they will be given a form identical to the one on the admin page to create and post their event |&check;
As an **organizer**, I want **to edit my events details** so that **I can keep them up to date** | Given the user is a bar owner they will be able to edit the events detail on their very own 'Manage you events' page. They should see an 'Edit' button, when clicked, should allow the bar owner to edit their event (Field inputs prepopulated with the previous information) |&check;
As an **organizer**, I want **to delete an event** so that **the event is no longer visible to the public** | As with the above user story, they will need to be on their event management page to be able to delete their events. This will show as a 'Delete' button(in red) they will then have a message pop up to ensure this is what they'd like to do. |&check;
As a **user**, I want **to see a list of upcoming events** so that **I can find something to attend** | Given the user is logged in, they will be able to see the list of upcoming events on the home screen. |&check;
As a **user**, I want **to filter events by date or category** so that **I can find relevant ones quickly** | Given the user is logged in, they will be able to filter the events to most recent dates and times, location of the events |&check;
As a **user**, I want **to see details of an event** so that **I can decide if I want to go** | Given the user has clicked on the event, when viewing the event's page, then they should see the date, time and location of the event  |&check;
As a **user**, I want **the past events not to be displayed** so that **I will not get confused about upcoming events** | Given the user is logged in, when on their saved events or the site's home page, then they will only see the events that are upcoming. The past events will have gone when the date has passed. |&check;
As a **user**, I want **to be able to comment on events** so that **I can ask questions or give my opinion** | Given the user is logged in and has clicked on an event on the page, they will be able to comment on the event at the bottom of the page. |&check;
As a **user**, I want **to be able to edit or delete my comments** so that **I can change the text or delete the comment** | Given the user is logged in and has created a comment. If they need to make amends to the comment made, they will be able to click on the edit button and the field will be prepopulated with the message they'd already written. There will be a delete button(in red) next to the edit button for the user to delete the comment completely. |&check;
As a **Superuser**, I want **to be able to monitor the comments** so that **I ensure that the comments made are appropriate** | Given the user is a Superuser, they will have the ability to monitor comments and delete them if need be. This is all done on the admin page. |&check;
As a **user**, I want **see when a comment is posted** so that **it can feed my nosy personality** | Given the user is logged in and has clicked on an event, they will be able to see the comments posted and when they were published to the site. |&check;


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

#### Status for the events that we're created
I wanted to the public only to see the published events and not the drafts. I added the 'status' to the EventForm in the forms.py then created an if statement for the events to show only if the status is equal to 1 ('Published'). Saved my work and refreshed the page...nothing! Had to think hard about this one as it was a Saturday and the beginning of the kids 6 weeks holiday. I found that it wasn't working because the if statement was used before the event in event_list for loop. I altered this and there it was, all the published events and the drafted events hidden.

#### Summernote W3C Validator
Minor HTML validation warnings may appear due to the django-summernote editor's rendering behavior. These are frontend-only and do not impact site performance or user experience.

#### Log in/Sign up button
This was a little bit of a pain in the bottom. I ran the code through the WAVE site(to test accessibility) and the button came up as a contrast error. I had fixed these and made it so that the error have gone and the contrast was just right!


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
    - YouTube
    - Google Photo search for testing my Cloudinary connection.
  
  - Acknowledgment
    - I'd like to thank my family for, again, being patient through this whole project. It's been one whirlwind!
    - Another MASSIVE thank you to my mentor Matt. I think I've caused more than one headache for him through this project! So, thank you and sorry!!