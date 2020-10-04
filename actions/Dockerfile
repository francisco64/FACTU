FROM rasa/rasa-sdk:1.10.2
USER root
WORKDIR /app
COPY . /app/actions
RUN pip install -r /app/actions/requerimientos.txt
#RUN apt-get update
#RUN apt-get install -y google-chrome-stable

