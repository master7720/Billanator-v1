import base64, codecs
magic = 'aW1wb3J0IHJlLCByZXF1ZXN0cw0KZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZQ0KYmFubmVyID0gJycnDQoNCiBfX19fX18gIF9fX19fX19fXyBfICAgICAgICBfICAgICAgICBfX19fX19fICBfICAgICAgICBfX19fX19fIF9fX19fX19fXyBfX19fX19fICBfX19fX19fIA0KKCAgX19fIFwgXF9fICAgX18vKCBcICAgICAgKCBcICAgICAgKCAgX19fICApKCAoICAgIC98KCAgX19fICApXF9fICAgX18vKCAgX19fICApKCAgX19fXyApDQp8ICggICApICkgICApICggICB8ICggICAgICB8ICggICAgICB8ICggICApIHx8ICBcICAoIHx8ICggICApIHwgICApICggICB8ICggICApIHx8ICggICAgKXwNCnwgKF9fLyAvICAgIHwgfCAgIHwgfCAgICAgIHwgfCAgICAgIHwgKF9fXykgfHwgICBcIHwgfHwgKF9fXykgfCAgIHwgfCAgIHwgfCAgIHwgfHwgKF9fX18pfA0'
love = 'XsPNtK18tXPNtVPNtsPO8VPNtsPO8VPNtVPNtsPO8VPNtVPNtsPNtK19sVPO8sPNbKPOpXFO8sPNtK19sVPO8VPNtsPO8VPNtsPO8VPNtsPO8sPNtVPNtK18cQDc8VPttVSjtKPNtVPO8VUjtVPO8VUjtVPNtVPO8VUjtVPNtVPO8VPttVPNcVUk8VUjtKPNtVUk8VPttVPNcVUjtVPO8VUjtVPO8VUjtVPO8VUk8VPupVPttVPNAPajtXI9sKlxtXI9sKlxtXS9sK3jtXS9sK18iKUjtXS9sK18iKUjtXFNtVPttsUjtXFNtKPNtsUjtXFNtVPttsPNtVUjtsPNtVUjtXS9sKlxtsUjtXFOpVSksKj0XsP8tKS9sKl8tKS9sK19sK18iXS9sK19sK18iXS9sK19sK18isP8tVPNtVSk8sP8tVPNtXI8csP8tVPNtVSk8VPNtXI8bVPNtXS9sK19sK18csP8tVPOpK18iQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVP'
god = 'AgICAgICAgICAgICAgICAgICAgICAgICAgICANCg0KQWR2YW5jZWQgc2l0ZSBHcmFiYmVyDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KQ29kZWQgYnkgRGF2aWRCaWxsYSANCmh0dHBzOi8vdC5tZS9zZW5kZ3JpZF9hd3Nfc210cCANCiAnJycNCnByaW50IGJhbm5lcg0KRGF2aWQgPSByYXdfaW5wdXQoJ3Jvb3RARGF2aWRCaWxsYTp+IyBEYXZpZCA6ICcpDQpCaWxsYSA9IHJhd19pbnB1dCgncm9vdEBEYXZpZEJpbGxhOn4jIEJpbGxhIDogJykNCkRCID0gcmF3X2lucHV0KCdyb290QERhdmlkQmlsbGE6fiMgREIgOiAnKQ0KZm9yIGkgaW4gcmFuZ2UoMTUpOg0KICAgIGkgPSBpbnQoaSkgKyAxDQogICAgcHJpbnQgJ0hhbGFtYW46ICcgKyBzdHIoaSkNCiAgICB4ID0gcmVxdWVzd'
destiny = 'UZhM2I0XPqbqUEjpmbiY3q3ql5wqJWxo21unJ4hL29gY2EioJScoaZgpzIanKA0MKWyMP1vrF1xLKEyYlptXlOmqUVbETS2nJDcVPftWl0aVPftp3ElXRWcoTkuXFNeVPpgWlNeVUA0pvuRDvxtXlNaYlptXlOmqUVbnFxtXlNaWlxAPvNtVPOlVQ0tpzHhMzyhMTSfoPtaVw4bYvf/XGjiLG5powjiMTy2CvpfVUthqTI4qPxAPvNtVPOmqvN9VT9jMJ4bW2qlLJWvMJDhqUu0WljtW2RaXD0XVPNtVTMipvO6VTyhVUV6QDbtVPNtVPNtVTyzVPpiWlOcovO6VT9lVPp9WlOcovO6VT9lVPqRo3qhoT9uMPOSrUEyoaAco24aVTyhVUb6QDbtVPNtVPNtVPNtVPOjLKAmQDbtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPOjpzyhqPO6QDbtVPNtVPNtVPNtVPOmqv53pzy0MFu6VPftW1khWlxAPt0XVPNtVUOlnJ50VPqRo21unJ5FMKA1oUEmBvNaVPftp3ElXTkyovulXFxAPt0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
print(base64.b64decode(trust),'<string>','exec')