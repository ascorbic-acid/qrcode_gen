import frappe
import pyqrcode

@frappe.whitelist()
def gen_qrcode(text):
    data = pyqrcode.create(text)
    qr64 = f'data:image/png;base64,{data.png_as_base64_str(scale=8)}'

    return qr64