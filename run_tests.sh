#!/usr/bin/env bash
docker build -t app .
docker run app pytest