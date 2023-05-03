"""Name: Vivian Sabga
CS230: Section 6
Data: Meteorite Landings on Earth
Description: This program offers insights to users interested in meteorite landings on earth. /n
Firstly it displays a map of the 500 heaviest meteorite landings.  Then it allows you to choose the start and end year,
and displays the number of meteorite landings between those years followed by a bar graph of your selected data.
Finally, it allows you to choose a class of meteorite and select top ‘n’ heaviest meteorites in that class,
followed by a graph of this data."""

#import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker


#import data
#def import_dataset(file_path):
#    data = pd.read_excel(file_path, engine='openpyxl')
 #   return data


# filter through data frame based on specified meteorite class and select top n rows based on mass.
#def filter_data_by_class_and_top_n_heaviest(data, meteorite_class, top_n):
#    filtered_data = data[data['recclass'] == meteorite_class].nlargest(top_n, 'mass (g)')
#    return filtered_data


# creates a bar chat showing the mass of the top n heaviest meteorites of class selected.
#def plot_heaviest_meteorites(filtered_data):
 #   plt.figure(figsize=(12, 6))
  #  plt.barh(filtered_data['name'], filtered_data['mass (g)']) # horizontal bar chart
   # plt.xlabel('Mass (g)') # filtered mass
    #plt.ylabel('Meteorite Name') # filtered name
    #plt.title('Top N Heaviest Meteorites of Selected Class')
    #st.pyplot(plt.gcf())

# filters a range of years selected
#def filter_data_by_year_range(data, start_year, end_year):
 #   return data[(data['year'] >= start_year) & (data['year'] <= end_year)]

# creates a bar chart showing the number of meteorites found per year
#def plot_meteorites_per_year(filtered_data):
    # calculate meteorites found per year and sort in chronological order
   # meteorites_per_year = filtered_data['year'].value_counts().sort_index()
    #plt.figure(figsize=(12, 6))
    #plt.bar(meteorites_per_year.index, meteorites_per_year.values)
    #plt.xlabel('Year')
    #plt.ylabel('Number of Meteorites')
    #plt.title('Meteorites per Year')

    # Set the x-axis to only show integers
    #ax = plt.gca()
    # ticks would be integers instead of floating points
    #ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# display plot
   # st.pyplot(plt.gcf())


#file_path = "Meteorite_Landings.xlsx"
#data = import_dataset(file_path)

# converting the data in the year column to numeric data
# Replaces value with NaN (not a number) if error occurs
# downcasting data in year to the smallest integer possible
#data['year'] = pd.to_numeric(data['year'], errors='coerce', downcast='integer')

# removes rows that contain NaN
#data = data.dropna(subset=['year'])

#st.title("Meteorite Landings")

# Add an image called "theme website.jpeg"
#st.image("website theme.jpeg")

# Create a new DataFrame (map_data) with the required columns
# copy ensures any changes do not affect orignial data frame

#map_data = data[['name','mass (g)', 'reclat', 'reclong']].copy()
#map_data = map_data.sort_values('mass (g)', ascending=False)
#map_data = map_data.iloc[:500]

# Rename 'reclat' and 'reclong' columns to 'latitude' and 'longitude'
#map_data.rename(columns={'reclat': 'latitude', 'reclong': 'longitude'}, inplace=True)

# Drop rows with missing latitude or longitude values
#map_data = map_data.dropna(subset=['latitude', 'longitude'])


# Display the map using st.map()
#st.header("Map of 500 Heaviest Meteorite Landings")
#st.map(map_data.iloc[ :500,:])
#st.map(map_data)
#print(map_data)


# Add a button for the Meteorites per Year chart
#if st.button("Show Meteorites per Year Chart"):
    # allows you to enter a start and end year within the boundries
 #   start_year = st.number_input("Start Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=2010, step=1)
  #  end_year = st.number_input("End Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=2020, step=1)

    #if start_year > end_year:
     #   st.error("Start Year cannot be greater than End Year.")
  #  else:
       # filtered_data = filter_data_by_year_range(data, start_year, end_year)
        #st.write(f"Number of meteorites between {start_year} and {end_year}: {len(filtered_data)}")
        #st.write(filtered_data)
        # creates bar hart of the number of metoerites per year
        #st.header("Chart of Meteorites per Year")
        #plot_meteorites_per_year(filtered_data)


# Add a button for the Top N Heaviest Meteorites of a Certain Class chart
#if st.button("Show Top N Heaviest Meteorites of a Certain Class"):
    # select a meteorite class from the recclass column
  #  unique_classes = data['recclass'].unique()
   # meteorite_class = st.selectbox("Select Meteorite Class", options=sorted(unique_classes))
    # use slider to select the number of meteorites you want to display
    #top_n = st.slider("Select Top N", min_value=1, max_value=len(data[data['recclass'] == meteorite_class]), value=10)

# subset of selected data
  #  filtered_data = filter_data_by_class_and_top_n_heaviest(data, meteorite_class, top_n)
   # st.write(f"Top {top_n} heaviest meteorites of class {meteorite_class}:")
    #st.write(filtered_data)
    # plots the heaviest meteorites in class selected
    #st.header("Chart of Heaviest Meteorites in Selected Class")
    #plot_heaviest_meteorites(filtered_data)
    
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker



#import data
def import_dataset(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')
    return data


# filter through data frame based on specified meteorite class and select top n rows based on mass.
def filter_data_by_class_and_top_n_heaviest(data, meteorite_class, top_n):
    filtered_data = data[data['recclass'] == meteorite_class].nlargest(top_n, 'mass (g)')
    return filtered_data


# creates a bar chat showing the mass of the top n heaviest meteorites of class selected.
def plot_heaviest_meteorites(filtered_data):
    plt.figure(figsize=(12, 6))
    plt.barh(filtered_data['name'], filtered_data['mass (g)']) # horizontal bar chart
    plt.xlabel('Mass (g)') # filtered mass
    plt.ylabel('Meteorite Name') # filtered name
    plt.title('Top N Heaviest Meteorites of Selected Class')
    st.pyplot(plt.gcf())

# filters a range of years selected
def filter_data_by_year_range(data, start_year, end_year):
    return data[(data['year'] >= start_year) & (data['year'] <= end_year)]

# creates a bar chart showing the number of meteorites found per year
def plot_meteorites_per_year(filtered_data):
    # calculate meteorites found per year and sort in chronological order
    meteorites_per_year = filtered_data['year'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.bar(meteorites_per_year.index, meteorites_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Meteorites')
    plt.title('Meteorites per Year')

    # Set the x-axis to only show integers
    ax = plt.gca()
    # ticks would be integers instead of floating points
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# display plot
    st.pyplot(plt.gcf())


file_path = "Meteorite_Landings.xlsx"
data = import_dataset(file_path)

# converting the data in the year column to numeric data
# Replaces value with NaN (not a number) if error occurs
# downcasting data in year to the smallest integer possible
data['year'] = pd.to_numeric(data['year'], errors='coerce', downcast='integer')

# removes rows that contain NaN
data = data.dropna(subset=['year'])

st.title("Meteorite Landings")

# Add an image called "theme website.jpeg"
st.image("website theme.jpeg")

# Create a new DataFrame (map_data) with the required columns
# copy ensures any changes do not affect orignial data frame

map_data = data[['name','mass (g)', 'reclat', 'reclong']].copy()
map_data = map_data.sort_values('mass (g)', ascending=False)
map_data = map_data.iloc[:500]

# Rename 'reclat' and 'reclong' columns to 'latitude' and 'longitude'
map_data.rename(columns={'reclat': 'latitude', 'reclong': 'longitude'}, inplace=True)

# Drop rows with missing latitude or longitude values
map_data = map_data.dropna(subset=['latitude', 'longitude'])


# Display the map using st.map()
st.header("Map of 500 Heaviest Meteorite Landings")
#st.map(map_data.iloc[ :500,:])
st.map(map_data)
print(map_data)


# Add a button for the Meteorites per Year chart
if st.button("Show Meteorites per Year Chart"):
    # allows you to enter a start and end year within the boundries
    start_year = st.number_input("Start Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=2010, step=1)
    end_year = st.number_input("End Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=2020, step=1)

    if start_year > end_year:
        st.error("Start Year cannot be greater than End Year.")
    else:
        filtered_data = filter_data_by_year_range(data, start_year, end_year)
        st.write(f"Number of meteorites between {start_year} and {end_year}: {len(filtered_data)}")
        st.write(filtered_data)
        # creates bar hart of the number of metoerites per year
        st.header("Chart of Meteorites per Year")
        plot_meteorites_per_year(filtered_data)


# Add a button for the Top N Heaviest Meteorites of a Certain Class chart
if st.button("Show Top N Heaviest Meteorites of a Certain Class"):
    # select a meteorite class from the recclass column
    unique_classes = data['recclass'].unique()
    meteorite_class = st.selectbox("Select Meteorite Class", options=sorted(unique_classes))
    # use slider to select the number of meteorites you want to display
    top_n = st.slider("Select Top N", min_value=1, max_value=len(data[data['recclass'] == meteorite_class]), value=10)

# subset of selected data
    filtered_data = filter_data_by_class_and_top_n_heaviest(data, meteorite_class, top_n)
    st.write(f"Top {top_n} heaviest meteorites of class {meteorite_class}:")
    st.write(filtered_data)
    # plots the heaviest meteorites in class selected
    st.header("Chart of Heaviest Meteorites in Selected Class")
    plot_heaviest_meteorites(filtered_data)
    print(filtered_data)

