FROM python:3.8
COPY utility/requirements.txt .
RUN pip install -r requirements.txt
COPY  utility/code/ .
CMD [ "python", "app.py" ]
