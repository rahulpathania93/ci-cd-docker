# Docker build instructions
# base image
FROM python:3.10-slim as base

# set a working deirectory inside conatainer
WORKDIR /app

# copy requirements.txt inside container
COPY requirements.txt .

# install dependencies to reduce image size
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

# copy all project files into conatiner
COPY . .

# Expose the flask app port but it is optional to use
EXPOSE 5009

# command to run the flask app
CMD ["python3","app.py"]

