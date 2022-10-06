"""
Fake function definitions
"""


class ProbablyAFakeName(Exception):
    """
    Thrown when someone is probably using a fake name.
    """


def say_whats_up_to_your_guests(
    guests_name: str,
    repetition_times: int = 1,
) -> None:
    """Greets guests with one or more messsages.

    Say what's up to your guests in a standard manner, or with
    a crazy custom message if you'd like. If you want to annoy
    your guests then repeat the greating as many times as you want.

    Args:
      guests_name: The name of the guest to greet.
      repetition_times: The number of times to repeat the greeting with
      a default value of 1. You can't repeat something over 10 times.

    Raises:
      ValueError: An error occured parsing the parameters.
      ProbablyAFakeName: A name that is unrealistically long is passed in.
    """
    if repetition_times < 1:
        raise ValueError("Must supply a repetition number greater than 1!")
    if repetition_times > 10:
        raise ValueError("You're talking too much!")
    if len(guests_name) > 100:
        raise ProbablyAFakeName(guests_name)
    greeting = f"Yo {guests_name}"
    print(greeting * repetition_times)
