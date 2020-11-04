import os

from flask import Flask, redirect, request, session, url_for
from flask.json import jsonify
from requests_oauthlib import OAuth2Session

app = Flask(__name__)
app.secret_key = os.urandom(24)


BASE_URL = "https://sandbox.api.service.nhs.uk" 
authorize_url = "https://sandbox.api.service.nhs.uk/oauth2/authorize"
access_token_url = "https://sandbox.api.service.nhs.uk/oauth2/token"

# replace "redirect_uri" with callback url,
# which you registered during the app registration
redirect_uri = "http://localhost:5000/callback"

# replace with your api key
client_id = "API_KEY"
# replace with your secret
client_secret = "SECRET_KEY"

@app.route("/")
@app.route("/login")
def login():
   nhsd = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
   authorization_url, state = nhsd.authorization_url(authorize_url)

   # State is used to prevent CSRF, keep this for later.
   session["oauth_state"] = state
   return redirect(authorization_url)

@app.route("/callback", methods=["GET"])
def callback():
   print(request.url)
   print(access_token_url)
   print(client_secret)
   nhsd = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, state = session["oauth_state"])
   token = nhsd.fetch_token(
       token_url=access_token_url,
       client_secret=client_secret,
       authorization_response=request.url,
   )
   session["oauth_token"] = token
   return redirect(url_for(".profile"))

@app.route("/profile", methods=["GET"])
def profile():
   # Fetching a protected resource using an OAuth 2 token.
   nhsd = OAuth2Session(client_id, token=session["oauth_token"])

   user_restricted_endpoint = jsonify(
       nhsd.get(f"{BASE_URL}/hello-world/hello/user").json()
   )
   return user_restricted_endpoint

if __name__ == "__main__":
   os.environ["FLASK_ENV"] = "development"
   os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
   app.run(debug=True)