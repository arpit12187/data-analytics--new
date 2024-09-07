import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# set pandas plotting backend to plotly
pd.options.plotting.backend='plotly'
@st.cache_data
def load_dataset():
    return pd.read_csv('datasets/canada_clean.csv')

st.title('Canada Immigration Analysis')

with st.spinner('Loading data...'):
    df= load_dataset()
    st.balloons()
with st.expander('show Datasets'):
    st.dataframe(df)

Country_list=df['Country']
Selected_country= st.selectbox('Select a Country',Country_list)
min_y,Max_y= st.slider('Select years',min_value=1980,max_value=2013,value=(1980,2013))
st.header(f'Country:{Selected_country}')
df= df.set_index('Country')
Country= df.loc[Selected_country,str(min_y):str(Max_y)]
fig= Country.plot()
st.plotly_chart(fig)