# Example 3.4
guests = ["Sara", "Umer", "Maha", "Ayesha", "Ali"]

for guest in guests:
    print(f"Hi {guest}, you are invited to dinner.")

# Example 3.5
print("\nAyesha can't make it to dinner")
guests[3] = "Soha"

# Example 3.6
guests.insert(2, "Zain")
guests.insert(4, "Alishba")
guests.append("Mahnoor")
print("\n")

for guest in guests:
    print(f"Hi {guest}, you are invited to dinner.")

# Example 3.7
print("\nOnly 2 people can be invited")

print("\n")
while len(guests) > 2:
    a = guests.pop()
    print(f"Sorry {a}, only 2 people can be invited.")

for guest in guests:
    print(f"Hi {guest}, you're still invited to dinner.")

del guests[1]
del guests[0]

print(f"\nGuests list: {guests}")

# Example 3.8

places = ["Japan", "Edinburgh", "South Korea", "Paris", "Indonesia"]
print(f"\n{places}")

places1 = sorted(places)
print(f"\nList in alphabetical order: {places1}")
print(f"Original List: {places}")

places2 = places
places2.reverse()
print(f"\nReversed List: {places2}")

places2.reverse()
print(f"\nTwice Reversed List: {places2}")

places3 = places
places3.sort()
print(f"\nSorted List: {places3}")

places3.sort(reverse=True)
print(f"\nTwice Sorted List: {places3}")
