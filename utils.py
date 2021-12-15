from config import FIRESTORE_CLIENT, DESTINATION_FIRESTORE_CLIENT

def sync(event, collection_name="collection-1"):

    # collection name to be sent
    doc_id = event.get('oldValue').get('name').split('/')[-1]
    doc_ref = FIRESTORE_CLIENT.collection(collection_name)\
                              .document(doc_id).get()

    doc_dict = doc_ref.to_dict()
    doc_path = doc_ref.reference.path
    
    DESTINATION_FIRESTORE_CLIENT.collection(doc_path)\
                                .set(doc_dict)
    
    