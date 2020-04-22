import requests

url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format":"json","code":"it"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "ZKlG5cLvaUmshojyPCrah5is1K9sp1qo8d5jsnNIAX62y2AJkI"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.content)