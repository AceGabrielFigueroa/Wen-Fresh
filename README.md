# Wen Fresh
A simple txt message application that accepts images of reciepts and tells you when they will spoil.

# Members of the Team
Name|Role|
---|---|
Ace Figueroa|Lead developer
Elizabeth Lim|Developer
Kaung Htet Myat|Developer
Kaung Nay Htet|Developer
WenTing Fei|Developer

# Services used
+ Flask
+ Google Cloud
  + Bucket-api
  + Google-vision
+ ngrok
+ Python
+ Twilio
  
  
# Setting up your own server
1. Clone the repo to a [directory](https://github.com/AceGabrielFigueroa/Wen-Fresh.git).

2. After cloning the repository, install the dependencies for python.
    + Flask
    + Twilio
    + google-cloud-storage

3. Set up your authentication tokens for google
    + exaxmple on windows `set GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_GOOGLE_CREDENTIALS.json`

4. Create a bucket in google cloud and edit the `BUCKET` variable in run.py to your newly created bucket name.

5. Run run.py

6. Run the in terminal `ngrok http 5000`

7. In twilio, use messaging incoming hooks to communicate with the applications

# Using the service
Simply text the number that you have choosen in twilio with a image of a reciept!
