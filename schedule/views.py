from typing import List
from django.shortcuts import render
from ninja import Router
from Tuhfa.utils.schemas import MessageOut, ScheduleOut
from categories.models import Category
from .models import Schedule
import datetime

schedule_controller = Router(tags=['schedule'])

# -----------------------------------------------------------------------------

# Create Schedule
@schedule_controller.post('create', response={
    201: ScheduleOut,
    400: MessageOut,
    404: MessageOut,
    200: MessageOut,
    500: MessageOut,
    409: MessageOut
})
def create_schedule(request,
    day: str = None,
    date: datetime.date = None,
    category_id: int = None,
    category_name: str = None,
):

    # is_admin_create_any_schedule_today = Schedule.objects.filter(created__icontains=datetime.date.today())

    # if not is_admin_create_any_schedule_today:

    if category_id:
        try:
            get_category_by_id = Category.objects.get(id=category_id)
        except:
            return 404, {
                'message': 'Thir Is No Category With This ID'
            }
    if category_name:
        try:
            get_category_by_name = Category.objects.filter(name__icontains=category_name)
        except:
            return 404, {
                'message': 'Thir Is No Category With This Name'
            }

    if category_id and category_name:
        return {
            'message': 'You Can Not Use Category ID And Category Name At The Same Time'
        }

    if category_id and not category_name:
        try:
            schedule = Schedule.objects.create(day=day, date=date, category=get_category_by_id)
        except:
            return {
                'message': 'Somthing Went Wrong',
            }
    if category_name and not category_id:
        try:
            schedule = Schedule.objects.create(day=day, date=date, category=get_category_by_name[0])
        except:
            return {
                'message': 'Somthing Went Wrong !!!',
            }

    return 201, schedule

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
def retrieve_schedule_by_date(request, date: datetime.date):
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