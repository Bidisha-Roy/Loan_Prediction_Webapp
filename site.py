# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:37:02 2022

@author: user
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')



data=pd.read_csv('D:/loan_stream/loan_data.csv')
# loading the saved model
loaded_model = pickle.load(open('D:/loan_stream/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    
    
   

     # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        
        return'The person is not eligible for loan'
    else:
        
        return'The person is eligible for loan'
        
def main():
    #giving a title
    st.title('Loan prediction webapp.....')
    #1.as side menu
    with st.sidebar:
        selected= option_menu(
            menu_title="Main Menu",
            options = ["Home","Predict","Visualize"],
            icons =["house","book","envelope"],
            menu_icon="cast",
            default_index=0,
            
            styles={
                "container":{"padding": "0!important","background-color":"rgb(166, 194, 151)"},
                "icon":{"color":"orange","font-size":"14px"},
                "nav-link":{
                    "font-size":"14px",
                    "text-align":"left",
                    "margin":"1px",
                    "--hover-color":"rgb(38, 92, 78)",                    
                    },
                
                 "nav-link-selected":{"background-color":"rgb(43, 82, 87)"},
                },
            )
        
    if selected == "Home":
     
      #  st.image('D:/diabetis_streamlit/vaccine.jpg')
        image = Image.open('D:/loan_stream/loan_photo.jpg')
        



#displaying the image on streamlit app

        st.image(image, caption='Timely return of a loan makes it easier to borrow a second one',width=550)

        if st.checkbox("Show Data Table"):
            st.table(data.head(10))
        st.write("....THE LONE DATASET THAT HAS BEEN USED FOR MACHINE LEARNING PREDICTION.... ")
        
    
        
        
    if selected == "Predict":
        
             
        st.subheader('loan prediction ???.....')
        #gender selection
        def gender():
         
            genre = st.radio(
                 "What's your Gender ??",
                 ('Male', 'Female'))

            if genre == 'male':
                 return 1
            else:
                 return 0

        gen=gender()
        
        # married or not
        
        def married():
         
            genre = st.radio(
                 "Are you Married ??",
                 ('Yes', 'No'))

            if genre == 'Yes':
                 return 1
            else:
                 return 0

        mar=married()
        #Dependents
            
        dep= st.text_input('Dependents')
        
        # Education
        def education():
         
            genre = st.radio(
                 "Are you Graduate ??",
                 ('Yes', 'No'))

            if genre == 'Yes':
                 return 1
            else:
                 return 0
        gra=education()
        #Self_Employed
        def employed():
         
            genre = st.radio(
                 "Are you Self_Employed ??",
                 ('Yes', 'No'))

            if genre == 'Yes':
                 return 1
            else:
                 return 0
        emp=employed()
        # ApplicantIncome
        
        app = st.text_input(' ApplicantIncome Rate')
        #CoapplicantIncome
        coa = st.text_input('CoapplicantIncome Rate' )
        # LoanAmount
        loa = st.text_input('LoanAmount Rate')
        # Loan_Amount_Term
        lor = st.text_input(' Loan_Amount_Term Rate')
        #Credit_History
        cre = st.text_input('Credit_History ')
        #Property_Area 
        def proper():
         
            genre = st.radio(
                 "Are you Self_Employed ??",
                 ('Rural', 'Semi-Urban','Urban'))

            if genre == 'Rural':
                 return 0
            elif genre=='Semi-Urban':
                
                return 1
            else:
                return 2
        prop=proper()
           
             # code for Prediction
        diagnosis = ''
         
              # creating a button for Prediction
         
        if st.button('Loan Test Result'):
            
                 
            diagnosis = diabetes_prediction([gen, mar, dep, gra, emp, app, coa, loa,lor,cre,prop])
               
            st.success(diagnosis)
            
    if selected == "Visualize":  
        data1=pd.read_csv('D:/loan_stream/loan_data.csv')
        data1.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)
        data1.replace({'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
        data1 = data1.replace(to_replace='3+', value=4)
        data1.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                              'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)



        html_temp = """
        	<div style="background-color:rgb(37, 117, 128);box-shadow:5px 5px 10px #00000057"><p style="color:white;font-size:20px;font-style: italic;padding:10px">Data Visualization</p></div>
        	"""
        st.markdown(html_temp,unsafe_allow_html=True)
        ## Plot and Visualization
        #st.subheader("Data Visualization")
        	# Correlation
        	# Seaborn Plot
        if st.checkbox("Correlation Plot[Seaborn]"):
            
        	st.write(sns.heatmap(data1.corr(),annot=True))
        	st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write("Heat-map shows the correlation between features,if value is close to positive one then the correlation is HIGHLY POSITIVE  and if the value is close to negative one then the correlation is HIGHLY NEGATIVE.. ")
        # Pie Chart
        if st.checkbox("Pie Plot"):
            
        	all_columns_names = data1.columns.tolist()
        	if st.button("Generate Pie Plot"):
               
        		st.success("Generating A Pie Plot")
        		st.write(data1.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
        		st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(" The pie-chart shows the percentage of people got the loan and the people did not get the loan..")

        # Customizable Plot

        st.subheader("Customizable Plot")
        all_columns_names = data1.columns.tolist()
        	
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        	
        selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

        if st.button("Generate Plot"):
            
        	st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

        		# Plot By Streamlit
        	if type_of_plot == 'area':
                
        		cust_data = data1[selected_columns_names]
        		st.area_chart(cust_data)

        	elif type_of_plot == 'bar':
                
        		cust_data = data1[selected_columns_names]
        		st.bar_chart(cust_data)

        	elif type_of_plot == 'line':
              
        		cust_data = data1[selected_columns_names]
        		st.line_chart(cust_data)
            # Custom Plot 
        	elif type_of_plot:
               
        		cust_plot= data1[selected_columns_names].plot(kind=type_of_plot)
        		st.write(cust_plot)
        		st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        if st.button("Thanks"):
            
            st.balloons()
        
        
        
         
         
        
if __name__ == '__main__':
    main()
    


