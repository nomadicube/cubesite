#Notes on Flask and Docker

Docker build and run:

<pre><code>cd .\cubesite
docker build -t nomadicube/site .
docker run -it --name cubesite -p 8080:8080 nomadicube/site
</code></pre>

Dockerfile config:

<pre><code>FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 
COPY . .
EXPOSE 8080
CMD ["python3", "src/app.py"]
</code></pre>

Manual setup:

<pre><code>cd .\cubesite
python -m venv venv
.\venv\Scripts\activate
python -m pip install flask, markdown 
python -m pip freeze > requirements.txt
</code></pre>

Posts retrieved by descending order:

<pre><code>cubesite\src
|
+---posts
|       001 - Notes on Flask and Docker.md
|       000 - Hello, world.md
</code></pre>

<p class="date">2024-10-31</p>
