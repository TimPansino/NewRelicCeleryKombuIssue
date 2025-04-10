from celery import Celery, shared_task

from kombu import Queue

import logging
import random

# Application connected to a dockerized redis broker.
app = Celery(
    "tasks",
    broker_url="redis://localhost:6379/0",
    result_backend="redis://localhost:6379/0",
)
logger = logging.getLogger("tasks")

# Setup kombu queues manually, doesn't seem to be required
app.conf.task_queues = (Queue("web", routing_key="web"),)
app.conf.task_default_queue = "web"


# Either decorator here seems to work
# @app.task(bind=True, queue="web")
@shared_task(bind=True, queue="web")
def rand_int_task(self):
    logger.critical("Task run.")
    return random.randint(1, 10)
