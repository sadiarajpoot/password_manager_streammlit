import streamlit as st
import re

# project
def check_password_strength (password):
    score = 0
    feedback=[]
    if len(password) >= 8:
     score += 1
    else:
     feedback.append("❌Increase the length to at least 8 characters.")
    if re.search(r'[A-Z]', password) and  re.search(r'[a-z]',password):
       score += 1
    else:
       feedback.append("🔡Include both uppercase and lowercase letters.")
    if re.search(r'\d',password):
       score += 1
    else:
       feedback.append("🔢Include at least one digit (0-9).")
    if re.search(r'[!@#$%^&*]',password):
       score +=1
    else:
       feedback.append("🔣Include at least one special character (!@#$%^&*).")
 # checking password score
    if score ==4:
       feedback= ["✅Strong password!🎉"]
    elif score == 3:
       feedback=["⚠️Moderate password. Consider adding missing elements.🔧"]
    else:
        feedback.append("🚨Weak password. Improve by following the suggestions.🔴")
        return score, feedback
# input passsword
  
   
    score, feedback = check_password_strength(password)
    return score, feedback
st.title("🔐 Password Strength Checker")
password = st.text_input("🔑 Enter your password:", type="password")  

if password:  # Jab user kuch enter kare
    score, feedback = check_password_strength(password)
    
    # Display results
    st.subheader("💡Password Feedback")
    for msg in feedback:
      st.write(msg)
      st.write("\n📊 **Password Score:**", "⭐" * score, f"({score}/4)")

# Auto generate password
import random
import string
# Defining the Password Generator Function
def generator_password (length,use_upper_case,use_digits,use_special):
# Selecting Character Set
    characters=string.ascii_lowercase 
    if use_upper_case:
        characters += string.ascii_uppercase
    if use_digits :
        characters +=string.digits
    if use_special :
        characters +=string.punctuation
 #  Generating a Random Password
    return "".join(random.choice(characters) for _ in range(length)) 
st.title("🔐 Password Generator")
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters (A-Z)")
use_digits = st.checkbox("Include Numbers (0-9)")
use_special = st.checkbox("Include Special Characters (@, #, $...)")
if st.button("Generate Password"):
 if not (use_uppercase or use_digits or use_special ):
    st.warning("Select at least one character type.")
 else:
    password = generator_password(length, use_uppercase, use_digits, use_special)
    st.success(f"Generated Password: {password}")



   
