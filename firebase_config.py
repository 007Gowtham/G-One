import firebase_admin
from firebase_admin import firestore,credentials

def init_firebase():
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firebase()