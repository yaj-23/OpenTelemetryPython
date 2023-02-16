To run:
Create a venv and install the following dependencies:
```
Flask==2.2.2
requests==2.28.2
opentelemetry-api==1.15.0
opentelemetry-exporter-jaeger==1.15.0
opentelemetry-exporter-jaeger-thrift==1.15.0
opentelemetry-sdk==1.15.0
opentelemetry-semantic-conventions==0.36b0
opentelemetry-instrumentation==0.36b0
```

Then start Jaeger:
Running Jaegar on Windows:
```d
docker run -d --name jaeger `
  -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 `
  -p 5775:5775/udp `
  -p 6831:6831/udp `
  -p 6832:6832/udp `
  -p 5778:5778 `
  -p 16686:16686 `
  -p 14268:14268 `
  -p 14250:14250 `
  -p 9411:9411 `
  jaegertracing/all-in-one:1.18
```
Running Jaegar on Mac:
```d
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
  -p 5775:5775/udp \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 14268:14268 \
  -p 14250:14250 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.18
```

Afterwhich run:
To run user-service:
```
opentelemetry-instrument python user/user_app.py
```
To view the app - go to: http://localhost:2000/user/profile

To run todo-service:
```
opentelemetry-instrument python todo/todo_app.py
```

To view the app - go to http://localhost:2001
http://localhost:2001/todo
http://localhost:2001/todo/1

Or, simply head over to root directory, and compose the `docker-compose.yml` file.