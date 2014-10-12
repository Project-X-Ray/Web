#!/usr/bin/env python
#coding: utf8 

from flask import Flask, request, redirect, render_template, Markup
import os
from urllib import urlopen
import json
#from bs4 import BeautifulSoup
import time
import csv
import os
import pdb, traceback, code, sys
import datetime

app = Flask(__name__)