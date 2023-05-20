#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/MS-DZULQURNAIN/NPubot.git /home/npubot/ \
    && chmod 777 /home/npubot \
    && mkdir /home/npubot /bin/

COPY ./sample_config.env ./config.env* /home/npubot/

WORKDIR /home/npubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
