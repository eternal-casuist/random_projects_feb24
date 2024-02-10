import time
import datetime
import pygame
pygame.init()

path="copy song location"
pygame.mixer.music.load(path)

invalid=True

while(invalid):
    print("ENter time in  HH:MM", end="")
    userinput=input(">>")

    alarmTime=[int(n) for n in userinput.split(":")]
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False
    seconds_hms = [3600, 60, 1]
    alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

    now = datetime.datetime.now()
    currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])


    secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

    if secondsUntilAlarm < 0:
        secondsUntilAlarm += 86400

    print("Alarm is set!")
    print("The alarm will ring in %s" % datetime.timedelta(seconds=secondsUntilAlarm))

    #pygame.mixer.music.play()
    #time.sleep(secondsUntilAlarm)
    
    for i in range(0, secondsUntilAlarm):
        time.sleep(1)
        secondsUntilAlarm -= 1
        print(datetime.timedelta(seconds=secondsUntilAlarm))
        

    pygame.mixer.music.play()
    time.sleep(20)

    print("Ring Ring... time to wake up!")
    
pygame.quit()

    
