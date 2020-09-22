FROM rasa/rasa:1.10.12-full
USER root
WORKDIR /app
RUN apt install sudo -y
RUN sudo apt install g++ -y
RUN pip install fasttext
COPY . /app

