# to add the entry for russia to the travel_log.

travel_log = [
    { 
        "Country" : "France", 
        "Cities_visited" : ["Paris","Lille","Dijon"],
        "Total_visits": 12
        },
    {   
        "Country" : "Germany",
        "cities_visited" : ["Berlin","Hamburg","Stuttgart"], 
        "Total_visits" : 5
        }, 
]

# travel_log.append({"Country" : "Russia", "Cities_visited" : ["Moscow","Saint petersburg","Novosibirsk"],"Total_visits":3})

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["Country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("russia",2,["Moscow","Saint petersburg"])
print(travel_log)