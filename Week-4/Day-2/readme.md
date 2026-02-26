
```bash
docker run --name postgres-db \
    -e POSTGRES_USER=myuser \
    -e POSTGRES_PASSWORD=mypassword \
    -e POSTGRES_DB=mydatabase \
    -p 5432:5432 \
    -d postgres:15
```


```bash
docker run --name postgres-db \
    -e POSTGRES_USER=myuser \
    -e POSTGRES_PASSWORD=mypassword \
    -e POSTGRES_DB=mydatabase \
    -p 5432:5432 \
    -v dummy_data:/var/lib/postgresql/data \
    -d postgres:15
```

<!-- postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'testdb')} -->


<!-- postgresql://{username:password}@{host}:5432/{db_name} -->
postgresql://myuser:mypassword}@{localhost:5432/mydatabase




505  docker build -t app:day2 .
  506  docker run --name postgres-db     -e POSTGRES_USER=myuser     -e POSTGRES_PASSWORD=mypassword     -e POSTGRES_DB=mydatabase     -p 5432:5432     -d postgres:15
  507  docker run --name postgres-db     -e POSTGRES_USER=myuser     -e POSTGRES_PASSWORD=mypassword     -e POSTGRES_DB=mydatabase     -p 5432:5432     -d postgres:15
  508  docker run --name postgres-db     -e POSTGRES_USER=myuser     -e POSTGRES_PASSWORD=mypassword     -e POSTGRES_DB=mydatabase     -p 5432:5432     -d postgres:15
  509  docker ps
  510  docker images
  511  docker run -td --name appday2 app:day2
  512  docker ps
  513  docker ps -a
  514  docker logs 0baa100c7cb5
  515  RUN pip install -r requirements.txt
  516  pip install -r requirements.txt
  517  docker run -td --name appday2 -p 8000:5000 app:day2
  518  docker run -td --name app-day2 -p 8000:5000 app:day2
  519  docker ps -a
  520  docker logs 64a1e5e29f00
  521  docker build -t app:day2 .
  522  docker run -td --name app-day2 -p 8000:5000 app:day2
  523  docker ps -a
  524  docker logs 022fc11b05a4
  525  history


  app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)



"C:\Program Files\PostgreSQL\18\bin\pg_ctl.exe" runservice -N "postgresql-x64-18" -D "C:\Program Files\PostgreSQL\18\data" -w