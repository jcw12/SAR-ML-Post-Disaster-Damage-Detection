# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:16:57 2024

@author: user
Taken entirely from ChatGPT
"""

import subprocess

def run_snap_gpt(xml_file):
    # Path to the SNAP GPT executable
    gpt_path = r"C:\Program Files\snap\bin\gpt.exe"  # Update this with your actual path

    # Command to execute SNAP GPT with the XML file
    command = [gpt_path, xml_file]

    try:
        # Run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Check if there's any error
        if error:
            print("Error:", error.decode("utf-8"))
        else:
            print("Output:", output.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

# Example usage
#xml_file = r"D:\SNAP Scoping SNAPPY\Graphs\TempINT.xml"
#run_snap_gpt(xml_file)