import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

#st.set_page_config(layout="wide")

rawdata = pd.read_csv("./sodetails.csv")

st.header("SO Analysis")
# st.write(rawdata)

st.markdown("# *StoreOnce* usage *analysis*.")

# st.header("Bar chart 📊")
#
# st.bar_chart(rawdata[['date', 'catstore', 'dedup']],
#              x='catstore',
#              y='dedup')

# st.header("Interactive Chart 🪄")
# st.write("It's your turn to select a StoreOnce")
#
# selected_storeonce = st.selectbox("Select a storeonce", list(rawdata.soname.unique())[::-1], key="one", index=list(rawdata.soname.unique())[::-1].index("cstoreonce07"), )
#
# if selected_storeonce:
#     df_selected_storeonce = rawdata[rawdata.soname == selected_storeonce]
#     selected_catstore = st.selectbox("Select Catalyst Store", list(df_selected_storeonce.catstore.unique())[::-1],
#                                      key="three")
#
#     if selected_catstore:
#         df_selected_catstore = df_selected_storeonce[df_selected_storeonce.catstore == selected_catstore]
#
#         chart_data = pd.DataFrame(df_selected_catstore)
#
#         # Display chart
#         # st.write(chart_data)
#         st.bar_chart(chart_data, x="date", y="dedup", color="catstore", )

st.header("How about a line chart? 📈")
st.write("Track changes over time")

selected_storeonce = st.selectbox("Select a storeonce", list(rawdata.soname.unique())[::-1], key="two", index=list(rawdata.soname.unique())[::-1].index("cstoreonce07"),)

if selected_storeonce:
    df_selected_storeonce = rawdata[rawdata.soname == selected_storeonce]

    df_line_chart = pd.DataFrame(df_selected_storeonce)
    df_line_chart['date'] = pd.to_datetime(df_line_chart['date'], format="%d-%m-%Y", dayfirst=True)

    df_line_chart["Formatted_Date"] = df_line_chart['date'].dt.strftime("%m-%d-%y")

    df_line_chart = df_line_chart.sort_values(by="Formatted_Date")

    c = (
        alt.Chart(df_line_chart)
        .mark_line()
        .encode(x=alt.X('Formatted_Date'),
                y=alt.Y('dedup'),
                color=alt.Color('catstore'))
        .configure_legend(
            orient="bottom",
            direction="vertical",
            labelLimit = 400,
            titleFontSize = 24
        )
        .properties(
            width=800,
            height=750)
    )

    st.altair_chart(c, use_container_width=True)


st.header("5. Sprinkle in more interactivity 🪄")


selected_storeonce = st.selectbox("Select a storeonce", list(rawdata.soname.unique())[::-1], key="three", index=list(rawdata.soname.unique())[::-1].index("cstoreonce07"),)

# Date Range
start_date = datetime(2025, 1, 2)
end_date = datetime(2025, 3, 5)

# Slider for Date Selection
selected_dates = st.slider(
    "Select Date Range",
    min_value=start_date,
    max_value=end_date,
    value=(start_date, end_date),
    format="DD-MM-YYYY"
)
st.write("Selected Start Date:", selected_dates[0])
st.write("Selected End Date:", selected_dates[1])


if selected_storeonce:
    df_selected_storeonce = rawdata[rawdata.soname == selected_storeonce]

    df_line_chart = pd.DataFrame(df_selected_storeonce)
    df_line_chart['date'] = pd.to_datetime(df_line_chart['date'], format="%d-%m-%Y", dayfirst=True)

    df_line_chart["Formatted_Date"] = df_line_chart['date'].dt.strftime("%m-%d-%y")

    df_line_chart = df_line_chart.sort_values(by="Formatted_Date")
    df_line_chart = df_line_chart[df_line_chart['date'].between(selected_dates[0], selected_dates[1])]

    c = (
        alt.Chart(df_line_chart)
        .mark_line()
        .encode(x=alt.X('Formatted_Date'),
                y=alt.Y('dedup'),
                color=alt.Color('catstore'))
        .configure_legend(
            orient="bottom",
            direction="vertical",
            labelLimit = 400,
            titleFontSize = 24
        )
        .properties(
            width=800,
            height=750)
    )

    st.altair_chart(c, use_container_width=True)