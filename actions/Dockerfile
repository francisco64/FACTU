FROM rasa/rasa-sdk:1.10.2
USER root
WORKDIR /app
COPY . /app/actions
RUN pip install -r /app/actions/requerimientos.txt
RUN apt update
RUN apt upgrade -y
RUN apt install sudo -y
RUN sudo apt-get install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN sudo apt install ./google-chrome-stable_current_amd64.deb -y
