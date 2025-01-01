# gladysngangaextracredit_168120

# Airline System API

Welcome to the **Airline System API**, a robust platform for managing flights, passengers, and bookings. Built using Django, this API supports dynamic pricing, seat selection, ticket issuance, and more, providing seamless interaction through RESTful endpoints.

---

## Getting Started

### Prerequisites
To run this project, ensure you have:
- Python 3.12 or higher
- Django 5.x
- Django REST Framework
- SQLite (default) or any preferred database

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/gladysnjoki05/gladysngangaextracredit_168120
    cd gladysngangaextracredit_168120
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
Access the API at `http://127.0.0.1:8000/api/`.

---

## API Endpoints

### Flights
- **GET /api/flights/**: List all flights.
- **POST /api/flights/**: Add a new flight.
- **GET /api/flights/{id}/**: View a specific flight.
- **PUT /api/flights/{id}/**: Update flight details.
- **DELETE /api/flights/{id}/**: Delete a flight.

### Passengers
- **GET /api/passengers/**: List all passengers.
- **POST /api/passengers/**: Add a new passenger.
- **GET /api/passengers/{id}/**: View a specific passenger.
- **PUT /api/passengers/{id}/**: Update passenger details.
- **DELETE /api/passengers/{id}/**: Remove a passenger.

### Bookings
- **GET /api/bookings/**: List all bookings.
- **POST /api/bookings/**: Create a new booking.
- **GET /api/bookings/{id}/**: View a booking.
- **PUT /api/bookings/{id}/**: Update a booking.
- **DELETE /api/bookings/{id}/**: Cancel a booking.

---

## Core Features

### Models

1. **Flight**
   - Contains details like flight number, schedules, origin, destination, capacity, and pricing.
   - Supports dynamic seat classes (Economy, Business, First-Class) via a JSONField.
   - Method: `calculate_dynamic_price()` to adjust pricing based on demand and seat class.

2. **Passenger**
   - Stores personal details and seat class preferences.

3. **Booking**
   - Links passengers to one or more flights.
   - Method: `calculate_total_price()` to compute the booking total with dynamic pricing.

### Serializers
- Convert model instances to JSON and validate API inputs.
- **FlightSerializer**, **PassengerSerializer**, and **BookingSerializer** handle respective models.

### Views
- Built with `viewsets.ModelViewSet` for automatic CRUD operations.
- Includes `FlightViewSet`, `PassengerViewSet`, and `BookingViewSet`.

### Signals
- Automatically generates PDF tickets when a passenger's seat class is confirmed.
- Utilizes the `issue_ticket()` signal with the `ReportLab` library.

---

## Advanced Features

- **Dynamic Pricing**: Adjusts ticket costs based on seat availability and demand.
- **PDF Ticket Generation**: Automatically issues a ticket upon passenger confirmation.
- **Multi-leg Bookings**: Supports many-to-many relationships between bookings and flights.

---

## Testing the API

1. Add test data via the Django Admin panel or shell.
2. Test endpoints using Postman or any REST client for various HTTP methods (GET, POST, PUT, DELETE).

---

## Contributing

We welcome contributions! Fork the repository, make your changes, and submit a pull request. Review the [LICENSE](LICENSE) for terms.

---

## License

This project is open-source and available under the MIT License.

