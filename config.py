import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

# source project
# auth using application default credentials
PROJECT_NAME = 'project-1'
CREDENTIALS = credentials.ApplicationDefault()
firebase_admin.initialize_app(CREDENTIALS, {
    'projectId': PROJECT_NAME,
})
FIRESTORE_CLIENT = firestore.client()

# destination project
# auth using service account
DESTINATION_PROJECT_NAME = 'project-2'
DESTINATION_FIRESTORE_CLIENT = firestore.client(
    firebase_admin.get_app(DESTINATION_PROJECT_NAME)
)
DESTINATION_FIRESTORE_CREDENTIALS = os.environ["DESTINATION_FIRESTORE_CREDENTIALS"]
cred = credentials.Certificate(DESTINATION_FIRESTORE_CREDENTIALS)
app = firebase_admin.initialize_app(cred)
DESTIONATION_FIRESTORE_CLIENT = firestore.client(app=app)