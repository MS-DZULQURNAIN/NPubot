#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Ayiin-Userbot https://github.com/tokonandapedia/NandaPediaUbot /home/NandaPediaUbot/ \
    && chmod 777 /home/NandaPediaUbot \
    && mkdir /home/NandaPediaUbot/bin/

COPY ./sample_config.env ./config.env* /home/NandaPediaUbot/

WORKDIR /home/NandaPediaUbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
