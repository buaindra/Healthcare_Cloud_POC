# Author: Indranil Pal
# Created Date: 18th Jan, 2022

#run: python3 ./Healthcare_Cloud_POC/python_script/onetime_startup_script.py

# libraries
import subprocess
import shlex
import json

from googleapiclient import discovery
from google.cloud import storage

# global variable
project_id = "poc01-330806"
location = "us-central1"
gcs_bucket = project_id + "-healthcare-bucket"
gcs_bucket_location = "us"
composer_env_name = "h-comp-env"
composer_imgage_version = "composer-1.17.7-airflow-2.1.4"
content_uri = gcs_bucket+"/input/000000*.dcm"

# Healthcare API
dataset_id = "dicom-healthcare-dataset"
dicom_store_id = "dicom-store-01"

# Google Client Library
api_version = "v1"
service_name = "healthcare"


# enable the Api
enable_healthcare_api = "gcloud services enable healthcare.googleapis.com"
enable_healthcare_api_out = subprocess.check_output(shlex.split(enable_healthcare_api))

# create GCS bucket
# gsutil mb -c standard -b off -l $location gs://$GCS_BUCKET_


def create_gcs_bucket(gcs_bucket, project_id, gcs_bucket_location):
    gcs_client = storage.Client()
    
    bucket = gcs_client.bucket(gcs_bucket)
    bucket.storage_class = "STANDARD"
    bucket.requester_pays = True
    bucket_response = gcs_client.create_bucket(bucket_or_name = bucket, location = gcs_bucket_location)
    print("Created GCS Bucket: gs://{}".format(gcs_bucket))
    return bucket_response

def sample_dicom_data_load(gcs_bucket, project_id):
    
    source_bucket_uri = "gcs-public-data--healthcare-nih-chest-xray/dicom/000000*.dcm"
    command = "gsutil cp -r -u gs://"+ source_bucket_uri + " gs://" + gcs_bucket +"/input/dicom/"
    output = subprocess.check_output(shlex.split(command))
    print("Added Source Data into Bucket gs://{}".format(gcs_bucket))
    return output
    
    '''
    gcs_client = storage.Client()
    dest_bucket = gcs_client.get_bucket(gcs_bucket)
    dest_blob = dest_bucket.blob("/input/dicom")
    dest_blob.upload_from_filename("gs://gcs-public-data--healthcare-nih-chest-xray/dicom/000000*.dcm")
    print("Added Source Data into Bucket gs://{}".format(gcs_bucket))
    '''
    '''
    gcs_client = storage.Client()
    source_bucket = gcs_client.bucket(bucket_name="gcs-public-data--healthcare-nih-chest-xray", user_project=project_id)
    source_blob = source_bucket.blob("/dicom") 
    destination_bucket = gcs_client.bucket(bucket_name=gcs_bucket, user_project=project_id)
    destination_blob = destination_bucket.blob("input/dicom")
    blob_copy = source_bucket.copy_blob(source_blob, destination_bucket, destination_blob)
    print("Added Source Data into Bucket gs://{}".format(gcs_bucket))
    return blob_copy
    '''
    '''
    bucket_name = "gcs-public-data--healthcare-nih-chest-xray"
    blob_name = "/dicom"
    new_bucket_name = gcs_bucket
    new_blob_name = "/input/dicom"

    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)
    return new_blob
    '''
# create composer environment
def create_composer_env(composer_env_name, location, project_id, composer_imgage_version):
    composer_env_create_gcloud = "gcloud composer environments create "+ composer_env_name + " --location "+ location + " --async" \
        + " --image-version " + composer_imgage_version + " --project " + project_id

    print("Composer env: ", composer_env_name, " is going to be created ..")
    print("gcloud command: ", composer_env_create_gcloud)
    composer_env_create_gcloud_out = subprocess.check_output(shlex.split(composer_env_create_gcloud))
    print(composer_env_create_gcloud_out)


# create environment variable


# create healthcare dataset
# gcloud healthcare datasets create DATASET_ID --location=LOCATION

def create_healthcare_dataset(project_id, location, dataset_id):
    client = discovery.build(service_name, api_version)

    dataset_parent = "projects/{}/locations/{}".format(project_id, location)

    api_request = (
        client.projects()
        .locations()
        .datasets()
        .create(parent=dataset_parent, body={}, datasetId=dataset_id)
    )

    api_response = api_request.execute()
    print("created dataset: {}".format(dataset_id))

    return api_response


# Create DICOM Store
# gcloud healthcare dicom-stores create test-dicom-store --dataset=test-dataset --pubsub-topic=projects/my-project/topics/test-pubsub-topic

def create_dicom_store(project_id, location, dataset_id, dicom_store_id):
    client = discovery.build(service_name, api_version)

    store_parent = "projects/{}/locations/{}/datasets/{}".format(project_id, location, dataset_id)

    api_request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .create(parent=store_parent, body={}, dicomStoreId=dicom_store_id)
    )

    api_response = api_request.execute()
    print("Created DICOM Store: {}".format(dicom_store_id))
    return api_response  


# import to daicom store
#gcloud beta healthcare dicom-stores import gcs $DICOM_STORE_ID --dataset=$DATASET_ID --location=$REGION --gcs-uri=gs://gcs-public-data--healthcare-nih-chest-xray/dicom/000000* --project=$PROJECT_ID

def import_dicom_instance_from_gcs(project_id, location, dataset_id, dicom_store_id, content_uri):
    client = discovery.build(service_name, api_version)

    dicom_store_name = "projects/{}/locations/{}/datasets/{}/dicomStores/{}".format(project_id \
        , location, dataset_id, dicom_store_id)
    body = { "gcsSource": { "uri": "gs://{}".format(content_uri)}}

    api_request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .import_(name=dicom_store_name, body=body)
    )

    api_response = api_request.execute()
    print("Imported dicom_instance: {}".format(content_uri))
    return api_response


if __name__ == "__main__":
    #create_gcs_bucket(gcs_bucket, project_id, gcs_bucket_location)
    sample_dicom_data_load(gcs_bucket, project_id)
    #create_composer_env(composer_env_name, location, project_id, composer_imgage_version)
    create_healthcare_dataset(project_id, location, dataset_id) 
    create_dicom_store(project_id, location, dataset_id, dicom_store_id)
    import_dicom_instance_from_gcs(project_id, location, dataset_id, dicom_store_id, content_uri)



    
