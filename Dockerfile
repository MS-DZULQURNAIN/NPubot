#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/tokonandapedia/nandapediaubot /home/nandapediaubot/ \
    && chmod 777 /home/nandapediaubot \
    && mkdir /home/nandapediaubot/bin/

COPY ./sample_config.env ./config.env* /home/nandapediaubot/

WORKDIR /home/nandapediaubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
