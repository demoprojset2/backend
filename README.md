# Online-EHR Records
![example workflow](https://github.com/shruti-17/OpenEHR-Project/actions/workflows/main.yml/badge.svg)

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

### Goal:
- Target Audience 
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



