from pydantic import BaseModel, HttpUrl


class JobCreate(BaseModel):
    title: str
    company: str
    description: str | None = None
    location: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    job_url: HttpUrl
    source: str | None = None
    employment_type: str | None = None
    experience_required: str | None = None


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    description: str | None
    location: str | None
    salary_min: int | None
    salary_max: int | None
    job_url: str
    source: str | None
    employment_type: str | None
    experience_required: str | None

    class Config:
        from_attributes = True