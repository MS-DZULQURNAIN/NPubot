#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ms-dzulqurnain/npubot:buster

RUN git clone -b NPubot https://github.com/MS-DZULQURNAIN/NPubot /home/npubot/ \
    && chmod 777 /home/npubot \
    && mkdir /home/npubot /bin/

COPY ./sample_config.env ./config.env* /home/npubot/

WORKDIR /home/npubot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
