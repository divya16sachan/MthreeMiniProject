FROM python:slim
WORKDIR /app
COPY requirements.txt requirements.txt 
COPY api.py api.py

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

