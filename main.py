"""
main.py

Console-based temperature converter application.
Allows the user to convert temperatures between
Celsius and Fahrenheit in both directions.
"""

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def print_menu() -> None:
    """Display the main menu."""
    print("\n====== TEMPERATURE CONVERTER ======")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")


def read_temperature(prompt: str) -> float:
    """
    Safely read a temperature value from the user.

    Re-prompts until a valid number is entered.
    """
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric temperature value.")


def handle_celsius_to_fahrenheit() -> None:
    """Handle conversion from Celsius to Fahrenheit."""
    celsius = read_temperature("Enter temperature in Celsius: ")
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f} °C  =  {fahrenheit:.2f} °F")


def handle_fahrenheit_to_celsius() -> None:
    """Handle conversion from Fahrenheit to Celsius."""
    fahrenheit = read_temperature("Enter temperature in Fahrenheit: ")
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.2f} °F  =  {celsius:.2f} °C")


def main() -> None:
    """Main application loop."""
    while True:
        print_menu()
        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            handle_celsius_to_fahrenheit()
        elif choice == "2":
            handle_fahrenheit_to_celsius()
        elif choice == "3":
            print("Exiting Temperature Converter. Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
