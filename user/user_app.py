import requests
from flask import Flask, jsonify

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
trace.set_tracer_provider(
   TracerProvider(
       resource=Resource.create({SERVICE_NAME: "user-service"})
   )
)
jaeger_exporter = JaegerExporter(
   agent_host_name="localhost",
   agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
   BatchSpanProcessor(jaeger_exporter)
)
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("User"):
   with tracer.start_as_current_span("Service"):
           print("Hello world! - User Service")

app=Flask(__name__)

@app.route('/user/profile')
def get_user_profile():
    user={
        "userId": "1234-yaj",
        "email": "user@example.com",
        "organization": "example.com"
    }
    return jsonify(user)


if __name__ == "__main__":
    app.run( host='localhost', port=2000)
