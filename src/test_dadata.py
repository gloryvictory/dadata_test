#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : test_dadata.py
#   Created         : 25th November 2019
#   Last Modified	: 25th November 2019
#   Version		    : 1.0
#
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will test some REST from dadata and manipulate some data

import cfg
from dadata import DaDataClient

client = DaDataClient(
    key=cfg.DADATA_KEY,
    secret=cfg.DADATA_SECRET,
)

client.address = "мск сухонска 11/-89"
client.address = ["мск сухонска 11/-89", "спб невский 18"]
client.address.request()
print(client.result.region_kladr_id)
print(client.response.content)