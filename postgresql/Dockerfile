FROM postgres:latest

#Define variables to config the PostgreSQL
ENV POSTGRES_DB=TP_BD1
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234

# Directory where initialization SQL scripts will be copied
# These scripts will automatically run on container startup
COPY ./initdb /docker-entrypoint-initdb.d/

# Export the default PostgreSQL port
EXPOSE 5432
