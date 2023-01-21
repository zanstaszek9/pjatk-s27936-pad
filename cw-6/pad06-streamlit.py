from importlib_metadata import csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('PAD 06')


tab1, tab2 = st.tabs(["Survey", "Stats"])

with tab1:
   st.header("Survey")
   with st.form("my_form"):
    name = st.text_input("First Name")
    surname = st.text_input("Surname")

    submitted = st.form_submit_button("Submit")
    if submitted:
        success_notification = '<p style="color:Green; font-size: 22px">Succesful save!</p>'
        st.success("Succesful save!")

with tab2:
    st.header("Stats")

    csv_file = st.file_uploader("Choose CSV", type=["csv"])
    if csv_file is not None:
        st.progress(1)   

        # bytes_data = csv_file.getvalue()
        st.write("File uploaded:", csv_file.name)
    

        df = pd.read_csv(csv_file)


        select_chart = st.selectbox("Chart:", ["Histogram", "Violin"])
        if select_chart is "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df, bins=20)

            st.pyplot(fig)
        elif select_chart is "Violin":
            fig, ax = plt.subplots()
            ax.violinplot(df)

            st.pyplot(fig)

