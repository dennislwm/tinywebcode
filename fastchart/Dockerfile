FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apt-get update \
  && apt-get clean && rm -rf /tmp/* /var/tmp/*
EXPOSE 7000
WORKDIR /app
COPY api_v1/*.py app/*.py .
RUN pip install --no-cache-dir -r requirements.txt
"""
Usage:  uvicorn main:app --host 0.0.0.0 --port 6001
"""
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]