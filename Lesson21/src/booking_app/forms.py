from django import forms


class BookingRoom(forms.Form):
    hotel_name = forms.CharField(max_length=255, initial='Hill Inc')
    number_of_room = forms.CharField(max_length=10, initial='2')
    user = forms.CharField(max_length=50, initial='Jose Smith')
    start_date = forms.DateField(initial='2024-06-01')
    end_date = forms.DateField(initial='2024-06-02')
