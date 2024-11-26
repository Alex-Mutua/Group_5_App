import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import streamlit.components.v1 as components


st.markdown("<h1 style='text-align: center; color: black;'>GROUP FIVE SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
In this app performs webscraping of data from expat-dakar over multiples pages. And we can also
download scraped data from the app directly without scraping them.
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")

# Web scraping of Rental-appartment data on expat-dakar
@st.cache_data

def convert_df(df):
# IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
def load(dataframe, title, key, key1) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key1):
        # st.header(title)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

        csv = convert_df(dataframe)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Data.csv',
            mime='text/csv',
            key = key)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Fonction for web scraping Rental appartment 1
def load_Appartment1_data(mul_page):
    # create a empty dataframe df
    df = pd.DataFrame()
    # loop over pages indexes
    for pages in range(1, int(mul_page)+1):
        url = f'https://www.expat-dakar.com/appartements-a-louer?page={pages}'
        res_c = requests.get(url)  # Fetch the page
        soup_c = bs(res_c.text, 'html.parser')  # Parse the HTML content
        containers=soup.find_all("div", class_="listings-cards__list-item")

        data = []
        for container in containers:  # Loop through each listing
            try:
                # Get the listing link
                link = container.find('a')['href']
                res_c = requests.get(link)  # Fetch the listing details page
                soup_c = bs(res_c.text, 'html.parser')  # Parse the listing details page
                
                # Extract details
                Details = soup_c.find('div', class_="listing-item__details").text.split()[6]
                
                # Extract area
                Area = soup_c.find("dd", class_="listing-item__properties__description").text.strip().replace("m²", "")
                
                # Extract address
                Adress = soup_c.find("div", class_="listing-item__address").text.strip().replace("\n", "").replace("                           ", "")
                
                # Extract price
                Price = soup_c.find("span", class_="listing-card__price__value").text.strip().replace("\u202f", "").replace("F Cfa", "")
                
                # Extract image link
                ImageLink = soup_c.find("div", class_="gallery__image__inner").img["srcset"]
                
                # Append the extracted data as a dictionary
                dic = {
                    'Details': Details,
                    'Area': Area,
                    'Adress': Adress,
                    'Price': Price,
                    'ImageLink': ImageLink
                }
                data.append(dic)
            except:
                
                pass
            return df 

        # Convert data to DataFrame and concatenate with the main DataFrame
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)


def load_Appartment_2_data(mul_page):
    df = pd.DataFrame()
    for pages in range (1,int(mul_page)+1):
        url = f'https://www.expat-dakar.com/appartements-meubles?page={pages}'
        res_c = requests.get(url)  # Fetch the page
        soup_c = bs(res_c.text, 'html.parser')  # Parse the HTML content
        containers=soup.find_all("div", class_="listings-cards__list-item")

        data = []  # Temporary list to store data from the current page

        for container in containers:  # Loop through each listing
            try:
                # Get the listing link
                link = container.find('a')['href']
                res_c = requests.get(link)  # Fetch the listing details page
                soup_c = bs(res_c.text, 'html.parser')  # Parse the listing details page
                
                # Extract details
                Details = soup_c.find('div', class_="listing-item__details").text.split()[6]
                
                # Extract area
                Area = soup_c.find("dd", class_="listing-item__properties__description").text.strip().replace("m²", "")
                
                # Extract address
                Adress = soup_c.find("div", class_="listing-item__address").text.strip().replace("\n", "").replace("                           ", "")
                
                # Extract price
                Price = soup_c.find("span", class_="listing-card__price__value").text.strip().replace("\u202f", "").replace("F Cfa", "")
                
                # Extract image link
                ImageLink = soup_c.find("div", class_="gallery__image__inner").img["srcset"]
                
                # Append the extracted data as a dictionary
                dic = {
                    'Details': Details,
                    'Area': Area,
                    'Adress': Adress,
                    'Price': Price,
                    'ImageLink': ImageLink
                }
                data.append(dic)
            except:
            
                pass

        # Convert data to DataFrame and concatenate with the main DataFrame
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df   


def load_Appartment_3_data(mul_page):
    df = pd.DataFrame() 
    # loop over pages indexes
    for p in range (1,int(mul_page)+1):
        url = f'https://www.expat-dakar.com/terrains-a-vendre?page={p}'
        res_c = requests.get(url)  # Fetch the page
        soup_c = bs(res_c.text, 'html.parser')  # Parse the HTML content
        containers = soup_c.find_all("div", class_="listings-cards__list-item")  # Extract listings

        data = []  # Temporary list to store data from the current page

        for container in containers:  # Loop through each listing
            try:
                # Get the listing link
                link = container.find('a')['href']
                res_c = requests.get(link)  # Fetch the listing details page
                soup_c = bs(res_c.text, 'html.parser')  # Parse the listing details page
                
                # Extract details
                Details = soup_c.find('div', class_="listing-item__details").text.split()[6]
                
                # Extract area
                Area = soup_c.find("dd", class_="listing-item__properties__description").text.strip().replace("m²", "")
                
                # Extract address
                Adress = soup_c.find("div", class_="listing-item__address").text.strip().replace("\n", "").replace("                           ", "")
                
                # Extract price
                Price = soup_c.find("span", class_="listing-card__price__value").text.strip().replace("\u202f", "").replace("F Cfa", "")
                
                # Extract image link
                ImageLink = soup_c.find("div", class_="gallery__image__inner").img["srcset"]
                
                # Append the extracted data as a dictionary
                dic = {
                    'Details': Details,
                    'Area': Area,
                    'Adress': Adress,
                    'Price': Price,
                    'ImageLink': ImageLink
                }
                data.append(dic)
            except Exception as e:
                # Optionally, you can print the error for debugging:
                # print(f"Error processing container: {e}")
                pass

        # Convert data to DataFrame and concatenate with the main DataFrame
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df   

st.sidebar.header('User Input Features')
Pages = st.sidebar.selectbox('Pages indexes', list([int(pages) for pages in np.arange(1, 123)]))
Choices = st.sidebar.selectbox('Options', ['Scrape the data using beautifulSoup', 'Download scraped data', 'Dashbord of the data',  'Fill the form'])

local_css('Group_5.css')  

if Choices=='Scrape the data using beautifulSoup':

    Appartment_1_data_mul_pag = load_Appartment1_data(Pages)
    Appartment_2_data_mul_pag = load_Appartment_2_data(Pages)
    Appartment_3_data_mul_pag = load_Appartment_3_data(Pages)


    load(Appartment_1_data_mul_pag, 'Rental_Appartment_1 data', '1', '101')
    load(Appartment_2_data_mul_pag, 'Rental_Appartment_2 data', '2', '102')
    load(Appartment_3_data_mul_pag, 'Rental_Appartment_3 data', '3', '103')
elif Choices == 'Download the scraped data': 
    Appartment_1_data = pd.read_csv('Apartment_1.csv')
    Appartment_2_data = pd.read_csv('Apartment _2.csv')
    Appartment_3_data = pd.read_csv('Apartment_3.csv') 

    load(Appartment_1_data, 'Rental_Appartment_1_Data', '1', '101')
    load(Appartment_2_data, 'Rental_Appartment_2_Data', '2', '102')
    load(Appartment_3_data, 'Rental_Appartment_3_Data', '3', '103') 

elif  Choices == 'Dashbord of the data': 
    df1 = pd.read_csv('Apartment _1.csv')
    df2 = pd.read_csv('Apartment _2.csv')
    df3 = pd.read_csv('Apartment _3.csv')

    col1, col2= st.columns(2)

with col1:
    plot1 = plt.figure(figsize=(11, 7))
    color = (0.2,  
             0.4,  
             0.2,  
             0.6) 
    plt.bar(df1.Area.value_counts()[:10].index, df1.Area.value_counts()[:10].values, color=color)
    plt.title('Top 10 Appartments with highest Area')
    plt.xlabel('Area')
    st.pyplot(plot1)


    with col2:
        plot2 = plt.figure(figsize=(11, 7))
        color = (0.5,  # red component
                0.7,  # green component
                0.9,  # blue component
                0.6)  # transparency
        plt.bar(df2.Area.value_counts()[:7].index, df2.Area.value_counts()[:7].values, color=color)
        plt.title('The Top 7 Appartments in Land Comparisson')
        plt.xlabel('Area')
        st.pyplot(plot2)








        
