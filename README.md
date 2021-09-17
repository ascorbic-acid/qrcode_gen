## Qrcode Gen

this simple app uses pyqrcode library to generate **QRCodes** in ERPNext.




install the app to your site and send GET request to:
http://my-site.tld/api/method/qrcode_gen.qrcode.gen_qrcode
with (text) argument equal to the text which you want generate QR Code for, the returned data is png base64 which can be used directly in the image src attribute


#####Print Format, you can use the example below to show QRCode in any print format doctype
```
<img src="{{ gen_qrcode(doc.name) }}" width="100" />
```



#### License

MIT