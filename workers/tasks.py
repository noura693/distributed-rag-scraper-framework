from celery_app import celery_app
import random
import time


@celery_app.task(bind=True, max_retries=3)
def unreliable_task(self, job_id):

    try:

        print(f"Running job {job_id}")

        time.sleep(2)

        if random.random() < 0.8:
            raise Exception("Failure")

        print(f"Job {job_id} succeeded")

        return job_id

    except Exception as exc:

        if self.request.retries >= 3:

            with open(
                "failed_jobs.txt",
                "a"
            ) as f:
                f.write(
                    f"Job {job_id}\n"
                )

            print(
                f"Job {job_id} moved to DLQ"
            )

            return

        raise self.retry(
            exc=exc,
            countdown=5
        )