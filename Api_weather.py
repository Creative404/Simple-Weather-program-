from time import sleep
import requests
from unidecode import unidecode

HIDDEN_API_XD = "9b2f90024cef0b54d1f8"
day_checker = True
weather_program = True

sleep(0.1)
print("\nWelcome in simple weather program\n")
sleep(0.4)

while weather_program:

    while day_checker:
        try:
            day = int(input("How much day ahead you wanna know? (0-7days default: today ): "))
            if day >= 0 and 7 >= day:
                day_checker = False
                day_counter = day
            else:
                print("enter value in range 0-7")
        except ValueError:
            print("please type correct value\n")
            sleep(0.1)

    sleep(0.1)
    city = input("What city you want check?: ").lower()
    city = unidecode(city)
    city = city.replace(" ","-")

    for days in range(day+1):
        url = f"https://dobrapogoda24.pl/api/v1/weather/simple?city={city}&day={days}&token={HIDDEN_API_XD}"
        connection = requests.get(url)

        if connection.status_code == 200:
            json_converted = connection.json()
            weather = json_converted
            day = weather['day']
            night = weather['night']

            print(f"\n\ndate: {weather['date']}\n")
            sleep(0.1)
            print("Day:")
            print(f"temperature max: {day["temp_max"]} ℃")
            print(f"temperature min: {day["temp_min"]} ℃")
            print(f"temperature (felt) max: {day["temp_felt_max"]} ℃")
            print(f"temperature (felt) min: {day["temp_felt_min"]} ℃")
            print(f"humidity: {day["humidity"]} %")

            sleep(1)

            print("\nNight:")
            print(f"temperature max: {night["temp_max"]} ℃")
            print(f"temperature min: {night["temp_min"]} ℃")
            print(f"temperature (felt) max: {night["temp_felt_max"]} ℃")
            print(f"temperature (felt) min: {night["temp_felt_min"]} ℃")

            if day_counter > 0:
                input("\npress anything to show next day")
                day_counter -= 1

            elif day_counter == 0:
                decison = input("\npress anything to check diffrent city or exit(type exit): ").lower()

                if decison == "exit":
                    weather_program = False





        elif connection.status_code == 404:
            print("Error 404: city not Found\n")
            sleep(0.4)

        elif connection.status_code == 401:
            weather_program = False
            Error = 401
            print("Error 401: Unauthorized or invalid API key\n")
            sleep(0.4)

        elif connection.status_code == 500:
            print("Error 500: Internal Server Error \n")
            sleep(0.4)
            weather_program = False
            Error = 500

        else:
            print("Error\n")
            sleep(0.4)

    day_checker = True


if Error == 401:
    print("API is invalid contact creator and report this problem")
    input("press any key to exit:")

elif Error == 500:
    print("Internal error try later")
    input("press any key to exit:")

print("Thanks for using my simple weather program")
sleep(1)
exit()