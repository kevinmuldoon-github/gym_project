# Controller for booking functionality

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html' , title = 'Bookings' , bookings = bookings)



# Function to delete a booking
@bookings_blueprint.route("/bookings/<id>/delete" , methods = ['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect ('/bookings') # Redirect user back to the main bookings page