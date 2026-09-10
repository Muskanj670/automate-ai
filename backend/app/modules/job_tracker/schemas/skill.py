from pydantic import BaseModel, Field


class SkillCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    category: str | None = Field(
        default=None,
        max_length=100
    )


class SkillResponse(SkillCreate):
    id: int

    class Config:
        from_attributes = True


class CandidateSkillCreate(BaseModel):
    skill_id: int = Field(gt=0)
    proficiency: str | None = Field(
        default=None,
        max_length=50
    )


class CandidateSkillResponse(BaseModel):
    id: int
    profile_id: int
    skill_id: int
    proficiency: str | None

    class Config:
        from_attributes = True


class JobSkillCreate(BaseModel):
    skill_id: int = Field(gt=0)
    is_required: bool = True


class JobSkillResponse(BaseModel):
    id: int
    job_id: int
    skill_id: int
    is_required: bool

    class Config:
        from_attributes = True