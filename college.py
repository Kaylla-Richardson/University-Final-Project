import streamlit as st
import pandas as pd
import altair as alt 
import numpy as np

st.set_page_config(layout="wide")

#import the university data set
university_data = pd.read_excel("universityrankings.xlsx")

st.title("World Rankings by University")
st.sidebar.header("Interact with me!")


user_name = st.sidebar.text_input('What is your name?')


if user_name != "":
    st.write(f"Welcome {user_name}!")
else:
     st.write(f"Please enter your name!")


tab1, tab2, tab3, tab4, tab5= st.tabs(['Stats','World', 'USA', "NC", "Data"])

with tab1: 

    st.caption("This tab will allow you to compare the rankings and stats of two Universities. Please follow the prompts below.")

    university = university_data["Institution"].unique()
    university_name = st.selectbox("Choose one of your favorite Universities to view!",university)
    if university_name != "":
        st.write(f"Your favorite University is {university_name}!")
    else:
        st.write(f"Please choose a university!")
    university_name2 = st.selectbox("Choose a University to compare!", university)

    compare_df = university_data[(university_data['Institution'] == university_name) | (university_data['Institution'] == university_name2)]

    df_university = university_data[university_data['Institution']== university_name]
    df_university2 = university_data[university_data['Institution']== university_name2]


    if university_name2 != "":
        st.subheader(f"You're comparing {university_name} to {university_name2}!")
    else:
        st.write(f"Please choose a university to compare!")

    
    #st.subheader(f"The National Ranking for {university_name} is {df_national}.")
    st.write(compare_df)

    col1, col2 = st.columns(2)

    with col1:

        RankChart = alt.Chart(df_university).mark_bar(size=50, color='red').encode(
            x = alt.X ('World Rank'),
            y = alt.Y ('National Rank')
        ).properties(width='container', title=f"{university_name}")
        st.altair_chart(RankChart, use_container_width=True)

    with col2:
        AnotherRankChart = alt.Chart(df_university2).mark_bar(size=50, color = 'red').encode(
            x = alt.X ('World Rank'),
            y = alt.Y ('National Rank')
        ).properties(width='container', title=f"{university_name2}")
        st.altair_chart(AnotherRankChart, use_container_width=True)

with tab2:
    st.caption("This tab shows you the Top 10 Universities in the World.")
    st.subheader(f"Top 10 Universities in the World")
    
    df_rank = university_data[university_data['World Rank'] < 11]

    RankChart2 = alt.Chart(df_rank).mark_bar(size=50, color = 'red').encode(
        alt.X ('Institution', sort='-y',),
        alt.Y ('Score', axis=alt.Axis(tickCount=10))
        ).properties(height=500)
    st.altair_chart(RankChart2, use_container_width=True)

    df_rank



with tab3:
    st.caption("This tab shows you the Top 10 Universities in the United States.")
    st.subheader(f"Top 10 Universities in the United States")

    df_loc = university_data[(university_data['World Rank'] < 13) & (university_data['Location'] == 'USA')]

    RankChart3 = alt.Chart(df_loc).mark_bar(size=50, color='red').encode(
            alt.X ('Institution', sort='-y',),
            alt.Y ('Score', axis=alt.Axis(tickCount=10))
            ).properties(height=500)
    st.altair_chart(RankChart3, use_container_width=True)

    df_loc 

with tab4: 
    st.caption("This tab shows you the Top 9 Universities in North Carolina.")
    st.subheader(f"Top Universities in North Carolina")
    
    df_nc = university_data[(university_data['Institution'] == "Duke University") 
        | (university_data['Institution'] == "University of North Carolina at Chapel Hill")
        | (university_data['Institution'] == "North Carolina State University")
        | (university_data['Institution'] == "Wake Forest University")
        | (university_data['Institution'] == "University of North Carolina at Charlotte")
        | (university_data['Institution'] == "East Carolina University")
        | (university_data['Institution'] == "University of North Carolina at Greensboro")
        | (university_data['Institution'] == "University of North Carolina Wilmington")
        | (university_data['Institution'] == "Appalachian State University")
        ]

    RankChart4 = alt.Chart(df_nc).mark_bar(size=55, color='red').encode(
            alt.X ('Institution', sort='-y',),
            alt.Y ('Score', axis=alt.Axis(tickCount=10))
            ).properties(height=500)
    st.altair_chart(RankChart4, use_container_width=True)
    df_nc

with tab5: 
    st.caption("This tab shows you the data/excel file used for this program.")
    st.write(university_data)



#Resources: 
# https://public.tableau.com/app/profile/kaylla.richardson/viz/DSBA5122DataProject-WorldUniversity2/Story1
# https://altair-viz.github.io/user_guide/scale_resolve.html
# https://docs.streamlit.io/knowledge-base/using-streamlit/hide-row-indices-displaying-dataframe

