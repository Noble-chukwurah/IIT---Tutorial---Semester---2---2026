print("Celsius \t\t Fahrenheit")
for c in range(10,31,5):
    f = (9/5) * c + 32
    print(c, "\t\t", f)
    
phrase = input("Enter phrase")
phrase = phrase.lower()
count = 0
for ch in phrase:
    if ch in "aeiou":
        count = count + 1
        
print("The phrase contains", count, "Vowels")

movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []
while True:
    title = input("Enter movie name (or done)").lower()
    if title == "done":
        break
    if title not in movies:
        print("Not available, Available movies are: ", movies.keys())
    qty = int(input("Enter Quantity: "))
    purchases.append((title,qty))

# Receept
def line_total(qty, price_each):
    total = qty * price_each
    if qty >= 4:
        total*= 0.90
    return total

subtotal = 0.0
print("\nReceipt")
for title, qty in purchases:
    price = movies[title]
    it = line_total(qty, price)
    subtotal += it
    print(f"{title:14s} x{qty:2d} @ ${price:2f} -> ${it:2f}")
    

#  Summaries
tickets_by_movie = {}
revenue_by_movie = {}
for title, qty in purchases:
    price = movies[title]
    it = line_total((qty, price))
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title,0.0) + it
print("\n Summary (tickets):", tickets_by_movie)
print("\n Summary (revenue):", revenue_by_movie)

# Top Seller
if tickets_by_movie:
    top_title = max(tickets_by_movie, key = tickets_by_movie.get)
    print("Top Seller:", top_title, tickets_by_movie[top_title])