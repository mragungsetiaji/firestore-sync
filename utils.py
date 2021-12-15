from config import FIRESTORE_CLIENT, DESTINATION_FIRESTORE_CLIENT

def sync(event, collection_name="collection-1"):

    # collection name to be sent
    doc_id = event.get('oldValue').get('name').split('/')[-1]
    doc_ref = FIRESTORE_CLIENT.collection(collection_name)\
                              .document(doc_id).get()
    doc_dict = doc_ref.to_dict()
    
    DESTINATION_FIRESTORE_CLIENT.collection(collection_name)\
                                .document(doc_id)\
                                .set(doc_dict)
    
    
