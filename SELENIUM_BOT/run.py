from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.currency_change("USD")
        bot.destination("Kathmandu")
        bot.booking_date("2025-04-23", "2025-04-25")
        bot.no_of_passengers(5)
        bot.search()
        bot.apply_filter()
        bot.result()
except:
    print("SORRY FOR THE INCONVENIENCE, THERE'S A PROBLEM AT THE MOMENT")

