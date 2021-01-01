# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jobin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from pylibdmtx.pylibdmtx import encode
from PIL import Image


class matrix(Document):
	pass

@frappe.whitelist(allow_guest=True)
def encode_data(doctype,name):
    img_path=frappe.get_site_path()
    value='22'
    value=value.encode('utf-8')
    encoded_data = encode(value)
    img = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
    img_path_final = '/private/files/'
    img_name = name+".png"
    img.save(img_path+img_path_final+img_name)
    state = save_img(img_path_final,img_name)
    return(name)

def save_img(path,name):
    attach_image = frappe.get_doc({
            "doctype":"File",
            "file_name":name,
            "file_url":path+name
            })
    attach_image.insert()
    return name



#from  frappe.utils import get_site_name
#site_name = get_site_name(frappe.local.request.host)