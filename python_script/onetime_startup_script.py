# Author: Indranil Pal
# Created Date: 18th Jan, 2022

#run: python3 ./Healthcare_Cloud_POC/python_script/onetime_startup_script.py

# libraries
import subprocess
import shlex
import json

from googleapiclient import discovery


# global variable
project_id = "poc01-330806"
location = "us-central1"
composer_env_name = "h-comp-env"
composer_imgage_version = "composer-1.17.7-airflow-2.1.4"
content_uri = "gs://healthcare-bucket//"

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
gcs_bucket_create_gcloud = "gsutil cr "

'''
# create composer environment
composer_env_create_gcloud = "gcloud composer environments create "+ composer_env_name + " --location "+ location + " --async" \
    + " --image-version " + composer_imgage_version + " --project " + project_id
print("Composer env: ", composer_env_name, " is going to be created ..")
print("gcloud command: ", composer_env_create_gcloud)
composer_env_create_gcloud_out = subprocess.check_output(shlex.split(composer_env_create_gcloud))
print(composer_env_create_gcloud_out)
'''

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

def import_dicom_instance(project_id, location, dataset_id, dicom_store_id, content_uri):



if __name__ == "__main__":
    #create_healthcare_dataset(project_id, location, dataset_id) 
    #create_dicom_store(project_id, location, dataset_id, dicom_store_id)
    pass
