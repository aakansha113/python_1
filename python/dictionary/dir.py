dict_data = {  # Renamed to avoid using built-in name `dict`
    "name": "abu",
    "place": "kolad",
    "contact": "nji"
}

# Changing values
dict_data["name"] = "Aakansha"
dict_data["place"] = "pune"
dict_data["contact"] = "123456"

print(dict_data)

# Correct way to access keys, values, and items
print(dict_data.keys())  # No argument is needed
print(dict_data.values())  # No argument is needed
print(dict_data.items())  # Returns key-value pairs

# Using `get()`
print(dict_data.get("name"))  # Correct way to use `get()`

# Using `update()`
dict_data.update({"email": "aakansha@example.com"})  # Adding a new key-value pair

