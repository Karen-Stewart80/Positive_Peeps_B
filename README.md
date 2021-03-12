# Positive Peeps

### TrelloBoard

### Description

Positive Peeps is a social app that allows users to connect with each other. The problem with most social apps is the amount of trolling, negative comments and bullying that goes on between users. To solve this issue, I've created Positive Peeps, which users pledge to only create positive posts abstain from negative interactions. Allowing users to be a part of an uplifting community without the fear of harassment and negative judgement. For this reason the initial application will not have profile images, the option to delete or change/update profiles or the option of sending messages. This way the initial version is a higher level of protection from insensitive messages or images or people changing their profile after posting something unsavoury, so there is accountability. Posts can be deleted though. The 2.0 version in the future will offer those options for those wanting a less restrictive service. 

### Instructions
**Install python 3.9**
$ apt-get install python3.9

**Clone repository**
$ git clone https://github.com/Karen-Stewart80/Positive_Peeps_B.git

**Change directory into app**
$ cd Positive-Peeps

**Install venv**
$ pip install venv

**Create virtual environment**
$ python3.9 -m venv venv

**Activate virtual environment**
$source venv/bin/activate

**Install dependencies**
$ pip install -r requirements.txt

**Run app**
$ python src/main.py

**Set Flask variables**
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run

**Testing end points**

to perform tests

cd into src folder
cd src


in terminal
set environment
export FLASK_ENV=testing

python -m unittest discover tests/

### How to use website

Step 1 - enter positive-peeps.tk in web browser
Step 2 - Press sign up button. Enter email and password and click sign up button
Step 3 - Press log in button. Enter email and password (the same used to sign up) and click log in button
Step 4 - Press Create a new Profile button. Enter username, first name and last name and click create profile
Step 5 - Press Create a new Post button. Enter name of Post and enter your post and click create post button

There are options to go back or cancel if needed. You must have a profile to create a post.




### CICD pipeline
Code will be pushed to Github repository and use git-hub actions.. Unittest will run tests.
Continuous-integration yaml runs the tests, and then does a fresh install of the application onto an ec2 instance with gunicorn running as a background system. With a script installed to copy the env file from an s3 bucket. Route 53 handling the routing of the webpage, nginix running as a web server and have an ssl cert


#### Purpose

The purpose of Positive Peeps is to create a social website that has a positive impact on it's users. Cyber bullying has had a detrimental impact on mental health, whether it be body-shaming or ridiculing or just making people feel like they aren't enough. Positive Peeps aims to create a welcoming, positive social community. People can  create  their own profile and create positive vibe posts. This allows members of all ages to feel safe online while still being able to be social.

#### Functionality/features

An interactive website 
A simple profile and post social media application
Email and password registration and signing in
Positive attitude and behaviour pledge when joining
Profile details read and create 
Posts create, read and delete
Logout feature when not in use

#### Target Audience

Positive Peeps website is targeted at users of all ages who wish to be social online away from negativity, bullying and online trolls. This includes people from a diverse range of backgrounds. For example people from all different ethnicities, sexual orientation, religious beliefs and education. Both adults and children. Everyone that wants to be a part of a positive and inclusive environment.

### Tech Stack


sql alchemy is the ORM
marshmallow is the serializer,
gunicorn is the application server
nginix is the web server
github for source control
github-actions for CI/CD
flask for the backend framwork

Front-end Technologies: HTML5, CSS, Python
Backend Technologies: Python
Backend Frameworks: Marshmallow, Jinja, Flask 
Database and Access Library: PostgreSQL
Deployment: AWS EC2 S3


### Wireframes

The wireframes are of the future 2.0 version of the app, that also include this current lite versions features of posts, profiles, login and sign up.


![Landing Page](docs/wireframes/Landing_wireframe.png)
![Profile Page](docs/wireframes/Profile_wireframe.png)
![Posts Page](docs/wireframes/Posts_wireframe.png)
![Friends Page](docs/wireframes/Friends_wireframe.png)
![Messages Page](docs/wireframes/Messages_wireframe.png)

### Application Architecture

Two diagrams showing the Application Architecture for the Application Positive Peeps 
This diagram shows the front end technologies in the blue box, which are HTML and CSS. It communicates with the backend in the purple box using Jinja, Flask Server  and Marshmellow. This communicates with the Database in the green box using postgreSQL.
![App Architecture](docs/app_architecture_diagram.pdf)

This diagram shows the Application AWS architecture
The user sees the frontend and it communicates with the backend that is stored in the AWS Cloud within the Availability Region and in a Virtual Private Cloud. It is in an EC2 instance so that it may expand with demand.
![AWS Architecture](docs/aws_architecture.pdf) 

### Data Flow Diagram

The Data Flow Diagram is for the Application Positive Peeps future 2.0 version, that also includes the features of this lite version which includes the features of post, profile, signup and login. 

It demonstrates the flow of data from the External Entity, the user, throughout the application. From the User, it shows the Processes Create, Update/Add, Read and Delete for the Profiles, Messages, Friends and Posts all which have their data in their own tables. Arrows show the direction of data flow. Yellow circles are for CRUD process, pink rectangles are for data stores and the green large rectangle is for the user/external entity.

![Data Flow Diagram](docs/data_flow_diagram.pdf) 

### User Personas and user stories

3 Personas of people of our target audience, those wanting positive company online in a safe environment.

![User Personas](docs/user_personas.pdf)

Trello user stories
Screenshots of User stories of what a user wants from the Positive Peep Application. Including login features with email and password, to add and delete friends, messages and posts.etc.

![User Stories1](docs/trello_user_stories/user_story1.png)
![User Stories2](docs/trello_user_stories/user_story2.png)
![User Stories3](docs/trello_user_stories/user_story3.png)
![User Stories4](docs/trello_user_stories/user_story4.png)
![User Stories5](docs/trello_user_stories/user_story5.png)

### Task Management with Trello

List of tasks for T4A2- A and the start of tasks for the upcoming assignment T4A2 -B

![Task1](docs/trello_tasks/task1.png)
![Task2](docs/trello_tasks/task2.png)
![Task3](docs/trello_tasks/task3.png)
![Task4](docs/trello_tasks/task4.png)
![Task5](docs/trello_tasks/task5.png)
![Task6](docs/trello_tasks/task6.png)
![Task7](docs/trello_tasks/task7.png)
![Task8](docs/trello_tasks/task8.png)
![Task9](docs/trello_tasks/task9.png)
![Task10](docs/trello_tasks/task10.png)
![Task11](docs/trello_tasks/task11.png)
![Task12](docs/trello_tasks/task12.png)
![Task13](docs/trello_tasks/task13.png)
![Task14](docs/trello_tasks/task14.png)
![Task15](docs/trello_tasks/task15.png)
![Task16](docs/trello_tasks/task16.png)
![Task17](docs/trello_tasks/task17.png)
![Task18](docs/trello_tasks/task18.png)
![Task19](docs/trello_tasks/task19.png)
![Task20](docs/trello_tasks/task20.png)

### Task Delegation

Tasks have been divided into teams. Project management for the running and organisation of the project, Front end Developers for the User interface and wireframes and Htmls, Backend developers for the framework and function coding of the app, DevOps for the CICD pipeline, yaml file, github actions, AWS services such as EC2, S3 and route 53. See following delegation boards:

![Taskdel1](docs/task_delegation/taskdel.1.png)
![Taskdel2](docs/task_delegation/taskdel.2.png)
![Taskdel3](docs/task_delegation/taskdel.3.png)
![Taskdel4](docs/task_delegation/taskdel.4.png)


### Manual Testing

The following are images of the manual testing of the application performed by developers and other users. These were carried out during production and deployment of the application

![Test1](docs/manual_testing/manual_testing.1.png)
![Test2](docs/manual_testing/manual_testing.2.png)
![Features](docs/manual_testing/features.png)



### Handling the privacy of user data and security features

Hashing passwords makes system breaches and attacks less successful. Passwords will be hashed to make hacking more complicated and time consuming for the attacker and provide more security for the user.

Amazon Web Services (AWS)offer secure services to store and run data. Running flask on an EC2 server will allow access to the database stored on AWS Virtual Private Cloud. This adds security and ensures only those with permissions can access the database through the NAT gateway. 

Nginx, a secure webserver utilising HTTPS ensuring connection is secure and to make sure that data is encrypted and protected while transferring TLS is used.

Time sensitive JSON Web Tokens(JWT)are used for performing actions and logging in.

Object Relations-Mappers(ORM) ensures user input is sanitized and checked, before storing it in the database and helps prevent accidental or malicious code injection. Utilising datatypes and having specific field requirements not only ensures that data is inputted correctly but also provides protection against opportunist attacks. 


### Professional, ethical and legal obligations as a developer

Professional obligations - Clarifying the requirements for the project, developing a realistic project time line and comprehensive task list is imperative to project success. Trello board will assist in outlining the comprehensive tasks with a 'to do', 'doing' and 'completed' task table. Checkpoints will be given so that tasks will be completed on time and as reminder to use testing and deployment of the project using continuous integration and continuous deployment. This ensures testing and maintenance is regularly done and allows bugs to be eliminated during the project development process. CICD pipeline allows developers to continually develop, test and deploy improvements.

Ethical obligations - The project stores sensitive user data and images, and therefore will be protected in private secure servers. User's information and images will also only be utilised for the purpose of the app and not be accessed, given or sold to other individuals or organisations. There will also be a User Terms and Conditions document, ensuring users abide by these and other conditions, such as ensuring messaging between developers is only for the purpose described and no inappropriate, sexual, drug or offensive material is to put on profiles, posts or messages. Support for users will be available to ensure any breaches of conditions are handled promptly and should a user or support, delete or modify their profile or post, it will be permanently deleted.

Legal obligations - The project will be subject to a confidentiality agreement so those funding the project and developers are protected from others taking or copying the project. 
Ensure there is mockup/wireframe of project and functionality, as evidence of idea and proving ownership to protect from Copyright laws.
An App Developer Contract will be used to show ownership of the app, timeline, expectations and costs.
Protecting the app IP with trademark registration to have formal Intellectual Property protection.
A Privacy Policy will ensure private information, given in confidence will be protected and outline responsibilities for the protection of that information.
The Terms and Conditions policy will ensure users must abide by ethical terms as described above, as well as other conditions in order to use the app.





 
