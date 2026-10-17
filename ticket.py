ticket_name = "Ticket"
price = 100.0
quantity = 200
is_available = True

print(f"Ticket Name: {ticket_name}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Available: {'Yes' if is_available else 'No'}")

print("\nTicket Details:")
ticket_details = {  
    "Name": ticket_name,
    "Price": price,
    "Quantity": quantity,
    "Available": is_available
}

for key, value in ticket_details.items():
    print(f"{key}: {value}")
