FROM kong
USER root
RUN apk add postgresql-client
COPY wait-for-it.sh /tmp
RUN chmod +x /tmp/wait-for-it.sh
USER kong