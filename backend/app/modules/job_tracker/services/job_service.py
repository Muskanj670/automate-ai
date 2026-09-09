from sqlalchemy.orm import Session

from app.modules.job_tracker.models.job import Job
from app.modules.job_tracker.schemas.job import JobCreate


def create_job(
    db: Session,
    job_data: JobCreate
) -> Job:

    job = Job(
        **job_data.model_dump(mode="json")
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_jobs(
    db: Session
) -> list[Job]:

    return (
        db.query(Job)
        .order_by(Job.id.desc())
        .all()
    )