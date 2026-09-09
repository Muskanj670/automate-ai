from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.job_tracker.schemas.skill import (
    SkillCreate,
    SkillResponse
)

from app.modules.job_tracker.services.skill_service import (
    add_skill,
    get_profile_skills
)


router = APIRouter(
    prefix="/api/job-tracker/profile",
    tags=["Job Tracker - Skills"]
)


@router.post(
    "/{profile_id}/skills",
    response_model=SkillResponse
)
def create_skill(
    profile_id: int,
    skill_data: SkillCreate,
    db: Session = Depends(get_db)
):
    return add_skill(
        db,
        profile_id,
        skill_data
    )


@router.get(
    "/{profile_id}/skills",
    response_model=list[SkillResponse]
)
def get_skills(
    profile_id: int,
    db: Session = Depends(get_db)
):
    return get_profile_skills(
        db,
        profile_id
    )