# ENGLISH GROWS
  
![image](https://github.com/user-attachments/assets/d93bcbc5-c5b2-4834-94b3-8beb290e27f0)
      
## Overview
This site is an **e-commerce** with integrated **marketing tools** capable of easily creating a **marketing emailing campaign** within minutes, apart from creating and sending a newsletter to subscribers. This functionality allows authorized users to **create customized email templates, and send an email campaign/newsletter to all subscribers**.  
  
The site offers services in the education industry, both to B2C and B2B potential customers. More specifically, online English teaching services by live qualified English teachers. The services provided are the following:  
  
- **B2C**
  * Individual Lesson Packs
  * Reduced Group courses

- **B2B**
  * Customized corporate professional training plans

## Live Site
- You can view the deployed site on Heroku [here](https://english-grows-477471d17e50.herokuapp.com/)

## Repository
- You can check the Github repository [here](https://github.com/Ethra8/english-grows)

## Author
Edna Torres Munill


# TABLE OF CONTENTS
  
- [PROJECT OVERVIEW](#project-overview)  
    * [Live Site](#live-site)  
    * [Repository](#repository)  
    * [Author](#author)
- [UX](#ux)
    * [Target Audience](#target-audience)
    * [Project Goals](#project-goal)
    * [User Stories](#user-stories)
    * [User Profiles](#user-profiles)
 - [UI](#ui)
    - [Agile Methodology](#agile-methodology)
    - [Structure](#structure)
      * [Pages](#pages)
      * [Site Structure](#site-structure)
      * [Database Structure](#database-structure)
    - [Design Choices](#design-choices)
      * [Hero Image](#hero-image)
      * [Color Palette](#color-palette)
      * [Typography](#typography)
    - [Wireframes](#wireframes)
    - [Features](#features)
      * [Implemented Features](#implemented-features)
        - [Responsiveness](#responsiveness)
        - [Accessibility](#accessibility)
        - [User Authentication](#user-authentication)
        - [Online Payments - Stripe Integration](#online-payments---stripe)
        - [CRUD Functionality](#crud-functionality)
        - [Navigation Bar](#navigation-bar)
        - [Footer](#footer)
        - [Forms](#forms)
            * [B2B Contact Form](#contact-form)
            * [Newsletter Form](#newsletter-form)
        - [Service Sorting](#service-sorting)
        - [Search Bar](#search-bar)
        - [Shopping Bag](#shopping-bag)
        - [Organize Users by Groups or Levels](#organize-users-by-groups-or-levels)
        - [404 Error Page](#404-error-page)
        - [Admin Console - CRUD Functionality](#admin-console)
      * [Future Features](#future-features)
    - [Web Marketing Techniques](#web-marketing-techniques)
      * [Search Engine Optimization (SEO)](#search-engine-optimization-(SEO))
      * [Social Media Marketing](#social-media-marketing)
      * [Email Marketing](#email-marketing)
- [TESTING](#testing)
  * [Defect Tracking](#defect-tracking)
    - [Github Issues](#github-issues)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
  * [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
  * [Core Web Vitals](#core-web-vitals)
    - [Lighthouse Reports](#lighthouse-reports)
  * [Code Validation](#code-validation)
    - [HTML 5](#html-5)
    - [CSS 3](#css-3)
    - [JS ES6](#js-es6)
    - [Python 3.12](#python-3.12)
  * [Accessibility Testing](#accessibility-testing)
    - [Contrast Validation Reports](#contrast-validation-reports)
    - [General WCAG 2.1 Report](#general-wcag-2.1-report)
  * [Manual Testing](#manual-testing)
- [TECHNOLOGIES USED](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
- [DEPLOYMENT](#deployment)
  * [Version Control](#version-control)
  * [Heroku](#heroku)
- [CREDITS & ACKNOWEDGEMENTS](#credits-and-acknowledgements)
  
  
# UX
You will find in the points stated below a brief study aiming at providing the user with the best possible experience when visiting this site.  
  
## Target Audience
### B2B
Any company interested in improving its employees' level of English for one of the following reasons:
* Wants to compete in the international market
* Operates locally with international customers
  
### B2C  
Any individual person wanting to improve their level of English for one of the following reasons:  
* Travel
* Careers
* University Students (e.g: Students must certify a B2 level of English to apply to the Erasmus program)
  
## Project Goal
  1. The site aims at providing B2B and B2C customers with services they can buy: live online lessons in individual or reduced groups format.
  2. Any user can register for an account.
  3. B2B users can send a contact form to receive customized offers on the type of service desired for their company.
  4. B2C services available can be stored in a shopping bag and bought online through Stripe API.
  5. All users can subscribe to the monthly newsletter. Members of the monthly newsletter are informed of interesting cultural events, and social and historic facts related to the British culture, and English speaking countries around the world.
  
  
## USER STORIES
  
### AS A FIRST-TIME VISITOR 
#### B2C and B2B
- [X] 1. **MUST:** I want to ***check the social media links*** to see the website profile on social media platforms such as FB, for instance, to look at photos from past events, and maybe follow.
- [X] 2. **MUST:** I want to ***check the about page***, to be informed of the site's purpose.
- [X] 3. **MUST:** I want to clearly ***see at first glance the part of the site that is specially dedicated to me (B2B or B2C)***
- [X] 4. **MUST:** I want to ***subscribe to the newsletter*** to receive special offers and tips.
  
#### B2B
- [X] 5. **MUST:** I want to be able to easily ***contact the site*** to receive a customized training plan and quote.  
     
#### B2C
##### Viewing and Navigation
- [X] 6. **MUST:** I want to view ***all the available services listed***, so that I can easily choose what service suits me best.
- [X] 7. **SHOULD:** I want to be able to ***view specific type of service, so that I can quickly find services I'm interested in*** without having to go through all the services (e.g.: individual exam preparation classes)
- [X] 8. **MUST:** I want to be able to ***view individual service details***, so that I can read a more detailed description, and check further details.
- [X] 9. **SHOULD:** I want to be able to easily ***view the total of my purchase at any time***, so that I can avoid spending too much.
    
##### Sorting and Searching
- [X] 10. **SHOULD:** I want to ***sort the full list*** of available services ***by categories*** or ***by price***, so that I can easily identify the one that suits me best.
- [X] 11. **SHOULD:** I want to ***sort*** a ***specific category*** of services ***by price***, or ***alphabetically*** so that I can identify the best-priced services in a specific category.
  
### AS A RETURNING VISITOR
- [X] 12. **MUST:** I want to be able to easily **register for an account**, and ***receive an email confirmation*** after registering, so that I can verify that my account registration was successful.
  
### AS AN AUTHENTICATED USER & SHOPPER
- [X] 13. **MUST:** I want to be able to ***easily login and logout***, so that I can access my personal account information.
- [X] 14. **MUST:** I want to be able to ***easily recover my password*** in case I forget it, so that I can recover access to my ccount.
- [X] 15. **MUST:** I want to be able to ***have a personalized user profile***, so that I can view my personal order history and order confirmations.
- [X] 16. **MUST:** I want to be able to ***update and save my personal account information*** on my user profile.
- [X] 17. **MUST:** I want to able to easily ***access my bag, and update or delete*** any items in it.
- [X] 18. **MUST:** I want to be sure that ***my personal  is secured***, and that no one else can access my profile, nor my order urls, which also contain personal .
- [X] 19 **MUST:** I want to make ***secure online payments*** to be able to purchase online teaching services.
- [X] 20. **MUST:** I want to ***receive a confirmation email after a purchase***, with the details of my order.
- [x] 21. **MUST:** I want to be able to ***view past orders, and read their full information*** from my ***personal profile***.
- [X] 22. **MUST:** I want to ***see success or error messages for every action undertaken*** so that I can ***be informed of the state of my actions***.
  
### AS A SITE OWNER OR ADMIN USER:
- [X] 23. **MUST:** I want to be able to **sort orders by users**, so that I can easily check the orders related to a specific user.
- [X] 24. **MUST:** Each **order is automatically linked to the authenticated user** making it.
- [x] 25. **SHOULD:** Each **user's email is stored in a separate email list**, to easen up future emailing campaigns.
- [X] 26. **MUST:** I want to be able to **store  in admin from B2B contact requests**, so that I can easily rewiew company requests, and have their contact emails, name, company name, and request secured and handy.
- [X] 27. **SHOULD:** I want to be able to **edit and delete existing services directly from the site**, without having to access the lesser user-friendly admin panel.  
- [X] 28. **SHOULD:** I want to be able to **add a new service directly through the site**, without having to access the lesser user-friendly admin panel.
- [X] 29. **MUST:** I want that **only authenticated users can make an order**, so that personal  from all users is protected.

### AS A MARKETER
- [X] 30. **SHOULD:** I want to be able to create editable email templates for the newsletter or emailing campaigns (Marketing campaigns).
- [X] 31. **SHOULD:** I want to be able to send marketing campaigns to subscribed users.
- [X] 32. **SHOULD:** I want to be able to send a newsletter to users that are subscribed.

  
N.B.: FUTURE FEATURES or 'WISHES' stated in [Future Features](#future-features)
    
  
# UI
  
## AGILE METHODOLOGY
This project has been development with the Agile development method in mind, although at times, it might not have fully followed the methodology to a full extent.
- [User stories](#user-stories) have been created and implemented one at a time, and have been labelled following the **MoSCoW priorization logic**: ***Must*** & ***Should*** have. Future features have been, and will be, created following the same logic, adding ***Could*** and ***Won't/Wish*** labels.  
- Keeping in line with the Agile development methodology, a Kanban board has been created, and used to track user sttories, and bugs during development: [Kanban Project](https://github.com/users/Ethra8/projects/7)


## STRUCTURE
  
### PAGES
The following fully responsive pages form the structure of this site:
  
#### HOME Page
  
  https://github.com/user-attachments/assets/a3283894-c476-4bd6-98bf-72cc7ab3c06f
  
#### INDIVIDUAL SERVICES Page
  
  https://github.com/user-attachments/assets/56db04fd-8737-46c1-899b-8afe30d44451
  
#### SERVICE DETAILS Page
  
  https://github.com/user-attachments/assets/0c807135-ca7d-4d4f-bc54-47af789c394e
        
#### BAG Page
  
  https://github.com/user-attachments/assets/c9ef0617-dd11-48c8-b93a-ca5bdd9b9bba

#### CHECKOUT Page
- MOBILE:
  
  https://github.com/user-attachments/assets/2f8fd19e-c285-4dee-860b-7150cd71fd62
    
- TABLETS:
  
  ![image](https://github.com/user-attachments/assets/e073b890-7571-4666-b1d7-c885eeac99d1)
  
- DESKTOP:
  
  ![image](https://github.com/user-attachments/assets/110f6110-6966-4874-9b6d-c9a55620af93)
  
    
#### COMPANIES Page
    
  https://github.com/user-attachments/assets/cc97328c-17c1-4754-bc7f-b57c525c3553
  
#### ABOUT Page
  
  ![image](https://github.com/user-attachments/assets/d1defeb8-b45c-4522-965b-1874f8011f43)
  
#### 404 ERROR Page
  
  ![image](https://github.com/user-attachments/assets/4ed25394-ce01-4613-be51-bda7f8e5e6b1)
  
  
#### ACCOUNT Pages
- User authentication has been implemented in this site by installing django-allauth, whose User model is also used.
- An instance of the ***UserProfile model*** in the ***profile app*** is automatically created each time a new **User** model instance is created. Therefore, each time a user registers for an account, a personalized user profile is created, which includes basic user personal information, and past order details.  
- The django default templates have been customized to match the look and feel of the site.  
  
<details>
<summary>CLICK HERE to view a sample of the MOBILE customized account pages</summary>
 
  - ![image](https://github.com/user-attachments/assets/4bd20d72-cf95-4614-a0aa-1dd6f7ea26ef)
  - ![image](https://github.com/user-attachments/assets/cb69672f-148a-4c84-b11a-667785cdc76f)
  - ![image](https://github.com/user-attachments/assets/9c292026-7189-449b-afe2-532bee0b61e1)
</details>
   
<details>
<summary>CLICK HERE to view a sample of the TABLET customized account pages</summary>
  
 - ![image](https://github.com/user-attachments/assets/7c2323a0-d419-4b86-b96c-ec2dd6b8216e)
 - ![image](https://github.com/user-attachments/assets/5dabb85a-6fed-4d6d-b22b-d17639d3a94a)
 - ![image](https://github.com/user-attachments/assets/5a07d5de-e971-4418-9c4b-dc1c06ed4707)
</details>
  
<details>
<summary>CLICK HERE to view a sample of the TABLET customized account pages</summary>

 - ![image](https://github.com/user-attachments/assets/f4459c3f-bd66-41ed-80d4-b6399b5dfc15)
 - ![image](https://github.com/user-attachments/assets/39b9a0ec-ae6f-4bf2-ae3a-ede2e7275879)
 - ![image](https://github.com/user-attachments/assets/3a538725-93c4-4c40-892e-0bf197a18db5)
</details>

  
### SITE STRUCTURE
The site has been developed using ***Django 5.1*** framework for ***Python 3.12***, and contains the 5 different apps stated below, forming its overall structure. Within each app, different ***models***, ***views***, ***urls***, and ***templates*** create the logic of the site. The User model from django all-auth has also been used:
- **DJANGO CUSTOM APPs:**  
  * **Bag**  
  * **Checkout**  
  * **Home**  
  * **Individual_services**  
  * **Profiles**  
  
  
#### BAG app
This app does not contain any model, but contains different ***views***, ***templates*** and ***urls*** to perform the following functionalities:
- **Add items in bag**
- **Show styled bag to user**
- **Update de quantity** of a specific item in the bag
- **Delete** a specific item. 
  
  
#### CHECKOUT app
This app contains the following pages *(templates)* and functionalities *(models & views)*:  
- **PAGES:**
  * **Checkout page**
  * **Checkout Success page *(order details)***
  * **Checkout Confirmation Email *(template used to send order confirmation email to user)***
  
- **FUNCTIONALITIES:**
  * **Create an order if user if authenticated, for  protection**
  * **Include in the order the items in the bag**
  * **Stripe API Integration to allow secure online payments**
  * **Checkout functionality**
  * **Sends order confirmation email to user**
  
  
#### HOME app
This app contains the following pages *(templates)* and functionalities *(models & views)*:  
- **PAGES:**
  * **Home page**
  * **Companies page *(B2B contact form)***
  * **About page**
  * **Subscribe form page**
  
- **FUNCTIONALITIES:**
  * **Users can navigate to different sections of the site from the home page, which is the landing page**
  * **Users can check the about page**
  * **B2C & B2B customers can identify their dedicated section, and can navigate anywhere on the site**
  * **B2B can send a contact request via the form in the companies page**
  * **Users can subscribe to the newsletter**
  * **Admin Users can create email templates for a newsletter or an emaling campaign**
  
  
#### INDIVIDUAL SERVICES app
This app contains the following pages *(templates & urls)* and **CRUD functionalities** *(models & views)*:  
- **PAGES:**
  * **View all individual services**
  * **View service details page**
  * **Add a new service page**
  * **Update a service page**
  * **Delete a service page**
  
- **CRUD FUNCTIONALITIES**
  * **Authorized users can CREATE *(add)* a service**
  * **Users can READ (view) all services for individuals**
  * **Authorized users can UPDATE a service**
  * **Authorized users can DELETE a service**
  
- **OTHER FUNCTIONALITIES**
  * **Users can sort services by type or price, and sort within a certain type by price or alphabetical order**
  * **Users can search the site for a specific word**
  * **Users can check each service's details page**
  * **Users can adjust quantity of a specific service to include in the bag**
    
  
#### PROFILES app
This app contains the following pages *(templates & urls)* and **CRUD functionalities** *(models & views)*:  
- **PAGES:**
  * **Profile page**
  
- **FUNCTIONALITIES:**
  * **Users can update their personal information**
  * **Users can view past order details**
    
### DATABASE STRUCTURE - MODELS
- A PostgreSQL database has been used to build this project from scratch. For th initial stages of the developments, the sjango sqlite3 was utilized at first, but quickly moved to PostgreSQL database.
- Several apps have been created to store the different modules that have been created, using Django 5.1 framework, in order to store the site's data in the database. All the data models of the site can be found in [this Googlesheet](https://docs.google.com/spreadsheets/d/1jID6FXBd1tZINHULIWNXjc0iRhyYGC6ce3y9dMppRVg/edit?gid=956386076#gid=956386076)


#### ERD (Entity Relationship Diagram)
Als [on this sheet](https://docs.google.com/spreadsheets/d/1jID6FXBd1tZINHULIWNXjc0iRhyYGC6ce3y9dMppRVg/edit?gid=1982826762#gid=1982826762):
  
  ![image](https://github.com/user-attachments/assets/d38ee880-f5f6-4d5a-ad92-ae515883afea)
  
        
#### CHECKOUT App - Models
This app has the following models:  
  
  ![image](https://github.com/user-attachments/assets/c3de7eae-a040-46be-adef-095ce6ff703d)
  
    
#### HOME App - Models
This app has been created to store the home page *index.html* template, views and urls. For simplicity sake, the model that store data from the ***Companies*** section form has also been included in this app. Should the companies' section be widenned in the future, an independent app would be created to store this model and the subsequent templates, urls, and views.  
This app contains 2 forms, whose data is stored, and CRUD can be performed from the admin panel by an authorized user:  
  
- The **B2B Contact Form** takes user input in the *companies page* form, and posts the user request from CompanyContactform model, passing data to CompanyContact model whihc takes all the data and is registered to the admin model.
- The **Subcribe Form** only takes the name and email of any user, and stores it to create marketing campaigns, more specifically, emailing campaings. The data is reflected in the admin.
- The **EmailTemplate** model allows authorized users to perform CRUD functionality, to create email templates for marketing campaigns.
- The function send_email_campaign in the utils file is included in the options dropdown of the Email Template model in the admin panel.
- To conduct a marketing campaign (emailing), the authorized user only has to create or edit an existing email template, then save it, select it, select the option *send email campaign* on the dropdown, click on ***go***, and the email template selected is automatically and instantly sent to all subscribers.
  
   ![image](https://github.com/user-attachments/assets/bacf0bfd-957f-4ed3-b56d-ee3b6ab070ed)

  
  
#### INDIVIDUAL SERVICES App - Models
  
  ![image](https://github.com/user-attachments/assets/4f56a1f6-f387-4e71-86b7-f043e5f7dd71)
  
  
#### PROFILES App - Models
  
  ![image](https://github.com/user-attachments/assets/0e6956b9-e197-49dc-86f6-ef96b4f4a6c6)
  
   
## DESIGN CHOICES
The design of this site has been thought to reflect professionality and inspire trust.
  
### HERO IMAGE
The following image has been created to be the hero image. The globe is the same as in the logo, and has been selected to represent both the global reach that online classes have, and the global importance of English as a *lingua franca*. Three small birds have been included to the image, to represent the *freedom* that learning English can bring to people (traveling, business, etc.), the *communication capability* boost, and all three form a small group, to represent the small group learning format offered. The colours of the hero image match the look and feel of the site, also in harmony with the logo.

  ![image](https://github.com/user-attachments/assets/d8a08d0d-a9bb-43d8-a56f-7c3d1467d481)

  
### COLOUR PALETTE
This is the palette used, contrasting with white fonts on darker backgrounds. Blue tones are proven to foster a state of relaxation and wellbeeing, optimal for the learning process:
  
![English Grows color palette](https://github.com/user-attachments/assets/e4736fe3-98b4-4a52-9692-04e88e3bf1f9)  

  
### TYPOGRAPHY
The following fonts have been used, all from Google Fonts:
- **Montserrat**: Used for all main text in the site, the header and subheader of the *For Companies* page, and the alert messages.
- **Big Shoulders Display**: On the main heading of the landing page for the title *English Grows*, to match the logo styling, as well as for the other pages headings  
- **Charmonman**: Used for the landing page's subheading/slogan, and for the services page's part of the heading that says'for you', to match the logo styling

  https://github.com/user-attachments/assets/8560d6db-694a-4b88-8e77-bf1dabdbb580

    
## WIREFRAMES
  
### MOBILE & TABLET (Portrait)
  
<details>
<summary>CLICK HERE to see the Mobile & Tablet (portrait) Wireframes</summary>
- HOME Page
  
  ![image](https://github.com/user-attachments/assets/f1ff2dc3-dab8-4148-8458-bca729c1103e)
   
  
- INDIVIDUAL SERVICES Page

  ![image](https://github.com/user-attachments/assets/a475da96-e85b-4e53-abc1-eaf8cf2bebc4)
 

- SERVICE DETAILS Page

  ![image](https://github.com/user-attachments/assets/ebddef38-1203-4983-994c-65b0dc80d028)
   
    
- SHOPPING BAG Page (form)
  
  ![image](https://github.com/user-attachments/assets/214d0c04-16bf-45ec-ac71-6a8d12cfeff2)
   
  
- MY PROFILE Page (list)

  ![image](https://github.com/user-attachments/assets/258e896a-4b65-4a61-972f-7443b6600b48)
   
  
- COMPANIES CONTACT Page (form)
  
  ![image](https://github.com/user-attachments/assets/33dbc871-2b95-4fde-a68a-a160e301f523)
   
  
- ABOUT Page

  ![image](https://github.com/user-attachments/assets/e8288bda-5346-40d1-9825-3a9d0b4d4a57)


- SUBSCRIBE Page

  ![image](https://github.com/user-attachments/assets/7d6319d9-7b34-463d-8946-3a3e3ae7bed7)

    
</details>  

  
### DESKTOP & TABLET (Landscape)
  
<details>
<summary>CLICK HERE to see the Desktop and Tablet (Landscape) Wireframes</summary>

  - HOME Page
      
    ![image](https://github.com/user-attachments/assets/ddc49bf0-a2bb-4c75-a50f-dc3a601540de)
    
    
  - INDIVIDUAL SERVICES Page
    
    ![image](https://github.com/user-attachments/assets/04878b1f-6993-4c48-bc4d-6210c8f8b0e4)

        
  - PACK DETAILS Page
    
    ![image](https://github.com/user-attachments/assets/65efcf9a-dd87-45d0-ba5c-a644dfd90075)
    
    
  - SHOPPING BAG Page
  
    ![image](https://github.com/user-attachments/assets/af85acb3-c0a7-4dc7-ae64-50767a7003e4)
      
      
  - MY PROFILE Page
  
    ![image](https://github.com/user-attachments/assets/162a3e7b-32a0-41c3-9311-2b01521d4e91)

        
  - COMPANIES Page (B2B contact form)
      
    ![image](https://github.com/user-attachments/assets/6a8065bb-a2c1-46c5-9d2f-7217acbb1504)
          
    
  - ABOUT Page
  
    ![image](https://github.com/user-attachments/assets/277e3916-d1dc-43a7-8781-00530ebde3ce)

  - SUBSCRIBE Page (newsletter susbscription form)

    ![image](https://github.com/user-attachments/assets/7854e1d7-4c38-4f69-9b6f-44350ba031b1)

    
</details>  
  
  
# FEATURES
  
## IMPLEMENTED FEATURES  
## Responsiveness
This site has been designed and coded to be fully responsive, even in extra small devices of the range of a 250px wide viewport, assuring that the site has an optimal display to virtually every device in the market.  
    
## Accessibility
This site has been coded by always keeping accessibility in mind, and achieving good results during the testing phase. For further reference, please check the accessibility reports [here](#accessibility-testing).
    
## User Authentication
* These models also come from django-allauth, and is used to give certain permissions to users, to verify them manually, update information, or delete them. Groups can be created to group users by current English language level, for instance:  
  
   ![image](https://github.com/user-attachments/assets/da898b54-7842-40b4-aa9b-4ad09b7bdafd)  
    
Django ***all-auth*** module has been implemented in the site. It allows to easily secure user personal imnformation stored in the profile, or to restrict access to order url to the same authenticated user. **Templates have been customized to match the *look and feel* of the site**.
  
<details>
<summary>CLICK HERE to see the customised templates</summary>
  
   - ![image](https://github.com/user-attachments/assets/90ed2427-bbf5-4117-bf76-0ca0f0859436)   
    
   - ![image](https://github.com/user-attachments/assets/0324af75-5a15-4b25-bd67-de054fe30373)  
    
   - ![image](https://github.com/user-attachments/assets/cbbcab9d-a5f5-4bdb-8c66-0e01795f29e5)  
  
   - ![image](https://github.com/user-attachments/assets/19f04349-82f4-4bbe-b33e-f674599d5a9e)  
  
   - ![image](https://github.com/user-attachments/assets/c654fa7b-8e72-4d86-9eef-f7ebfb2d6bdb)  
  
   - ![image](https://github.com/user-attachments/assets/eafc5285-6a9e-45d7-975a-5d61768fa0a5)  
  
   - ![image](https://github.com/user-attachments/assets/ed6abc95-9488-4eaa-958d-a5305101eefd)  
  
   - ![image](https://github.com/user-attachments/assets/42bf8fa0-b1b4-479d-b47e-b05a3afac143)  

</details>  
    
  https://github.com/user-attachments/assets/a05ad833-22d2-4918-af9c-399ab638847e
    
## Online Payments - STRIPE API  
[Stripe](https://www.stripe.com) secure payment platform has been implemented in this site, and is fully functional. Users receive a confirmation email after the purchase, and webhooks have also been implemented:  
  
  ![image](https://github.com/user-attachments/assets/cc65c560-fec2-431c-8a76-39c68e2e3694)  
    
  ![image](https://github.com/user-attachments/assets/8697aa36-0ae5-4dd3-a9bd-18b5e21c3301)  

## CRUD Functionalities
### Admin Console - CRUD Funtionalities
The admin console reflects most of the models present in this site, and also some features from django-allauth module's user model. Authorized users (admin *superusers*) can ***create***,***read***,***update*** and ***delete*** ***(CRUD)*** any data model from the admin panel. Therefore, admin users with the necessary permissions can perform full CRUD functionalities on the following data models stored in its postgreSQL database: 
  
  * Services
  * Types of Services
  * Users
  * User Profiles (profile model)
  * Contact Requests (via B2B contact form)
  * Orders

    ![image](https://github.com/user-attachments/assets/e291b79f-118a-4056-ae2d-e5ee263cc1b6)  
  
#### Accounts
From django User model, stores **registered users' emails** for future emailing campaigns.
 
#### Profile
 * After each user is created, a profile is automatically created as well, and is stored in the admin. The user can update their information through their 'profile', but the admin can  also update each user profile manually:  
   
   ![image](https://github.com/user-attachments/assets/43a9c341-bb08-45b7-9bf9-5f1438f3840c)  
    
#### Home
- As the contact form on the 'For Companies' page is stored in the *home* app, this model has been created to store the contact requests sent by the users:  
 
 ![image](https://github.com/user-attachments/assets/2be02964-8be9-42c6-aedc-91b253e51f93)  
 
 ![image](https://github.com/user-attachments/assets/648e5c59-0485-4ca1-92f7-16c2387e79e5)  

- This app also features the subscription form, and the functionality to create an emailing campaign directly and easily from the admin panel. Authorized users can create an email template with user-friendly editable text area (used *django-summernote* for this purpose), and a function sends the email to all subscribers with just one click:

  https://github.com/user-attachments/assets/982ba163-91f3-4da2-8747-4b9ca192a019

    
### Checkout
The orders created by the Order model are stored in the database, and reflected in the admin panel:  
  
  ![image](https://github.com/user-attachments/assets/27bff2b5-0fdf-49f3-a2c0-b235e22f4017)  
  
  ![image](https://github.com/user-attachments/assets/fee8e06e-3b76-4baf-a081-373f9f13976f)  

 
### Services - CRUD from site
 * To improve UX and the overall UI, authorized users (admin *superusers*) can ***create***,***read***,***update*** and ***delete*** ***(CRUD)*** the data model for Individual Services, including the service image, directly through the site without need to enter the lesser user-friendly admin panel. Thus, **Services can be created, read, updated, or/and deleted** through the main service page in the site:  
  
   ![image](https://github.com/user-attachments/assets/4cf94aba-6e49-4c50-a9b3-a4bf8d2f4c55)    
  
   ![image](https://github.com/user-attachments/assets/7b238e2b-a507-47c1-bc55-bc60e9bfaa82)    

  
## Navigation Bar
There are two navigation bars and both are fully responsive:
1. The first, ***topnav***, is fixed to the top of each page in the site, including the 404 error page, for an improved UX. It has a dark blue *#003366* background color, with white font and icons. It contains the logo on the left, which links to the home page, and two icons taken from [Fontawesome](https://fontawesome.com/):
  * [**user icon**](https://fontawesome.com/icons/user?f=classic&s=solid): Has a ***dropdown*** menu whose options link to the user's ***profile*** (when signed in) and ***logout*** (when signed in, ***login*** if logged out). When the user is logged in, the user name displays below the icon.
  * [**bag icon**](https://fontawesome.com/icons/bag-shopping?f=classic&s=solid): Links to the shopping bag. Below the icon, the total amount of items stored in the bag is displayed.
2. The second, ***nav***, is only present in the individual services page, accessed through the *For You* button on the home page. It has a search bar to search for specific words within all the services names and descriptions.  
  
  https://github.com/user-attachments/assets/71ea8143-fb09-4948-8eb5-bf2eeeb86a10  

## Footer
The fully responsive footer is pushed to the bottom of every page, including the customized 404 error page. It includes the following features and links:
    
  ![image](https://github.com/user-attachments/assets/bd08a7ec-d693-4769-bb56-746afc5b1804)
  
  - Links to the following pages of the site, as some sort of **secondary navigation bar**:
    * About Page
    * Services Page for B2C customers (*your you*)
    * Companies page *(B2B contact form)*
  - Banner links to newsletter subscription form
  - Social media **icons** for *facebook*, *instagram*, *youtube*, and *twitter*
  - Copyright notice
  
  https://github.com/user-attachments/assets/e62d886d-13a4-4de8-a3b6-32719accf8ea
    
## Forms
### B2B CONTACT Form
  
  https://github.com/user-attachments/assets/148b0e3d-b0d0-4f58-9eed-d86b26624faa  

### SUBSCRIBE FORM

  ![image](https://github.com/user-attachments/assets/0db91451-d214-4648-829d-40ea3100b523)

## Product Sorting
  
  https://github.com/user-attachments/assets/bafbf9ec-4e4d-4802-9856-65bd3ae02a98  
  
## Search Bar
The search bar is on the ***for you*** service page:
  
  ![image](https://github.com/user-attachments/assets/58f3b28c-3e3d-46cc-a2fc-81a298bd6c82)
  
  
## Shopping Bag
Whithin the shopping bag, users can **update quantity** of service packs to buy, and **delete any service** from the bag as well. The **subtototal is updated too** depending on the quantity of each item. Then the user can check out, or return to services. Please refer to the following videos and screen captures to see all these features in action.  
  
  https://github.com/user-attachments/assets/c5d745df-9c5d-490b-afe4-098bc30c4d05   
  
  ![image](https://github.com/user-attachments/assets/33e28d23-3d08-4886-b6e8-9658dde6d3b5)  
  
  ![image](https://github.com/user-attachments/assets/9c2d5574-e4e5-4a82-b32e-741e31c64035)  
  
  https://github.com/user-attachments/assets/75625e41-44d3-4b62-b630-76f3f1d1a89a  

  * For the sake of improving UX on mobile, without loosing too much screen space, a quantity picker has been added to the bag:

    ![image](https://github.com/user-attachments/assets/6ef294f3-b4b3-4a86-a85c-75feac016161)


## Organize Users by Groups or Levels
This site offers the possibility to the admin users to create groups with unique names, and include users in them:  

  ![image](https://github.com/user-attachments/assets/398355f9-c657-49ee-b47c-42f43c66f20b)

  
## 404 Error Page
To improve UX, the 404 error page has been styled to the look and feel of the site.
  
 ![image](https://github.com/user-attachments/assets/438748da-fb3f-4c70-8655-7fc0874ac368)
  
  
## WEB MARKETING
  
### SEARCH ENGINE OPTIMIZATION (SEO)
    
#### KEYWORDS AND METATAGS
To improve SEO ranking, the tool [Word Tracker](https://www.wordtracker.com/) has been used to research keywords.  
- **Keywords and phrases have been included in the about page** within <strong> tags to highlight their importance to the SE:  
  
  ![image](https://github.com/user-attachments/assets/d895403c-90d8-4be6-b074-bd5c145a88aa)
  
- I have included the following **meta tags** and other SEO relevant info:
  
```$python
<meta name="theme-color" content="teal">
<meta name="description" content="English Grows is a site that offers English teaching services online to B2B and B2C customers, offering     
   individual lesson packs and reduced group formats">
<meta name="keywords" content="English learning, teaching English, English classes online, English lessons online, English tutor, online teacher, English teacher, private lessons online, reduced group classes, online reduced groups, e-learning, corporate English lessons, online reduced classes, live English lessons">
<meta name="author" content="Edna Torres Munill">
```
  
#### sitemap.xml
This file lists the website’s essential pages, making sure Google can find and crawl them all. It also helps search engines understand the website structure, and can help speed up content discovery. Having included this file, improves the site quality, allowing for a better SEO indexing.  
  
To create the file, follow these steps:  
1. Go to [Xml-sitemaps.com](https://www.xml-sitemaps.com/), and include the site's url to generate the xml file, and click on START:  
  
   ![image](https://github.com/user-attachments/assets/7479ba77-1d7f-454d-b07e-a9bd9541d636)
  
2. The file will automatically be generated after the tool crawls all the site's urls (could take a moment, depending on site's complexity). Once completed, click on 'view sitemap details':  
  
   ![image](https://github.com/user-attachments/assets/5cda3f5f-ee2e-4edc-96e9-bbcb7d13c107)
   
3. Download the file, and include it in the site's main root directory
   
  
#### robots.txt
This files disallows crawler spiders to crawl to certain urls in the site, which should not be shown to users on a search engine. All urls of the following directories have been disallowed for security and for a meaningfulness search:  
- Account
- Bag
- Profile
  
  
### SOCIAL MEDIA MARKETING
To promote this site's visibility and to improve customer reach, a mockup profile has been created in the social media platform of facebook:  

  ![image](https://github.com/user-attachments/assets/8661d04c-dc81-4b23-943f-784f047823de)

    
### EMAIL MARKETING
### NEWLETTER 
A form has been included to enable users to subscribe in order to receive special offers and tips. Only a name a an email is requested, and the data is stored and easily accessed through the admin panel. A model allows authorized users to perform CRUD functionlity on the admin panel to create email templates for a newsletter, in this case.
  
#### EMAIL MARKETING CAMPAIGNS
A model allows authorized users to perform CRUD functionlity on the admin panel to create email templates for emailing campaigns, in this case. A fucntion hsa been added, so that when a specific email is checked (selected), and the option *send email campaign* is selected on the dropdown in the email templates model, when the user clicks on ***go***, the email template selected gets automatically sent to all the users who subscribed to the newsletter.
  
This way, this function has a double purpose: To send the newsletter, and to send other marketing campaigns.
  
  https://github.com/user-attachments/assets/22b75b97-b13c-4c99-9b23-2bd8f1cb2f03
    
     
## FUTURE FEATURES
These future features are thought of as being some of the user's imagined ***wishes***:  
  
* [ ] **WISH**: As an **admin user**, I want to **include additional fields in the user profile**, in order to be able to **track students' progress**.
* [ ] **WISH**: As an **admin user**, I want to **receive an email each time a B2B user sends a request via the contact form**, in order to be able to **easily keep track of incomming requests**.
* [ ] **WISH**: As an **B2B user**, I want to **receive a copy of the request made via the contact form**, in order to be able to **have a reminder of my request**.
  
       
# TESTING  
## DEFECT TRACKING
  
### GITHUB ISSUES
All issues have been solved, and closed in Github by the creator of this site.  
  
  
### DEFECTS OF NOTE
No defects of note have been detected on this site.  
  
  
### OUTSTANDING DEFECTS
No outstanding defects have been detected in this site.  


## COMPATIBILITY AND RESPONSIVE TESTING  

### PRESELECTING TESTING TARGETS
- For a meaningful testing of the site, [Stat Counter](https://gs.statcounter.com) has been used, in order to get an insight of the following:
    
    * **BROWSER MARKET SHARE** - Most commonly used browsers worldwide:

    ![image](https://github.com/user-attachments/assets/7a7c49ff-13d3-48f9-ae03-1a4e84a70167)

     * **BROWSER VERSION MARKET SHARE** - Most commonly used browser versions worldwide:

    ![image](https://github.com/user-attachments/assets/05f21ad4-3469-4e97-b870-f6f6334751f5)

    * **OS MARKET SHARE** - Most commonly used operation systems worldwide:

    ![image](https://github.com/user-attachments/assets/217ec506-783f-455c-b6e3-821f5269c326)

    * **MOBILE vs DESKTOP vs TABLET MARKET SHARE** - Most commonly used devices worldwide:

    ![image](https://github.com/user-attachments/assets/7b5b8335-2f93-46a8-908b-4e470b42f2a4)

    * **SCREEN RESOLUTION STATS** - Most common screen resolution (in pixels) worldwide:

    ![image](https://github.com/user-attachments/assets/550ec6df-12c2-4055-8662-53c6758dc221)



### TESTING TARGETS TABLE
Following all the above information, compatibility and responsive testing has been done on the most common *browser versions*, *OS*, and *screen resolution* combinations, by using [Browser Stack](https://chrome.google.com/webstore/detail/browserstack/nkihdmlheodkdfojglpcjjmioefjahjb) Chrome extension, the *Chrome Dev tool's emulator*, and real devices. On the mobile real device, XRecorder app has been used.  
*NB: As BrowserStack now charges for testing a device over 1 minute limit time for their free version, the following testings for this project have been adapted to this inconvenience. In case of it being a real business, I would pay the subscription to get a full-time testing account.*

Please find the correspondent **compatibility and responsive testing** reflected in the following table:

| TEST no.| TOOL               | DEVICE               | BROWSER            | OS              | VIEWPORT width x height (px) |
|---------|--------------------|----------------------|--------------------|-----------------|------------------------------|
| [1](#test-1)        | Chrome Dev emulator| [Samsung Galaxy S8](https://blisk.io/devices/details/galaxy-s8)   | Chrome 117 |Windows 11  |360 x 740             | 
| [2](#test-2)        | BrowserStack       | [Samsung Galaxy S20](https://blisk.io/devices/details/galaxy-s20)   | Samsung    |Android 10.0 |360 x 800           |
| [3](#test-3)        | BrowserStack       | [iPhone XS](https://blisk.io/devices/details/iphone-xs)| Safari   | iOS 15.0   |375 x 812            |
| [4](#test-4)        | REAL mobile device | Samsung Galaxy A22 5G| Chrome             | Android 13.0    |384 x 729                     |
| [5](#test-5)        | BrowserStack       | [Samsung Galaxy S23 Ultra](https://blisk.io/devices/details/galaxy-s23-ultra)| Chrome | Android 13.0  |384 × 824  |
| [6](#test-6)        | BrowserStack       | [iPhone 15  Pro](https://blisk.io/devices/details/iphone-15-pro) | Safari 17  | iOS    |393 × 852                   |
| [7](#test-7)        | REAL Laptop Device | HP Laptop 15s-fq4xxx| Chrome 129.0.6668.72    |Windows 11 Home|1536 x 776                    |
| [8](#test-8)       | BrowserStack               | HP Laptop 15s-fq4xxx         | Firefox 131      | Windows 11 -64bit           |1536 x 776                    |
| [9](#test-9)       | BrowserStack               | MAC         | Safari 17      | MacOs Sequoia           |                   1536 x 776 |

### TEST RESULT VIDEOS
TEST 1
-
  
  https://github.com/user-attachments/assets/d089cf81-eb38-4f1e-9a4a-9a6494fc520b
  
      
TEST 2
-
  
  https://github.com/user-attachments/assets/e666756c-da6d-4a52-a38b-cce301d781b0
  
  
TEST 3
-

  https://github.com/user-attachments/assets/c917bd4f-0cc7-47c9-a595-a94e8b155e22

  
TEST 4
-
  
  https://github.com/user-attachments/assets/7b4cd189-a91a-4d2a-a395-09288cd7a8be
  
  
TEST 5
-  
  
  https://github.com/user-attachments/assets/e456158b-6422-466b-8d27-fcde917aebd6
  
  
TEST 6
-  
  
  https://github.com/user-attachments/assets/45d67030-1556-41cd-ad68-64845575983a
  
  
TEST 7
-
  
  https://github.com/user-attachments/assets/b2202841-1519-44f0-a89c-57c71d90a100
  
  
TEST 8
-
  
  https://github.com/user-attachments/assets/0e9551a3-1d0f-4f7f-9f8d-2bc2e2f9fec2
  
  
TEST 9
- 
  
  https://github.com/user-attachments/assets/2c14d3b4-de0a-415a-8f51-8b0c156de0f9

    
## CORE WEB VITALS
The following tests have been run for this project:  
  
### LIGHTHOUSE REPORTS 
**To improve my first report, the following actions have been taken:**  
- Include a ***site.manifest***

  
<details>
<summary>Click HERE to check the HOME PAGE Lighthouse Reports</summary>
    
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - Home page.pdf](https://github.com/user-attachments/files/17694778/Lighthouse.report.MOBILE.-.Home.page.pdf)
      
  ![image](https://github.com/user-attachments/assets/2178cdde-c5dd-462c-93b6-7df98a4ce39c)
        
  - Laptop and Desktop
    * You can access full report: [Lighthouse report DESKTOP - Home page.pdf](https://github.com/user-attachments/files/17694782/Lighthouse.report.DESKTOP.-.Home.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/f4be1aaa-2730-4fd9-9e43-27250e959177)
  
</details>   

  
<details>
<summary>Click HERE to check the COMPANIES PAGE Lighthouse Reports</summary>
  
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - Companies page.pdf](https://github.com/user-attachments/files/17694791/Lighthouse.report.MOBILE.-.Companies.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/d03912a4-53cf-4408-aee5-6f8d73f900cd)
    
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - Companies page.pdf](https://github.com/user-attachments/files/17694802/Lighthouse.report.DESKTOP.-.Companies.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/f1bf1996-2613-41e7-a6e6-d592ded2ab95)

</details> 

  
<details>
<summary>Click HERE to check the ABOUT PAGE Lighthouse Reports</summary>  
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - About page.pdf](https://github.com/user-attachments/files/17694805/Lighthouse.report.MOBILE.-.About.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/c42245ef-5ed0-40de-aa94-7fe7aa0b1e44)
    
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - About page.pdf](https://github.com/user-attachments/files/17694810/Lighthouse.report.DESKTOP.-.About.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/8e4a1970-4bf8-41e2-a93e-a34d0172c356)

</details>

  
<details>
<summary>Click HERE to check the INDIVIDUAL SERVICES PAGE Lighthouse Reports</summary> 
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - Individual services page.pdf](https://github.com/user-attachments/files/17694753/Lighthouse.report.MOBILE.-.Individual.services.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/c2092868-2142-45a9-aaf4-f7a36d181c95)
       
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - Individual services page.pdf](https://github.com/user-attachments/files/17694842/Lighthouse.report.DESKTOP.-.Individual.services.page.pdf)
  
  ![image](https://github.com/user-attachments/assets/bc69b4f9-141c-4815-9cc3-98e6e87fc696)
  
</details>

  
<details>
<summary>Click HERE to check the SERVICE DETAILS PAGE Lighthouse Reports</summary> 
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse.report.MOBILE.-.services.details.page.pdf](https://github.com/user-attachments/files/17706699/Lighthouse.report.MOBILE.-.services.details.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/e4f9fec2-d31a-4173-acc2-bd94f643fc73)
      
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - services details page.pdf](https://github.com/user-attachments/files/17706710/Lighthouse.report.DESKTOP.-.services.details.page.pdf)
        
  ![image](https://github.com/user-attachments/assets/bc13a15d-6bca-4ca0-ae55-7a8d70c9a732)

</details>

  
<details>
<summary>Click HERE to check the SERVICE DETAILS PAGE Lighthouse Reports</summary> 
  - Mobile & Tablet (portrait)

  You can access full report: [Lighthouse report MOBILE - bag page.pdf](https://github.com/user-attachments/files/17706878/Lighthouse.report.MOBILE.-.bag.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/acc0e2ea-3887-4ba6-b86a-7110e05bcbb6)
      
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - bag page.pdf](https://github.com/user-attachments/files/17706896/Lighthouse.report.DESKTOP.-.bag.page.pdf)
      
  ![image](https://github.com/user-attachments/assets/827b6eca-7146-48e2-bbeb-1eebfd95a9f7)


</details>

  
<details>
<summary>Click HERE to check the CHECKOUT PAGE Lighthouse Reports</summary> 
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - checkout page.pdf](https://github.com/user-attachments/files/17706908/Lighthouse.report.MOBILE.-.checkout.page.pdf)
        
  ![image](https://github.com/user-attachments/assets/cf8568dc-1e50-4f91-9586-ee8d100c3332)
      
  - Desktop & Tablet (landscape)
You can access full report: [Lighthouse report DESKTOP - checkout page.pdf](https://github.com/user-attachments/files/17706949/Lighthouse.report.DESKTOP.-.checkout.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/9de1129c-26e7-4de5-ae74-d691a367c0f3)
  
</details>

  
<details>
<summary>Click HERE to check the PROFILES PAGE Lighthouse Reports</summary> 
  
  - Mobile & Tablet (portrait)
    * You can access full report: [Lighthouse report MOBILE - Profile page.pdf](https://github.com/user-attachments/files/17708017/Lighthouse.report.MOBILE.-.Profile.page.pdf)
  
  ![image](https://github.com/user-attachments/assets/5a9e0045-7d1f-4d99-ac4d-4895414ece90)
    
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - Profile page.pdf](https://github.com/user-attachments/files/17708028/Lighthouse.report.DESKTOP.-.Profile.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/3b8f6225-7b63-4b82-aea6-63b14a31373c)
  
</details>

  
<details>
<summary>Click HERE to check the 404 ERROR PAGE Lighthouse Reports</summary> 
  
  - This customized 404 error page has received a 100% score in accessibilitty, although, of course, SEO and Best Practices encounter the 404 error in the system and therefore reesult in a lower percentage due, precisely at fact of it being a 404 error page. <small>(pardon the redundancy)</small>.  
  
  - Mobile & Tablet (portrait)
You can access full report: [Lighthouse report MOBILE - 404 Error page.pdf](https://github.com/user-attachments/files/17708349/Lighthouse.report.MOBILE.-.404.Error.page.pdf)
  
  ![image](https://github.com/user-attachments/assets/359989e7-56a5-4d43-8539-69161042d383)
    
  - Desktop & Tablet (landscape)
You can access full report: [Lighthouse report DESKTOP - 404 Error page.pdf](https://github.com/user-attachments/files/17708354/Lighthouse.report.DESKTOP.-.404.Error.page.pdf)
  
  ![image](https://github.com/user-attachments/assets/f09847fb-abf3-4c30-b95c-8377f1548eef)
   
</details>
  
<details>
<summary>Click HERE to check the ACCOUNT PAGES Lighthouse Reports</summary> 
  
  As these are django built-in templates which have only been styled using some CSS classes, only one page has been tested, as to reflect their overall performanco"
  - Mobile & Tablet (portrait)
    * You can access full report:  [Lighthouse report MOBILE - login page.pdf](https://github.com/user-attachments/files/17694737/Lighthouse.report.MOBILE.-.login.page.pdf)
  
  ![image](https://github.com/user-attachments/assets/1c823916-db42-4d7c-b188-1bc10ed06e6a)
  
  - Desktop & Tablet (landscape)
    * You can access full report: [Lighthouse report DESKTOP - login page.pdf](https://github.com/user-attachments/files/17694721/Lighthouse.report.DESKTOP.-.login.page.pdf)
    
  ![image](https://github.com/user-attachments/assets/28d14efb-fb13-42a6-ac7e-116b81ae0259)

</details>

  
## CODE VALIDATION
  
### HTML 5
No errors nor warnings have been found when passing [HTML validator](https://validator.w3.org/nu/):  
  
  - **BAG App**
    * ***bag.html***
      
      ![image](https://github.com/user-attachments/assets/af72a27b-5601-46cc-bcb6-e02e9c3b6c51)    
        
  - **CHECKOUT App**
    * ***checkout.html***
      ![image](https://github.com/user-attachments/assets/6f66cdc1-38ae-418c-8edc-c4c4c9c1e983)    

    * ***checkout_success***
      ![image](https://github.com/user-attachments/assets/8b555fae-510d-4a59-8aaf-ed0031ebee6b)    

    * ***order_confirmation_email.html***
      ![image](https://github.com/user-attachments/assets/86a0c277-e202-4ad8-a030-3c79baf28673)    
        
  - **HOME App**
    * ***about.html***
      ![image](https://github.com/user-attachments/assets/b9bfed42-e43d-44f7-9755-b7c29aeb9304)    
      
    * ***companies.html***
      ![image](https://github.com/user-attachments/assets/152ab0a9-5148-4c8f-a509-f001575e1804)    
      
    * ***index.html***
      ![image](https://github.com/user-attachments/assets/d2c97972-9c87-4a75-85ba-c6ae2c39a7fe)    
      
    * ***subscribe_form-html***
      ![image](https://github.com/user-attachments/assets/576eaaf1-7e0f-48bb-b9a6-5c8b6b713331)    
      
  - **INDIVIDUAL SERVICES App**
    * ***add_service.html***
      ![image](https://github.com/user-attachments/assets/e1357e5b-694b-488e-94b7-ebe9771fe159)    

    * ***delete_confirmation.html***
      ![image](https://github.com/user-attachments/assets/7f183237-3a82-4d8c-8dc1-cfdb2abf9caa)    

    * ***edit_service.html***
      ![image](https://github.com/user-attachments/assets/d86814b5-0da8-4a45-aa22-5d1e0f79c622)    
      
    * ***individual_services.html***
    ![image](https://github.com/user-attachments/assets/2fc5efa9-f899-49d5-a853-69abaf217fc0)    

    * ***pack_details.html***    
    ![image](https://github.com/user-attachments/assets/6499d192-04a4-4155-a3bd-c070e00e71f1)    

  - **PROFILES App**
    * ***profiles.html***
      ![image](https://github.com/user-attachments/assets/7bc8145d-2958-4d13-8cb2-ce95692f1128)  

      
### CSS 3
No errors were found when passing the [W3C validator](https://jigsaw.w3.org/css-validator/):    
  
#### Main CSS
This file contains the main CSS of the site. It is in the directory: */static/css/base.css*. [Check the file here](https://english-grows1.s3.eu-west-3.amazonaws.com/static/css/base.css)
  
  ![image](https://github.com/user-attachments/assets/747b3bf3-b11a-4d63-9495-8144057b3888)

#### Profiles CSS
This file contains some CSS specific for the profiles app. It is in the directory: */profiles/static/profiles/css/profiles.css*. [Check the file here](https://english-grows1.s3.eu-west-3.amazonaws.com/static/profiles/css/profiles.css):  
  
  ![image](https://github.com/user-attachments/assets/ecc0fc73-5581-4838-9aba-37f32f70f946)
  
### JS ES6
The validation of the code has been successful. The validator used has been [JShint](https://jshint.com/). In order to remove inaccurate warnings related solely to the fact that it by itself does not support JS ES6, I [found the helpful and easy way](https://teamtreehouse.com/community/why-does-jshint-give-me-these-warnings-about-es6#:~:text=By%20default%2C%20JSHint%20gives%20you%20warnings%20if%20you%20use%20new%20ES6%20features) to make the tool read and analyse the ES6 code effectively, by simply adding this comment to the top of the code:  
```// jshint esversion: 6```  
  
- [**checkout/static/checkout/js/stripe_elementss.js**](https://english-grows1.s3.eu-west-3.amazonaws.com/checkout/js/stripe_elements.js) - Initial errors fixed:
  * JShint was not recognizing $ JQuery, so I click on 'CONFIGURE' at the top, and activate JQuery.
  * JSHint was flagging Stripe as an undefined variable because it didn't know that Stripe is defined in the Stripe.js library, which is loaded externally. To fix this in JSHint, I declared Stripe as a global variable by adding a JSHint directive at the top of the file. This way, JSHint understands that Stripe is expected to be available globally:
    ```/* global Stripe */```
  
  ![image](https://github.com/user-attachments/assets/0db221e6-19bc-4bdc-856b-e7c60ae38f9a)

- [**static/js/quantity_selector.js**](https://english-grows1.s3.eu-west-3.amazonaws.com/js/quantity_selector.js) - No errors found:  
  
  ![image](https://github.com/user-attachments/assets/a3eae4bd-9b32-4a9d-9f03-b972b11a1934)
   

### PYTHON 3.12
**Validation has been done using [CI Python Linter by Code Institute](https://pep8ci.herokuapp.com/), and the results have been the following:**  

#### BAG APP
  * contexts.py - No errors found:
    
    ![image](https://github.com/user-attachments/assets/a1c7e008-f1b0-41e8-bec5-551d2115f27b)
    
  * views.py - 
    
     ![image](https://github.com/user-attachments/assets/2cf5b3d1-6255-4bd5-9e2a-dd45b5dd66b2)
    
#### CHECKOUT APP
  * admin.py
    
    ![image](https://github.com/user-attachments/assets/fe158cab-bf16-4eee-abbf-63d702a5e51e)
        
  * forms.py
    
     ![image](https://github.com/user-attachments/assets/6b498a0c-9c0a-4e3a-bd19-b99d051c1f16)
    
  * models.py - The only line that is too long, is due to the unability to separate the operation in two lines

     ![image](https://github.com/user-attachments/assets/d007159f-2697-4ac9-9d76-5235dc09ada8)
    
  * views.py
    
     ![image](https://github.com/user-attachments/assets/a2e4ba93-fd8e-4b22-9737-b939b198bc14)
    
#### ENGLISH GROWS PROJECT
  * settings.py
    
     ![image](https://github.com/user-attachments/assets/f916b47a-7065-4f08-96e8-0afa1e0e5f50)
    
#### HOME APP
  * admin.py

    ![image](https://github.com/user-attachments/assets/899c3a0b-a425-47d3-81bb-7c69b8cdd8f0)
    
    
  * forms.py
    
     ![image](https://github.com/user-attachments/assets/d801c609-2bbb-4b21-8d8a-66c702707ce2)
    
           
  * models.py
    
     ![image](https://github.com/user-attachments/assets/ca2edfe6-f30c-456b-a6ed-38dd92fdfedb)
    
    
  * utils.py
    
    ![image](https://github.com/user-attachments/assets/c1ee2afa-ac8f-4d12-a05a-c3cbda2bf50a)
  
              
  * views.py
    
    ![image](https://github.com/user-attachments/assets/240d9e03-108b-4048-8e6b-a216d1be95ad)
    
      
#### INDIVIDUAL SERVICES APP
  * admin.py
  
    ![image](https://github.com/user-attachments/assets/92174d30-15f8-4d23-a6dc-05141e46f98b)
  
  * forms.py
    
    ![image](https://github.com/user-attachments/assets/72d641bb-e218-46a6-9404-7e77002eb237)
    
  * models.py
    
    ![image](https://github.com/user-attachments/assets/32265043-49a6-4889-a10a-05498994477c)
    
  * views.py
  
    ![image](https://github.com/user-attachments/assets/9284aa0d-8c59-4dbc-96e3-5b6b6cf625a3)
  
       
#### PROFILES APP
  * admin.py
  
    ![image](https://github.com/user-attachments/assets/a1de9736-cd86-45f1-b819-46dd49a28860)
  
  * forms.py
    
    ![image](https://github.com/user-attachments/assets/bc74c7fc-dae1-457d-b82e-91f4bfe20c2b)
    
  * models.py
    
     ![image](https://github.com/user-attachments/assets/8c68a1bd-8ab9-47ad-9acf-6c4b26c85712)
    
  * views.py
    
     ![image](https://github.com/user-attachments/assets/de0f810e-84ad-4586-8d88-31a84d3eb2ae)

      
## ACCESSIBILITY TESTING
This site has been tested to be ADA compliant, and has achieved **WCAG 2.1 validation**. Find below the contrast audits from ***Juicy Studio*** website and the general accessibility reports generated by ***EqualWeb Accessibility Checker*** Chrome extension, which have all achieved positive results. 
  
### CONTRAST VALIDATION REPORTS
Font and backgroud colors have passed at AAA and AA levels, as can be seen in the following reports that have been generated by [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php):  
  
  ![image](https://github.com/user-attachments/assets/4d7ec2f4-1ef4-4814-b928-761bf5f6d374) ![image](https://github.com/user-attachments/assets/0502fbeb-d05e-4e57-843e-e883d2786fce)  
  
  
### GENERAL WCAG 2.1 REPORT
This website is compliant with all international standards, as proved after ***EqualWeb Accessibility Checker*** scan of the site, which gave no errors:  
  
  ![image](https://github.com/user-attachments/assets/c2345929-ca26-4995-a2b9-3fc32b71d119)
    
## MANUAL TESTING
Manual testing of the site has been performed following the user's stories:
  
- [X] 1. **Check the social media links to see the site's social media profile**:
      [Check Facebook profile](https://www.facebook.com/people/English-Grows/61561504216913/)

  ![image](https://github.com/user-attachments/assets/f00aab74-e73c-4c4a-acdf-5e310a123e8c)

- [X] 2. **Check the about page**
  
  https://github.com/user-attachments/assets/e8feecd2-bda6-44d9-828e-4a4ab6dba8da
    
- [X] 3. **See at first glance the part of the site that is specially dedicated to me (B2B or B2C)**

  ![image](https://github.com/user-attachments/assets/25e596c0-b804-439b-93b4-3a7db8906a32)

- [X] 4. **Users can subscribe to the newsletter**
      - Users can register to the newsletter via the form, and get success message:
  
    https://github.com/user-attachments/assets/1dcfb229-a354-4ae6-b03a-7bc1b8fc3918
      - ***Admin user can perform CRUD functionality on subscribers via the admin panel***:
    
    https://github.com/user-attachments/assets/f1ed2455-708a-442f-834e-7fc76ad79554
    
    
### CONTACT FORM (B2B customers)
- [X] 5. **B2B can contact the site to receive a customized training plan**.

  https://github.com/user-attachments/assets/e203231d-416a-48f2-ae6e-bd445409c255

  
### VIEW AND SORT SERVICES
  
- [X] 6. **All available services are listed**
  
  https://github.com/user-attachments/assets/fdd602da-0263-4d3e-9783-050ddd8607c2
        
- [X] 7. **View specific type of service**
  
  https://github.com/user-attachments/assets/60b8cf12-8fc6-4cbd-9fc0-bf22cc73700f
      
- [X] 8. **View individual service details**
  
  https://github.com/user-attachments/assets/7899e77f-0e75-4f2d-baf4-3eaa44a5ee57
      
- [X] 9. **view the total of my pending purchase at any time**
  
  https://github.com/user-attachments/assets/3ca7b314-2375-428f-bf65-e1d390d48025
  
- [X] 10. **sort the full list of available services ***by categories (types)*** or ***by price*****
      
  * ***By Types***:  
    
    https://github.com/user-attachments/assets/35f2ce28-7356-4233-b839-b18f61fc66c5
    
  * ***By price***:
    
    https://github.com/user-attachments/assets/17f2d278-6e01-40f4-9bd7-c4418695c0b3
        
- [X] 11. **sort specific category of services *by price*, or *alphabetically***
  
    https://github.com/user-attachments/assets/714e410d-55d2-45ea-9bd3-1cfea9a64e63
  
  
### ACCOUNT - USER AUTHENTICATION
- [X] 12. **Register for an account**, and **receive an email confirmation** after registering.
  * Once a new user is registered, its data is automatically stored in the database.
    
    https://github.com/user-attachments/assets/386b7ac4-0856-4a36-b26c-872b15fd74ae
    
  * User receives verification email  
       
    ![image](https://github.com/user-attachments/assets/71fea570-d858-4a0d-978d-28a19945e781)
    
  * Verification url in email works as expected, and once user clicks on 'verify', he is redirected to home page, already logged in:   
    
    https://github.com/user-attachments/assets/803fe5ce-6cb5-42fe-946c-582734f2064c
    
- [X] 13. **Easily login and logout**.
    
    https://github.com/user-attachments/assets/c35028e9-868c-455e-9d6f-f880d6a7e611
        
- [X] 14. **Easily recover user password**:
    * After user clicks on 'forgotten password", user inputs the account email and confirmation message is displayed
    * User receives an email with link to restore password     
    * Link to restore password works as expected  
    
    https://github.com/user-attachments/assets/1f96dfc6-27cd-4202-a3b7-3394d4d988d7
         
- [X] 15. **Have a personalized user profile**:  
  
  ![image](https://github.com/user-attachments/assets/359d6421-941e-4ef2-bfe6-e7ba3243d3ff)
  
- [X] 16. **Update and save my personal account information on my user profile**:  
  
  https://github.com/user-attachments/assets/5e701fe1-f151-472b-991e-be666ad0d15e
    
- [X] 17. **Access my bag, and update or delete any items in it**:
  
  https://github.com/user-attachments/assets/1a2f3d9d-1068-471f-87e6-bd876d82900c
    
- [X] 18. **Users' personal data is secured**: No one else can access a user's profile, nor order urls, which also contain personal data:
  
  https://github.com/user-attachments/assets/6a691416-ecde-4719-a3df-d81dc41f77e7
    
- [X] 19. **ONLINE PAYMENT - STRIPE API** - Users can make secure online payments
      * **User can easily access the checkout page and proceed to checkout** *(video below)*
      * **Stripe API works as expected and payment intent is successfully reflected on Stripe API, without any errors** *(video below)*   
      * **User views an order confirmation message and order details on the screen**
      ![image](https://github.com/user-attachments/assets/333f2309-98d1-4d95-818d-7035faa56a77)

https://github.com/user-attachments/assets/7cb762e4-d078-4aab-9eec-7a2e210c844b
    

- [X] 20. **Receive a confirmation email after a purchase, with details of the order**:
  
  https://github.com/user-attachments/assets/8b745505-3301-40fa-a746-bdab04d73abe
    
- [x] 21. **View past orders, and read their full information on the user's personal profile**:
  
  https://github.com/user-attachments/assets/76f75603-112f-42c5-bb5a-c5d2936be615

- [X] 22. **See success or error messages for every action undertaken***:
  
### ADMIN 
- [X] 23. **Sort orders by users (by profiles)**:
  
  https://github.com/user-attachments/assets/e8786ea1-12e5-4c27-a1b7-5985f6a7ddb3
  
- [X] 24. **Order is automatically linked to the authenticated user** who made it:

  ![image](https://github.com/user-attachments/assets/536a66bb-fae0-41bf-916b-c029261b1f39)
  
- [x] 25. **User's email is stored in a separate email list**, to easen up future **emailing campaigns**.
  
  ![image](https://github.com/user-attachments/assets/0f59e72b-054d-43a2-a5d3-5fcf2b3c8b6f)
    
- [X] 26. **Store data in admin from B2B contact requests**:

  ![image](https://github.com/user-attachments/assets/b65e47d7-bea6-4a02-b88b-873bbc33e11a)

  
- [X] 27. **Edit and delete existing services directly from the site**, without having to access the lesser user-friendly admin panel.
  
  https://github.com/user-attachments/assets/93e2744f-ae24-4779-a48b-deb5dfb6f039
  
- [X] 28. **Add service directly directly from the site**
  
  https://github.com/user-attachments/assets/bce43c89-e04b-4024-b9bd-1687f4fd18f6
      
- [X] 29. **Only authenticated users can make an order**, so that personal data from all users is protected. 
  
  https://github.com/user-attachments/assets/fbb0422c-48af-4d08-a3fd-0c7c9b34931d


### MARKETING STRATEGIES
#### SUBSCRIPTION to NEWSLETTER  
All the functionalities described below related to marketing have been tested, and work as expected, summing up to the facebook profile page created, to improve social media presence of the brand, as part of the marketing campaign (num. Please refer to the video below num. 32 which includes the three features testing: 
- [X] 30. **create editable email templates for the newsletter or emailing campaigns (Marketing campaigns).**
- [X] 31. **send marketing campaigns to subscribed users.**
- [X] 32. **send a newsletter to users that are subscribed.**
  
  https://github.com/user-attachments/assets/0faa4b3a-89f6-4b62-87c9-9f1c085f4d33  

  ![image](https://github.com/user-attachments/assets/6072cb60-adad-4490-98c0-08f229639044)

  ![image](https://github.com/user-attachments/assets/e013ca55-d82b-4f46-9dbe-591b2a8143cb)

  **PROOF of EMAILING CAMPAIGN FUNCTIONING: One subscription was made using test@test.co email (does not exist), and when sending campaign to all subscribers, I receive an error email informing that email could not be delivered to inexistent email test@test.co:

  ![image](https://github.com/user-attachments/assets/975f0be1-331a-43c7-ba2f-153a70f4cd44)

  
### INDIVIDUAL SERVICE - CRUD Full Functionality
    
#### Create Service
- The Admin user can easily create a service directly through the admin, with no need to upload fixtures, as initially.
- Only authorized users can add/update/delete service.
  
  https://github.com/user-attachments/assets/55f780fb-778c-4d62-b354-0d0dd5bb3d81
  
#### Read Service
- Services created can be **Read**, or viewed:  
  
  https://github.com/user-attachments/assets/298dd3fe-2ec1-4745-9c94-021c244506d7
    
#### Update Service
Admin users can **Update** a service directly through the site, without need to access the admin panel, for a better UX. This can be done on the general services page, or on the service details page, both with a success message to inform user of the action completed:  
  
  https://github.com/user-attachments/assets/e8e13700-7d55-4a26-8ec4-03d31c0a9f20
    
#### Delete Service
Admin users can **Delete** a service, with confirmation step, and success message:  
  
  https://github.com/user-attachments/assets/b2efff85-51fb-46c8-a5c3-9689b65c14b4  

  
### MARKETING STRATEGIES
#### SUBSCRIPTION to NEWSLETTER  
All the functionalities described below reñlated to marketing have been tested, and work as expected, summing up to num. 1 story, which allows users to chceck social media profile at FB, as part of the marketing techniques. Please refer to the video below num. 29 which includes the three features testing: 
- [X] 27. **create editable email templates for the newsletter or emailing campaigns (Marketing campaigns).**
- [X] 28. **send marketing campaigns to subscribed users.**
- [X] 29. **send a newsletter to users that are subscribed.**

  
  
# TECHNOLOGIES USED
  
## LANGUAGES
- **Python 3.12**
- **JS ES6**
- **CSS3**
- **HTML5**
  
  
## FRAMEWORKS, LIBRARIES AND PROGRAMS USED
The following have been used for the development of this site:  
  - **Django 5.1** - Whithin django framework, many libraries and modules have been used. For mode details on these, please refer to *requirements.py* on the root directory. - Check [Django 5.1 Documentation](https://docs.djangoproject.com/en/5.1/)
  - Chrome Dev Tools - To inspect the elements, and be able to spot what element was having an unexpected behaviour, and correct it more efficiently. Also have used **_Lighthouse_** tool's reports to check and improve core web vitals.
  - [Github](https://github.com) - To deploy the code in order to be accessed by Heroku.
  - [Heroku](https://heroku.com) - To deploy this python site.
  - [PostgreSQL](https://www.postgresql.org) - A database has been created through Code Institute handy link, to store all the site's data, such as user personal data, order details, available services, users' contact requests, and more.
  - [AWS](https://aws.amazon.com/) - Amazon Web Services have been used to create an ***s3 bucket*** to store all media and static files of this site.
  - **Bootstrap 5** - Check documentation [here](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - **Django Summernote** - To enable the site owner to easily create an email template to launch an email marketing campaign to subscribers, or a newsletter. Documentation can be found [here](https://github.com/lqez/django-summernote/blob/main/README.md)
  - [Favicon](https://favicon.io/) - To create the necessary files for the logo to be on the upper part of the browser tab next to the site tir.
  - [Font Awesome](https://fontawesome.com/) - For the icons used
  - [Google Fonts](https://fonts.google.com/) - To select fonts and implement them in the site
  - [Github](https://github.com) - To deploy the site online, and Github desktop app to link _Visual Studio Code_ to Github.com
  - [Coolors](https://coolors.co) - To insert colors selected previously directly through visual studio code, but used this tool to display the palette beautifully, and insert it in this readme file.
  - [Amiresponsive](https://ui.dev/amiresponsive) - To display the site in all types of devices simultaneously.
  - [EqualWeb Accessibility Checker](https://chrome.google.com/webstore/detail/equalweb-accessibility-ch/imemciokfejbnonkkinhcdfigdilcllg/related?utm_source=chrome-ntp-icon) - Google Chrome extension to check general errors and contract errors for optimal accessibility.
  - [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php) tool to generate accessibility reports related to contrast, following the **WCAG 2.0**'s luminosity contrast algorithm.
  - [Blisk](https://blisk.io/devices) to check the viewport of multiple devices, very useful for selecting testing targets.
  - [Viewport Sizer](https://viewportsizer.com/devices/) - Used to check the viewport of multiple devices, very useful for selecting testing targets.
  - [BrowserStack](browserstack.com) to test responsiveness by emulating different devices, operating systems and browser vendors.
  - [XRecorder](https://videoeditor-videorecorder-screenrecorder.en.uptodown.com/android) for Android, to record the compatibility and responsiveness testing performed on real Android device.
  - [Google Gmail](https://support.google.com/mail/answer/56256?hl=en#:~:text=Gmail-,Create%20a%20Gmail%20account,-To%20sign%20up): Used as email provider to send  emails to users and customers, also via *smtp*.  
  - [Word Tracker](https://www.wordtracker.com/) - To track the best keywords to include for SEO improved ranking.
  - [XML sitemaps](ml-sitemaps.com) - To generate the sitemap.xml file for this site



    
# DEPLOYMENT
## VERSION CONTROL
The site was created using Gitpod editor and pushed to Github to the remote repository **‘english-grows**.  
The following git commands were given to the terminal throughout development to push updated code to the remote repo on Github:
1. ```git add .``` - Command to add the updated file(s) to the staging area before they are committed to the *main branch*, represented by a '**.**'.
2. ```git commit -m “commit text”``` - Command to commit changes to the local repository queue ready for the final push.
3. ```git push``` - Command to push all updated code to the remote repository on Github.
4. ```python3 manage.py runserver``` - Command to run **python** app on local server.

### REQUIREMENTS
- Make sure all the modules and requirements have been correctly installed by:
    * Install the necessary modules with command:
      ```pip3 install module```
    * Make sure you install versions that are compatible, to avoid system issues. Check the requirements file in this repository for surther reference, and type the command on the terminal:
      ```pip3 install -r requirements.txt```
  
### SECRETS
**WARNING - DATA PROTECTION** To avoid pushing sensible credentials stores in variables (e.g.: DATABASE_URL, SECRET_KEY) to Github:
1. Create an ***env.py*** file on the main directory of the app.
2. Ensure that env.py is included in the ***.gitignore*** file.
3. To include secret variables on the env.py file:
   - (i) On the top of the file, include the imports:
   -```import os
       from pathlib import Path```
   - (ii) Include eac hsecret var following this example:
   - ```os.environ.setdefault('DATABASE_URL', 'your-data-base-url')```
   - (iii) Import Operational System to your ***settings.py***, so it can access the system variables secretly stored in your env.py file:
   - ```import os```
   - (iv) To access the system variables in your settings.py file, use the following method to store them in other safe variables:
   - ```DATABASE_URL = os.environ.get("DATABASE_URL")```
4. BEFORE COMMITTING TO GITHUB:
   - On the terminal, type ```git add .```, then ```git status``` and make sure the env.py file is not in the list. Once you are reassured that it is not in the list of files to be committed, safely commit.

## HEROKU
### App Preparation
1. Create and add the **'Procfile'** to the root directory of the app, and include ```web: gunicorn candlelight.wsgi --log-file -```  Heroku relies on this file to determine how to run your application, ensuring the correct setup of your web server. Use commands like ```web: gunicorn PROJECT_NAME.wsgi``` in the 'Procfile' to instruct Heroku on starting your web server with Gunicorn.
2. If you haven't done so yet, create a ***requirements.txt*** file to store necessary modules and libraries:
   - ```pip3 install -r requirements.txt```
3. Ensure you have updated the ***requirements.txt*** file listing all project dependencies. The comnmand to update the file is ```pip3 freeze > requirements.txt```
4. Set up necessary **configuration variables** in Heroku ***setting tab > Config Vars*** *(eg. SECRET_KEY, DATABASE_URL, etc.)*.
5. Add Heroku to your ALLOWED_HOSTS in your app's *'settings.py'* file: ```candlelight-worlds.herokuapp.com```.

   
### Create Heroku App
1. Sign up to an account on [Heroku](https://heroku.com)
2. Create new app. Remember that app name must be unique on the whole of Heroku site.
3. Store all the secret environment variables (secret keys) on **settings** > **Config Vars**.
  
   
### Deployment Method
1. Ensure that in your **settings.py**, ```DEBUG = False``` before doing the last commit to Github before deploying to Heroku.
2. **On Heroku**, click the **deploy** tab on the top navigation bar.
3. Scroll down and select Github as 'Deployment method'
4. Use the github link and type in the name of your repository
5. Scroll down, to **'Manual Deploy'** configuration and select ***main*** on the dropdown for the ***branch the deploy***
6. Then click on **deploy from branch**
7. Once the app is loaded, click on the 'View' button that appears only then.
8. Once your application is running, you can switch to **Automatic Deploys** so that any changes in the repositori are automatically reflected in Heroku deployed app.  
  
  
   
# CREDITS & ACKNOWEDGEMENTS
## Images
- All the images are free copyright, and have been taken from [Pexels.com]
- The logo had previously been created by the creator of this site with the free version of [Canva](www.canva.com) for her personal freelance website as a certified teacher of English as a second language.

## Acknowledgements
- Some nice tutors and mentor [Rory Patrick Sheridan](https://github.com/Ri-Dearg) at Code Institute for their patience and useful insights.
- I have searched thorough [Bootstrap 4 documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/).
- I have searched thorough [Django 5.1 documentation](https://docs.djangoproject.com/en/5.1/).
- I have searched Stackoverflow, Youtube, W3School, Geeksforgeeks among other sites when encountering issues or knowledge blockers.
- I have found inspiration and revieved material from Code Institute Full Stack Web development course.
- I have searched throughout [Google Developers documentation](https://developers.google.com)
- I have read [how to make links crawlable](https://developers.google.com/search/docs/crawling-indexing/links-crawlable?visit_id=638668769044808898-1063643142&rd=1) on Google Developers documentation to improve SEO.
- I have read on how to [make select element accessible](https://dequeuniversity.com/rules/axe/4.10/select-name) article from [Deke University](https://dequeuniversity.com/) to improve accessibility.
- I have read about [ARIA searchbox role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/searchbox_role) in *Developer Mozilla* to make search bar accessible to screen readers, and improve accessibility.
- I have read on how to [include discernible text in links](https://dequeuniversity.com/rules/axe/4.10/link-name) article from [Deke University](https://dequeuniversity.com/) to improve accessibility.
- I have read this article about [robots.txt](https://developer.chrome.com/docs/lighthouse/seo/invalid-robots-txt/?utm_source=lighthouse&utm_medium=devtools) on *Chrome for Developers*, to fix invalid text and improve SEO.
- I have read on [aria-labels for buttons](https://dequeuniversity.com/rules/axe/4.10/label) article from [Deke University](https://dequeuniversity.com/) to improve accessibility.



