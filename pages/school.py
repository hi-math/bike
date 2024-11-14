import streamlit as st
import pandas as pd

data = pd.read_csv("학생현황.csv")
data

with st.form("input"):
    region = st.multiselect("지역", data['Region'].unique())
    gender = st.multiselect("성별", data['Gender'].unique())
    school = st.multiselect("학교", data['School'].unique())
    submitted = st.form_submit_button("조회")

if submitted:
    result = data["Year"].drop_duplicates().sort_values().reset_index(drop=True)
    name_list = []
    for re in region:
        for ge in gender:
            for sc in school:
                name = f"{re}_{ge}_{sc}"
                name_list.append(name)
                selected_df = data[(data['Region'] == re) & (data['Gender'] == ge)& (data['School'] == sc)]
                selected_df = selected_df[["Year","Students"]].rename(columns={"Students": name})
                result = pd.merge(result, selected_df, on='Year').sort_values('Year')
    
    st.line_chart(data=result, x='Year', y=name_list, use_container_width=True)