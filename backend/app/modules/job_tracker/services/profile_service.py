from sqlalchemy.orm import Session

from app.modules.job_tracker.models.profile import CandidateProfile
from app.modules.job_tracker.schemas.profile import ProfileCreate


def create_profile(
    db: Session,
    profile_data: ProfileCreate
) -> CandidateProfile:

    profile = CandidateProfile(
        **profile_data.model_dump()
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def get_profile(
    db: Session
) -> CandidateProfile | None:

    return db.query(CandidateProfile).first()