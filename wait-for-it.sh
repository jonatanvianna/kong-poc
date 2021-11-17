#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"
echo $KONG_PG_PASSWORD
echo $host
until PGPASSWORD=$KONG_PG_PASSWORD psql -h "$host" -U "kong" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd