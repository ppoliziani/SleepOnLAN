#!/usr/bin/env python

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

"""
<?php
        $command = escapeshellcmd('test.py');
        $output = shell_exec($command);
        echo $output;
    ?>"""

@app.route('/')
def index():
  return render_template('sleep.html')

@app.route('/html')
def html():
  return render_template('home.html')

@app.route('/bs')
def bs():
  return render_template('basic.php')

@app.route('/backend')
def putToSleep():
    subprocess.call([r'C:\Users\Philip\Desktop\sleep.bat'])
    # print("sleeping")
    return ("nothing")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")