
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from getClass import getClass
from findRate import findTeacher

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    body = request.values.get('Body', None)
    resp = MessagingResponse()
    result = getClass(body)

    
    sectionsOutput = f'There are {len(result)} sections for {body}.\n'
    teacherSet = set()
    for section in result:
        teacherSet.add(section.teacher)
        sectionsOutput += f"Section Name: {section.sectionName}, Teacher Name: {section.teacher}, Time: {section.time} \n"
        sectionsOutput += "\n"
    # ratings = findRating(result)

    resp.message(sectionsOutput)

    # resp.message(ratings)

    return str(resp)