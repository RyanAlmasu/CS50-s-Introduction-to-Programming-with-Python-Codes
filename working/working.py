import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d\d?[:\s][0-5]?\d?\s?[APM]+)\sto\s(\d\d?[:\s][0-5]?\d?\s?(?:AM|PM))$", s):
        return f"{to_24(matches.group(1))} to {to_24(matches.group(2))}"
    raise ValueError

def to_24(time):
    minutes = "00"
    if ":" in time:
        hour, am_pm = time.split(" ")
        hour, minutes = hour.split(":")
    else:
        hour, am_pm = time.split(" ")
    if int(hour) > 12:
        raise ValueError

    if am_pm == "AM":
        if hour == "12":
            return '00' + ':' + minutes
        else:
            return hour.zfill(2) + ':' + minutes
    elif am_pm == "PM":
        if hour == "12":
            return hour.zfill(2) + ':' + minutes
        else:
            return str(int(hour) + 12) + ':' + minutes

if __name__ == "__main__":
    main()