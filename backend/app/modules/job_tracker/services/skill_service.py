from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.job_tracker.models.skill import Skill
from app.modules.job_tracker.models.candidate_skill import CandidateSkill
from app.modules.job_tracker.models.job_skill import JobSkill

from app.modules.job_tracker.schemas.skill import (
    SkillCreate,
    CandidateSkillCreate,
    JobSkillCreate
)

def create_skill(
    db: Session,
    skill_data: SkillCreate
) -> Skill:

    skill_name = skill_data.name.strip()

    existing_skill = (
        db.query(Skill)
        .filter(
            Skill.name.ilike(skill_name)
        )
        .first()
    )

    if existing_skill:
        raise HTTPException(
            status_code=400,
            detail="Skill already exists."
        )

    skill = Skill(
        name=skill_name,
        category=skill_data.category
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill


def get_skills(
    db: Session
) -> list[Skill]:

    return (
        db.query(Skill)
        .order_by(Skill.name)
        .all()
    )


def add_candidate_skill(
    db: Session,
    profile_id: int,
    skill_data: CandidateSkillCreate
) -> CandidateSkill:

    existing = (
        db.query(CandidateSkill)
        .filter(
            CandidateSkill.profile_id == profile_id,
            CandidateSkill.skill_id == skill_data.skill_id
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Skill already assigned to this candidate."
        )

    candidate_skill = CandidateSkill(
        profile_id=profile_id,
        **skill_data.model_dump()
    )

    db.add(candidate_skill)
    db.commit()
    db.refresh(candidate_skill)

    return candidate_skill


def get_candidate_skills(
    db: Session,
    profile_id: int
) -> list[CandidateSkill]:

    return (
        db.query(CandidateSkill)
        .filter(
            CandidateSkill.profile_id == profile_id
        )
        .all()
    )


def add_job_skill(
    db: Session,
    job_id: int,
    skill_data: JobSkillCreate
) -> JobSkill:

    existing = (
        db.query(JobSkill)
        .filter(
            JobSkill.job_id == job_id,
            JobSkill.skill_id == skill_data.skill_id
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Skill already assigned to this job."
        )

    job_skill = JobSkill(
        job_id=job_id,
        **skill_data.model_dump()
    )

    db.add(job_skill)
    db.commit()
    db.refresh(job_skill)

    return job_skill

def get_job_skills(
    db: Session,
    job_id: int
) -> list[JobSkill]:

    return (
        db.query(JobSkill)
        .filter(
            JobSkill.job_id == job_id
        )
        .all()
    )