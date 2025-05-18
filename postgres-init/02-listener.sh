#!/bin/bash

# Wait for PostgreSQL to be fully started
sleep 60

# Execute the index creation function
PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -d $POSTGRES_DB -c "SELECT create_n8n_indexes();"

# Set up a cron job to run VACUUM ANALYZE periodically
echo "0 2 * * * PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -d $POSTGRES_DB -c 'VACUUM ANALYZE;'" > /var/spool/cron/crontabs/postgres
chmod 600 /var/spool/cron/crontabs/postgres 