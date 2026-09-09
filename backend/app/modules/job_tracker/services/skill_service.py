from sqlalchemy.orm import Session

from app.modules.job_tracker.models.skill import Skill
from app.modules.job_tracker.schemas.skill import SkillCreate


def add_skill(
    db: Session,
    profile_id: int,
    skill_data: SkillCreate
) -> Skill:

    skill = Skill(
        profile_id=profile_id,
        **skill_data.model_dump()
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill


def get_profile_skills(
    db: Session,
    profile_id: int
) -> list[Skill]:

    return (
        db.query(Skill)
        .filter(Skill.profile_id == profile_id)
        .all()
    )