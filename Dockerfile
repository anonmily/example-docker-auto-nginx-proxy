FROM python:3.6

RUN pip install Flask

ADD server.py /src/server.py
WORKDIR /src
ENV PORT 5000
EXPOSE 5000
CMD ["python","/src/server.py"]
