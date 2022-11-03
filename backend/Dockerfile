FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /backend
