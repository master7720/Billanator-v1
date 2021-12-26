import base64, codecs
magic = 'aW1wb3J0IG9zDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLGluaXQNCg0KaWYgb3MubmFtZSA9PSAibnQiOg0KCW9zLnN5c3RlbSgiY2xzIikNCmVsc2U6DQoJb3Muc3lzdGVtKCJjbGVhciIpDQoNCmluaXQoY29udmVydD1UcnVlKQ0KDQpjbGFzcyBzZXR0aW5nczoNCgl5ID0gRm9yZS5ZRUxMT1cNCglyID0gRm9yZS5SRUQNCgliID0gRm9yZS5CTFVFDQoNCmRlZiBjbGVhbigpOg0KCWxpbmVzX3NlZW4gPSBzZXQoKQ0KCW91dGZpbGUgPSBvcGVuKCdkb3Jrcy50eHQnLCAiYSIpDQoJaW5maWxlID0gb3BlbignZG9ya3N0ZXN0LnR4dCcsICJyIikNCglmb3IgbGluZSBpbiBpbmZpbGU6DQoJCWlmIGxpbmUgbm90IGluIGxpbmVzX3NlZW46DQoJCQlvdXRmaWxlLndyaXRlKGxpbmUpDQoJCQlsaW5lc19zZWVuLmFkZChsaW5lKQ0KCW91dGZpbGUuY2xvc2UoKQ0KCWluZmlsZS5jbG9zZSgpDQoJaWYgb3MubmFtZSA9PSAibnQiOg0KCQlvcy5zeXN0ZW0oImRlbCBkb3Jrc3Rlc3QudHh0IikNCgllbHNlOg0KCQlvcy5zeXN0ZW0oInJtIC1yZiBkb3Jrc3Rlc3QudHh0IikNCglwcmludCgiW3t9K3t9XSBEdXBsaWNhdGUgZG9ya3MgcmVtb3ZlZCBzdWNjZXNzZnVsbHkhIi5mb3JtYXQoc2V0dGluZ3MucixzZXR0aW5ncy55KSkNCglwcmludCgiXG5be30re31dIERvcmtzIHNhdmVkIGFzIHt9ZG9ya3MudHh0e30hIi5mb3JtYXQoc2V0dGluZ3MucixzZXR0aW5ncy55LHNldHRpbmdzLmIsc2V0dGluZ3MueSkpDQoNCg0KcHJpbnQoIiIie30NCg0KIF9fX19fX18gICBfXyAgX18gIF9fICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF9fICAgICAgICAgICAgICAgICAgICAgICAgIA0KLyAgICAgICBcIC8gIHwvICB8LyAgfCAgIERhdmlkQmlsbGEgICAgICAgICAgICAgICAgICAgLyAgfCAgICAgICAgICAgICAgICAgICAgICAgIA0KJCQkJCQkJCAgfCQkLyAkJCB8JCQgfCAgX19fX19fICAgX19fX19fXyAgICBfX19fX18gICBfJCQgfF8gICAgIF9fX19fXyAgICBfX19fX18gIA0KJCQgfF9fJCQgfC8gIHwkJCB8JCQgfCAvICAgICAgXCAvICAgICAgIFwgIC8gICAgICBcIC8gJCQgICB8ICAgLyAgIC'
love = 'NtVSjtVP8tVPNtVPOpVN0XWPDtVPNtWPD8VPDxVUjxWPO8WPDtsPNxWPDxWPDtVUjxWPDxWPDxVPO8VPDxWPDxWPNtsPDxWPDxWP8tVPNiWPDxWPDxVPO8YlDxWPDxWPNtsN0XWPDxWPDxWPNtsPDxVUjxWPO8WPDtsPNiVPNtVPDxVUjxWPO8VPNxWPO8VP8tVPNtWPDtsPNtWPDtsPOsKlNxWPO8VPNxWPO8WPDtsPNtWPDiVN0XWPDtsS9sWPDtsPDxVUjxWPO8WPDtsP8xWPDxWPDxVUjxWPO8VPNxWPO8YlDxWPDxWPDtsPNtWPDtsP8tVUjxWPOpK18xWPO8WPDtsPNtVPNtVN0XWPDtVPNtWPDiVPDxVUjxWPO8WPDtsPDxVPNtVPDxVUjxWPO8VPNxWPO8WPDtVPNtWPDtsPNtWPDtVPDxYlNxWPNtVPNxWP8tWPDtsPNtVPNtVN0XWPDxWPDxWP8tVPDxYlNxWP8tWPDiVPNxWPDxWPDxYlNxWP8tVPNxWP8tVPDxWPDxWPDiVPNtVPDxWPDiVPNtWPDxWPDxYlNtWPDiVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XnUE0pUZ6Yl90Yz1yY3AyozEapzyxK2S3p19moKEjVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtQDcAo3A0VRSxqzShL2IxVREipzftGJSeMKVtMz9lVTkupzS2MJjAPvVvVv5zo3WgLKDbp2I0qTyhM3ZhrFkmMKE0nJ5apl5lYUAyqUEcozqmYaxfp2I0qTyhM3ZhpvkmMKE0nJ5apl55YUAyqUEcozqmYaVfp2I0qTyhM3ZhrFkmMKE0nJ5apl5lYUAyqUEcozqmYaxfp2I0qTyhM3ZhpvkmMKE0nJ5apl55XFxAPt0XpUWcoaDbVw0vXwLjXD0XqTI4qPN9VTyhpUI0XPWpoyg7sFc7sI0tHTkyLKAyVTyhpUI0VTShrFO0MKu0VQbtVv5zo3WgLKDbp2I0qTyhM3ZhpvkmMKE0nJ5apl55XFxAPaqipzEmVQ0tqTI4qP5mpTkcqPtvVPVcQDcjpzyhqPtvJ3g9X3g9KFNvYzMipz1uqPumMKE0nJ5apl5lYUAyqUEcozqmYaxcVPftp3ElXTkyovu3o3WxplxcVPft'
god = 'IiB0ZXh0IHZlcmlmaWVkISBOb3cgbGV0J3MgbWFrZSBzb21lIGRvcmtzIVxuIikNCnByaW50KCI9Iio2MCkNCnByaW50KCJcblt7fTF7fV0gV29yZFByZXNzIi5mb3JtYXQoc2V0dGluZ3MucixzZXR0aW5ncy55KSkNCnByaW50KCJbe30ye31dIEpvb21sYSIuZm9ybWF0KHNldHRpbmdzLnIsc2V0dGluZ3MueSkpDQpwcmludCgiW3t9M3t9XSBPcGVuQ2FydCIuZm9ybWF0KHNldHRpbmdzLnIsc2V0dGluZ3MueSkpDQpjbXMgPSBpbnB1dCgiXG5be30qe31dIFdoaWNoIENNUyBkb3JrcyBkbyB5b3Ugd2FudCB0byBtYWtlPyA6ICIuZm9ybWF0KHNldHRpbmdzLnIsc2V0dGluZ3MueSkpDQppZiBjbXMgPT0gIjEiOg0KCXByaW50KCJbe30re31dIFByZXBhcmVkIGRvcmtzOiIuZm9ybWF0KHNldHRpbmdzLnIsc2V0dGluZ3MueSkgKyAiXG4iKQ0KCXdwZG9ya3MgPSB7JygiQ29tbWVudCBvbiBIZWxsbyB3b3JsZCEiKScsDQoJCQkgICAnKCJDb21lbnRhcmlvcyBlbiBIZWxsbyB3b3JsZCEiKScsDQoJCQkgICAnKCJhdXRob3IvYWRtaW4iKScsDQoJCQkgICAnKCJ1bmNhdGVnb3JpemVkL2hlbGxvLXdvcmxkIiknLA0KCQkJICAgJygiY2F0ZWdvcnkvc2luLWNhdGVnb3JpYSIpJywNCgkJCSAgICcoInVuY2F0ZWdvcml6ZWQiKScsDQoJCQkgICAnKCJQcm91ZGx5IHBvd2VyZWQgYnkgV29yZFByZXNzIiknLA0KCQkJICAgJygiV2VsY29tZSB0byBXb3JkUHJlc3MuIFRoaXMgaXMgeW91ciBmaXJzdCBwb3N0LiIpJywNCgkJCSAgICcoIkp1c3QgYW5vdGhlciBXb3JkUHJlc3Mgc2l0ZSIpJywNCgkJCSAgICcoIk1yIFdvcmRQcmVzcyBvbiBIZWxsbyB3b3JsZCEiKScsDQoJCQkgICAnKCIvd3AvaGVsbG8td29ybGQvIiknfQ0KCWZvciB3cGRvcmsgaW4gd3Bkb3JrczoNCgkJZm9yIHdvcmQgaW4gd29yZHM6DQoJCQlwcmludCh3cGRvcmsgKyB3b3JkKQ0KCQkJdHJ5Og0KCQkJCXdpdGggb3BlbigiZG9ya3N0ZXN0LnR4dCIsImEiKSBhcyBmOg0KCQkJCQlmLndyaXRlKHdwZG9yayArIHdvcmQgKyAiXG4iKQ0KCQkJZXhjZXB0Og0KCQkJCXBhc3MNCglpbnB1dCgiXG5be30qe31dIFBsZWFzZSBlbnRlciB0byByZW1vdm'
destiny = 'HtMUIjoTywLKEyVTEipzgmYv4hVv5zo3WgLKDbp2I0qTyhM3ZhpvkmMKE0nJ5apl55XFxAPtywoTIuovtcQDbAPzIfnJLtL21mVQ09VPVlVwbAPtyjpzyhqPtvJ3g9X3g9KFODpzIjLKWyMPOxo3WepmbvYzMipz1uqPumMKE0nJ5apl5lYUAyqUEcozqmYaxcVPftVykhVvxAPtydoJEipzgmVQ0trlqcozEyrP5jnUN/o3O0nJ9hCJAioI91p2IlplNaYN0XPDxWVPNtW2yhMTI4YaObpQ9ipUEco249L29gK2cwMFNaYN0XPDxWVPNtWltvL29gK3ImMKVvXFq9QDbWMz9lVTcgMT9lnlOcovOdoJEipzgmBt0XPDyzo3Vtq29lMPOcovO3o3WxpmbAPtxWPKOlnJ50XTcgMT9lnlNeVUqipzDcQDbWPDy0pax6QDbWPDxWq2y0nPOipTIhXPWxo3Wep3Eyp3DhqUu0VvjvLFVcVTSmVTL6QDbWPDxWPJLhq3WcqTHbnz1xo3WeVPftq29lMPNeVPWpovVcQDbWPDyyrTAypUD6QDbWPDxWpTSmpj0XPJyhpUI0XPWpoyg7sFc7sI0tHTkyLKAyVTIhqTIlVUEiVUWyoJ92MFOxqKOfnJAuqTHtMT9ln3ZhYv4vYzMipz1uqPumMKE0nJ5apl5lYUAyqUEcozqmYaxcXD0XPJAfMJShXPxAPt0XMJkcMvOwoKZtCG0tVwZvBt0XPKOlnJ50XPWor30er31qVSOlMKOupzIxVTEipzgmBvVhMz9loJS0XUAyqUEcozqmYaVfp2I0qTyhM3ZhrFxtXlNvKT4vXD0XPJ9wMT9ln3ZtCFO7W2yhMTI4YaObpQ9lo3I0MG1jpz9xqJA0VPpfQDbWPDxtVPNanJ5xMKthpTujC3WiqKEyCFq9QDbWMz9lVT9wMT9lnlOcovOiL2EipzgmBt0XPDyzo3Vtq29lMPOcovO3o3WxpmbAPtxWPKOlnJ50XT9wMT9lnlNeVUqipzDcQDbWPDy0pax6QDbWPDxWq2y0nPOipTIhXPWxo3Wep3Eyp3DhqUu0VvjvLFVcVTSmVTL6QDbWPDxWPJLhq3WcqTHbo2Axo3WeVPftq29lMPNeVPWpovVcQDbWPDyyrTAypUD6QDbWPDxWpTSmpj0XPJyhpUI0XPWpoyg7sFc7sI0tHTkyLKAyVTucqPOyoaEypvO0olOlMJ1iqzHtMUIjoTywLKEyVTEipzgmYv4hVv5zo3WgLKDbp2I0qTyhM3ZhpvkmMKE0nJ5apl55XFxAPtywoTIuovtcQDbAPzIfp2H6QDbWpUWcoaDbVyg7sF17sI0tFJ52LJkcMPOCpUEco25hVFOHo29fVTAfo3AyMPRvYzMipz1uqPumMKE0nJ5apl5lYUAyqUEcozqmYaxcXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
print(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec')