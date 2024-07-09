#Set the base image of python
FROM python:3.9-slim as build 
#Set the working directory
WORKDIR /app
#copy only the requirement text first
COPY api/requirements.text .
#Install dependencies
RUN pip install --no-cache-dir -r requirements.text
#Second stage for optimization
FROM python:3.9-slim
#Set the working directory 
WORKDIR /app
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY api/ .
EXPOSE 5000
ENV FLASK_APP = app.python
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask","run"]

