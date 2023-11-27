import http.client

conn = http.client.HTTPSConnection("api.gptzero.me")

payload = "{\n  \"document\": \"string\",\n  \"version\": \"string\"\n}"

headers = {
    'x-api-key': "",
    'Content-Type': "application/json",
    'Accept': "application/json"
}

conn.request("POST", "/v2/predict/text", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))