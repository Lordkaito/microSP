## MicroSP

This is a simple Python server that provides user authentication using JWT.
It uses the Flask framework to handle HTTP requests and generate JWT tokens.
The server exposes two endpoints: /login and /protected.
The /login endpoint expects a POST request with a JSON payload containing a username and password.
If the credentials are valid, the server generates a JWT token and returns it in the response.
The /protected endpoint expects a GET request with an Authorization header containing the JWT token.
If the token is valid, the server returns a JSON payload containing a message indicating that the user is authenticated.
If the token is invalid or missing, the server returns a 401 Unauthorized response.

To run the server, simply execute this file with Python 3:
  python3 app.py

The server listens on port 5000 by default. You can change this by setting the PORT environment variable.
For example, to listen on port 8080, run:
  PORT=8080 python3 server.py

Dependencies:
- Flask (https://pypi.org/project/Flask/)
- PyJWT (https://pypi.org/project/PyJWT/)
