FROM python:3.7.3

LABEL "com.github.actions.name"="KuramiBook Publisher"
LABEL "com.github.actions.description"="Publish crawl result to website"
LABEL "com.github.actions.icon"="book"
LABEL "com.github.actions.color"="blue"

LABEL "repository"="https://github.com/flyinglimao/KuramiBook"
LABEL "homepage"="https://limaois.me/KuramiBook"
LABEL "maintainer"="flyinglimao <hi@limaois.me>"

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN sh /entrypoint