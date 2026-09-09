from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    proficiency: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    profile = relationship(
        "CandidateProfile",
        back_populates="skills"
    )