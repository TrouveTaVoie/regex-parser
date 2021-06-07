FROM registry.marketfiler.com/utilitaire/centos_faiss

WORKDIR /www
RUN pip3 install phonenumbers
RUN pip3 install requests
RUN pip3 install resume-parser
RUN python -m spacy download en_core_web_sm
RUN python3 -m spacy download fr_dep_news_trf
RUN python3 -m spacy download fr_core_news_lg
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader universal_tagset
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader brown
RUN python -m nltk.downloader maxent_ne_chunker
COPY ./src /www/
CMD ["python3", "/www/code/index.py"]