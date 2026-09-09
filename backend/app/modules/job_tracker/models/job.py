from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    company: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    salary_min: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    salary_max: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    job_url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        unique=True
    )

    source: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    experience_required: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )