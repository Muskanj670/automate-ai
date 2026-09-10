from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.job_tracker.schemas.skill import (
    SkillCreate,
    SkillResponse,
    CandidateSkillCreate,
    CandidateSkillResponse,
    JobSkillCreate,
    JobSkillResponse
)

from app.modules.job_tracker.services.skill_service import (
    create_skill,
    get_skills,
    add_candidate_skill,
    get_candidate_skills,
    add_job_skill,
    get_job_skills
)


router = APIRouter(
    prefix="/api/job-tracker",
    tags=["Job Tracker - Skills"]
)


# -------------------------
# Global Skills
# -------------------------

@router.post(
    "/skills",
    response_model=SkillResponse
)
def create_skill_endpoint(
    skill_data: SkillCreate,
    db: Session = Depends(get_db)
):
    return create_skill(
        db,
        skill_data
    )


@router.get(
    "/skills",
    response_model=list[SkillResponse]
)
def get_skills_endpoint(
    db: Session = Depends(get_db)
):
    return get_skills(db)


# -------------------------
# Candidate Skills
# -------------------------

@router.post(
    "/profile/{profile_id}/skills",
    response_model=CandidateSkillResponse
)
def add_candidate_skill_endpoint(
    profile_id: int,
    skill_data: CandidateSkillCreate,
    db: Session = Depends(get_db)
):
    return add_candidate_skill(
        db,
        profile_id,
        skill_data
    )


@router.get(
    "/profile/{profile_id}/skills",
    response_model=list[CandidateSkillResponse]
)
def get_candidate_skills_endpoint(
    profile_id: int,
    db: Session = Depends(get_db)
):
    return get_candidate_skills(
        db,
        profile_id
    )


# -------------------------
# Job Required Skills
# -------------------------

@router.post(
    "/jobs/{job_id}/skills",
    response_model=JobSkillResponse
)
def add_job_skill_endpoint(
    job_id: int,
    skill_data: JobSkillCreate,
    db: Session = Depends(get_db)
):
    return add_job_skill(
        db,
        job_id,
        skill_data
    )


@router.get(
    "/jobs/{job_id}/skills",
    response_model=list[JobSkillResponse]
)
def get_job_skills_endpoint(
    job_id: int,
    db: Session = Depends(get_db)
):
    return get_job_skills(
        db,
        job_id
    )