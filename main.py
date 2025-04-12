import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=10.75&lon=106.66667&appid=53c361690f181bb571cb47a71dd2e5cd"

ketqua = requests.get(url)

print(ketqua.status_code)

print(ketqua.json()["weather"][0]["main"])