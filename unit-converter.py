
import streamlit as st

# Dictionary containing unit conversion factors
conversions = {
    "Length": {
        "meters": {"kilometers": 0.001},
        "kilometers": {"meters": 1000},
    },
    "Mass": {
        "grams": {"kilograms": 0.001},
        "kilograms": {"grams": 1000},
    },
    "Time": {
        "seconds": {"minutes": 1 / 60},
        "minutes": {"seconds": 60, "hours": 1 / 60},
        "hours": {"minutes": 60, "days": 1 / 24},
        "days": {"hours": 24, "weeks": 1 / 7},
        "weeks": {"days": 7, "months": 1 / 4},
        "months": {"weeks": 4, "years": 1 / 12},
        "years": {"months": 12},
    },
    "Area": {
        "square meters": {"square kilometers": 1e-6},
        "square kilometers": {"square meters": 1e6},
    },
    "Fuel Economy": {
        "mpg": {"kmpl": 0.425},
        "kmpl": {"mpg": 2.352},
    },
}

# Function to perform the conversion
def convert_units(value, unit_from, unit_to, category):
    try:
        return value * conversions[category][unit_from][unit_to]
    except KeyError:
        return "Conversion not supported"

# Streamlit UI
st.title("Advanced Unit Converter")

# Select category
category = st.selectbox("Select Category:", list(conversions.keys()))

# Select units based on category
unit_from = st.selectbox("Convert from:", list(conversions[category].keys()))
unit_to = st.selectbox("Convert to:", list(conversions[category][unit_from].keys()))

# User input for value
value = st.number_input("Enter value:", min_value=0.0, step=1.0)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to, category)
    st.write(f"Converted Value: {result} {unit_to}")
