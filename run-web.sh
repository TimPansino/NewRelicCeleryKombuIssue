#!/bin/bash

export NEW_RELIC_CONFIG_FILE=newrelic.ini
export NEW_RELIC_ENVIRONMENT=tasks
newrelic-admin run-program gunicorn web:app -t 120
