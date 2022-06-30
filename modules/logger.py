from time import localtime, sleep


# Function which checking list of data on length
def checked_time() -> dict:
    # Getting values and appending our list with time
    time = [localtime().tm_mday, localtime().tm_mon,
            localtime().tm_year, localtime().tm_hour, localtime().tm_min]
    data = {
        "month": time[0],
        "d_month": time[1],
        "year": time[2],
        "hour": time[3],
        "minutes": time[4],
    }
    # Iteration in dictionary for better numbers in name of log 
    for i in data:
        if len(str(data[i])) == 1:
            data.update({i: f'0{data[i]}'})
    return data


# The main function which contains the general script's logic
def main():
    while True:
        time = checked_time()
        # Checking every 30 minutes
        sleep(60 * 30)
        # Creating logs with data at the moment
        with open(f'logs/{time["month"]}.{time["d_month"]}.{time["year"]}-{time["hour"]}.{time["minutes"]}.log', 'w') as f:
            pass


if __name__ == '__main__':
    main()
