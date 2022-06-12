FROM python:3.10

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/

#  Install pckages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r\
    requirements.txt