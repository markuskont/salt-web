#!/usr/bin/env bash

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  apt-key add -
apt-get update
echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pg.list
apt-get update
apt-get install -y postgresql-9.3 postgresql-9.2
