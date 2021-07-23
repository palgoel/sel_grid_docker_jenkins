FROM  python:3-alpine
MAINTAINER Pallavi Rungta
WORKDIR /usr/share/sel_test
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-s", "-n=1"]