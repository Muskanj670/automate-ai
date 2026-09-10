from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CandidateSkill(Base):
    __tablename__ = "candidate_skills"

    __table_args__ = (
        UniqueConstraint(
            "profile_id",
            "skill_id",
            name="uq_candidate_skill"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("candidate_profiles.id"),
        nullable=False,
        index=True
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        nullable=False,
        index=True
    )

    proficiency: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    profile = relationship(
        "CandidateProfile",
        back_populates="candidate_skills"
    )

    skill = relationship(
        "Skill",
        back_populates="candidate_skills"
    )