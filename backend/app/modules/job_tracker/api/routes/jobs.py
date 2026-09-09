from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.job_tracker.schemas.job import (
    JobCreate,
    JobResponse
)

from app.modules.job_tracker.services.job_service import (
    create_job,
    get_jobs
)


router = APIRouter(
    prefix="/api/job-tracker/jobs",
    tags=["Job Tracker - Jobs"]
)


@router.post(
    "",
    response_model=JobResponse
)
def create_job_endpoint(
    job_data: JobCreate,
    db: Session = Depends(get_db)
):
    return create_job(
        db,
        job_data
    )


@router.get(
    "",
    response_model=list[JobResponse]
)
def get_jobs_endpoint(
    db: Session = Depends(get_db)
):
    return get_jobs(db)