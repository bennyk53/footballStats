import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def runButtonClicked():
    st.session_state.runButton = True
    st.session_state.passButton = False
    st.session_state.bothButton = False

def passButtonClicked():
    st.session_state.passButton = True
    st.session_state.runButton = False
    st.session_state.bothButton = False

def bothButtonClicked():
    st.session_state.passButton = False
    st.session_state.runButton = False
    st.session_state.bothButton = True

def local_css(fileName):
    with open(fileName) as f:
        st.markdown(f"<style>{f.read()}</sytle>", unsafe_allow_html=True)


def intro():
    import streamlit as st

    st.write("# Welcome to Dumb Guard Football Analytics! :football:")
    st.sidebar.success("Select a module above.")


    st.markdown(
    """
    Dumb Guard Football Analytics provides a place for coaches, players, team managers, or fans
    can upload a CSV file and use our tools to find insights into your own teams performance, or a
    scouting report for you next opponent.   

    ### Offensive Analysis   
    
    - Download example CSV file """)

    with open("Offense.csv", "rb") as file:
        btn = st.download_button(
            label="Download Template",
            data=file,
            file_name="OffenseTemplate.csv",
            mime="text/csv"
          )

    st.markdown(
    """
    - Make sure when editing the template that the column names remain the same but your plays, formations and personnell packages can all be your own
    - Once your CSV file is ready to upload navigate to the 'Upload Files' module from the sidebar :point_left:

    ### Defensive Analysis 

    - Download example CSV file """)
    
    with open("Defense.csv", "rb") as file:
        btn = st.download_button(
            label="Download Template",
            data=file,
            file_name="DefenseTemplate.csv",
            mime="text/csv"
          )

    st.markdown(
    """
    - Make sure when editing the template that the column names remain the same but your fronts, blitzes, coverages and stunts can all be your own
    - Once your CSV file is ready to upload navigate to the 'Upload Files' module from the sidebar :point_left:

    """
    )

def upload_files():
    offence_files = st.file_uploader("Choose a Offense CSV file", accept_multiple_files=True)
    if offence_files:
        for file in offence_files:
            file.seek(0)
        uploaded_data_read = [pd.read_csv(file) for file in offence_files]
        rawOff = pd.concat(uploaded_data_read)
        st.dataframe(rawOff)
        st.session_state.dfO = rawOff

    defense_files = st.file_uploader("Choose a Defense CSV file", accept_multiple_files=True)
    if defense_files:
        for file in defense_files:
            file.seek(0)
        uploaded_data_read = [pd.read_csv(file) for file in defense_files]
        rawDef = pd.concat(uploaded_data_read)
        st.dataframe(rawDef)
        st.session_state.dfD = rawDef


def offence():
    if 'runButton' not in st.session_state:
        st.session_state.runButton = False

    if 'passButton' not in st.session_state:
        st.session_state.passButton = False

    if 'bothButton' not in st.session_state:
        st.session_state.bothButton = True

    
    st.write("# Offensive Analysis")
    try:
        st.write('Use the tools on the side bar to load and analyze your data')
        st.sidebar.header('User Input Features')
        df = st.session_state.dfO
        df = df[df['PLAY'].notna()]

        options = ['Formation','Personnel','Play']
        selected_cat = st.sidebar.multiselect('Catagories', options, [])

        s = []
        selected_form = ''

        if (len(selected_cat) > 0):
            cat1 = selected_cat[0]
            vals1 = df[cat1.upper()].unique().tolist()
            if (cat1 == 'Play'):
                st.sidebar.write(cat1)
                autoList = []
                runButton = st.sidebar.button('Run Plays',on_click=runButtonClicked)
                if (st.session_state.runButton):
                    autoList = df.loc[df['R/P'] == 'R']['PLAY'].unique().tolist()
                passButton = st.sidebar.button('Pass Plays',on_click=passButtonClicked)
                if (st.session_state.passButton):
                    autoList = df.loc[df['R/P'] == 'P']['PLAY'].unique().tolist()
                bothButton = st.sidebar.button('All Plays',on_click=bothButtonClicked)
                if (st.session_state.bothButton):
                    autoList = df['PLAY'].unique().tolist()
                selected_vals1 = st.sidebar.multiselect('Specific Plays', vals1, autoList)
            else:
                selected_vals1 = st.sidebar.multiselect(cat1, vals1, [])
        
            if (len(selected_cat) > 1 and len(selected_vals1) > 0):
                cat2 = selected_cat[1]
                vals2 = df[cat2.upper()].unique().tolist()
                if (cat2 == 'Play'):
                    st.sidebar.write(cat2)
                    autoList = []
                    runButton = st.sidebar.button('Run Plays',on_click=runButtonClicked)
                    if (st.session_state.runButton):
                        autoList = df.loc[df['R/P'] == 'R']['PLAY'].unique().tolist()
                    passButton = st.sidebar.button('Pass Plays',on_click=passButtonClicked)
                    if (st.session_state.passButton):
                        autoList = df.loc[df['R/P'] == 'P']['PLAY'].unique().tolist()
                    bothButton = st.sidebar.button('All Plays',on_click=bothButtonClicked)
                    if (st.session_state.bothButton):
                        autoList = df['PLAY'].unique().tolist()
                    selected_vals2 = st.sidebar.multiselect('Specific Plays', vals2, autoList)
                else:
                    selected_vals2 = st.sidebar.multiselect(cat2, vals2, [])

                if (len(selected_cat) > 2 and len(selected_vals2) > 0):
                    cat3 = selected_cat[2]
                    vals3 = df[cat3.upper()].unique().tolist()
                    if (cat3 == 'Play'):
                        st.sidebar.write(cat2)
                        autoList = []
                        runButton = st.sidebar.button('Run Plays',on_click=runButtonClicked)
                        if (st.session_state.runButton):
                            autoList = df.loc[df['R/P'] == 'R']['PLAY'].unique().tolist()
                        passButton = st.sidebar.button('Pass Plays',on_click=passButtonClicked)
                        if (st.session_state.passButton):
                            autoList = df.loc[df['R/P'] == 'P']['PLAY'].unique().tolist()
                        bothButton = st.sidebar.button('All Plays',on_click=bothButtonClicked)
                        if (st.session_state.bothButton):
                            autoList = df['PLAY'].unique().tolist()
                        selected_vals3 = st.sidebar.multiselect('Specific Plays', vals3, autoList)
                    else:
                        selected_vals3 = st.sidebar.multiselect(cat3, vals3, [])
            
            d = df.groupby(cat1.upper()).count()['DN']
            x = pd.DataFrame({cat1:d.index, 'Number of Plays':d.values})
            st.dataframe(x)

            controlOptions = ['Yards Gained','Hash','D & D']
            controls_selected = st.sidebar.multiselect('Controllers', controlOptions, [])

            for x in selected_vals1: 
                a = df.loc[df[cat1.upper()] == x]
                if (len(selected_cat) > 1):
                    a = a[a[cat2.upper()].isin(selected_vals2)]
                    if (len(selected_cat) > 2):
                        a = a[a[cat3.upper()].isin(selected_vals3)]
                st.write(x)
                if ('Yards Gained' in controls_selected):
                    y = st.slider('Yards gained', -10, 20, 5, key=x)
                    a = a.loc[a['GAIN'] >= y]
                if ('Hash' in controls_selected):
                    hashMark = st.radio( "Hash:",('Right Hash', 'Left Hash','Middle'), key=x)
                    hashMark = hashMark[0]
                    print(hashMark)
                    a = a.loc[a['HASH'] == hashMark]     
                if ('D & D' in controls_selected):
                    dAndD = st.radio( "D & D:",('1st and 10', '2nd and 1-3','2nd and 4-6','2nd and 7+'), key=x)
                    if (dAndD == '1st and 10'):
                        a = a.loc[(a['DN'] == 1) & (a['DST'] == 10)]
                    elif (dAndD == '2nd and 1-3'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 1) & (a['DST'] <= 3)]
                    elif (dAndD == '2nd and 4-6'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 4) & (a['DST'] <= 6)]
                    elif (dAndD == '2nd and 7+'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 7)]
                        
                        
                st.dataframe(a)
                csv = a.to_csv().encode('utf-8')
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name= x+'.csv',
                    mime='text/csv',
                    )
    except:
        st.write("An error has occurred. Make sure you have a valid CSV uploaded, or contact us using the feedback section")
        

def defence():
    st.write("# Defensive Analysis")
    try:
        st.write('Use the tools on the side bar to load and analyze your data')
        st.sidebar.header('User Input Features')
        df = st.session_state.dfD
        df = df[df['FRONT'].notna()]

        options = ['Front','Blitz','Coverage','Stunt']
        selected_cat = st.sidebar.multiselect('Catagories', options, [])

        s = []
        selected_form = ''

        if (len(selected_cat) > 0):
            cat1 = selected_cat[0]
            vals1 = df[cat1.upper()].unique().tolist()
            selected_vals1 = st.sidebar.multiselect(cat1, vals1, [])

            if (len(selected_cat) > 1 and len(selected_vals1) > 0):
                cat2 = selected_cat[1]
                vals2 = df[cat2.upper()].unique().tolist()
                selected_vals2 = st.sidebar.multiselect(cat2, vals2, [])

                if (len(selected_cat) > 2 and len(selected_vals2) > 0):
                    cat3 = selected_cat[2]
                    vals3 = df[cat3.upper()].unique().tolist()
                    selected_vals3 = st.sidebar.multiselect(cat3, vals3, [])

                    if (len(selected_cat) > 3 and len(selected_vals3) > 0):
                        cat4 = selected_cat[3]
                        vals4 = df[cat4.upper()].unique().tolist()
                        selected_vals4 = st.sidebar.multiselect(cat4, vals4, [])
            
            d = df.groupby(cat1.upper()).count()['DN']
            x = pd.DataFrame({cat1:d.index, 'Number of Plays':d.values})
            st.dataframe(x)

            controlOptions = ['D & D']
            controls_selected = st.sidebar.multiselect('Controllers', controlOptions, [])

            for x in selected_vals1: 
                a = df.loc[df[cat1.upper()] == x]
                if (len(selected_cat) > 1):
                    a = a[a[cat2.upper()].isin(selected_vals2)]
                    if (len(selected_cat) > 2):
                        a = a[a[cat3.upper()].isin(selected_vals3)]
                st.write(x)    
                if ('D & D' in controls_selected):
                    dAndD = st.radio( "D & D:",('1st and 10', '2nd and 1-3','2nd and 4-6','2nd and 7+'), key=x)
                    if (dAndD == '1st and 10'):
                        a = a.loc[(a['DN'] == 1) & (a['DST'] == 10)]
                    elif (dAndD == '2nd and 1-3'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 1) & (a['DST'] <= 3)]
                    elif (dAndD == '2nd and 4-6'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 4) & (a['DST'] <= 6)]
                    elif (dAndD == '2nd and 7+'):
                        a = a.loc[(a['DN'] == 2) & (a['DST'] >= 7)]
                    
                st.dataframe(a)
                csv = a.to_csv().encode('utf-8')
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name= x+'.csv',
                    mime='text/csv',
                    )
    except:
        st.write("An error has occurred. Mformajimake sure you have a valid CSV uploaded, or contact us using the feedback section")

def feedback():
    st.write("# Feedback")
    st.markdown(
    """
    If you have any issues with the application, or have feedback on how we can improve the system please email us
    at dumguard.53@gmail.com.

    We appreciate your use of our application and your assitance in making this a tool that helps coaches all over
    Canada. 

    """)

    

page_names_to_funcs = {
    "Weclome": intro,
    "Upload Files": upload_files,
    "Offence Analysis": offence,
    "Defence Analysis": defence,
    "Feedback": feedback
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
