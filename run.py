# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import upload
import gvis
import os

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()

    # Declare download directory
    DOWNLOAD_DIRECTORY=".//reciepts"

    if request.values['NumMedia'] != '0':

        # Use the message SID as a filename.
        filename = request.values['MessageSid'] + '.png'
        with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
            # Write to image
            image_url = request.values['MediaUrl0']
            f.write(requests.get(image_url).content)


        # Upload info to server!
        upload.upload_blob('la-hacks-2019-parsley-parsnips', '{}/{}'.format(DOWNLOAD_DIRECTORY, filename),
                           filename)

        # Google Vision
        lst=gvis.detect_text('{}/{}'.format(DOWNLOAD_DIRECTORY, filename))
        print(lst)
        # Remove files
        os.remove('{}/{}'.format(DOWNLOAD_DIRECTORY, filename))
    
        resp.message("Thanks for the image!")

        # Download files
        
    elif request.values.get('Body', None) == 'list':
        for x in lst:
            resp.message('{} will decay in {}.'.format(x[0],x[1]))
                         
    else:
        resp.message("Try sending a picture message.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)


