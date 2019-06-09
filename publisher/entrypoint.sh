#!/bin/bash
# install git
apt-get update && \
apt-get install -y git && \

# go directory
cd $GITHUB_WORKSPACE && \

# install dependencies
pip install -r requirements.txt && \
python main.py publisher/tmp.json && \
cd publisher && \
mkdir dist && \
cp static/* dist && \
python make.py && \
cd dist && \

# config git
git init && \
git branch gh-pages && \
git config --global user.email "${COMMIT_EMAIL}" && \
git config --global user.name "${COMMIT_NAME}" && \
REPOSITORY_PATH="https://${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" && \

# publish
git add . && \
git commit -m "Auto generate $(date +"%F")" && \
git push $REPOSITORY_PATH gh-pages && \
echo "DONE!!!!"

