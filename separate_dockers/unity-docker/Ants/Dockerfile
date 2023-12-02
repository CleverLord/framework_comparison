FROM ubuntu:latest
WORKDIR /app
COPY ./ /app/
USER root
RUN apt-get update
RUN apt-get install -y python3
#create alias for python3
RUN ln -s /usr/bin/python3 /usr/bin/python
CMD ["./run_all_v2.sh","2>&1"]
