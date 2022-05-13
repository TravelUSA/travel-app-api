# travel-app-api
This will store the apis to retrieve images from google drive

# run locally
bin/setup - to set-up the local env of docker containers
create user by visiting http://127.0.0.1:8080/api/user/create/
create token by visiting http://127.0.0.1:8080/api/user/token/ and providing the email/pwd that was created in above step
We are using modheader for providing the token to the api. Go to modheader to update the token as `Token <token generated>` for Request Headers -> Authorization
