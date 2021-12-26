import base64, codecs
magic = 'I2N1cmwgLXNxSCdBY2NlcHQ6IGFwcGxpY2F0aW9uL2pzb24nICdodHRwczovL2xlYWtpeC5uZXQvc2VhcmNoP3E9KiZzY29wZT1zZXJ2aWNlJ3xqcQ0KaW1wb3J0IHJlcXVlc3RzLCBqc29uDQppbXBvcnQgb3MNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUNCmZyb20gbXVsdGlwcm9jZXNzaW5nLmR1bW15IGltcG9ydCBQb29sDQoNCmprdDQ4ID0gew0KICAnYXBpLWtleSc6J0dHMkJscEZWcFJnM3RnNkhyOE5JcnRKSFJYR2RNa2xpRUp3VVdUcmhNVmxpSHZ2SycsICMgY2hhbmdlIHlvdXIgYXBpIGtleQ0KICAnQWNjZXB0JzonYXBwbGljYXRpb24vanNvbicNCn0NCg0KYmFubmVyID0iIiINCg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLi0nJyctLiAgICAgICAgICAgICANCiAgICAgICAgICAgICAgLi0tLS4uLS0tLiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJyAgIF8gICAgXCAgICAgICAgICAgDQovfCAgICAgICAgLi0tLnwgICB8fCAgIHwgICAgICAgICAgICAgXy4uLl8gICAgICAgICAgICAgICAgICAgICAvI'
love = 'PNtY2NtWl4tVPOpVPNtVPNtVPNtVN0XsUjtVPNtVPNtVUksK3k8VPNtsUjtVPO8VPNtVPNtVPNtVPNhWlNtVPNtWl4tVPNtVPNtVPNtVPNtVPNtVPNhVPNtsPNtVPNtKPNtWlNtVPNtVPNtVPNAPak8VPNtVPNtVPNhYF0hsPNtVUk8VPNtsPNtVPNtVPNtVPNhVPNtYv0hVPNtYvNtVPNtVPNtVPNtVPNtYajtsPNtVPptVPNtVPO8VPNaYv0fYv0gYvNtQDc8sPNtK18tVPNtsPNtsUjtVPO8sPNtVUjtVPNtK18tVPNtsPNtWlNtVPptVUjtVPNtK18tVPNtVPNhWlO8K1jtVPNtKPNtVPNtYlNiVUjtVP4gYvO8VN0XsUjiW19sVPphVUjtVUk8VPNtsUjtVPO8VP46YF0hWl4tVUjtVUjtVPO8VPO8VP46YF0hWl4tVP4aVPNtVPO8LP4tVPOtVP4hWlNiVPO8VUjtVUjtsPNAPaj6Y2NtVPphVPq8VPO8sPNtVUk8VPNtsP8tsPNtVSjtsPO8VPO8VPNtsPNtsP8tsPNtVSjtsPpgYF4tVP4gWlNtVPpgYv4hYFqtVPNtsPO8VPO8VUjtQDc8sPNtVPNtsPO8sPNtsUjtVPO8sPNtVUktVvOsKlO8VUjtsPNtsPNtVUjtVUktVvOsKlO8VUjtVPO8VPO8VPNtVPNtVPNtVPNtVPNtVUjtsPNtWl0tVN0XsUkpVPNtVP8tW3ksK3k8VPNtsUjtVPO8VP4aYv'
god = 'cnfCB8IHwgIHwgICB8ICB8IC4nLicnfCB8ICAgfCAgfCAgICAgICAgICAgICAgICB8IHwgICAgICANCnwvXCcuLicgLyAgICAgJy0tLScnLS0tJy8gLyAgIHwgfF98ICB8ICAgfCAgfC8gLyAgIHwgfF8gIHwgICcuJyAgICAgICAgICAgICAgfCB8ICAgICAgDQonICBgJy0nYCAgICAgICAgICAgICAgICBcIFwuXyxcICcvfCAgfCAgIHwgIHxcIFwuXyxcICcvICB8ICAgLyAgICAgICAgICAgICAgIHxffCAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgIGAtLScgIGAiICctLScgICAnLS0nIGAtLScgIGAiICAgYCctJyAgICAgICAgICAgICAgICAgICAgICAgICANCkEgUHJpdmF0ZSBNZXRob2QgdG8gZ2V0IGZyZXNoIGlwcw0KDQpodHRwczovL3QubWUvc2VuZGdyaWRfYXdzX3NtdHANCg0KY29kZWQgYnkgaHR0cHM6Ly90Lm1lL2RhdmlkXzNpbGxhDQoiIiINCnByaW50IChiYW5uZXIpDQp0cnk6DQogcSA9IHJhd19pbnB1dCgnIHJvb3RARGF2aWRCaWxsYTp+IyBRdWVyeSA6ICcpDQogdGhyZWFkID0gcmF3X2lucHV0KCdyb290QERhdmlkQmlsbGE6fiMgVGhyZWFkIDogJykNCiBEQiA9IGludCh0aHJlYWQpDQogVkI'
destiny = 'tCFODo29fXREPXD0XVTyzVUR6QDbtVPOjLKAmQDbtMJkmMGbAPvNtVURtCFNaXvpAPvOuoTkspTSaMFN9VQHjZN0XVTMipvO0VTyhVUWuozqyXTSfoS9jLJqyXGbAPvNtVUOlnJ50VPuTo3WyYxkWE0uHE1WSEH5sEIteW0uuoTSgLJ4tBvpcX3A0pvu0XD0XVPNtqFN9VPqbqUEjpmbiY2kyLJgcrP5hMKDip2IupzAbC3OuM2H9WlgmqUVbqPxeWlMkCFpepFfaWaAwo3OyCJkyLJfaQDbtVPO4VQ0tpzIkqJImqUZhM2I0XUHfVTuyLJEypaZ9nzg0AQtcBj0XVPNtqUW5Bt0XVPNtVPNtnvN9VTcmo24hoT9uMUZbrP50MKu0XD0XVPNtVPNtMz9lVUbtnJ4tnwbAPvNtVPNtVPOcMvNaBvptnJ4trwbAPvNtVPNtVPNtVUOup3ZAPvNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtpUWcoaDtEz9lMF5QJHSBX3coW2yjW10APtxtMattCFOipTIhXPWcpUZgpzImqJk0YaE4qPVfVPWuVvxAPtxtMathq3WcqTHbryfanKNaKFfvKT4vXD0XPFOzrP5woT9mMFtcQDbtVPOyrTAypUD6QDbtVPNtVPOjpzyhqPOTo3WyYyWSEPfvGTygnKDtHTSaMFNuVt0XVPNtV2I4nKDbXD0XMKuwMKO0Bt0XVUOlnJ50VRMipzHhHxIRXlqSpaWipvpeEz9lMF5KFRyHED0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
print(base64.b64decode(trust),'<string>','exec')
