from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(hour="*", minute=5)), name="", ignore_result=True)
def perform_base_online_checkup():
    """
    Make lookups across worlds, log players and create models
    later used as source for online time counters
    """
    print('check')
    pass
