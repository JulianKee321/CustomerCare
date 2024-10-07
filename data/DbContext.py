import streamlit as st
import pandas as pd

class Sessions:
    def __init__(self, data=None):
        if data is not None:
            self.df = pd.read_csv(f'C:\\Users\\JulianKee\\Desktop\\Projects\\CustomerCare\\AgentAssist\\data\\{data}.csv')#,index_col=0)
        else:
            self.df = pd.DataFrame()
    
    def get_dataframe(self):
        return self.df
    
    def get_active_email_sessions(self):
        self.df = self.df[(self.df['Status'] == "Active") & (self.df['Channel'] == "Email")]
        return self.df
        
    def get_closed_email_sessions(self):
        self.df = self.df[(self.df['Status'] == "Closed") & (self.df['Channel'] == "Email")]
        return self.df

