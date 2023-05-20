#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/MS-DZULQURNAIN/NPubot /home/NPubot/ \
    && chmod 777 /home/NPubot \
    && mkdir /home/NPubot /bin/

COPY ./sample_config.env ./config.env* /home/NPubot/

WORKDIR /home/NPubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
