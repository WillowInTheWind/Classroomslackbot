import os
from flask import Flask
import slackManager
import classroomManager
app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/post/<message>')
def postmessage(message):
    slackManager.post_message_to_slack(message, None)
    return 'Message posted!'

@app.route('/class')
def postmessage():
    classroomManager.get_classroom_announcement( )
    return 'Message gotten!'


if __name__ == '__main__':
    if app.debug:
        app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
