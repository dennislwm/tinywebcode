FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apt-get update \
  && apt-get clean && rm -rf /tmp/* /var/tmp/*
EXPOSE 7000
COPY . .
RUN pip install --no-cache-dir -r requirements-docker.txt
WORKDIR /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7000"]