import streamlit as st

st.title("unit converter")
st.markdown(" Convert Length, Weight and Time instantly")
st.write("Welcome! select a catagory, enter a value and get a converted result instantly")
catagory = st.selectbox("Choose a catagory",["Length","Weight","Time"])

def convert_units(catagory, value, unit):
    if catagory == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371 
        
    elif catagory == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilogarams":
            return value / 2.20462 
        
    elif catagory == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60 

        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
if catagory == "Length":
    unit = st.selectbox("Select conversation",["Kilometers to Miles","Miles to Kilometers"])
elif catagory == "Weight":
    unit = st.selectbox("Select conversation",["Kilograms to pounds","Pounds to Kilograms"])
elif catagory == "Time":
    unit = st.selectbox("Select conversation",[
        "Seconds to Minutes","Minutes to Seconds",
        "Minutes to Hours","Hours to Minutes",
        "Hours to Days","Days to Hours"])
    
value = st.number_input("Input the value to convert")

if st.button("Convert"):
    result = convert_units(catagory, value, unit)
    st.success(f"The result is {result: .2f}")












