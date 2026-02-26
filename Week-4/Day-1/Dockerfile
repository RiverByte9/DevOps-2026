# get python
# copy the code
# install python dependencies
# run the code

FROM python

WORKDIR /app

# copy the code to the container on /app path
COPY . /app

# COPY requirements.txt  /app
# install the dependencies
RUN pip install -r requirements.txt

# COPY app.py  /app
# open port 8000
EXPOSE 8000
# run the code
CMD ["python", "app.py"]

