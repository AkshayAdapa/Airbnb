import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
from PIL import Image

# Set page config
st.set_page_config(page_title="AirBnb Analysis by [Your Name]", page_icon=":bar_chart:", layout="wide")

# Title and styling
st.title(":bar_chart:   AirBnb Analysis")
st.markdown('<style>div.block-container{padding-top:1rem; background-color: #f0f2f6;}</style>', unsafe_allow_html=True)

# Sidebar navigation
SELECT = option_menu(
    menu_title=None,
    options=["Home", "Explore Data", "Contact"],
    icons=["house", "bar-chart", "at"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white", "size": "cover", "width": "100"},
        "icon": {"color": "#6F36AD", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}
    }
)

# Home Page
if SELECT == "Home":
    st.header('Welcome to AirBnb Analysis')
    st.subheader("This project aims to analyze AirBnb data to derive valuable insights.")
    st.subheader('Skills Acquired:')
    st.subheader('Python Scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau')
    st.subheader('Domain:')
    st.subheader('Travel Industry, Property Management, and Tourism')

# Data Exploration Page
if SELECT == "Explore Data":
    # Data loading
    fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
    if fl is not None:
        filename = fl.name
        st.write(filename)
        df = pd.read_csv(filename, encoding="ISO-8859-1")
    else:
        filename = "C:/Users/Akshay/OneDrive/Desktop/GUVI_Projects/Capstone(4)-Airbnb/AB_NYC_2019.csv"
        df = pd.read_csv(filename, encoding="ISO-8859-1")

    # Sidebar filters
    st.sidebar.header("Choose your filter: ")
    neighbourhood_group = st.sidebar.multiselect("Pick your neighbourhood_group", df["neighbourhood_group"].unique())
    neighbourhood = st.sidebar.multiselect("Pick the neighbourhood", df["neighbourhood"].unique())

    # Data filtering based on selected filters
    if not neighbourhood_group and not neighbourhood:
        filtered_df = df
    elif not neighbourhood:
        filtered_df = df[df["neighbourhood_group"].isin(neighbourhood_group)]
    elif not neighbourhood_group:
        filtered_df = df[df["neighbourhood"].isin(neighbourhood)]
    else:
        filtered_df = df[df["neighbourhood_group"].isin(neighbourhood_group) & df["neighbourhood"].isin(neighbourhood)]

    # Room type and neighbourhood group analysis
    room_type_df = filtered_df.groupby(by=["room_type"], as_index=False)["price"].sum()

    # Visualization - Room Type
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Room Type Analysis")
        fig = px.bar(room_type_df, x="room_type", y="price", text=['${:,.2f}'.format(x) for x in room_type_df["price"]],
                     template="plotly", color_discrete_sequence=["#6F36AD"])
        st.plotly_chart(fig, use_container_width=True, height=200)

    # Visualization - Neighbourhood Group
    with col2:
        st.subheader("Neighbourhood Group Analysis")
        fig = px.pie(filtered_df, values="price", names="neighbourhood_group", hole=0.5, color_discrete_sequence=px.colors.qualitative.Plotly)
        fig.update_traces(text=filtered_df["neighbourhood_group"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    # Additional visualizations and data exploration can be added here

# Contact Page
if SELECT == "Contact":
    Name = (f'{"Name :"}  {"Akshay Kumar Adapa"}')  # Replace with your name
    mail = (f'{"Mail :"}  {"akshayadapa2427@gmail.com"}')  # Replace with your email
    description = "[Your Description]"  # Add your description
    social_media = {
        "Youtube": "Your Youtube link",  # Replace with your YouTube link
        "GitHub": "Your GitHub link",  # Replace with your GitHub link
        "LinkedIn": "Your LinkedIn link"}  # Replace with your LinkedIn link

    col1, col2 = st.columns(2)
    col1.image(Image.open("C:/Users/Akshay/OneDrive/Desktop/GUVI_Projects/Capstone(4)-Airbnb/New_York_City_.png"), width=300)  # Replace with path to your image

    with col2:
        st.header('AirBnb Analysis')
        st.subheader("This project aims to analyze AirBnb data to derive valuable insights.")
        st.write("---")
        st.subheader(Name)
        st.subheader(mail)

    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
