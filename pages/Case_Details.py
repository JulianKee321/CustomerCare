import streamlit as st
import streamlit.components.v1 as components
from services import services

st.set_page_config(layout='wide')

#watsonx logo
with st.sidebar:
    #Logo
    st.logo("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\assets\\IBM_watsonx_logo.png")

#NavBar visual
#NavBar CSS
st.markdown(open("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\views\\sessions.css").read(), unsafe_allow_html=True)

#NavBar HTML
st.markdown(open("C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\views\\sessions.html").read(), unsafe_allow_html=True)

try:
    sessionDetails = None
    caseDetails = None
    sessionDetails = st.session_state['SessionDetails']
    caseDetails = st.session_state['CaseDetails']

except Exception as e:
    print(f"Session Details are {sessionDetails}")
    print(f"Case Details are {caseDetails}")

#Tabs to switch between Email and Call
tab1, tab2 = st.tabs(["Case Details", "QnA"])

with tab1:
    if sessionDetails is not None:
        #st.write(st.session_state['SessionDetails'])
        test = st.session_state['SessionDetails']
        
        #Case/Ticket Information
        st.markdown("**Ticket Information**")
        st.write(f"**Case ID:** {sessionDetails['TicketID']}")
        st.write(f"**Severity:** Medium")
        st.write(f"**Category:** Upgrade/Downgrade")
        st.write(f"**NRIC:** 850204-10-5324")


        st.write(services.IsNewTicket())

        st.markdown("Email")
        with st.container(border=True, height=200):
            st.write("Test")
        
        st.markdown("Summary")
        with st.container(border=True, height=200):
            st.write("Test")
        
        st.markdown("Suggested Response")
        with st.container(border=True, height=200):
            st.write("Test1")
    
        with tab2:
            st.markdown("QnA")
            #Create session chat history
            if 'messages' not in st.session_state:
                st.session_state.messages = []           

            #Chat session
            if user_input := st.chat_input("Ask me anything"):
                st.chat_message("user").markdown(user_input)
                st.session_state.messages.append({"role": "user", "content": user_input})

                with st.chat_message("assistant"):
                    st.markdown(f"User said: {user_input}")
                    st.session_state.messages.append({"role": "assistant", "content": f"User said: {user_input}"})

            with st.expander("Chat History"):
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

    
    else:
        st.write("***Select a session or case first***")

