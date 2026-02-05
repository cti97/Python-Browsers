#!/bin/bash
cd ~/git/Python-Browsers/p1
while true; do
    echo "Updating git ..."
    date
    git pull
    echo "----------------"
    python job_runner.py > ~/logs/job_runner.log 2>&1
    # upload logs to aws s3 bucket and add timestamp to filename
    aws s3 cp ~/logs/job_runner.log s3://bitgod.xyz/logs/job_runner_$(date +%Y%m%d%H%M%S).log
    sleep 106
    echo "Done. Sleeping for 106 seconds."
done
