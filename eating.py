class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name}, we're open! Book Now to avoid dissapointment")

# three restauraunts 
black_lock = Restaurant("Black Lock", "A Chop House")
black_lock.describe_restaurant()
black_lock.open_restaurant()

monohon = Restaurant("Monohon", "Ramen")
monohon.describe_restaurant()
monohon.open_restaurant()

leongs_legend = Restaurant("Leongs Legend", "Taiwanese Dim Sum")
leongs_legend.describe_restaurant()
leongs_legend.open_restaurant()
