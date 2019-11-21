
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from getClass import getClass
from findRate import findTeacher, findRating

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
    
    RatingsOutput = f'These are the ratings for these professors I can find on RMP:\n'
    teachers = [findTeacher(i) for i in teacherSet] 

    for teacher in teachers:
        if teacher != None:
            RatingsOutput += findRating(teacher)

    print(sectionsOutput)
    resp.message(sectionsOutput)

    print(RatingsOutput)
    resp.message(RatingsOutput)

    return "Running Right Now!"