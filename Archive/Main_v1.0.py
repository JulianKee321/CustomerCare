import streamlit as st
from streamlit_option_menu import option_menu
#import streamlit.components.v1 as components

# Set the page layout to wide for more space
st.set_page_config(layout="wide")

# Custom CSS for styling the navbar
st.markdown("""
    <style>
    body, html {
        margin: 0;
        padding: 0;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #4682B4;
        padding: 10px;
        width: 100%
        position: absolute;
        left: 0px;
        top: 0px;
    }
    .navbar img.logo {
        height: 50px;
    }
    .navbar img.profile {
        border-radius: 50%;
        height: 40px;
        width: 40px;
    }
    .navbar .profile-container {
        display: flex;
        align-items: center;
        border-right: 10px;
    }
    .navbar .profile-container .welcome-text {
        color: white;
        font-size: 20px;
        border-right: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar HTML
st.markdown("""
    <div class="navbar">
        <img src="https://via.placeholder.com/100x50?text=Logo" class="logo" alt="Logo">
        <div class="profile-container">
            <span class="Welcome-text">Welcome, User</span>
            <img src="https://via.placeholder.com/40x40?text=Profile" class="profile" alt="Profile Photo">
        </div>
    </div>
""", unsafe_allow_html=True)

#with st.sidebar:
#    with st.echo():
#        st.write("This code will be printed to the sidebar.")
 
st.sidebar.title("")
selection = st.sidebar.radio("",["Sessions", "Cases"])

# Main content based on the selected option
if selection == "Sessions":
    tab1, tab2 = st.tabs(["Email", "Call"])

    with tab1:
        st.header("Email")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("Call")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    
elif selection == "Cases":
    st.title("Dog Pictures")
    st.write("Here are some pictures of dogs:")
    st.image([
        "https://placedog.net/800/600",  # Example image URL for a dog
        "https://placedog.net/801/600",
        "https://placedog.net/802/600"
    ], caption=["Dog 1", "Dog 2", "Dog 3"], use_column_width=True)
 

