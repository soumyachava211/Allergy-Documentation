import pandas as pd
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.fhirdate import FHIRDate
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.patient import Patient
from datetime import datetime

def create_allergy_intolerance(
    patient_id,
    substance_code,
    substance_text,
    reaction_text=None,
    severity=None,
    recorder=None,
    record_date=None
):
    """Creates a valid FHIR AllergyIntolerance resource."""

    allergy = AllergyIntolerance(
        patient=Patient(id=str(patient_id)),
        code=CodeableConcept(
            coding=[Coding(
                system="http://snomed.info/sct",
                code=substance_code,
                display=substance_text
            )]
        ),
        clinicalStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
                code="active"
            )]
        ),
        verificationStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/allergyintolerance-verification",
                code="confirmed"
            )]
        ),
        reaction=[{
            "description": reaction_text,
            "severity": severity
        }] if reaction_text else None,
        recorder=recorder,
        recordedDate=FHIRDate(record_date if record_date else datetime.utcnow())
    )

    return allergy.json(indent=2)

def build_fhir_allergy_dataset(df):
    """Converts dataframe rows into FHIR AllergyIntolerance JSON entries."""
    resources = []
    for _, row in df.iterrows():
        resource_json = create_allergy_intolerance(
            patient_id=row["patient_id"],
            substance_code=row["substance_code"],
            substance_text=row["substance"],
            reaction_text=row.get("reaction"),
            severity=row.get("severity", "mild"),
            recorder=row.get("recorder", "Clinician"),
            record_date=row.get("recorded_date")
        )
        resources.append(resource_json)
    return resources
