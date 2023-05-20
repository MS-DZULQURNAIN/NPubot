#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ms-dzulqurnain/npubot:buster

RUN git clone -b npubot https://github.com/MS-DZULQURNAIN/NPubot.git /home/npubot/ \
    && chmod 777 /home/npubot \
    && mkdir /home/npubot /bin/

COPY ./sample_config.env ./config.env* /home/npubot/

WORKDIR /home/npubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
