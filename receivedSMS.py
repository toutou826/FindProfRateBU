
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
        sectionsOutput += f'Section Name: {section.sectionName}, Teacher Name: {section.teacher}, Time: {section.time} \n'
    
    RatingsOutput = 'These are the ratings for these professors I can find on RMP:\n'


    for teacher in teacherSet:
        Teacherid = findTeacher(teacher) 
        if Teacherid != None:
            RatingsOutput += f'Teacher: {teacher}:\n{findRating(Teacherid)}'

    print(sectionsOutput)
    resp.message(sectionsOutput)

    print(RatingsOutput)
    resp.message(RatingsOutput)

    return str(resp)