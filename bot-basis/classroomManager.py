import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Other ideas
#     take in  commitees and assign positions by schools
#     easily assignable positions
#     take in information about delegate and format awards, and give slide
#     mockmun simulator
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]
USER_TOKEN = [" "]


def init_google_client():
    client = "client_secrets.json";
    return client


client = init_google_client()


def post_classroom_announcement(text: str):
    print("Posting classroom announcement...")
    # todo


def get_classroom_announcement():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("classroom", "v1", credentials=creds)

        # Call the Classroom API
        # results = service.courses().list(pageSize=10).execute()
        # courses = results.get("courses", [])
        #
        # if not courses:
        #     print("No courses found.")
        #     return
        # # Prints the names of the first 10 courses.
        # print("Courses:")
        # for course in courses:
        #     print(course["name"])

    except HttpError as error:
        print(f"An error occurred: {error}")


def webhook_manager():
    print("* hiii")
