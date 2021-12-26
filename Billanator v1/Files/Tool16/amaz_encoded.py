import base64, codecs
magic = 'CnByaW50KCJbK11BbWF6b24gVmFsaWQgRW1haWwgQ2hlY2tlciIpCmltcG9ydCByZXF1ZXN0cwpsaXZlID0gb3BlbignQW1hem9uX2xpdmUudHh0JywgJ3cnKQpkZWFkID0gb3BlbignQW1hem9uX2RlYWQudHh0JywgJ3cnKQpDaGVja2VkID0gIkNoZWNrZWQgYnkgRGF2aWRCaWxsYSIKcHJpbnQoIl8iKjUwKQpwcmludCgiQW1hem9uIFZhbGlkIEVtYWlsIENoZWNrZXIiKQpwcmludCgiICIpCmxpc3Q9IGlucHV0KCJFbnRlciBFbWFpbCBMaXN0IDoiKQpsaW5rID0gImh0dHBzOi8vd3d3LmFtYXpvbi5jb20vYXAvcmVnaXN0ZXIlM0ZvcGVuaWQuYXNzb2NfaGFuZGxlJTNEc21hbGxwYXJ0c19hbWF6b24lMjZvcGVuaWQuaWRlbnRpdHklM0RodHRwJTI1M0ElMjUyRiUyNTJGc3BlY3Mub3BlbmlkLm5ldCUyNTJGYXV0aCUyNTJGMi4wJTI1MkZpZGVudGlmaWVyX3NlbGVjdCUyNm9wZW5pZC5ucyUzRGh0dHAlMjUzQSUyNTJGJTI1MkZzcGVjcy5vcGVuaWQubmV0JTI1MkZhdXRoJTI1MkYyLjAlMjZvcGVuaW'
love = 'DhL2kunJ1yMS9cMPHmETu0qUNyZwHmDFHlAGWTWGV1ZxMmpTIwpl5ipTIhnJDhozI0WGV1ZxMuqKEbWGV1ZxLlYwNyZwHlEzyxMJ50nJMcMKWsp2IfMJA0WGV2o3OyozyxYaWyqUIloy90olHmETu0qUOmWGV1Z0RyZwHlEvHlAGWTq3q3YaAgLJkfpTSlqUZhL29gWGV1ZxMmnJqhnJ4yZwMgLKWeMKEDoTSwMHyxWGARDGWMDycCHHkVJGVmIIDyZwMwoTyyoaEQo250MKu0WGARZGt3YGRmZmRlZwNgBQHkZQZjAlHlAaOuM2IWMPHmETS1qTujo3W0LJkspzIanKA0MKVyZwMipTIhnJDhoJ9xMFHmETAbMJAenJEsp2I0qKNyZwMmnKEyH3EuqTHyZ0EznJ5uoSWyqUIloyEiIKWfWGV1Z0EbqUEjplHlAGV1Z0RyZwHlAGWTWGV1ZwHlEaq3ql5moJSfoUOupaEmYzAioFHlAGV1ZxMwo250LJA0qKZyZwHlAGWTZGt3YGRmZmRlZwNgBQHkZQZjAlHlAGV1Z0MupUOOL3Eco24yZwHlAGARD29hqTSwqSImGTShMTyhMlHlAGV1ZwMjMy9lMS9gWGV1ZwHmERRlGSOIF1tlEGqBHSSJWGV1ZwHlAzSjpRSwqTyioyEin2IhWGV1'
god = 'MjUzRGxwdGtlVVFmYmhvT1UzdjRTaHlNUUxpZDUzWWozRCUyNTI1MjZpZSUyNTI1M0RVVEY4JTI1MkNyZWdpc3QlMjUzRHRydWUiCmhlYWQgPSB7J1VzZXItYWdlbnQnOidNb3ppbGxhLzUuMCAoaVBob25lOyBDUFUgaVBob25lIE9TIDEyXzAgbGlrZSBNYWMgT1MgWCkgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzEyLjAgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjEnfQpzID0gcmVxdWVzdHMuc2Vzc2lvbigpCmcgPSBzLmdldChsaW5rLCBoZWFkZXJzPWhlYWQpCmxpc3QgPSBvcGVuKGxpc3QsICdyJykKcHJpbnQoIi0iKjU1KQp3aGlsZSBUcnVlOgoJZW1haWwgPSBsaXN0LnJlYWRsaW5lKCkucmVwbGFjZSgnXG4nLCcnKQoJaWYgbm90IGVtYWlsOgoJCWJyZWFrCgliYWtlciA9IGVtYWlsLnN0cmlwKCkuc3BsaXQoJzonKQoJeHh4ID0geydjdXN0b21lck5hbWUnOidNYXNrb2ZmJywnZW1haWwnOiBiYWtlclswXSwnZW1haWxDaGVjayc6IGJha2VyWzBdLC'
destiny = 'qjLKAmq29lMPp6W0EuqzyxDzyfoTRaYPqjLKAmq29lMRAbMJAeWmbaDKEmnJgmMT9hMmRmZmpasDbWo3NtCFOmYaOip3DboTyhnljtnTIuMTIlpm1bMJSxYPOxLKEuCKu4rPxhqTI4qNbWnJLtVyyiqFOcozEcL2S0MJDtrJ91VTSlMFOuVT5yqlOwqKA0o21ypvjtLaI0VTShVTSwL291oaDtLJklMJSxrFOyrTymqUZtq2y0nPO0nTHtMF1gLJyfVvOcovOipQbXPDyjpzyhqPtvKQNmZ1fmZwfkoHkWIxIpZQZmJmOgVUjtVvgyoJScoPfvVUjtCG0+VRAbMJAeMJDvXDbWPJkcqzHhq3WcqTHbMJ1unJjtXlNaKT4aXDbWMJkmMGbXPDyjpzyhqPtvKQNmZ1fmZGfkoHESDHEpZQZmJmOgVUjtVvgyoJScoPfvVUjtCG0+VRAbMJAeMJDvXDbWPJEyLJDhq3WcqTHbMJ1unJjtXlNaKT4aXDcjpzyhqPtvYFVdAGNcPaOlnJ50XPWpZQZmJmZ1BmSgDHkZVRIADHyZHlOQFRIQF0IRVSAID0ASH1ATIHkZJIjjZmAoZT0vXDcjpzyhqPtvDJ1urz9hVSMuoTyxVRIgLJyfVUquplOGLKMyMPOcovOOoJS6o25soTy2MF50rUDvXDbX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
print(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec')