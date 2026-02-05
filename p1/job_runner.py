#!/usr/bin/env python3
import requests
import subprocess
import time
import json
import os
import socket
from datetime import datetime

# Configuration
DEFAULT_API_BASE_URL = "localhost:8000"
DEFAULT_SYSTEM = socket.gethostname()
DEFAULT_OWNER = "p10"
DEFAULT_POLL_INTERVAL = 10  # seconds
DEFAULT_TOKEN = "1234567890"

CONFIG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", ".config")
)

def _load_config(path):
    """Load key=value pairs from a .config file."""
    config = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        return {}
    return config

_config = _load_config(CONFIG_PATH)
if not _config:
    _config = _load_config(os.path.join(os.getcwd(), ".config"))

API_BASE_URL = _config.get("API_BASE_URL", DEFAULT_API_BASE_URL)
SYSTEM = socket.gethostname()
OWNER = _config.get("OWNER", DEFAULT_OWNER)
POLL_INTERVAL = int(_config.get("POLL_INTERVAL", DEFAULT_POLL_INTERVAL))
TOKEN = _config.get("TOKEN", DEFAULT_TOKEN)
def get_last_pending_job():
    """Fetch the last pending job from the API"""
    try:
        url = f"{API_BASE_URL}/api/functions/getLastPendingJob"
        params = {"system": SYSTEM, "owner": OWNER, "token": TOKEN}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("job")
    except Exception as e:
        print(f"Error fetching job: {e}")
        return None

def update_job(te_key, update_data):
    """Update job status via API"""
    try:
        url = f"{API_BASE_URL}/api/functions/updateJob"
        payload = {"te_key": te_key, "token": TOKEN, **update_data}
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error updating job: {e}")
        return None

def execute_job(job):
    """Execute the job command and return result"""
    job_cmd = job.get("job_cmd")
    job_name = job.get("job_name")
    te_key = job.get("te_key")
    
    print(f"[{datetime.now()}] Executing job: {job_name} (te_key: {te_key})")
    print(f"Command: {job_cmd}")
    
    # Update status to Running
    update_job(te_key, {"job_status": "R"})
    
    try:
        # Execute the command
        result = subprocess.run(
            job_cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=3600  # 1 hour timeout
        )
        
        return_code = result.returncode
        print(f"Job completed with return code: {return_code}")
        
        # Update job with results
        update_data = {
            "job_status": "C" if return_code == 0 else "F",
            "job_rc": return_code,
            "job_finish_date": datetime.utcnow().isoformat() + "Z"
        }
        update_job(te_key, update_data)
        
        return return_code == 0
        
    except subprocess.TimeoutExpired:
        print(f"Job timed out after 1 hour")
        update_job(te_key, {
            "job_status": "F",
            "job_rc": -1,
            "job_finish_date": datetime.utcnow().isoformat() + "Z"
        })
        return False
        
    except Exception as e:
        print(f"Error executing job: {e}")
        update_job(te_key, {
            "job_status": "F",
            "job_rc": -2,
            "job_finish_date": datetime.utcnow().isoformat() + "Z"
        })
        return False

def main():
    """Main loop to continuously check and execute jobs"""
    print(f"Job Runner started for system={SYSTEM}, owner={OWNER}")

    try:
        # Get the last pending job
        job = get_last_pending_job()
        
        if job:
            execute_job(job)
        else:
            print(f"[{datetime.now()}] No pending jobs found")
        
    except KeyboardInterrupt:
        print("\nJob runner stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
