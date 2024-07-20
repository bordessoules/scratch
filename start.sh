#!/bin/sh

set -e

# Wait for the database to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

echo "Using database URL: $DATABASE_URL"

# Check if migrations folder exists
if [ ! -d "/app/migrations" ]; then
    echo "Initializing migrations..."
    flask db init
    echo "Migrations initialized."
fi

# Check current revision and head revision
current_rev=$(flask db current 2>/dev/null || echo "None")
head_rev=$(flask db heads 2>/dev/null || echo "None")

if [ "$current_rev" = "None" ] || [ "$current_rev" != "$head_rev" ]; then
    echo "Applying existing migrations..."
    flask db upgrade
fi

# Generate a new migration if there are changes
echo "Checking for model changes..."
flask db migrate -m "Auto-generated migration"

# Apply any new migrations
echo "Applying migrations..."
flask db upgrade

# Start the application
echo "Starting the application..."
gunicorn --bind 0.0.0.0:5000 run:app