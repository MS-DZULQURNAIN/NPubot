#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/MS-DZULQURNAIN/NPubot /home/ayiin-userbot/ \
    && chmod 777 /home/ayiin-userbot \
    && mkdir /home/npubot /bin/

COPY ./sample_config.env ./config.env* /home/npubot/

WORKDIR /home/npubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
