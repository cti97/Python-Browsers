#!/bin/bash
while true; do
    echo "Updating..."
    date
    git pull
    sleep 60*60
done