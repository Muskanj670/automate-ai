from pydantic import BaseModel, EmailStr


class ProfileCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    location: str | None = None
    experience_years: int = 0
    preferred_roles: str | None = None
    preferred_locations: str | None = None
    expected_salary: int | None = None
    notice_period: int | None = None


class ProfileResponse(ProfileCreate):
    id: int

    class Config:
        from_attributes = True