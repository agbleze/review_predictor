FROM python:3.10-slim
WORKDIR /app


RUN apt-get update -y && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

WORKDIR app/

RUN ls

CMD ["shiny", "run", "--host=0.0.0.0", "--port=8000"]