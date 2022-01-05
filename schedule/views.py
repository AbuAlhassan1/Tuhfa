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
    start_time: datetime.time = None,
    end_time: datetime.time = None,
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
            schedule = Schedule.objects.create(day=day, date=date, category=get_category_by_id, start_time=start_time, end_time=end_time)
        except:
            return {
                'message': 'Somthing Went Wrong',
            }
    if category_name and not category_id:
        try:
            schedule = Schedule.objects.create(day=day, date=date, category=get_category_by_name[0], start_time=start_time, end_time=end_time)
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
        schedule = Schedule.objects.filter(date=date)
    except:
        return {
            'message': 'No Such A Schedule !!!',
        }

    return 200, schedule

# -----------------------------------------------------------------------------

# Retrieve Schedule[s] By Start Time
@schedule_controller.get('retrieve_schedule_by_start_time', response={
    200: List[ScheduleOut],
    404: MessageOut,
    500: MessageOut
})
def retrieve_schedule_by_start_time(request, start_time: datetime.time):
    try:
        schedule = Schedule.objects.filter(start_time=start_time)
    except:
        return {
            'message': 'No Such A Schedule !!!',
        }

    return 200, schedule

# -----------------------------------------------------------------------------

# Retrieve Schedule[s] By End Time
@schedule_controller.get('retrieve_schedule_by_end_time', response={
    200: List[ScheduleOut],
    404: MessageOut,
    500: MessageOut
})
def retrieve_schedule_by_end_time(request, end_time: datetime.time):
    try:
        schedule = Schedule.objects.filter(end_time=end_time)
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
def update_schedule(request, 
    id: int,
    category_id: int = None,
    day: str = None,
    date: datetime.date = None,
    start_time: datetime.time = None,
    end_time: datetime.time = None,
):
    try:
        schedule = Schedule.objects.get(id=id)
    except:
        return {
            'message': 'Somthing Went Wrong !!!',
        }
    
    try:
        get_categroy = Category.objects.get(id=category_id)
    except:
        return {
            'message': 'Category Not Found !!!',
        }

    schedule.day = day
    schedule.date = date
    schedule.start_time = start_time
    schedule.end_time = end_time
    schedule.category = get_categroy

    schedule.save()

    return 200, schedule

# -----------------------------------------------------------------------------

# Update Schedule by Date
# @schedule_controller.put('update_by_id', response={
#     200: ScheduleOut,
#     404: MessageOut,
#     500: MessageOut
# })
# def update_schedule(request, 
#     date: datetime.date,
#     category_id: int = None,
#     day: str = None,
#     new_date: datetime.date = None,
#     start_time: datetime.time = None,
#     end_time: datetime.time = None,
# ):
#     try:
#         schedule = Schedule.objects.filter(date=date)
#     except:
#         return {
#             'message': 'Somthing Went Wrong !!!',
#         }
    
#     try:
#         get_categroy = Category.objects.get(id=category_id)
#     except:
#         return {
#             'message': 'Category Not Found !!!',
#         }

#     schedule.day = day
#     schedule.date = date
#     schedule.start_time = start_time
#     schedule.end_time = end_time
#     schedule.category = get_categroy

#     schedule.save()

#     return 200, schedule

# -----------------------------------------------------------------------------