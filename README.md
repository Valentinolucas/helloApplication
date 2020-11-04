# helloApplication.py
Example python code for granting access to Hello World API from your localhost

## Creating an application
To create an application:

1. In a new browser tab, navigate to My developer account.
2. Sign in to your developer account by selecting 'Sign in' in the top navigation bar.
3. View your applications by selecting 'My applications'.
4. Create a new application by clicking the '+NEW APP' button.
5. Give your new application a name, such as 'Hello World Example Application', and a description, such as 'Application for learning how to call APIs'.
6. Activate the Hello World API for your application. To do this, further down the page, find the Hello World API (Sandbox environment) and click 'Enable API'. This will then prompt you to enter a Callback URL, enter 'http://localhost:5000/callback'.
7. Select 'Create' to create the application. Your new application details will be displayed.

## Using Python
To call the API from a Python script:

1. Install the following library  by running the following command: ```pip install requests-oauthlib flask```.
3. cd into the repository
2. Run ```python helloApplication.py```
3. Once running, open your browser at http://localhost:5000. You should be redirected to our sign-in page.
4. Sign in using the simulated login page
5. If all is successful, you should be greeted with { "message": "Hello User!" }
