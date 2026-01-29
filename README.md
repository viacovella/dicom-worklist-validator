# DICOM Modality Worklist Validator & Simulator

A Dockerized environment to simulate a RIS (via REST API) and a Modality Worklist SCP (via Orthanc) for testing MRI/CT scanners integration.

## Quick Start:

```Bash
git clone https://github.com/viacovella/dicom-worklist-validator/
docker-compose up --build
```
## Usage 
* You can try to post fake study data to generate a worklist file, using Windows Powershell:

```Powershell
$body = @{
    patient_name = "Fake^Name"
    patient_id = "MR12345"
    accession_number = "ACC999"
    patient_sex = "M"
    scheduled_ae_title = "MRSCANNER"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/create-worklist" -Method Post -Body $body -ContentType "application/json"
```

* You can try to post fake study data to generate a worklist file using curl on a bash shell
```Bash
curl -X POST http://localhost:8000/create-worklist \
     -H "Content-Type: application/json" \
     -d '{"patient_name":"Fake^Name","patient_id":"MR12345", "accession_number":"ACC999", "patient_sex":"M", "scheduled_ae_title":"MRSCANNER"}
```

## Testing
* you can use a one-line docker instruction with dcm4che docker image
```Bash
docker run --rm dcm4che/dcm4che-tools:5.32.0 findscu -c DOCKER_MWL@host.docker.internal:4242 -M -m ScheduledStationAETitle=MRSCANNER -r PatientName
```
## AI Usage Disclaimer
This project was developed using an AI-assisted workflow. Large Language Models (LLMs) were utilized as a pair programming partner to accelerate code scaffolding, debug configuration files (Orthanc/Docker), and refine the DICOM implementation logic. All AI-generated code has been reviewed, tested, and validated by the author to ensure accuracy and adherence to standards.
