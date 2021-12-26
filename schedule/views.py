from typing import List
from django.shortcuts import render
from ninja import Router
from Tuhfa.utils.schemas import MessageOut, ScheduleIn, ScheduleOut
from .models import Schedule
import datetime

schedule_controller = Router(tags=['schedule'])

# -----------------------------------------------------------------------------

# Create Schedule
@schedule_controller.post('create', response={
    201: ScheduleOut,
    400: MessageOut,
    200: MessageOut,
    500: MessageOut,
    409: MessageOut
})
def create_schedule(request,
    Sunday: str = None,
    Monday: str = None,
    Tuesday: str = None,
    Wednesday: str = None,
    Thursday: str = None,
    Friday: str = None,
    Saturday: str = None
):

    is_admin_create_any_schedule_today = Schedule.objects.filter(created__date=datetime.date.today())
    # Schedule.objects.raw('SELECT * FROM Schedule WHERE created=%s', [datetime.date.today()])

    if not is_admin_create_any_schedule_today:
        try:
            schedule = Schedule.objects.create(
                Sunday=Sunday,
                Monday=Monday,
                Tuesday=Tuesday,
                Wednesday=Wednesday,
                Thursday=Thursday,
                Friday=Friday,
                Saturday=Saturday
            )
        except:
            return {
                'message': 'Somthing Went Wrong !!!',
            }

        return 201, schedule
    else:
        return 200,{
            'message': 'You Can Create Schedule Only Once Per Day !!! If SomeThing Went Wrong Please Update The Exist Schedule !!!',
        }

# -----------------------------------------------------------------------------

# Retrieve All Schedules
@schedule_controller.get('retrieve_all_schedules', response={
    200: List[ScheduleOut],
    500: MessageOut
})
def retrieve_all_schedules(request):
    try:
        schedules = Schedule.objects.all()
    except:
        return {
            'message': 'Somthing Went Wrong !!!',
        }

    return 200, schedules

# -----------------------------------------------------------------------------

# Retrieve Schedule By ID
@schedule_controller.get('retrieve_schedule_by_id', response={
    200: ScheduleOut,
    404: MessageOut,
    500: MessageOut
})
def retrieve_schedule_by_id(request, id: int):
    try:
        schedule = Schedule.objects.get(id=id)
    except:
        return {
            'message': 'Somthing Went Wrong !!!',
        }

    return 200, schedule

# -----------------------------------------------------------------------------

# Retrieve Schedule[s] By Date
@schedule_controller.get('retrieve_schedule_by_date', response={
    200: List[ScheduleOut],
    404: MessageOut,
    500: MessageOut
})
def retrieve_schedule_by_date(request, date: str):
    try:
        schedule = Schedule.objects.filter(created__icontains=date)
    except:
        return {
            'message': 'No Such A Schedule !!!',
        }

    return 200, schedule

# -----------------------------------------------------------------------------

# Update Schedule by id
@schedule_controller.put('update_by_id', response={
    200: ScheduleOut,
    404: MessageOut,
    500: MessageOut
})
def update_schedule(request, id: int,
    Sunday: str = None,
    Monday: str = None,
    Tuesday: str = None,
    Wednesday: str = None,
    Thursday: str = None,
    Friday: str = None,
    Saturday: str = None
):
    try:
        schedule = Schedule.objects.get(id=id)
    except:
        return {
            'message': 'Somthing Went Wrong !!!',
        }

    schedule.Sunday = request.Sunday
    schedule.Monday = request.Monday
    schedule.Tuesday = request.Tuesday
    schedule.Wednesday = request.Wednesday
    schedule.Thursday = request.Thursday
    schedule.Friday = request.Friday
    schedule.Saturday = request.Saturday

    schedule.save()

    return 200, schedule

# -----------------------------------------------------------------------------

# Update Schedule by Date
@schedule_controller.put('update_by_date', response={
    200: ScheduleOut,
    404: MessageOut,
    500: MessageOut
})
def update_schedule_by_date(request,date: str,
    Sunday: str = None,
    Monday: str = None,
    Tuesday: str = None,
    Wednesday: str = None,
    Thursday: str = None,
    Friday: str = None,
    Saturday: str = None
):
    try:
        schedule = Schedule.objects.filter(created__icontains=date)
    except:
        return {
            'message': 'Somthing Went Wrong !!!',
        }

    if len(schedule) > 1:
        return {
            'message': 'Thir is more than one schedule !!!',
        }

    schedule.Sunday = request.Sunday
    schedule.Monday = request.Monday
    schedule.Tuesday = request.Tuesday
    schedule.Wednesday = request.Wednesday
    schedule.Thursday = request.Thursday
    schedule.Friday = request.Friday
    schedule.Saturday = request.Saturday

    schedule.save()

    return 200, schedule

# -----------------------------------------------------------------------------