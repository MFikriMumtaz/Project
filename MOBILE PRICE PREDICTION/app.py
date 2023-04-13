import streamlit as st
import pandas as pd
import joblib

# import model
with open('SVC_Model.pkl','rb') as file_1:
  model = joblib.load(file_1)

st.title("Mobile Price Prediction")

st.subheader("Insert feature to predict")

# user input
battery_power = st.slider(label="Mobile Battery Power", min_value=501, max_value=1998, value=501)
st.write('You Selected : ', battery_power)

blue = st.selectbox(label='Does it have Bluetooth?', options=[0, 1])
st.write('You Selected : ')
if blue == 0:
    st.write('No')
else:
    st.write('Yes')
         

clock_speed = st.slider(label='Mobile Clock Speed', min_value=0.5, max_value=3.0, value=0.5)
st.write('You Selected : ', clock_speed)

dual_sim = st.selectbox(label='Does it support Dual Sim?', options=[0, 1])
st.write('You Selected : ')
if dual_sim == 0:
    st.write('No')
else:
    st.write('Yes')

fc = st.slider(label="Mobile Front Camera Resolution (MP)", min_value=0, max_value=19, value=0)
st.write('You Selected : ', fc)

four_g = st.selectbox(label='Does it support 4G?', options=[0, 1])
st.write('You Selected : ', four_g)

int_memory = st.slider(label="Mobile Internal Memory (GB)", min_value=2, max_value=62, value=2)
st.write('You Selected : ', int_memory)

m_dep = st.slider(label="Mobile Depth (cm)", min_value=0.1, max_value=1.0, value=0.1)
st.write('You Selected : ', m_dep)

mobile_wt = st.slider(label="Mobile Weight (Gram)", min_value=80, max_value=200, value=80)
st.write('You Selected : ', mobile_wt)

n_cores = st.slider(label="Number of Cores", min_value=1, max_value=8, value=1)
st.write('You Selected : ', n_cores)

pc = st.slider(label="Mobile Primary Camera Resolution (MP)", min_value=0, max_value=20, value=0)
st.write('You Selected : ', pc)

px_height = st.slider(label="Pixel Height (px)", min_value=0, max_value=1960, value=0)
st.write('You Selected : ', px_height)

px_width = st.slider(label="Pixel Width (px)", min_value=0, max_value=1998, value=0)
st.write('You Selected : ', px_width)

ram = st.slider(label="Mobile RAM Value (MB)", min_value=256, max_value=3998, value=256)
st.write('You Selected : ', ram)

sc_h = st.slider(label="Screen Height (cm)", min_value=5, max_value=19, value=5)
st.write('You Selected : ', sc_h)

sc_w = st.slider(label="Screen Width (cm)", min_value=0, max_value=18, value=0)
st.write('You Selected : ', sc_w)

talk_time = st.slider(label="Longest time that a single battery charge will last when you are in calls (Hour)", min_value=2, max_value=20, value=2)
st.write('You Selected : ', talk_time)

three_g = st.selectbox(label='Does it support 3G?', options=[0, 1])
st.write('You Selected : ')
if three_g == 0:
    st.write('No')
else:
    st.write('Yes')

touch_screen = st.selectbox(label='Does it support Touch Screen?', options=[0, 1])
if touch_screen == 0:
    st.write('No')
else:
    st.write('Yes')

wifi = st.selectbox(label='Does it support Wifi?', options=[0, 1])
if wifi == 0:
    st.write('No')
else:
    st.write('Yes')

# convert into dataframe
data = pd.DataFrame({'Battery_Power': [battery_power],
                'Bluetooth': [blue],
                'Clock_Speed': [clock_speed],
                'Dual_Sim':[dual_sim],
                'Front_Camera': [fc],
                'Four_G': [four_g],
                'Internal_Memory': [int_memory],
                'Mobile_Depth': [m_dep],
                'Mobile_Width': [mobile_wt],
                'Number_of_Cores':[n_cores],
                'Primary_Camera': [pc],
                'Pixel_Height': [px_height],
                'Pixel_Width': [px_width],
                'Bluetooth': [blue],
                'RAM': [ram],
                'Screen_Height':[sc_h],
                'Screen_Width': [sc_w],
                'Talk_Time': [talk_time],
                'Three_G': [three_g],
                'Touch_Screen': [touch_screen],
                'Wifi': [wifi]
})

data = data.rename(columns={
    'Battery_Power': 'battery_power',
    'Bluetooth': 'blue',
    'Clock_Speed': 'clock_speed',
    'Dual_Sim': 'dual_sim',
    'Front_Camera': 'fc',
    'Four_G': 'four_g',
    'Internal_Memory': 'int_memory',
    'Mobile_Depth': 'm_dep',
    'Mobile_Width': 'mobile_wt',
    'Number_of_Cores': 'n_cores',
    'Primary_Camera': 'pc',
    'Pixel_Height': 'px_height',
    'Pixel_Width': 'px_width',
    'RAM': 'ram',
    'Screen_Height': 'sc_h',
    'Screen_Width': 'sc_w',
    'Talk_Time': 'talk_time',
    'Three_G': 'three_g',
    'Touch_Screen': 'touch_screen',
    'Wifi': 'wifi'
})

# interpretation
if st.button('Predict'):
    classifications = model.predict(data).tolist()[0]
    st.write('Prediction Result : ')
    if classifications == 0:
        st.subheader('Low Price')
    elif classifications == 1:
        st.subheader('Medium Price')
    elif classifications == 2:
        st.subheader('High Price')
    else:
        st.subheader('Very High Price')
