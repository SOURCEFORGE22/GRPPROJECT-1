import streamlit as st
import streamlit.components.v1 as com
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from matplotlib.pyplot import figure

# Set page config
st.set_page_config(
    page_title="BIOMOLECULE PREDICTION SYSTEM",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None,
)


# Read HTML file and display it using the com.html component
with open("App/Pages/homecopy.html", "r", encoding="utf-8") as html_file:
    source_code = html_file.read()
com.html(source_code, height=1000)

def const_data():
    # Import dataset
    df_train = pd.read_csv("App/Data/train.csv")
    features = list(df_train.drop("Activity", axis=1).columns)
    # Load model from pickle
    with open("App/Data/rfmodel.pkl", "rb") as pickle_file:
        pickled_model = pickle.load(pickle_file)

    return df_train, features, pickled_model

df_train, features, pickled_model = const_data()

with st.container():
    def add_bg_from_url():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://images.unsplash.com/photo-1528460033278-a6ba57020470?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGRhcmslMjB3aGl0ZSUyMGJhY2tncm91bmR8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    add_bg_from_url() 
    cl1, cl2 = st.columns(2, gap="small")
    with cl1:
        st.header("VISUALS CORNER")
        st.write("Class Imbalance Outcome")
        # sns.catplot(x = 'Activity', hue = 'Activity',data = df_train, kind = "count")
        st.image("App/images/classImbalance.png", use_column_width="always")

        st.write("Histogram and Violin Plot of A feature")
        column = st.text_input(
            "Choose between D1 - D1776", value="D1", max_chars=5, key="search"
            )
        if column not in features:
            st.write("Please enter a feature name between D1 and D1776, inclusive.")
        else:
            st.write("Plots:")
            tab1, tab2 = st.tabs(["Histogram", "Violin"])
            with tab1:
                # counts, bins = np.histogram(df_train[column])
                # figure(figsize=(8, 6), dpi=80)
                fig = plt.figure()
                # plt.stairs(counts, bins)
                # fig_html = mpld3.fig_to_html(fig)
                # com.html(fig_html, height=600)
                sns.histplot(
                    data=df_train[column], stat="probability", kde=True
                ).set(
                    title="Normal Distribution Plot of Independent Feature: " + column
                )
                st.pyplot(fig)
            with tab2:
                fig = plt.figure()
                sns.violinplot(data = list(df_train[column])).set_title("Violin Plot of Independent Feature: "+ column)
                st.pyplot(fig)
        st.write("Top 10 Most Important Features:")
        df_features = pd.read_csv("App/Data/importantFeatures.csv")
        feat = plt.figure()
        plt.barh(df_features.Features[:10], df_features.importance[:10])
        plt.xlabel("Random Forest Feature Importance")
        st.pyplot(feat)
        feat_csv = df_features.to_csv(index = False)
        st.write("Click button to download .csv file of feature importance. Note that the higher the value in the 'importance' column, the higher the importance of the feature in influencing the biological response.")
        st.download_button("DOWNLOAD FEATURE IMPORTANCE DATASET", feat_csv, 'Molecule feature importance .csv')


    with cl2:
        with st.form(key = 'prediction', clear_on_submit = False):
            st.header("PREDICTION SQUARE")
            instructions =  """
                                ### *Guidelines* <br>
                                Follow these guidelines to successfully generate predictions: <br>
                                1. The imported .csv file should have column names (in first row), in the following order, starting from the first column: D1, D2, D3, ..., D1776 <br>
                                2. There should be 1776 columns in the .csv file <br>
                                3. No other column should be present other than those indicated in (1) above <br>
                            """
            st.markdown(instructions, unsafe_allow_html = True)
            st.markdown("### *Upload file*", unsafe_allow_html = True)
            csv_file = st.file_uploader("Choose a CSV file", accept_multiple_files = False)
            st.form_submit_button("SUBMIT")
        predict = False
        if csv_file is not None:
            #confirming file type is .csv
            if csv_file.name[-3:] == 'csv':
                df_test = pd.read_csv(csv_file)
                columns_test = list(df_test.columns)
                if "Activity" in columns_test:
                    st.write("Please provide a csv file with the correct structure")
                elif features != columns_test:
                    st.write("Please provide a csv file with the correct structure.\nError: Unexpected arrangement of columns or unexpected column name found. Please confirm that the columns you have submitted have names from D1 to D1776 in ascending order")
                else:
                    predict = True                
        
        #prediction
        inactive_button = True
        if predict == True:
            inactive_button =False
        st.markdown("### *Predict*", unsafe_allow_html = True)
        st.write('Click the "Predict" button to get predictions')
        if st.button("PREDICT", help = "The button will only activate if the csv file is valid", disabled = inactive_button):
            predictions = pickled_model.predict(df_test)
            l = len(predictions)
            observations = [x for x in range(1,l+1,1)]
            output = pd.DataFrame({"Observation": observations, "Prediction": predictions})
            st.write("The probability of showing the biological response is:\n")
            output_csv = output.to_csv(index = False)
            st.download_button("DOWNLOAD CSV", output_csv, 'biological response prediction.csv')
            with st.expander("Click to view the predictions in a table", expanded = False):
                st.dataframe(output)
            
