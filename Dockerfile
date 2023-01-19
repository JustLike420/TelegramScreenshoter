FROM python:3.10

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
  && tar -xvzf geckodriver* \
  && chmod +x geckodriver \
  && mv geckodriver /usr/local/bin/

WORKDIR /app
COPY . /app

ENV PATH=$PATH:/usr/local/bin/geckodriver

RUN pip install -r requirements.txt

CMD ["python", "main.py"]