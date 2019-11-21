
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from getClass import getClass
from findRate import findTeacher, findRating

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    #Get class name from text
    body = request.values.get('Body', None)

    #set up response
    resp = MessagingResponse()

    #find class schedules
    result = getClass(body)
    sectionsOutput = f'There are {len(result)} sections for {body}.\n'
    teacherSet = set()
    for section in result:
        teacherSet.add(section.teacher)
        sectionsOutput += f'Section Name: {section.sectionName}, Teacher Name: {section.teacher}, Time: {section.time} \n'
    
    #Find Ratings
    RatingsOutput = ''
    for teacher in teacherSet:
        Teacherid = findTeacher(teacher) 
        if Teacherid != None:
            RatingsOutput += f'Teacher: {teacher}:\n{findRating(Teacherid)}'
    

    #Check if can find any ratings
    if RatingsOutput:
        RatingsOutput = 'These are the ratings for these professors I can find on RMP:\n' + RatingsOutput
    else:
        RatingsOutput = 'Cannot find any rating on RMP'


    #Send Texts

    # print(sectionsOutput)
    resp.message(sectionsOutput)
    # print(RatingsOutput)
    resp.message(RatingsOutput)

    return str(resp)