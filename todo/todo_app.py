import requests
from flask import Flask, jsonify


from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
trace.set_tracer_provider(
   TracerProvider(
       resource=Resource.create({SERVICE_NAME: "todo-service"})
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
with tracer.start_as_current_span("ToDo"):
   with tracer.start_as_current_span("Service"):
           print("Hello world! - Todo Service")


app=Flask(__name__)
user_service_host='localhost'

@app.route('/')
def index():
    return "hello world"

def get_user():
    r = requests.get(f'http://{user_service_host}:2000/user/profile')
    return r.json()

@app.route('/todo')
def get_todo():
    user = get_user()
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    return jsonify(r.json())

@app.route('/todo/<id>')
def get_todo_by_id(id):
    user = get_user()
    r = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    return jsonify(r.json())

if __name__ == '__main__':
    app.run( host='localhost', port=2001)
