import time
import os
import pydicom
from pydicom.dataset import Dataset, FileDataset
from datetime import datetime

# Percorso condiviso
SHARED_DIR = "/shared_data"

print(f"Writer DICOM avviato. Destinazione: {SHARED_DIR}")

def create_worklist_file(patient_id, accession_number, sps_id):
    # Creazione dataset minimale
    ds = Dataset()
    ds.is_little_endian = True
    ds.is_implicit_VR = True
    
    # Dati Paziente
    ds.PatientName = f"Rossi^Mario^{patient_id}"
    ds.PatientID = patient_id
    ds.PatientBirthDate = "19800101"
    ds.PatientSex = "M"
    
    # Dati Studio/Richiesta
    ds.AccessionNumber = accession_number
    ds.StudyInstanceUID = pydicom.uid.generate_uid()
    ds.RequestedProcedureDescription = "RM Encefalo"
    
    # Scheduled Procedure Step Sequence (Cruciale per la Worklist!)
    sp_step = Dataset()
    sp_step.ScheduledProcedureStepStartDate = datetime.now().strftime("%Y%m%d")
    sp_step.ScheduledProcedureStepStartTime = datetime.now().strftime("%H%M%S")
    sp_step.Modality = "MR"
    sp_step.ScheduledStationAETitle = "PRISMA" # Deve coincidere con la macchina
    sp_step.ScheduledProcedureStepID = sps_id  # <--- Il famoso SPS ID!
    sp_step.ScheduledProcedureStepDescription = "RM Encefalo Standard"
    
    ds.ScheduledProcedureStepSequence = [sp_step]

    # Salvataggio file .wl
    filename = f"mwl_{patient_id}.wl"
    filepath = os.path.join(SHARED_DIR, filename)
    
    # Preambolo e salvataggio
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.31' # MWL Find SOP Class
    file_meta.MediaStorageSOPInstanceUID = '1.2.3'
    file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
    
    ds_file = FileDataset(filepath, {}, file_meta=file_meta, preamble=b"\0" * 128)
    ds_file.update(ds)
    ds_file.save_as(filepath)
    print(f"[WRITER] Generato file worklist: {filename}")

# Ciclo infinito: genera un paziente nuovo ogni 30 secondi
counter = 1
while True:
    pid = f"PAT{counter:03d}"
    acc = f"ACC{counter:03d}"
    sps = f"SPS{counter:03d}"
    
    create_worklist_file(pid, acc, sps)
    
    counter += 1
    time.sleep(30)