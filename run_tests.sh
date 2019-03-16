#!/usr/bin/env bash
docker build -t app .
docker run -it app pytest