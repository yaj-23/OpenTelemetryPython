FROM python:latest 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . .
CMD [ "Opentelemtry-instrument", "python" , "todo_app.py"]


