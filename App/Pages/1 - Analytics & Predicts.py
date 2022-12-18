
import sys
import streamlit as st
import streamlit as st
import streamlit.components.v1 as com
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pickle
from sklearn.ensemble import RandomForestClassifier
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

sys.settrace
def const_data():

    #import dataset
    df_train = pd.read_csv("Data/train.csv")
    features = list(df_train.drop('Activity', axis = 1).columns)
    #load model from pickle
    pickled_model = pickle.load(open('Data/rfmodel.pkl', 'rb'))

    return df_train, features, pickled_model

df_train, features, pickled_model = const_data()

with st.container():
    cl1, cl2 = st.columns(2, gap = "small")
    with cl1:
        st.header("VISUALS CORNER")
        st.write("Class Imbalance Outcome")
        # sns.catplot(x = 'Activity', hue = 'Activity',data = df_train, kind = "count")
        st.image("images/classImbalance.png", use_column_width = 'always')
    
        st.write("Histogram and Violin Plot of A feature")
        column = st.text_input("Choose between D1 - D1776", value = 'D1', max_chars = 5, key = 'search')
        if column not in features:
            st.write("Please enter a feature name between D1 and D1776, inclusive.")
        else:
            st.write("Plots:")
            tab1, tab2 = st.tabs(['Histogram', 'Violin'])
            with tab1:
                #counts, bins = np.histogram(df_train[column])
                #figure(figsize=(8, 6), dpi=80)
                fig = plt.figure()
                #plt.stairs(counts, bins)
                #fig_html = mpld3.fig_to_html(fig)
                #com.html(fig_html, height=600)
                sns.histplot(data = df_train[column],
                            stat = 'probability', 
                            kde = True
                            ).set(title = "Normal Distribution Plot of Independent Feature: "+ column)
                st.pyplot(fig)
            with tab2:
                fig = plt.figure()
                sns.violinplot(data = list(df_train[column])).set_title("Violin Plot of Independent Feature: "+ column)
                st.pyplot(fig)
    with cl2:
        with st.form(key = 'prediction', clear_on_submit = False):
            st.header("PREDICTION SQUARE")
            st.write("Click button to upload .csv file:")
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

        st.write('Click the "Predict" button to get predictions')
        if st.button("PREDICT", help = "The button will only activate if the csv file is valid", disabled = inactive_button):
            predictions = pickled_model.predict(df_test)
            l = len(predictions)
            observations = [x for x in range(1,l+1,1)]
            output = pd.DataFrame({"Observation": observations, "Prediction": predictions})
            st.write("The probability of showing the biological response is:\n")
            output_csv = output.to_csv(index = False)
            #with st.expander("Click to view the predictions in a table", expanded = False):
                #st.dataframe(output)
                # gb = GridOptionsBuilder.from_dataframe(output)
                # gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                # gb.configure_side_bar() #Add a sidebar
                # gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                # gridOptions = gb.build()
                # grid_response = AgGrid(
                #                         data,
                #                         gridOptions=gridOptions,
                #                         data_return_mode='AS_INPUT', 
                #                         update_mode='MODEL_CHANGED', 
                #                         fit_columns_on_grid_load=False,
                #                         theme='blue', #Add theme color to the table
                #                         enable_enterprise_modules=True,
                #                         height=350, 
                #                         width='100%',
                #                         reload_data=True
                #                     )

                # data = grid_response['data']
                # selected = grid_response['selected_rows'] 
                # df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df
            st.download_button("DOWNLOAD CSV", output_csv, 'biological response prediction.csv')



            

            
