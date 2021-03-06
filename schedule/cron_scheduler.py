from crontab import CronTab
import os


USER = 'pi'


def create_cron(name: str, hour: int, id_: str, slot: int, phone_num: str = '9786185596'):
    """
    - adds a new cron job to run the dispenser script on dow day of the week
      at time time of the day
    - cron job will have comment <id>
    - parameters
        - dow is "SUN"-"MON"
        - hour is int: 0-23
        - number is the number to dispense
        - slot is the number to rotate to
    """
    print("cron-scheduler - create_cron id: " + str(id_) + " hour: " + str(hour))
    cron = CronTab(user=USER)
    job = cron.new(command='python3 /home/pi/Desktop/IOT-Automatic-Pill-Dispenser/schedule/dispense.py "{}" "{}" "{}"'.format(name, str(slot), phone_num), comment='{}'.format(id_))
    if hour < 0:
        job.minute.every(2)
    else:
        job.hour.on(hour)
        job.minute.on(int((slot * 2.5) // 1))
    cron.write(user=USER)
    os.system('service cron start')


def remove_cron(id_: str):
    """
    - removes a cron job with name <id_>
    """
    print("cron_scheduler - remove_cron id: " + str(id_))
    cron = CronTab(user=USER)
    commands = cron.remove_all(comment='{}'.format(id_))
    cron.write(user=USER)

