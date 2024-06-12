from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView

from .models import Person, Hotels, HotelsComment, User, Room, Booking, Feedback, Comment
from .forms import BookingRoom, UserModelAddForm, FeedbackModelAddForm


# Create your views here.
def index(request):
    return render(request=request, template_name="base.html")


def hotels(request):
    hotels_list = [
        {"name": "Happy Hotel", "address": "123 Main Street, Anytown", "stars": 2},
        {"name": "Cozy Cottage Inn", "address": "456 Elm Avenue, Somewhereville", "stars": 1},
        {"name": "Sunset Resort", "address": "789 Beach Road, Paradise City", "stars": 3},
        {"name": "Mountain View Lodge", "address": "101 Pine Lane, Serenity Valley", "stars": 4},
        {"name": "Tranquil Retreat", "address": "555 Lakefront Drive, Peaceful Town", "stars": 5},
    ]
    context = {'hotel_list': hotels_list}

    return render(
        request=request,
        template_name="hotels.html",
        context=context,
    )


def users(request):
    context = {
        'users_list': User.objects.all()
    }

    return render(
        request=request,
        template_name="users.html",
        context=context,
    )


@login_required(login_url="/admin/login/")
@permission_required("booking_app.view_persons")
def persons(request):
    context = {
        'persons_list': Person.objects.all().prefetch_related("hotel_comments").prefetch_related("hobbies")
    }

    return render(
        request=request,
        template_name="persons.html",
        context=context,
    )


def hotels_view(request):
    context = {
        'hotels_list_view': Hotels.objects.all().prefetch_related("owners").prefetch_related("hotel_comments")
    }

    return render(
        request=request,
        template_name="hotels_view.html",
        context=context,
    )


# перенаправление на страницу, если успешно забронирована комната
def details_orders_view(request):
    context = {
        'Details': Booking.objects.all()
    }

    return render(
        request=request,
        template_name="details_orders.html",
        context=context,
    )


def booking_form_view(request, error=''):
    form = BookingRoom()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'booking_form.html', context)


# получаем имя постояльца
def get_user_full_name(full_name):
    first_name, last_name = full_name.split()
    return User.objects.get(Q(first_name=first_name) & Q(last_name=last_name))


# получить номер комнаты из отеля
def get_room_from_hotel(number_of_room, hotel_name):
    return Room.objects.get(hotel__name=hotel_name, number=number_of_room)


# сделать бронирование комнаты
def book_room(request):
    if request.method == "POST":
        form = BookingRoom(request.POST)
        if form.is_valid():
            # import pdb
            # pdb.set_trace()
            number_of_room = int(request.POST['number_of_room'])
            hotel_name = request.POST['hotel_name']
            user = request.POST['user']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']

            try:
                room = get_room_from_hotel(number_of_room, hotel_name)
            except:
                # messages.error(request, "Отель не найден")
                return booking_form_view(request, error='Комната не найдена')

            try:
                hotel = Hotels.objects.get(name=hotel_name)
            except Hotels.DoesNotExist:
                # messages.error(request, "Отель не найден")
                return booking_form_view(request, 'Отель не найден')

            try:
                user = get_user_full_name(user)
            except User.DoesNotExist:
                # messages.error(request, "Пользователь не найден")
                return booking_form_view(request, 'Пользователь не найден')

            is_room_booked = Booking.objects.filter(
                room__hotel__name=hotel_name,
                room__number=number_of_room,
                start_date__lte=start_date,
                end_date__gte=end_date
            ).exists()
            # print(is_room_booked)

            if not is_room_booked:
                with transaction.atomic():
                    Booking.objects.create(
                        room=room,
                        start_date=start_date,
                        end_date=end_date,
                        customer_full_name=user,

                    )
                    room.is_booked = True
                    # room.user = user
                    room.save()
                return booking_form_view(request, error='Бронирование сформировано')
            else:
                return booking_form_view(request, error='Данная комната уже забронирована')
        print(form.errors)
    return booking_form_view(request, error='')


def feedback_add_view(request, error=''):
    form = FeedbackModelAddForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add_feedback.html', context)


def feedback_add(request):
    if request.method == "POST":
        form = FeedbackModelAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("feedbacks")
        # print(form.errors)
    return feedback_add_view(request, error='')


def feedbacks_view(request):
    context = {
        'feedbacks': Feedback.objects.all()
    }

    return render(
        request=request,
        template_name="feedbacks.html",
        context=context,
    )


users_list = [
        {
            "name": "John",
            "age": 25,
            "comments": ["Great post!", "I totally agree with you."]
        },
        {
            "name": "Alice",
            "age": 30,
            "comments": ["Interesting perspective.", "Nice work!"]
        },
        {
            "name": "Bob",
            "age": 28,
            "comments": ["Thanks for sharing.", "Well written."]
        },
        {
            "name": "Emily",
            "age": 35,
            "comments": ["I have a question.", "This is helpful."]
        },
        {
            "name": "David",
            "age": 22,
            "comments": ["I learned something new.", "Keep up the good work!"]
        },
        {
            "name": "Emma",
            "age": 27,
            "comments": ["Great post!", "I totally agree with you."]
        },
        {
            "name": "Michael",
            "age": 33,
            "comments": ["Interesting perspective.", "Nice work!"]
        },
        {
            "name": "Sophia",
            "age": 29,
            "comments": ["Thanks for sharing.", "Well written."]
        },
        {
            "name": "William",
            "age": 31,
            "comments": ["I have a question.", "This is helpful."]
        },
        {
            "name": "Olivia",
            "age": 26,
            "comments": ["I learned something new.", "Keep up the good work!"]
        }
    ]


def user_comments_view(request):

    context = {'users_list': users_list}

    return render(
        request=request,
        template_name="comments.html",
        context=context,
    )


class CommentTemplateView(ListView):
    template_name = "comments.html"
    model = HotelsComment
    queryset = HotelsComment.objects.all()
    context_object_name = "comments"
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comments"] = HotelsComment.objects.all()
    #     return context


def user_add_view(request, error=''):
    form = UserModelAddForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'user_add.html', context)


def user_add(request):
    if request.method == "POST":
        form = UserModelAddForm(request.POST)
        if form.is_valid():
            form.save()
    return user_add_view(request, error='')


class UserFormView(CreateView):
    template_name = 'user_add.html'
    form_class = UserModelAddForm
    success_url = '/booking_app/users'
