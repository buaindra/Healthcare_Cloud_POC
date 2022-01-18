# Healthcare_Cloud_POC

### Ref:
* Gcloud Command: https://cloud.google.com/sdk/gcloud/reference
* Gsutil command: 
* Health-Care-Api: https://cloud.google.com/healthcare-api
* Health-Care-Api: https://cloud.google.com/healthcare-api/docs/reference/rest?apix=true

### Python Scripting:
* google doc: https://cloud.google.com/healthcare-api/docs/samples/healthcare-export-dicom-instance-gcs
* Google Doc for healthcare Dataset: https://cloud.google.com/healthcare-api/docs/how-tos/datasets#gcloud
* Google Doc for Dicom Store: https://cloud.google.com/healthcare-api/docs/how-tos/dicom

### Healthcare data:
> Using Cloud Healthcare API, you can ingest and store data from electronic health records systems (EHRs), radiological information systems (RISs), and custom healthcare applications. 
>
> Cloud Healthcare API enables application access to healthcare data via widely-accepted, standards-based interfaces such as FHIR STU3 and DICOMweb.
>
> To support healthcare research, Cloud Healthcare API offers de-identification capabilities for FHIR and DICOM
>
>> Cloud Pub/Sub, which provides near-real-time updates when data is ingested into a Cloud Healthcare API data store
>
>> Import/export APIs, which allow you to integrate Cloud Healthcare API into both Google Cloud Storage and Google BigQuery.
>
> **Three modality-specific interfaces** that implement key industry-wide standards for healthcare data:
>> * FHIR, an emerging standard for health data interchange
>> * HL7v2, the most widely adopted method for health systems integration
>> * DICOM, the dominant standard for radiology and imaging-related disciplines
>
> **FHIR:**
>> Fast Healthcare Interoperability Resources (FHIR) data model
>> FHIR stores implement STU3, the current version of the FHIR specification,
>
> **DICOM:** (Digital Imaging and Communication in Medicine)
>> DICOM stores implement DICOMweb, a web-based standard for exchanging medical images

>> **DICOM Dataset**
>> Creating a dataset is the first step in using most of the features in the Cloud Healthcare API. After creating a dataset, you can create data stores that hold electronic health records, medical imaging data, user consents, and more.
>
>> **DICOM Stores**:
>> DICOM stores hold **DICOM instances**. You can add and manage DICOM instances in a DICOM store using the DICOMweb
>> modality-specific store use a request path that is comprised of two pieces: a **base path**, and a modality-specific **request path**
>>> base path (for identifying the store to be accessed) 
>>>> /projects/<_PROJECT>/locations/<_LOCATION>/datasets/<_DATASET>/<_STORE-TYPE>/<_STORE-NAME>
>>>
>>> request path (for identifying the actual data to be retrieved)
>>>> <_basePath>/resources/Patient/{patient_id}
>>>> 
>>>> <_basePath>/dicomWeb/studies/{study_id}/series?PatientName={patient_name}

>
>> **DICOMweb™**
>> DICOMweb™ is the DICOM Standard for web-based medical imaging. It is a set of RESTful services, enabling web developers to unlock the power of healthcare images using industry-standard toolsets. DICOMweb can be implemented directly or as a proxy to the DIMSE services to offer modern web-based access to DICOM-enabled systems.
>
