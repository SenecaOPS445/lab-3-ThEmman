#!/usr/bin/env python3
#Author ID: 159610229

import subprocess

def free_space():
    newProcess = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    free_space_output = newProcess.communicate()
    free_space_str = free_space_output[0].decode('utf-8').strip()
    return free_space_str