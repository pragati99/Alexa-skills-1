"""
This code sample is a part of a simple demo to show beginners how to create a skill (app) for the Amazon Echo using AWS Lambda and the Alexa Skills Kit.




"""

from __future__ import print_function

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "InfoIntent":
        return get_info_response()
    elif intent_name == "StaffIntent":
        return get_staff_response()
    elif intent_name == "StackIntent":
        return get_stack_response(intent_request)
    elif intent_name == "InstructorIntent":
        return get_instructor_response(intent_request)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():

    session_attributes = {}
    card_title = "CSOutreach"
    speech_output = "Welcome to new Skill. This skill will help you get information abut the summer camps beign offered at UTDallas for summer of 2017, at both onsite and Offsite locations."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with the same text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "Welcome to the help section for the Skill. A couple of examples of phrases that I can except are... What does the skill do?... or, who are the instructors. Lets get started now by trying one of these."

    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def get_info_response():
    session_attributes = {}
    card_title = "Info"
    speech_output = "The common camps offered on all locations include Java, javascript, C++, Minecraft, and many more"
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def get_staff_response():
    session_attributes = {}
    card_title = "outreach_Staff"
    speech_output = "The CS Outreach Program has a number of instructors at different locations, offsite or onsite. Our current locations are San Jose, Seattle, Burbank, Dallas, Washington DC, and Chicago. If you want information about a particular location you can ask the CS Outreach skill. So for example you can ask... who are the instructors at the Chicago location."
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def get_stack_response(intent_request):
    session_attributes = {}
    card_title = "Outreach_Stack"
    speech_output = ""
    outreach_city = intent_request["intent"]["slots"]["City"]["value"]

    if outreach_city == "Dallas":
        speech_output = "The Dallas location teaches C++, Javascript and Java."
    elif outreach_city == "San Jose":
        speech_output = "The San Jose location teaches Python."
    elif outreach_city == "Burbank":
        speech_output = "The Burbank location teaches Javascript, C,  and Minecraft."
    elif outreach_city == "Washington":
        speech_output = "The Washington DC location teaches only Object oriented Programming languages- Java, C++ and Python."
    elif outreach_city == "Chicago":
        speech_output = "The Chicago location teaches Python, MEAN, and Ruby on Rails."
    elif outreach_city == "Seattle":
        speech_output = "The Seattle location teaches Python, MEAN, IOS, and Ruby on Rails."
    else:
        speech_output = "Sorry, the CSOutreach does not have a location that matches what you have asked for."
    reprompt_text = speech_output
    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def get_instructor_response(intent_request):
    session_attributes = {}
    card_title = "CSOutreach_Stack"
    speech_output = ""
    outreach_city = intent_request["intent"]["slots"]["City"]["value"]

    if outreach_city == "Dallas":
        speech_output = "The Dallas instructors are Pragati and Prerana."
    elif outreach_city == "San Jose":
        speech_output = "The San Jose instructors are Brenda and Saurabh."
    elif outreach_city == "Burbank":
        speech_output = "The Burbank instructors are Chris, Eduardo, and Lance."
    elif outreach_city == "Washington":
        speech_output = "The Washington instructors are Mihn, and Dan."
    elif outreach_city == "Chicago":
        speech_output = "The Chicago instructors are Chris, and Mike."
    elif outreach_city == "Seattle":
        speech_output = "The Seattle instructors are Martin, Speros, and Charlie."
    else:
        speech_output = "Sorry, the UT Dallas does not have an offsite camp location that matches what you have asked for."
    reprompt_text = speech_output
    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"  
    speech_output = "Thank you for using CS Outreach skill! We hope you enjoyed the experience."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
