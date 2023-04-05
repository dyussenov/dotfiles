#!/bin/bash

CONTENT=$(
  cat <<EOF
version: '3'

services:
EOF
)

DEV=$(
  cat <<EOF

  postgresql:
    container_name: 'postgresql'
    image: postgres
    restart: always
    env_file:
      - ./.envs/.local/.postgres
    volumes:
      - ./postgres-data:/var/lib/postgresql/data/
    ports:
      - 5432:5432


  auth-ms:
    container_name: 'auth-ms'
    build: ./auth-ms/
    command: python main.py
    restart: always
    env_file:
      - ./.envs/.local/.auth-ms
      - ./.envs/.local/.postgres
    ports:
      - 5000:5000

  race-ms:
    container_name: race-ms
    build: ./race-ms
    working_dir: /race-ms
    env_file:
      - ./.envs/.local/.race-ms
      - ./.envs/.local/.postgres
      - ./.envs/.local/.redis
    ports:
      - 8000:8000

  front-ms:
    container_name: front-ms
    image: node:lts-alpine
    working_dir: /front-ms
    env_file:
      - ./.envs/.local/.front-ms
    command: sh -c "yarn install && yarn dev --host=0.0.0.0 --port=8080"
    volumes:
      - ./front-ms:/front-ms
    ports:
      - 8080:8080

race-ms
  redis:
    container_name: redis
    image: redis
    command: [sh, -c, "rm -f /data/dump.rdb && redis-server"]
    ports:
      - "6379:6379"
      
volumes:
  postgres-data:

EOF
)

PROD=$(
  cat <<EOF

  frontend:
    container_name: frontend
    build: ./frontend
    ports:
      - "443:443"
      - "80:80"
    depends_on:
      - backend
EOF
)

RED='\033[0;31m'
GREEN='\033[0;32m'

[ "$#" -eq 1 ] || {
  printf "%b%s" "$RED" "Ошибка. Необходимо ввести 1 аргумент."
  exit 1
}

arg="$1"
case "$arg" in
dev) CONTENT+=$DEV ;;
prod) CONTENT+=$PROD ;;
*)
  printf "%b%s" "$RED" "Ошибка. Недопустимый аргумент."
  exit 1
  ;;
esac

cat <<EOF >docker-compose.yml
$CONTENT
EOF

printf "%b%s" "$GREEN" "docker-compose.sh успешно сгенерирован."
