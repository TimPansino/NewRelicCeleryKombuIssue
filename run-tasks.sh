#!/bin/bash

export NEW_RELIC_CONFIG_FILE=newrelic.ini
export NEW_RELIC_ENVIRONMENT=web
newrelic-admin run-program celery -A tasks worker --concurrency=1 --loglevel=DEBUG
