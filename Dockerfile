FROM python:3.9

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
