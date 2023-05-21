#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/MS-DZULQURNAIN/NPubot /home/ayiinuserbot/ \
    && chmod 777 /home/ayiinuserbot \
    && mkdir /home/ayiin-userbot /bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
