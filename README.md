# Sync Firestore between 2 projects using Cloud Function

## Setup
- Activate cloud function in source project
- Create service account for destination project
- Rename `.env-example` to `.env`. Fill `DESTINATION_FIRESTORE_CREDENTIALS` with destination service account.
- Change `PROJECT_NAME` and `DESTINATION_PROJECT_NAME` in config.py file.
- Change `collection_name` in utils, the collection that need to be synced.
- Create cloud function in source project, each function only listen to one collection/document and one context event.
  example:
  ```bash
    # function that listen collection1 on write event
    gcloud functions deploy collection1-onwrite \
  --runtime python37 --trigger-event providers/cloud.firestore/eventTypes/document.write \
  --trigger-resource projects/PROJECT_ID/databases/(default)/documents/collection1
  ``` 

    ```bash
    # function that listen collection1 on update event
    gcloud functions deploy collection1-onupdate \
  --runtime python37 --trigger-event providers/cloud.firestore/eventTypes/document.update \
  --trigger-resource projects/PROJECT_ID/databases/(default)/documents/collection1
  ``` 

## Limiation
Note the following limitations for Cloud Firestore triggers for Cloud Functions:

- Ordering is not guaranteed. Rapid changes can trigger function invocations in an unexpected order.
- Events are delivered at least once, but a single event may result in multiple function invocations. Avoid depending on exactly-once mechanics, and write idempotent functions.
- Cloud Firestore triggers for Cloud Functions is available only for Cloud Firestore in Native mode. It is not available for Cloud Firestore in Datastore mode.