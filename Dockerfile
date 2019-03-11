FROM tensorflow/tensorflow:latest-py3
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev
COPY requirements.txt /
WORKDIR /
RUN pip install --trusted-host pypi.python.org -r requirements.txt
