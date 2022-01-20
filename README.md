## Healthcare POC Workflow

### Create Virtual Env:
        python3 -m virtualenv env1
        source env1/bin/activate
        deactivate

### Kaggle:
        pip install kaggle
        pip install kaggle --upgrade
        mkdir test
        cd test
        

### Step1:
    Create New Project
        gcloud projects create <new Project id> --name=<new project name>
        gcloud set config project <new Project id>
### Step2:

        python3 ./Healthcare_Cloud_POC/python_script/onetime_startup_script.py

### Errors:
1. BadRequestException: 400 Bucket is requester pays bucket but no user project provided.
2. "Cloud Healthcare Service Agent doesn't have all required permissions [storage.objects.list]
3. TypeError: build() got an unexpected keyword argument 'creadentials' --spelling wwrong(credentials)
4. AttributeError: 'Resource' object has no attribute 'setIAMPolicy' --setIamPolicy
5. Details: "Service account projects/poc01-330806/serviceAccounts/service-825137411523@gcp-sa-healthcare.iam.gserviceaccount.com does not exist.">
6.  Details: "the import pattern 'gs://poc01-330806-healthcare-bucket/input/dicom/' resolves to zero GCS objects">