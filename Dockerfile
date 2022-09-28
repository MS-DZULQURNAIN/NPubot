#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/wise-maestro/wisetelethon /home/wisetelethon/ \
    && chmod 777 /home/wisetelethon \
    && mkdir /home/wisetelethon/bin/

COPY ./sample_config.env ./config.env* /home/wisetelethon/

WORKDIR /home/wisetelethon/

RUN pip install -r requirements.txt

CMD ["bash","start"]
