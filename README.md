# kong-poc
```bash
> url -i -X GET http://0.0.0.0:8000/clients/s4f4d4/qualify
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 524
Connection: keep-alive
Date: Wed, 17 Nov 2021 22:23:39 GMT
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
X-Kong-Upstream-Latency: 364
X-Kong-Proxy-Latency: 2233
Via: kong/2.3.3

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.68.0",
    "X-Amzn-Trace-Id": "Root=1-619580eb-03351ce14b4a22d1055921ad",
    "X-Forwarded-Host": "0.0.0.0",
    "X-Forwarded-Path": "/clients/s4f4d4/qualify",
    "X-Forwarded-Prefix": "/clients/s4f4d4/qualify",
    "X-Tentant-Id": "s4f4d4"
  },
  "json": null,
  "method": "GET",
  "origin": "172.26.0.1",
  "url": "http://0.0.0.0/anything"
}

```