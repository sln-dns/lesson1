weather = {
    "city" : "Москва",
    "temperature" : "20"
}
print(weather["city"])

decrease = int(input('Введите уменьшение температуры '))
weather["temperature"] = int(weather["temperature"]) - decrease
print(weather)
print(weather.get("contry", "Россия"))
weather["date"] = "27.05.2019"
print(len(weather))
