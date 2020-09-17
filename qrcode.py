import pyqrcode

myname="sdasjdh"

MYQR=pyqrcode.create(myname)
MYQR.svg("MYDetails.svg")
