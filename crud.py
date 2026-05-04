from sqlalchemy.orm import Session
import models, schemas

def create_lead(db: Session, lead: schemas.LeadCreate):
    db_lead = models.Lead(
        lead_type=lead.leadType,
        name=lead.name,
        email=lead.email,
        country_code=lead.countryCode,
        phone=lead.phone,
        company=lead.company,
        service=lead.service,
        message=lead.message,
        contact_method=lead.contactMethod,
        discovery_call=lead.discoveryCall
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def get_all_leads(db: Session):
    return db.query(models.Lead).all()


def delete_lead(db: Session, lead_id: int):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if lead:
        db.delete(lead)
        db.commit()
        return True
    return False