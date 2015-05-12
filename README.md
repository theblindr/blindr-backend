[![Circle CI](https://circleci.com/gh/theblindr/blindr-backend.svg?style=svg)](https://circleci.com/gh/theblindr/blindr-backend)

# blindr-backend
Backend for [blindr](https://github.com/theblindr/blindr).
Developped in 24h for the [McHacks](http://mchacks.io/) hackathon by [@TyMarc](https://github.com/TyMarc), [@jerome-gingras](https://github.com/jerome-gingras), [@ldionmarcil](https://github.com/ldionmarcil) and [@isra17](https://github.com/isra17).

## Features
 * Authenticate user from a Facebook token
 * Endpoint to send message to other user or city channel
 * Endpoint to like other user
 * Endpoint to poll for new events to authenticated user
 * Store messages and matches events in AWS Dynamodb
 * Store users and matches in Postgres
 * Run on Heroku

## Setting the environment
1. Ensure Python 3, pip and virtualenv are installed
2. Enter your [AWS credentials](https://console.aws.amazon.com/iam/home) in `./instance/boto.cfg`
3. Create a virtual env: `virtualenv -p python3 venv`
4. Source the virtualenv: `source ./venv/bin/activate`
5. Install the dependancies: `pip install -r requirements/development.txt`
6. Create the databases' tables: `./bin/setup`

## Running in development
1. Ensure that you are in the virtualenv or activate: `source ./venv/bin/activate`
2. Execute the run script: `./bin/run`

## Update
1. Pull changes: `git pull`
2. Update pip requirements: `pip install -r requirements/development.txt`

## Other tools
 - Open a shell with the loaded environment: `./bin/shell.py`
