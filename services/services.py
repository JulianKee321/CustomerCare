import streamlit as st
import numpy as np


def IsNewTicket():
    sessionDetails = st.session_state['SessionDetails']
    caseID = sessionDetails['TicketID']
    if np.nan_to_num(caseID) == 0:
        return True
    else:
        return False

def GetCaseID():
    sessionDetails = st.session_state['SessionDetails']
    caseID = sessionDetails['TicketID']
    if np.nan_to_num(caseID) == 0:
        caseID = 'Test001'
        return caseID
    else:
        return caseID
    