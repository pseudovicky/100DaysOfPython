# Nesting 

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",

}

# Nesting a list in a dictionary 

travel_log = {
    "France": {"Cities_visited" : ["Paris","Lille","Dijon"],"Total_visits": 12},
    "Germany" : { "cities_visited" : ["Berlin","Hamburg","Stuttgart"], "Total_visits" : 5} ,
}

#  Nesting dictionary in a list 

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

print(travel_log)