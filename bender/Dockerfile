FROM python
RUN apt-get update && apt-get install -y supervisor
ADD . /app
ADD supervisord.conf /etc/supervisord.conf
WORKDIR ./app
RUN pip install -r requirements.txt
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
