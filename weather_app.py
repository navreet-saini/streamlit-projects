import streamlit as st
import requests
cities = [
    # Metro & Tier-1 Cities
    "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik", "Vadodara",
    "Coimbatore", "Thiruvananthapuram", "Vijayawada", "Ranchi", "Raipur", "Amritsar", "Varanasi", "Prayagraj", "Madurai", "Jodhpur",

    # Haryana Cities
    "Gurugram", "Faridabad", "Panipat", "Ambala", "Karnal", "Hisar", "Rohtak", "Yamunanagar", "Sirsa", "Bahadurgarh",
    "Sonipat", "Bhiwani", "Palwal", "Jind", "Rewari", "Kaithal", "Kurukshetra", "Fatehabad", "Jhajjar", "Charkhi Dadri",

    # North India & Other Important Cities
    "Guwahati", "Dehradun", "Chandigarh", "Mysuru", "Jamshedpur", "Udaipur", "Meerut", "Noida", "Ghaziabad",
    "Shimla", "Panaji", "Shillong", "Imphal", "Aizawl", "Kohima", "Itanagar", "Gangtok", "Puducherry", "Siliguri",

    # East, West, South Cities
    "Dhanbad", "Gwalior", "Tiruchirappalli", "Kozhikode", "Thrissur", "Salem", "Warangal", "Hubli", "Belgaum",
    "Bareilly", "Moradabad", "Aligarh", "Jabalpur", "Bhavnagar", "Gandhinagar", "Bilaspur", "Haridwar", "Ajmer",
    "Kota", "Rajkot", "Kolhapur", "Aurangabad", "Jalandhar", "Srinagar", "Leh", "Anantnag", "Rewa", "Satna",
    "Nanded", "Akola", "Latur", "Kurnool", "Nellore", "Tirupati", "Bhagalpur", "Muzaffarpur", "Sambalpur", "Cuttack",
    "Rourkela", "Bhilai", "Durg", "Tinsukia", "Tezpur", "Darbhanga", "Gaya", "Begusarai", "Chhapra", "Hajipur",
    "Firozabad", "Jhansi", "Bokaro", "Haldwani", "Nainital", "Karimnagar", "Nizamabad", "Eluru", "Machilipatnam",
    "Rajahmundry", "Kakinada", "Ongole", "Anantapur", "Tumakuru", "Davanagere", "Bellary", "Hassan", "Shimoga",
    "Bijapur", "Bidar", "Chikmagalur", "Gulbarga", "Mandya", "Mangalore", "Thanjavur", "Erode", "Vellore",
    "Nagercoil", "Dindigul", "Karur", "Sivakasi", "Tuticorin", "Ambattur", "Chengalpattu", "Bhuj", "Porbandar",
    "Surendranagar", "Mehsana", "Navsari", "Junagadh", "Gondia", "Beed", "Parbhani", "Chandrapur", "Solapur",
    "Sangli", "Ratnagiri", "Satara", "Wardha", "Yavatmal", "Baramati", "Palghar", "Bhiwandi"
]
API_KEY="4183104a9cac48f13632532a13b686c1"

st.title("⛈️ My Weather App")
choices=st.selectbox("Enter your city name:",cities)



if choices:
    url=f"https://api.openweathermap.org/data/2.5/weather?q={choices}&appid={API_KEY}"

    response=requests.get(url)

    if response.status_code==200:
        st.write("API working")    #writes the ouput
        # st.json(response.json())

        weather_info=response.json()
        st.write(weather_info)
    else:
        st.write("something went wrong")
        