
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from test import getResult
from findRate import findRating

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    body = request.values.get('Body', None)


    resp = MessagingResponse()


    result = getResult(body)

    ratings = findRating(result)

    resp.message(result)

    resp.message(ratings)

    return str(resp)