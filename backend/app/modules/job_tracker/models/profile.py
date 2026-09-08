from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    location: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    experience_years: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    preferred_roles: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    preferred_locations: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    expected_salary: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    notice_period: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )