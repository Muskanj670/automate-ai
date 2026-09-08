from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.modules.job_tracker.schemas.profile import (
    ProfileCreate,
    ProfileResponse
)
from app.modules.job_tracker.services.profile_service import (
    create_profile,
    get_profile
)


router = APIRouter(
    prefix="/api/job-tracker/profile",
    tags=["Job Tracker - Profile"]
)


@router.post(
    "",
    response_model=ProfileResponse
)
def create_candidate_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db)
):
    existing_profile = get_profile(db)

    if existing_profile:
        raise HTTPException(
            status_code=400,
            detail="Candidate profile already exists."
        )

    return create_profile(db, profile_data)


@router.get(
    "",
    response_model=ProfileResponse
)
def get_candidate_profile(
    db: Session = Depends(get_db)
):
    profile = get_profile(db)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found."
        )

    return profile