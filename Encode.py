# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jobin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from pylibdmtx.pylibdmtx import encode
from PIL import Image

@frappe.whitelist(allow_guest=True)
def encode():
    #size='10x10'
    value='22'
    value=value.encode('utf-8')
    encoded_data = encode(value)
    img = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
    img.save("test.png")










