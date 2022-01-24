# Online-EHR Records
![example workflow](https://github.com/shruti-17/OpenEHR-Project/actions/workflows/main.yml/badge.svg)
![example workflow](https://github.com/demoprojset2/backend/actions/workflows/CI-CD.yml/badge.svg)
![example workflow](https://github.com/demoprojset2/backend/actions/workflows/CODE_CHECKS.yml/badge.svg)

### Project Description :
- The health care system refers to the institutions, people and resources involved in delivering health care to individuals.
- The objective of the healthcare system is to make a record of information that will be available instantly and securely to a doctor or patient or health care     individuals


### Scope

- Users of this system have specific roles defined with specific jobs to be executed.
- Doctor as a user can deal with the handling of record of patients and patient as a user can access their respective details
- In this system, health information can be created and managed by authorized providers or doctors in a digital format capable of being shared with other care       taker’s across.


### Goal:
- Empower patients to be involved in their care with our patient portal. Our portal is integrated with the EHR and provides the patient with access to their         longitudinal record.
- Better health care by improving all aspects of patient care, including safety, effectiveness, patient-centeredness, communication,timeliness, efficiency, and       equity.

### Target Audience: 
 1. Doctors
 2. Patients
 3. Healthcare individuals

### Install and Run code 

1. Create database `django` project in current directory
`django-admin startproject <project_name> .`

3. Activate environment:
`pipenv shell`

4. Install the dependancies:
`pip install -r requirements.txt`

 
6. Run the code `python manage.py runserver`

7. Clean up `deactivate`

### Run locally with docker

Use docker-compose<br>
`docker-compose up --build`

### Test Code:
Django Unit-Test:<br>
`python manage.py test`

### Migrate DB
1. After changes in the models.py / DB, run the command:<br>
`python manage.py makemigrations`
2. To sync changes run: <br>
`python manage.py migrate`


## Tech stack
<strong>EAPR</strong> uses

<strong>Frontend</strong>:
1. HTML, CSS, JS
2. React
3. React Router
4. Bootstrap

<strong>Backend</strong>:
1. Django
2. Rest-frame Work
3. Auth using JWT

<strong>Database:</strong>
PostgreSQL

<strong>Testing:</strong>
1. Selenium
2. Postman 
3. Django UnitTest

## DB Diagram
![alt text](https://github.com/demoprojset2/backend/blob/main/EHR_dbdiagram.png?raw=true)

## Application Workflow
![alt text](https://github.com/demoprojset2/backend/blob/main/EHR_workflow.jpg?raw=true)

## Deployment Workflow
![alt text](https://miro.medium.com/max/700/1*Ur9w7sOGoNAc9K6u4uKatQ.png)



## Backend Deployment
The three AWS technologies were used for backend deployment are :
Elastic Container Service (ECS)
Elastic Container Registry (ECR)
Fargate.


### Deploying a Docker Container to ECS

<strong>The steps here are:<strong>
1. Create the Docker image
2. Create an ECR registry
3. Tag the image
4. Give the Docker CLI permission to access your Amazon account
5. Upload your docker image to ECR
6. Create a Fargate Cluster for ECS to use for the deployment of your container.
7. Create an ECS Task.
8. Run the ECS Task!

## Frontend Deployment
- Creating our react app:
>npx create-react-app frontend

- After adding different components according to functionalities.We can make
a build on our app so that it can be deployed easily.
>npm run build

- For connecting netlify directly from your terminal , we have to install
NETLIFY CLI .It will authorize us .
>npm install netlify-cli -g

- Adding a redirect file so that it will work according to our react router.
/apicall/* http://54.198.55.127:8000/:splat 200
/* /index.html 200

- Final step , deploy to netlify
>netlify deploy
>netlify deploy --prod

## Features 
- Doctors can access the portal through their respective login credentials which includes email-id and password.
- Upon logging in, a doctor can add a patient or search a registered patient from the list of patients.
- Doctors can register a patient by entering personal details of the respective patient and can also add medical details if required.
- Upon registration, the patient will get a mail on the registered email-id having his/her unique ID to access the portal.
- Doctors can add multiple medical details of the patient like vital details, allergy details, Problem details, Medication details and Social history.
- Doctors can view all the past medical records of a specific patient by searching that patient.
- Medical records of a specific patient can be updated or more details can be added if required.

- The patient can access their details by entering the unique id sent on the mail after registration.
- Patient is provided with the medical details entered by the doctor for their reference.
- Patients will have all the past medical records that are added by the doctor.
