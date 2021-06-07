FROM registry.marketfiler.com/utilitaire/centos_faiss

WORKDIR /www
RUN pip3 install phonenumbers
RUN pip3 install requests

COPY ./src /www/
CMD ["python3", "/www/code/index.py"]