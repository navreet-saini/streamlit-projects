import streamlit as st
import requests
from datetime import datetime
cities = [
    # Metro & Tier-1 Cities
    "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik", "Vadodara",
    "Coimbatore", "Thiruvananthapuram", "Vijayawada", "Ranchi", "Raipur", "Amritsar", "Varanasi", "Prayagraj", "Madurai", "Jodhpur",

    # Haryana Cities
    "Gurugram", "Faridabad", "Panipat", "Ambala", "Karnal", "Hisar", "Rohtak", "Yamunanagar", "Sirsa", "Bahadurgarh",
    "Sonipat", "Bhiwani", "Palwal", "Jind", "Rewari", "Kaithal", "Kurukshetra", "Fatehabad", "Jhajjar", "Charkhi Dadri","ladwa"

    # North India & Other Important Cities
    "Guwahati", "Dehradun", "Chandigarh","Panckula","Mohali" "Mysuru", "Jamshedpur", "Udaipur", "Meerut", "Noida", "Ghaziabad",
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
choices=st.selectbox("Choose your city name 📍:",cities)




if choices:
    url=f"https://api.openweathermap.org/data/2.5/weather?q={choices}&appid={API_KEY}"

    response=requests.get(url)
    data=response.json()

    if data["cod"]==200:

        st.subheader(f"Weather in {choices.title()}")
        sys=data["sys"]
        col1,col2=st.columns(2)

        with col1:
            weather=data["weather"][0]["main"]
            temp=data["main"]["temp"]
            feel_temp=data["main"]["feels_like"]
            humidity=data["main"]["humidity"]
            wind_speed=data["wind"]["speed"]
            wind_degree=data["wind"]["deg"]
            wind_degree=data["wind"]["deg"]
            

           
            st.write(f"**🌡️ Temperature :** {temp-273.15 :.2f}°C")  #by default it gives value in kelvin
            st.write(f"**🥵 Feels-Like :** {feel_temp-273.15 :.2f}%")
            st.write(f"**💧 Humidity :** {humidity}%")
            st.write(f"**🌬️ Wind Speed :** {wind_speed} m/s")
            st.write(f"**🧭 Wind degree :** {wind_degree}° ")
            st.write(f"**⛅ Condition :** {weather}")
            

        with col2:
            sunrise=datetime.fromtimestamp(sys['sunrise']).strftime('%H:%M:%S')
            sunset=datetime.fromtimestamp(sys['sunset']).strftime('%H:%M:%S')
            visibility=data["visibility"]
            pressure=data["main"]["pressure"]
            sea=data["main"]["sea_level"]
            ground=data["main"]["grnd_level"]


            
            st.write(f"**🌇 Sunrise :** {sunrise}")
            st.write(f"**🌆 Sunset :** {sunset}")
            st.write(f"**👁️ Visibility :** {visibility} m")
            st.write(f"**📈 Pressure :** {pressure} hPa")
            st.write(f"**🌊 Sea-Level :** {sea} hPa")
            st.write(f"**🏞️ Ground-Level :** {ground} hPa")





            
    else:
        st.error("City not found ❌")
       
    
        