#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:38:50 2019

@author: test
"""

import csv

QuoteFile = open('/home/test/Desktop/Email_Quotes/Raw_QuoteList.csv') # https://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/#13cea60f6c7a
QuoteReader = csv.reader(QuoteFile)
quotelist = list(QuoteReader)