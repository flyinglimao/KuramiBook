#!/bin/sh -l
# install git
echo "Install git" && \
apt-get update && \
apt-get install -y git && \

# go directory
echo "CD to workspace $GITHUB_WORKSPACE" && \
cd $GITHUB_WORKSPACE && \
# install dependencies
echo "Install dependencies" && \
pip install -r requirements.txt && \
cd publisher && \
mkdir dist && \
cp static/* dist && \
echo "Make page" && \
python make.py && \
cd dist && \

# config git
echo "Config git" && \
git init && \
git branch gh-pages && \
git config --global user.email "${COMMIT_EMAIL}" && \
git config --global user.name "${COMMIT_NAME}" && \
REPOSITORY_PATH="https://flyinglimao:${PUSH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" && \

# publish
echo "Publish page" && \
git add . && \
git commit -m "Auto generate $(date +"%F")" && \
git push $REPOSITORY_PATH gh-pages && \
echo "DONE!!!!"