# Dev_Connect

### TrelloBoard

### Description

This social/work app allows developers to connect and collaborate with other developers on projects. Each developer has a brief profile with a photo, their project description/link and what they are looking for example a back-end developer might be looking for a front-end developer to finish their project to be ready to launch. Developers can then message other developers to organise collaboration. 

This app is an extension of LinkedIn, a career app designed to connect those seeking work with employers, fellow work colleagues and industry professionals. Dev-Connect as an extension will allow a connection of developers to start working on projects together through LinkedIn networks.

### Instructions
**Install python 3.9**
$ apt-get install python3.9

**Clone repository**
$ git clone https://github.com/Karen-Stewart80/Dev_Connect.git

**Change directory into app**
$ cd Dev_Connect

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

email: test0@test.com
password: 123456

Copy the JWT token generated and perform actions. This is the admin user able to perform admin rights in the database dump end points. Faker and random generated data is used in the database.


### CICD pipeline
Code will be pushed to Github repository. Unittest will run tests.


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





 
