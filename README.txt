Coding Task 
 

INTRODUCTION -
 This project is a Django-based REST API for a mobile app that allows users to register,     search for contacts, report spam, and manage their profiles. The API is designed with  security, performance, and scalability in mind.

FEATURES - 
    1.User registration and authentication
    2.Profile management
    3.Search by name or phone number
    4.Report phone numbers as spam
    5.Secure API endpoints with token-based authentication


PREREQUISITES -
 Before you begin, ensure you have met the following requirements.
    A. Python 3.7+: Make sure Python is installed on your machine.
    B. Django 3.0+: The project is built with Django, so you'll need it installed.
    C. PostgreSQL (or another supported database): The project uses a relational database.

INSTALLATION -
 Follow these steps to set up the project locally:

   1.Clone the Repository:

   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

  2.Create and Activate a Virtual Environment:
   python3 -m venv venv
   source venv/bin/activate  

  3. Install Dependencies:
   pip install -r requirements.txt

  4.Set Up Environment Variables:

  Create a .env file in the root directory and add the necessary environment variables.
  SECRET_KEY=your-secret-key
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1
  DATABASE_URL=postgres://user:password@localhost:5432/dbname

RUNNING THE SERVER 

 To start the development server:
   python manage.py runserver
 The server will be available at http://127.0.0.1:8000/.

APPLYING MIGRATION
 Before running the project, you need to apply the migrations:
   python manage.py makemigrations
   python manage.py migrate
 This will set up your database tables according to the models defined in your project.


POPULATING THE DATABASE
 To populate the database with sample data for testing:
    python manage.py populate_data
 This command will generate random user and contact data.

RUNNING TESTS
 To run the unit tests:
    python manage.py test
 This will execute all tests in the contacts/tests.py file, ensuring that your code behaves as expected.



API ENDPOINTS
 Here are the main API endpoints provided by the application:

   .User Registration: POST /register/
   .User Login: POST /login/
   .Profile Management: GET /profile/, PUT /profile/
   .Search by Name or Phone Number: GET /search/
   .Report Spam: POST /report-spam/
   .Each endpoint requires authentication via a token, except for registration and login.

CONTRUBUTING
 To contribute to this project:

   1.Fork the repository.
   2. Create a new branch (git checkout -b feature/your-feature).
   3. Make your changes and commit them (git commit -m 'Add some feature').
   4. Push to the branch (git push origin feature/your-feature).
   5. pen a pull request.

