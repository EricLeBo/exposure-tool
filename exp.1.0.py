import streamlit as st
import pandas as pd

# date manipulation
import datetime
from dateutil.relativedelta import relativedelta 


st.sidebar.title("Exposure Tool for General Aviation")

st.markdown(
"""
<style>
.stApp{
    background-color: #a0d2eb;
}
.stSelectbox div[data-baseweb="select"] > div:first-child {
            background-color: #fceed1;
            border-color: #fceed1;
}

</style>
""",
       unsafe_allow_html=True
)
######  The functions  ######

def first_day_of_next_month(dt):
    '''Get the first day of the next month. Preserves the timezone.

    Args:
        dt (datetime.datetime): The current datetime

    Returns:
        datetime.datetime: The first day of the next month at 00:00:00.
    '''
    if dt.month == 12:
        return datetime.datetime(year=dt.year+1,
                                 month=1,
                                 day=1,
                                 tzinfo=dt.tzinfo)
    else:
        return datetime.datetime(year=dt.year,
                                 month=dt.month+1,
                                 day=1,
                                 tzinfo=dt.tzinfo)



def radio_cached(radio_label, radio_list, radio_name):
    cache1 = radio_name + '_cache1'
    cache2 = radio_name + '_cache2'

    if radio_name not in st.session_state or st.session_state[radio_name] is None:
        value = st.radio(radio_label, radio_list, index=None, horizontal=True, label_visibility='visible', key=cache1)
        st.session_state[radio_name] = st.session_state[cache1]

    elif radio_name in st.session_state:
        if cache1 not in st.session_state:
            st.session_state[cache1] = st.session_state[radio_name]
        value = st.radio(radio_label, radio_list, index=radio_list.index(st.session_state[cache1]), horizontal=True, label_visibility='visible', key=cache2)
        st.session_state[radio_name] = st.session_state[cache2]

    elif cache2 in st.session_state:
        value = st.radio(radio_label, radio_list, index=radio_list.index(st.session_state[cache2]), horizontal=True, label_visibility='visible', key=cache2)
        st.session_state[radio_name] = st.session_state[cache2]


    if cache1 in st.session_state and st.session_state[cache1] != st.session_state[radio_name]:
        st.session_state[radio_name] = st.session_state[cache1]

    if cache2 in st.session_state and st.session_state[cache2] != st.session_state[radio_name]:
        st.session_state[radio_name] = st.session_state[cache2]

    return value



def date_cached(date_label, date_default, date_name):
    cache1 = date_name + '_cache1'
    cache2 = date_name + '_cache2'

    if date_name not in st.session_state or st.session_state[date_name] is None:
        value = st.date_input(date_label, value=date_default, format='DD/MM/YYYY', help= 'Automatically set to the first day of next month', key=cache1)
        st.session_state[date_name] = st.session_state[cache1]
    
    elif cache2 in st.session_state:
        value = st.date_input(date_label, value=st.session_state[cache2], format='DD/MM/YYYY', help= 'Automatically set to the first day of next month', key=cache2)
        st.session_state[date_name] = st.session_state[cache2]

    elif date_name in st.session_state:
        if cache1 not in st.session_state:
            st.session_state[cache1] = st.session_state[date_name]
        value = st.date_input(date_label, value=st.session_state[cache1], format='DD/MM/YYYY', help= 'Automatically set to the first day of next month', key=cache2)
        st.session_state[date_name] = st.session_state[cache2]


    if cache1 in st.session_state and st.session_state[cache1] != st.session_state[date_name]:
        st.session_state[date_name] = st.session_state[cache1]

    if cache2 in st.session_state and st.session_state[cache2] != st.session_state[date_name]:
        st.session_state[date_name] = st.session_state[cache2]
    
    return value


def selectbox_cached(box_label, box_list, box_name):
    cache1 = box_name + '_cache1'
    cache2 = box_name + '_cache2'

    if box_name not in st.session_state or st.session_state[box_name] is None:
        value = st.selectbox(box_label, box_list, index = None, label_visibility = 'visible', help='From a CSV file', key=cache1)
        st.session_state[box_name] = st.session_state[cache1]
    
    elif cache2 in st.session_state:
        value = st.selectbox(box_label, box_list, index = box_list.index(st.session_state[cache2]), label_visibility = 'visible', help='From a CSV file', key=cache2)
        st.session_state[box_name] = st.session_state[cache2]

    elif box_name in st.session_state:
        if cache1 not in st.session_state:
            st.session_state[cache1] = st.session_state[box_name]
        value = st.selectbox(box_label, box_list, index = box_list.index(st.session_state[cache1]), label_visibility = 'visible', help='From a CSV file', key=cache2)
        st.session_state[box_name] = st.session_state[cache2]


    if cache1 in st.session_state and st.session_state[cache1] != st.session_state[box_name]:
        st.session_state[box_name] = st.session_state[cache1]

    if cache2 in st.session_state and st.session_state[cache2] != st.session_state[box_name]:
        st.session_state[box_name] = st.session_state[cache2]
    
    return value


def text_input_cached(text_label, text_name):
    cache1 = text_name + '_cache1'
    cache2 = text_name + '_cache2'

    if text_name not in st.session_state or st.session_state[text_name] is None:
        value = st.text_input(text_label, key=cache1)
        st.session_state[text_name] = st.session_state[cache1]
    
    elif cache2 in st.session_state:
        value = st.text_input(text_label,  value = st.session_state[cache2], key=cache2)
        st.session_state[text_name] = st.session_state[cache2]

    elif text_name in st.session_state:
        if cache1 not in st.session_state:
            st.session_state[cache1] = st.session_state[text_name]
        value = st.text_input(text_label,  value = st.session_state[cache1], key=cache2)
        st.session_state[text_name] = st.session_state[cache2]


    if cache1 in st.session_state and st.session_state[cache1] != st.session_state[text_name]:
        st.session_state[text_name] = st.session_state[cache1]

    if cache2 in st.session_state and st.session_state[cache2] != st.session_state[text_name]:
        st.session_state[text_name] = st.session_state[cache2]
    
    return value


def cache_data():
    def cache_data_item(item_name, item_init):
        if item_name not in st.session_state:
            st.session_state[item_name] = item_init

        elif f'{item_name}_cache' in st.session_state and item_name in globals():
            st.session_state[item_name] = globals()[item_name]

    cache_data_item('layers', layers_init)
    cache_data_item('curves', curves_init)
    cache_data_item('exposure', exposure_init)
    

def results_func(show=False, layers_update=False, curves_update=False):

    try :
        # Joining on 'Group' Exposure and Curves to retrieve 'GU ELR' and 'Weight'
        if curves_update:
            curves_df = curves.copy()
        else:
            curves_df = st.session_state.curves.copy()

        calc = st.session_state.exposure.copy()

        calc = calc.dropna(subset = ['Group'])
        for i in ['GU ELR', 'Weight', 'Curve']:
            calc = calc.merge(curves_df[['Group', i]], on='Group', how='left')

        calc['GU ELR'] = calc['GU ELR'] / 100
        calc['Weight'] = calc['Weight'] / 100
        calc['Exposure'] = calc['Sum Insured'] / calc['# Risks']

        premium_total = calc['Premium'].sum()  # Total premium

        # Expected loss per risk
        calc['ELR per risk'] = calc['Premium'] / calc['# Risks']* calc['GU ELR'] * calc['Weight'] * 10 # model to develop, utilizing curve models
     
        # Layers
        if layers_update:
            layers_df = layers.copy()
        else:
            layers_df = st.session_state.layers.copy()



        layers_num = layers_df[layers_df['Limit'].notnull()].shape[0]
        for i in range(layers_num):    # number of rows in layers_df
            calc[f'Layer {i+1}'] = (calc['ELR per risk'] - layers_df.iloc[i, 2]).clip(lower=0, upper=layers_df.iloc[i, 1]) * 0.005 * calc['# Risks'] # Value of the i_th layer


        # Create the results dataframe
        results = pd.DataFrame(columns=['Layer', 'EL', 'Rate', 'RoL', 'STDV'])
        for i in range(layers_num):
            results.loc[i] = [i+1, calc[f'Layer {i+1}'].sum(), calc[f'Layer {i+1}'].sum() / premium_total, calc[f'Layer {i+1}'].sum() / layers_df.iloc[i, 1], None]    #Layer number and Expected Loss

        results['Rate'] = results['Rate'].apply(lambda x:"{:.2%}".format(x))
        results['RoL'] = results['RoL'].apply(lambda x:"{:.2%}".format(x))

        results['STDV'] = 3 * results['EL'] 
        st.session_state.results = results

        st.session_state.exposure_calc = calc.copy()
        
        if show:
            st.dataframe(st.session_state.exposure_calc, width = 800, hide_index = True)

    except: pass

######  The constants  ######

# dates:
date_next_month = first_day_of_next_month(datetime.datetime.now())
date_year = date_next_month + relativedelta(years=1, days = -1)
date_months_ago = date_next_month + relativedelta(months=-6, days = 15)

profiles = ['LOD', 'RAD']


data = pd.read_csv('data.csv', sep=';', header=0)
underwriters = data.Underwriters.values.tolist()
underwriters = [item for item in underwriters if not(pd.isnull(item)) == True]

actuaries = data.Actuaries.values.tolist()
actuaries = [item for item in actuaries if not(pd.isnull(item)) == True]

currencies = data.Currencies.values.tolist()
currencies = [item for item in currencies if not(pd.isnull(item)) == True]



layers_init = pd.DataFrame(
    [
        {"Layer": i, "Limit": None, "Deductible": None} for i in range(1, 10)
    ]
)

curves_init = pd.DataFrame(
    [
       {"Group":i, "Source": None, "GU ELR": None, "Weight": None, "Curve": None} for i in range(1, 10)
   ]
)

exposure_init = pd.DataFrame(
    [
        {"Group": None, "Ref": None, "From": None, "To": None, '# Risks': None, 'Sum Insured': None, 'Premium':None} for i in range(1, 40)
    ]
)

curve_models = ['Fixed Wing', 'Rotor Wing', 'US Exposed PB&B', 'P10', 'P11', 'P12']


limit_profiles = [
    'Location – Sum Insured',
    'Location – PML/MFL',
    'Policy – Mostly Single Location Policies',
    'Policy – Large Schedules – Limit is a realistic worst-case loss ',
    'Policy – Large Schedules – Limit overstates the worst-case loss (e.g. TSI)',
    'Policy – Excess / Shared and Layered',
    'Policy – PML/MFL',
    'Unknown']




######  The pages  ######

# ______  The Program page  ______

page = st.sidebar.selectbox('Select Page',['Program','Curves', 'Exposure', 'Results'], label_visibility = 'collapsed', on_change = cache_data)


if page=='Program':

    # Split the page into two columns
    col1, col2 = st.columns(2)

    with col1:
        program = text_input_cached('Program', 'program')
        insurer = text_input_cached('Insurer', 'insurer')
        broker = text_input_cached('Broker', 'broker')

        underwriter = selectbox_cached('Underwriter',underwriters, 'underwriter')
        actuary = selectbox_cached('Actuary',actuaries, 'actuary')

#        try:
        if 'layers' in st.session_state:
            layers_test = st.session_state.layers.copy()
        else:
            st.session_state.layers = layers_init.copy()


        layers = st.data_editor(st.session_state.layers, hide_index = True, key = 'layers_cache',
            column_config={
                "Limit": st.column_config.NumberColumn(step='1'),
                "Deductible": st.column_config.NumberColumn(step='1'),
            },
            disabled = ['Layer']
        )

#        except: pass

    with col2:
        date_start = date_cached('Cover Start', date_next_month, 'date_start')
        date_end = date_cached('Cover End', date_year, 'date_end')
        date_profile = date_cached('Profile Date', date_months_ago, 'date_profile')
        currency = selectbox_cached('Currency',currencies, 'currency')
        profile = radio_cached('Profile', profiles, 'profile')
    

    try:
        # if the layers are modified, the result is recalculated
        if not layers_test.equals(layers):
            results_func(layers_update=True)

    except: pass


   
# ______  The Curves  ______

elif page =='Curves':
    
    try:
        # Limit profile type
        limit_profile = selectbox_cached('Limit Profile Type',limit_profiles, 'limit_profile')

        st.write('GU ELR, Weight and Curve assignemnt')
     
        curves_test = st.session_state.curves.copy()
        curves = st.data_editor(st.session_state.curves, hide_index = True, key = 'curves_cache',
          column_config={
              "Source": st.column_config.TextColumn(width=100),
              "GU ELR": st.column_config.NumberColumn(format = '%.0f %%', width=100),
              "Weight": st.column_config.NumberColumn(format = '%.0f %%', width=100),
              "Curve": st.column_config.SelectboxColumn(options=curve_models, width=180)
          },
          disabled = ['Group']
        )

        # if the Curves are modified, the result is recalculated
        if not curves_test.equals(curves):
            results_func(curves_update=True)

    except: pass


# ______  The Exposure  ______

elif page =='Exposure':
    
    try:
        st.write('Exposure')
        exposure = st.data_editor(st.session_state.exposure, hide_index = True, key = 'exposure_cache', num_rows = 'dynamic',
            column_config={
              'Group': st.column_config.NumberColumn(width=70),
              'Ref': st.column_config.TextColumn(width=100),
              'From': st.column_config.NumberColumn(step='1', width=100),
              'To': st.column_config.NumberColumn(step='1', width=100),
              '# Risks': st.column_config.NumberColumn(width=80),
              'Sum Insured': st.column_config.NumberColumn(step='1', width=100),
              'Premium': st.column_config.NumberColumn(step='1', width=100)
            }
        )

    except:
        pass



# ______  The Results  ______

elif page =='Results':
    try:
        st.write('Premium Split: SI')

        results_func(show=True)

    except:
        pass

elif page == 'draft':
    pass




# ______  Bottom of the sidebar  ______

try:
    st.sidebar.header(st.session_state.program)
    if st.session_state.profile is not None and st.session_state.currency is not None:
        st.sidebar.write(st.session_state.profile, ' in ', st.session_state.currency)

    st.sidebar.write("From ", st.session_state.date_start.strftime("%d-%m-%y"), " to ", st.session_state.date_end.strftime("%d-%m-%y"))
    st.sidebar.dataframe(st.session_state.results, hide_index = True)
    st.sidebar.text('Dummy figures')

except:
    pass

st.sidebar.title('')
st.sidebar.title('')
st.sidebar.text('Created by : Eric Le Boullenger')

#st.sidebar.write(st.session_state.exposure)
