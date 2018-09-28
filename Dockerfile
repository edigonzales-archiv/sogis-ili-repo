FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /opt/repository/

COPY ADA /opt/repository/ADA
COPY AFU /opt/repository/AFU
COPY AGI /opt/repository/AGI
COPY ALW /opt/repository/ALW
COPY AMB /opt/repository/AMB
COPY AVT /opt/repository/AVT
COPY AWA /opt/repository/AWA
COPY AWJF /opt/repository/AWJF
COPY Gemeinden /opt/repository/Gemeinden

COPY ilisite.xml /opt/repository/
COPY ilimodels2.xml /opt/repository/

