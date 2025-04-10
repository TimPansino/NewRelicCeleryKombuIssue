# New Relic Python Agent Crash Reproduction

This example applications aims to reproduce [this issue](https://github.com/newrelic/newrelic-python-agent/issues/1347) in `newrelic==10.8.1`. Unfortunately, it doesn't currently reproduce the problem. If you have suggestions on reproducing the issue, please open a Pull Request or Issue here on GitHub.

## Quickstart

1. Fill in your New Relic license key in the `newrelic.ini` file, or add it as an environment variable named `NEW_RELIC_LICENSE_KEY`.
2. Create a virtual environment and install the `requirements.txt` file into it.
  1. `python -m venv .venv` or `virtualenv .venv`
  2. `source .venv/bin/activate`
  3. `pip install -r requirements.txt`
3. Open 3 separate terminals and run the following.
  1. `docker compose up`
  2. `./run-web.sh`
  3. `./run-tasks.sh`
4. Open `http://localhost:8000` in a browser, or run `curl http://localhost:8000`.

You should now have a local `redis` instance, a web worker running `gunicorn + Flask`, and a celery worker running `Celery + kombu`. Repeat step 4 as needed to send traffic to the application.
