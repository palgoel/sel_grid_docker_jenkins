FROM  python:3-alpine
MAINTAINER Pallavi Rungta
ENV BROWSER=chrome
ENV HUB_HOST=localhost
WORKDIR /usr/share/sel_test
COPY . .
RUN apk add curl jq
RUN pip install --no-cache-dir -r requirements.txt
ADD healthcheck.sh healthcheck.sh
ENTRYPOINT pytest -s