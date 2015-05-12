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

## Run on dev
1. Ensure Python 3, pip and virtualenv are installed
2. Set the values in `./config/local.py`
3. Run the setup script: `./bin/setup`
4. Start the app with `ENV=debug ./bin/run`

## Update
1. Pull changes: `git pull`
2. Update pip requirements: `pip install -r requirements.txt`

## Other tools
 - Open a shell with the loaded environment: `./shell.py`
