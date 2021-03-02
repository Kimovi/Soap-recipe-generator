# Soap recipe generator
Calling for all soapers! Do not struggle with your soap recipe anymore! Just refresh the page and it will generate a random soap recipe for you. How to use it? simple, just refresh the page.

<img width="1280" alt="front_page" src="https://user-images.githubusercontent.com/59723479/109577020-ca4f5780-7aec-11eb-9f74-2a705a7efa9f.png">

# Intro
This time, I had a chance to try something new. The project subject was to create 3 APIs which generate random data and render it on the frontend. 
I'm a soaper and produce homemade soap from time to time, and I thought it would be nice to have a recipe generator. 
This application works very simply, Just hit refresh and it will generate a new recipe each time. 
I have build 3 APIs with Python, then rendered the frontend with Python, Flask, and Jinja. There are 4 VM instances used for Jenkins, Load balancer(Nginx), Docker swarm manager, and worker. 

- Trello Board
- Google Cloud Platform for VM instances
- SQL Database on GCP
- Python and Flask programming + Jinja2 for HTML rendering
- Unit testing with Pytest
- Git for version control
- Nginx for the Load balancer
- Jenkins server (pipeline)
- Ansible
- Docker Compose and Swarm
- ERD 
- Risk Assessment


Frontend page is handling API calls in between all 3 backend services and also store the generated data to MySQL DB. I have set up Nginx instance for users to access application through reverse proxy.
<img width="689" alt="Frontend" src="https://user-images.githubusercontent.com/59723479/109579641-30d67480-7af1-11eb-9db3-39978d8f9130.png">


# Trello board
This project required lots of tools and work. I was swamped with the amount of the stuff I had to manage and came up with a Trello board to organize the tasks. 
<img width="1280" alt="trello_board" src="https://user-images.githubusercontent.com/59723479/109577038-cd4a4800-7aec-11eb-83b8-a02bcdd60aaf.png">

This is my Trello board at the end of the project. 

# ERD
Below is an entity diagram design for this project. 
As a nature of the project, I only needed a simple DB structure where I could store 4 fields of data.
<img width="690" alt="ERD" src="https://user-images.githubusercontent.com/59723479/109577016-c91e2a80-7aec-11eb-9aac-e45dcef9ecc9.png">

I have used GCP SQL manager this time rather than setting one on my own on a VM instance. 

# GCP VM instances
I have used 4 instances for this project, 'project' instance for Docker swarm manager node, 'swarm-worker' for swarm worker node, 'nginx' for load balancer instance and 'jenkins' for CI server pipeline and Ansible. 
<img width="875" alt="GCP instance" src="https://user-images.githubusercontent.com/59723479/109577025-cb808480-7aec-11eb-94a4-e6fa24270b49.png">

# Docker swarm
Without using Ansible, I had tested Swarm manager node and Swarm worker node to ensure they are up and running. 

# Unit testing
After building up the APIs and connect my application to the SQL database, I ran the unit test with Pytest as my code was written in Python. The purpose of the test was to ensure API applications are working without an error.
<img width="899" alt="Pytest_service1" src="https://user-images.githubusercontent.com/59723479/109577031-cc191b00-7aec-11eb-86ca-63f2d8f6049e.png">
<img width="748" alt="Pytest_service2" src="https://user-images.githubusercontent.com/59723479/109577033-ccb1b180-7aec-11eb-8f15-b6c3c70bbb9d.png">
<img width="748" alt="Pytest_service3" src="https://user-images.githubusercontent.com/59723479/109577035-cd4a4800-7aec-11eb-976b-a5ae185c826c.png">
<img width="748" alt="Pytest_service4" src="https://user-images.githubusercontent.com/59723479/109577036-cd4a4800-7aec-11eb-9222-7d98ea6e2811.png">

3 out of 4 applications had 100% of the pass result, however, Service1 (frontend) hadn't passed the test as it had a DB connection issue which is one of the ongoing issues. 

For service2 & service3, I have tested APIs are giving the correct data listed. and for service4, I have tested whether it was giving the correct data depending on service2's outcome. I have tested several times to ensure all 3 services for the test consistency.

# Load balancer
# Ansible
Ok, Let's talk about Ansible which I struggled the most whilst working on this project. and yet, This is still an ongoing project for me to fix Ansible. 


# Jenkins pipeline 
<img width="915" alt="Jenkins_outcome" src="https://user-images.githubusercontent.com/59723479/109577027-cc191b00-7aec-11eb-8f68-d391c0a89e9d.png">

# Continuous Integration Workflow
<img width="689" alt="Workflow" src="https://user-images.githubusercontent.com/59723479/109581503-4dc07700-7af4-11eb-97fb-9cc06a85f770.png">

# Risk assessment

|Risk Description|Assessment|Impact|Action to take|  
|---|---|---|---|
|Unit testing failure|Service1(frontend) unit testing failed could lead to unstable service|Medium|Debug unit testing|
|Security issue|DB password is open|High|Implement environment variables|
|SQL database failure|In case of DB failure, all the data stored would be wiped|Low|Create a backup DB|
|GCP instance failure|In case of instance failure, the entire application wouldn't work as SQL and Jenkins are running on the instance|High|Create a backup instance|

# Future improvements
- Webhook
- Implement environment variables 
- Ansible on Jenkins
- Unit testing
- MySQL DB

# Contributor
Bora Kim






