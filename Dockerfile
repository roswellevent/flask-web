FROM python:3.6-slim
COPY . /flask-test
WORKDIR /flask-test
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
