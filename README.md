# Genshin Community Blog

*In this ReadMe, I use Genshin Impact, and the abbreviated Genshin, interchangeably*
<p>
Due to unforeseen circumstances, time spent on this project was limited to one week. As such, there are a few CSS styling issues left unresolved. They do not impact the functionality of the site, however I am eager to fix them once I have completed this course to maximize the visual aspects of this site.

- Encountered an issue where adding Issues to a Project in the repo caused issues with the workspace and led to restarting. As such, the kanban board can be found in a previous repository, [here](https://github.com/users/charlie-vf/projects/6/views/1). I have also added the User Stories into this ReadMe.

# Table of Contents
- [Introduction](#introduction)
- [UX](#ux)
    - [User Stories](#user-stories)
    - [Admin Stories](#admin-stories)
- [Development](#development)
- [Strategy](#strategy)
- [Target Audiences](#target-audiences)
- [The Website Should...](#the-website-should-allow-users-to)
- [Scope](#scope)
- [Skeleton](#skeleton)
- [Design](#design)
    - [Colours](#colors)
    - [Header](#header)
    - [Fonts](#fonts)
    - [Images](#images)
- [Features](#features)
    - [Nav Bar](#nav-bar)
    - [Header](#header)
    - [Contact](#contact)
    - [Footer](#footer)
    - [Site Pagination](#site-pagination)
    - [Home Page](#home-page)
    - [Posts](#posts)
    - [Categories](#categories-page)
    - [Create Post](#create-post-page)
    - [Edit & Delete posts](#edit--delete-pages)
    - [Notification Pop-up](#notification-pop-up)
    - [Login/Logout Pages](#login-page)
- [Future Features](#future-features)
- [Issues/Bugs](#issuesbugs)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [User Stories](#user-stories-1)
    - [Admin Stories](#admin-stories-1)
    - [Other Testing](#other-manual-testing)
- [Code Validation](#code-validation)
- [Deployment](#deployment)



## **Introduction**

This blog was created for my fourth project in Code Institute's Full-Stack Software Development Course.
It is a blog for Genshin Impact players to come together and share their experiences with the game, whatever they may be. 
Users can create, edit & delete their own posts, and interact with others' posts, too!

## UX

## **User Stories**

- As a Site User I can browse a paginated list of posts so that I can see all posts on the blog.
- As a Site User I can browse individual categories so that I can find posts related to my topic of interest.
- As a Site User I can register an account so that I can create posts and like & comment on other posts.
- As a Site User I can edit and delete my own posts.
- As a Site User I can click on posts so that view the full content and the comment discussion.
- As a Site User I can comment on posts so that I can talk to others & share my experiences with the game.
- As a Site User I can like/unlike posts so that I can interact with other content.

## **Admin Stories**

- As a Site Admin I can view posts in an editor so that I can manage the blog's content effectively.
- As a Site Admin I can view & approve comments before they are posted so that I can moderate content on the site.

## **Development**

This site is loosely based on inspiration from Reddit feeds and the HoyoLab website (a website by the game's creators for players of their two related games), however time constraints and abilities altered the finished outcome.

## **Strategy**

My aim with this website was to create an easily navigatable, minimilistic site for casual blogging by Genshin players.
Whilst the main goal is sharing content, it could also be used as a means for players to keep track of their favourite moments, build highlights and more.

## **Target audiences**

- Players of Genshin Impact
- People looking for a new game to play that has a healthy community

## **The website should allow Users to**:

- Browse posts and narrow by category
- Create an account
- Create, edit and delete posts
- Like and comment on posts from other Users

## The website should allow the Admin to:

- Manage comments on posts
- Override user authentication to delete posts which violate the idea of a healthy community

## **Scope**

Time constraints limited the amount of features from the original plan I was able to implement, however priority scoring ensured the most important features made their way into the finished site.

### The UX must:

- Allow Users to create an account
- Allow Users to create posts
- Allow Users to browse all posts, or by category

### The UX should:

- Allow Users to edit & delete their posts if authorised
- Allow Users to comment & like on other posts

### The UX may (future implementation):

- Allow Users to update their password
- Allow Users to create accounts with social media
- Allow Users to view only their own posts

## **Skeleton**

All pages follow the same basic setup, with the central section changing according to the page's contents. The Wireframe created using Figma.

![Skeleton](media-readme/genshin-homepage.png)

## **Design**

Various styling elements were taken from the free Bootstrap template Greyscale (link in credits section)

### **Colors**

My theme with the webpages I have created thusfar is purples, blues and black. For this site, as Genshin Impact is an incredibly bright game, I chose to scrap the black and stick to purples, blues, white and light-grey.
As this site is heavily image-based, a white background best displays the images, and aids in accessibility when using purples.

![Purples/Blues](media-readme/genshin-purples.png)
![Greys](media-readme/genshin-greys.png)

### **Header**

The header is the main feature of each page, with a full-width image and gradient text. For this reason, I chose a purple-themed image and white text to contrast the other headings on the pages.

### **Fonts**

I have used some harsher fonts on websites in the past, however for this site I chose to stick with gentler fonts. 
The fonts used were Roboto and Lato, from Google Fonts.

### **Images**

Users can upload their own images when publishing to the site; otherwise, a default image will load onto their post. This image is editable at any point using the Edit Post function.

## **Features**

### **Nav Bar**

The navigation bar features an oft-memed quote from the game ('Te Nnadayo'), links to Home, Create a Post, Categories dropdown and Register/Login/Logout, as well as the site's name on the far right.
On smaller screens, the navigation bar condenses into a full dropdown menu.
The navigation menu features on all webpages, and the Login link alters depending on the User's login status.
The Categories dropdown becomes a link to a full categories page when the User is not on the homepage.

### **Header**

The header features the site's name and a small extract summarising the purpose of the site. It is backed by a themed image taken from the most recent expansion in-game.
This features on every page.

### **Contact**

The contact page contains the contact details for my previous fictional gaming club site, Gay Street Games.
This features on every page.

### **Footer**

The footer is simple, with a short text on the creator and links to social network homepages.
This features on every page.

### **Site Pagination**

When a page has more than six posts, a button is added above the contact section to allow Users to navigate through the pages.

### **Home Page**

The homepage features the full directory of all posts on the blog.

### **Posts**

### Posts on Homepage

- Image
- Title & Extract - clickable link to full post content
- Date and time of creation
- Number of likes displayed as a heart icon with a number
- Author name
- Category

### Post on Individual Posts page

- Title
- Author
- Date & time of creation
- Category
- Image
- Content
- Likes and Comments, displayed as icons with numbers. Like icon will be filled in if the User has liked the post
- Edit & Delete buttons
- Comments
- Comment form

### Post on Category page

- Image
- Title - clickable link to full post content

### **Categories Page**

The categories page displays a list of all the currently created categories by the Site Admin. If more are added, this will dynamically update.
If a category is empty, a message will display informing the User of this.

### **Create Post Page**

Contains a form for Users to create their posts with. 
- Required Fields:
    - Title
    - Category (dropdown)
    - Content
    - Image (will be the default image if one is not uploaded)
- Optional Field:
    - Excerpt
- Other:
    - Submit button

### **Edit & Delete Pages**

These contain the same form as the Create Post page, with the button updated accordingly.

### **Notification Pop-Up**

Upon logging in/out, the User will be displayed with a pop-up message informing them of the action which will auto-dismiss after three seconds.

### **Login Page**

Allows the User to login with their credentials. If they have not yet created an account, there is a link to sign-up.
The sign-up page requires a username and repeated password, while email is optional.

### Logout Page

Follows the same formatting as the Login page & allows Users to logout.


## **Future Features**

- Sign-up with social media
- Require email on sign-up with ability for User to toggle whether they wish to receive updates on the blog
- Personal profile for Users where they can view their posts and likes
- Search bar to narrow post display further than categories allows
- Draft creation. Currently only available in Admin
- Add images to Categories page as the current list is plain - time constraints negated ability to work more on this page

## **Issues/Bugs**

- Category: general not displaying when adding links to posts from within the individual category page.
    - This was fixed by changing the name of the category to 'general stuff'
- SummerNote not loading in on website
    - This was fixed by following the directions [here](https://github.com/summernote/django-summernote) and adding '|safe' when loading in to the post_detail template.


## **Technologies Used**

- HTML5
- CSS3
- Python - Django functionality inc. models, views, urls

### Other:

- Django - used to build models, views and app urls
- Bootstrap - site responsiveness and extra design features
- Summernote - used on post creation forms for content styling
- Crispy Forms - used on create and edit forms
- Cloudinary - cloud-based storage
- ElephantSQL - database URL
- Google Fonts - provided the Roboto and Lato fonts
- Color Mind - generated color palettes
- Font Awesome - icons for likes and comments
- Figma - generated wireframe
- StartBootstrap - provided Grayscale template which I took various styling code from
- GitPod - development workspace
- Git - version control using GitPod terminal to commit and push to GitHub
- GitHub - store for website's code and content
- Heroku - hosting platform


## **Testing**

### **User Stories**

- As a Site User I can browse a paginated list of posts so that I can see all posts on the blog.
    - Created additional posts in each category to ensure pagination works throughout

- As a Site User I can browse individual categories so that I can find posts related to my topic of interest.
    - Navigated to categories from individual posts, categories dropdown and categories list page 

- As a Site User I can register an account so that I can create posts and interact with other posts.
    - Created two accounts to validate registration, login & logout

- As a Site User I can edit and delete my own posts.
    - Edit & Delete buttons available underneath posts
    - Checked editing/deleting only allowed if I was logged into the corresponding account for a post

- As a Site User I can click on posts so that view the full content and the comment discussion.
    - Title & excerpt are clickable links to full post content page
    - Clicking on a post brings User to full post content page

- As a Site User I can comment on posts so that I can talk to others & share my experiences with the game.
    - Comment form available under each post
    - Commented on posts from each account

- As a Site User I can like/unlike posts so that I can interact with other content.
    - Like icon available under each post
    - Liked and unliked posts from each account

### **Admin Stories**

- As a Site Admin I can view posts in an editor so that I can manage the blog's content effectively.
    - Can view a full list of posts in Django Admin
    - Can edit posts, including slug, author, likes and status, which are not available to regular site Users

- As a Site Admin I can view & approve comments before they are posted so that I can moderate content on the site.
    - Comments are passed to approval system before they are published
    - Approving a comment publishes it underneath the corresponding post


### **Other Manual Testing**

- Used all links in navigation bar on all pages
- Pages are responsive from large to small screens
- Social media links in footer work and open in new tabs
- Attempted to edit/delete posts when not logged in - not allowed

## **Code Validation**

- HTML5 - Passed W3C Markup Validator (did raise issues with use of {}, but none with actual HTML content)
- CSS - Passed W3C Markup Validator with no issues
- Python - Files tested with ExtendsClass - Returned no serious issues


## **Deployment**

This project was created using a GitPod workspace, commited to Git, pushed to GitHub and deployed on Heroku.

### Heroku Deployment

Steps taken:

#### Initial:
- Click New App
- Choose name and region

#### Environment Set-Up:
- Navigate to Settings > Reveal Config Vars
- Add the following:
    - DATABASE_URL - generated using ElephantSql
    - CLOUDINARY_URL - generated from Cloudinary API
    - SECRET_KEY - generated using command in terminal and hidden inside env.py file
- To settings.py in project workspace, add the following:
    - ALLOWED_HOSTS - heroku app name + localhost
    - TEMPLATES_DIR - join templates folder
    - allauth, cloudinary, summernote & crispy_forms to Installed Apps
    - SITE_ID
    - update TEMPLATES with created TEMPLATES_DIR
    - get DATABASE_URL from env.py and update DATABASES
    - STATIC_URL
    - STATICFILES_STORAGE
    - STATICFILES_DIRS
    - STATIC_ROOT
    - MEDIA_URL
    - DEFAULT_FILE_STORAGE
- Create Procfile
    - web: gunicon project-name.wsgi

#### Deployment
- Navigate to Deploy
- Link GitHub account and select relevant repository
- Click Manual Deploy, then enable Automatic Deployments

## **Credits**

- All images uploaded to the site were found on Google.
- [Grayscale](https://startbootstrap.com/theme/grayscale) Bootstrap template
- Helpful [videos](https://www.youtube.com/@Codemycom) for creating categories views
- [Summernote](https://github.com/summernote/django-summernote) help