from pydantic import BaseModel


class SkillCreate(BaseModel):
    name: str
    category: str | None = None
    proficiency: str | None = None


class SkillResponse(SkillCreate):
    id: int
    profile_id: int

    class Config:
        from_attributes = True