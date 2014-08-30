Simple Rest API
===========

The idea is to create a simple Angular app displaying information about the currently logged user. 

Authentication will use a JWT (more info: https://auth0.com/blog/2014/01/07/angularjs-authentication-with-cookies-vs-token/ )

#####The following REST api is available:

* Retrieve a new Web Token:

`curl -X POST -d "username=admin&password=abc123" http://localhost:8000/api/auth-token/`

* Retrieve account details:
`curl -H "Authorization: JWT <your_token>" http://localhost:8000/api/users/<user_id>/`

* Update user account:
`curl -X PUT -H "Authorization: JWT <your_token> » http://localhost:8000/api/users/<user_id>/ -d "username=<username>&email=<new_email>..."`



#####The following users are available:

| Login  | Password |
| ------ | -------- |
| user1  | secret1|
| user2  | secret2|

