FROM postgres
ENV POSTGRES_PASSWORD=odin
ENV POSTGRES_USER=odin
ENV POSTGRES_DB=analytics

RUN mkdir -p /tmp/psql_data/

COPY ./structure.sql /tmp/psql_data/
COPY ./structure.sql /docker-entrypoint-initdb.d/