# Kafka: Python Environment

Start the kafka docker container:

```sh
docker compose up -d
```

Stop docker container:

```sh
docker compose down
```

Create virtual environment:

```sh
python -m venv .venv
```

Enter to virtual environment:

```sh
.\.venv\Scripts\Activate.ps1 # powershell
.\.venv\bin\activate # Linux/macOS
```

Install requirements:

```sh
pip install -r requirements.txt
```

Verify the installation:

```sh
python -c "import confluent_kafka; print(confluent_kafka.__version__)"
```
