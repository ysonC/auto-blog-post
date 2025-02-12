#!/bin/bash

echo "Building hugo site..."

hugo

echo "Building docker image..."

docker build --platform linux/arm64 -t wyson002/my-hugo-blog .

echo "Pushing docker image..."

docker push wyson002/my-hugo-blog
