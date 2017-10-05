FROM python
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "gunicorn" ]
CMD [ "-c", "gunicorn.conf", "--reload", "app.app:BENDER" ]
