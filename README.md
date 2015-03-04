# blindr-backend
Backend for [blindr](https://github.com/ldionmarcil/blindr).
Developped in 24h for the [McHacks](http://mchacks.io/) hackathon by [@TyMarc](https://github.com/TyMarc), [@jerome-gingras](https://github.com/jerome-gingras), [@ldionmarcil](https://github.com/ldionmarcil) and [@isra17](https://github.com/isra17).

## Features

 * Authenticate user from a Facebook token
 * Endpoint to send message to other user or city channel
 * Endpoint to like other user
 * Endpoint to poll for new events to authenticated user
 * Store messages and matches events in AWS Dynamodb
 * Store users and matches in Postgres
 * Run on Heroku

## Setup

1. Create DynamoDB table with same schema as `models/events`
2. Install and Setup Boto https://github.com/boto/boto#getting-started-with-boto
3. Set the database connection string with `export DATABASE_URL={YOUR_CONNECTION_STRING}`
4. Create SQL table with `python database/setup.py`
5. Run the app with `foreman start`
