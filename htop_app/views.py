from django.shortcuts import render
from django.http import HttpResponse
import pytz
import os
import subprocess
from datetime import datetime

def htop_view(request):
   
    name = "Shrinivas C Dumbali"
    username = os.environ.get('USER', 'Unknown')  

   
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')


    try:
        top_output = subprocess.getoutput('top -b -n 1 | head -10')
    except OSError as e:
        top_output = f"Error running top command: {e}"

    
    html = f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html)
