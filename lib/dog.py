#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        # Validate name
        if name is not None:
            if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
            else:
                self.name = name

        # Validate breed
        if breed is not None:
            if breed not in APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
            else:
                self.breed = breed
