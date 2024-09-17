from itertools import count

"""Model for aircraft flights 
"""

class Flight:
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in {number}")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code {number}")
        if not number[2:].isdigit() and int(number[2:]) >= 9999:
            raise ValueError(f"Invalid route number {number}")
        
        self._number  = number
        self._aircraft = aircraft
        rows,seats = self._aircraft.seating_plan()
        self._seating  = [None] + [{letter: None for letter in seats} for _ in rows]
        
    def aircraft_model(self):
        return self._aircraft.model()
    
    def numbers(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)  
                   for row in self._seating 
                   if row is not None)
    
    def booking_seat(self, seat, passenger):
        """Allocates a seat to a passenger
        Args: 
            seat: A seat designator such as 12c, 20b
            passenger: the name of a passenger
            
        Raises:
            ValueError: if the seat is not available
        """
        row, seat_letter = self._parse_seat(seat)
        
        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"Seat {seat} is taken")
        
        self._seating[row][seat_letter] = passenger
        
    # move a passenger
    def relocate_passenger(self, from_seat, to_seat):
        """Relocates a passenger from one seat to another
        
            Args:
                from_seat: A seat where a passenger originally seats e.g. 20F
                to_seat A seat where a passenger intends to relocate to
            Raises:
                ValueError: in case from_seat is empty or to_seat is occupied
        """
        from_row, from_seat_letter = self._parse_seat(from_seat)
        to_row, to_seat_letter = self._parse_seat(to_seat)
        
        
        if self._seating[from_row][from_seat_letter] is None:
            raise ValueError(f"Seat {from_seat} is not occupied")
        
        if self._seating[to_row][to_seat_letter] is not None:
            raise ValueError(f"Seat {to_seat} is taken")
        
        self._seating[to_row][to_seat_letter] = self._seating[from_row][from_seat_letter]
        self._seating[from_row][from_seat_letter] = None
    
    # validate a seat 
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        seat_letter = seat[-1]
        
        if seat_letter not in seat_letters:
            raise ValueError("Invalid seat")
        
        row_num = seat[:-1]
        try:
            row = int(row_num)
        except ValueError:
            raise ValueError("Invalid seat row")
        
        if row not in rows:
            raise ValueError("Invalid row number")
        
        return row, seat_letter
    
    def make_boarding_cards(self, card_printer):
        """ Prints boarding cards for all passengers
            Args:
                card_printer: a function that prints out cards
        """
        for passenger, seat in sorted(self._occupied_seats()):
            card_printer(passenger, seat, self._number, self.aircraft_model())
            
    # gets all occupied seats and the passenger
    def _occupied_seats(self):
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in seats:
                passenger = self._seating[row][seat]
                if  passenger is not None:
                    yield(passenger, f"{row}{seat}")
    
class Aircraft:
    """ Creates an aircraft object
    """
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model =model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration (self):
        return self._registration
    
    def model(self):
        return self._model
    
    
    def seating_plan(self):
        return (range(1, self._num_rows+1), "ABCDEFGHJK"[:self._num_seats_per_row])
    
    
    
def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"        \
             f"  Flight: {flight_number}"  \
             f"  Seat: {seat}"             \
             f"  Aircraft: {aircraft}"     \
              " |"
              
    banner = "+" + "-" * (len(output)-2) + "+"
    border = "|" + " " * (len(output)-2) + "|"
    card = [banner, border, output, border, banner]
    
    lines = "\n".join(card)
    print(lines)
    print()
    
    
def make_flight():
    f = Flight("BA7580", Aircraft("KE-UPT", "Boeng 787", num_rows=20, num_seats_per_row=6))
    f.booking_seat("1A", "John Doe")
    f.booking_seat("1B", "Jane Smith")
    f.booking_seat("2A", "Michael Johnson")
    f.booking_seat("2B", "Emily Davis")
    f.booking_seat("3A", "Chris Brown")
    f.booking_seat("3B", "Laura Wilson")
    f.booking_seat("4A", "David Moore")
    f.booking_seat("4B", "Sophia White")
    f.booking_seat("5A", "James Taylor")
    f.booking_seat("5B", "Linda Martinez")
    return f