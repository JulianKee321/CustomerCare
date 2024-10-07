import streamlit as st
import pandas as pd
import copy

from streamlit_option_menu import option_menu
from data import DbContext

#import streamlit.components.v1 as components

# Set the page layout to wide for more space
st.set_page_config(layout="wide")

#watsonx logo
with st.sidebar:
    #Logo
    st.logo("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\assets\\IBM_watsonx_logo.png")

#NavBar visual
#NavBar CSS
st.markdown(open("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\views\\sessions.css").read(), unsafe_allow_html=True)

#NavBar HTML
st.markdown(open("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\views\\sessions.html").read(), unsafe_allow_html=True)

#Tabs to switch between Email and Call
tab1, tab2 = st.tabs(["Email", "Call"])

#Email tab
with tab1:
    session = DbContext.Sessions("sessions")
   
    st.subheader("Active Sessions")
    sessionActive = copy.copy(session)
    active_sessions = sessionActive.get_active_email_sessions()
    
    event_active = st.dataframe(
    active_sessions,
    on_select="rerun",
    selection_mode="single-row",
    hide_index=True
    )
    
    if len(event_active.selection["rows"]):
        selected_row = event_active.selection["rows"][0]
        sessionID = active_sessions.iloc[selected_row]["SessionID"]
        emailSender = active_sessions.iloc[selected_row]["Sender"]
        emailTitle = active_sessions.iloc[selected_row]["Email_Title"]
        emailBody = active_sessions.iloc[selected_row]["Email_Body"]
        status = active_sessions.iloc[selected_row]["Status"]
        ticketID = active_sessions.iloc[selected_row]["TicketID"]
        ticketCategory = active_sessions.iloc[selected_row]["TicketCategory"]
        severity = active_sessions.iloc[selected_row]["Severity"]
        channel = active_sessions.iloc[selected_row]["Channel"]
        
        st.session_state["SessionDetails"] = {"SessionID":sessionID,"Sender":emailSender,"Title":emailTitle,"Body":emailBody,"Status":status,"TicketID":ticketID,"TicketCategory":ticketCategory,"Severity":severity,"Channel":channel}
        st.page_link("pages/Case_Details.py", label="Click to create a new case", icon='🆕')
    
    st.subheader("Closed Sessions")
    sessionClosed = copy.copy(session)
    closed_sessions = sessionClosed.get_closed_email_sessions()
    
    event_closed = st.dataframe(
    closed_sessions,
    on_select="rerun",
    selection_mode="single-row",
    hide_index=True
    )
    
    if len(event_closed.selection["rows"]):
        selected_row = event_closed.selection["rows"][0]
        sessionID = closed_sessions.iloc[selected_row]["SessionID"]
        emailSender = closed_sessions.iloc[selected_row]["Sender"]
        emailTitle = closed_sessions.iloc[selected_row]["Email_Title"]
        emailBody = closed_sessions.iloc[selected_row]["Email_Body"]
        status = closed_sessions.iloc[selected_row]["Status"]
        ticketID = closed_sessions.iloc[selected_row]["TicketID"]
        ticketCategory = closed_sessions.iloc[selected_row]["TicketCategory"]
        severity = closed_sessions.iloc[selected_row]["Severity"]
        channel = closed_sessions.iloc[selected_row]["Channel"]
        
        st.session_state["SessionDetails"] = {"SessionID":sessionID,"Sender":emailSender,"Title":emailTitle,"Body":emailBody,"Status":status,"TicketID":ticketID,"TicketCategory":ticketCategory,"Severity":severity,"Channel":channel}
        st.page_link("pages/Case_Details.py", label="Click to view case details", icon='🔍')

#Calls tab
with tab2:
    st.header("Call")
    st.subheader("Feature coming soon")
    st.image("https://img.freepik.com/free-vector/red-grunge-style-coming-soon-design_1017-26691.jpg", width=600)