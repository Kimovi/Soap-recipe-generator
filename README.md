# Soap recipe generator
Calling for all soapers! Do not struggle with your soap recipe anymore! Just refresh the page and it will generate a random soap recipe for you. How to use it? simple, just refresh the page.

![front_page](https://user-images.githubusercontent.com/59723479/110504941-94fec700-80f5-11eb-80bb-89027e15d4d1.png)

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


<img width="689" alt="Frontend" src="https://user-images.githubusercontent.com/59723479/109579641-30d67480-7af1-11eb-9db3-39978d8f9130.png">

The frontend page is handling API calls in between all 3 backend services and also stores the generated data to MySQL DB. I've set up Docker swarm manager, worker and Nginx instance for load balancer where user can access the application through the reverse proxy.

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
<img width="737" alt="GCP instance" src="https://user-images.githubusercontent.com/59723479/110504534-29b4f500-80f5-11eb-9e88-3fc7a3e8879c.png">

# Unit testing
After building up the APIs and connect my application to the SQL database, I ran the unit test with Pytest as my code was written in Python. The purpose of the test was to ensure API applications are working without an error.

<img width="899" alt="Pytest_service1" src="https://user-images.githubusercontent.com/59723479/109577031-cc191b00-7aec-11eb-86ca-63f2d8f6049e.png">
<img width="748" alt="Pytest_service2" src="https://user-images.githubusercontent.com/59723479/109577033-ccb1b180-7aec-11eb-8f15-b6c3c70bbb9d.png">
<img width="748" alt="Pytest_service3" src="https://user-images.githubusercontent.com/59723479/109577035-cd4a4800-7aec-11eb-976b-a5ae185c826c.png">
<img width="748" alt="Pytest_service4" src="https://user-images.githubusercontent.com/59723479/109577036-cd4a4800-7aec-11eb-9222-7d98ea6e2811.png">

3 out of 4 applications had 100% of the pass result, however, Service1 (frontend) hadn't passed the test as it had a DB connection issue which is one of the ongoing issues.

For service2 & service3, I have tested APIs are giving the correct data listed. and for service4, I have tested whether it was giving the corresponding data depending on service2's outcome. I have tested several times to ensure all 3 services for the test consistency.

# Load balancer
For load balancer, I have set an instance with Nginx configuration. Any users accessing the web page will reach this server first, and Nginx will split the traffic and distribute it to either Swarm manager or Swarm worker. 

<img width="443" alt="Nginx" src="https://user-images.githubusercontent.com/59723479/109619643-f096e680-7b30-11eb-9b06-9ee7d15af8ed.png">

# Ansible
Ansible was used for this project to join Swarm manager and Swarm worker. 

This is how it looks when Ansible is running on the Jenkins instance manually. 
<img width="1146" alt="Ansible" src="https://user-images.githubusercontent.com/59723479/109619634-ed9bf600-7b30-11eb-8b80-d23d0941e4fa.png">

I have included Ansible on Jenkins pipeline and when it's successfully connected you will see this outcome. 
<img width="825" alt="Ansible running on jenkins" src="https://user-images.githubusercontent.com/59723479/110504519-27529b00-80f5-11eb-904e-1d918a69e389.png">

# Jenkins pipeline 
There is 4 stage on Jenkins Pipeline to test, set Ansible, build and deploy. 
On the Test stage, Jenkins will test 3 backend applications and when it passes, it will set trigger Ansible. Ansible will join the Swarm manager instance and Swarm worker instance. Build stage was added to simply build docker images and push them to Dockerhub as Docker Swarm will only work when images are pre-build and on Dockerhub. 
For the last, It's now ready to deploy the application. Firstly it will copy the docker-compose.yaml file to the Swarm manager instance and SSH into the manager node. then it will stack deploy the application meaning it's now up and running on both Swarm manager and Swarm worker node. 

<img width="1280" alt="Jenkins_outcome" src="https://user-images.githubusercontent.com/59723479/110504537-2a4d8b80-80f5-11eb-9389-c628c58af2f0.png">


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
- Unit testing
- MySQL DB

# Contributor
Bora Kim