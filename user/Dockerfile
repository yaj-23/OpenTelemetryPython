FROM python:latest 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["opentelemtry-instrument","python" , "user_app.py"]
