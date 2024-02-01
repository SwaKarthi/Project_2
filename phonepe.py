import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px
import os
import json
from streamlit_option_menu import option_menu
#Aggregated Transaction

def agg_trans():
    path1 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/aggregated/transaction/country/india/state/"
    agg_trans_list=os.listdir(path1)


    columns1 = {"States":[],"Years":[],"Quarter":[],"Transaction_Type":[],"Transaction_count":[],"Transaction_amount":[]}
    for state in agg_trans_list:
        cur_states = path1 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
            cur_years = cur_states + year + "/"
            agg_quater_list = os.listdir(cur_years)
            
            for file in agg_quater_list:
                cur_file = cur_years + file
                data = open(cur_file,'r')
                A = json.load(data)
                for i in A['data']['transactionData']:
                    Name = i['name']
                    count = i['paymentInstruments'][0]['count']
                    amount = i['paymentInstruments'][0]['amount']
                    columns1['Transaction_Type'].append(Name)
                    columns1['Transaction_count'].append(count)
                    columns1['Transaction_amount'].append(amount)
                    columns1['States'].append(state)
                    columns1['Years'].append(year)
                    columns1['Quarter'].append(int(file.strip('.json')))
    Agg_Trans = pd.DataFrame(columns1)
    return Agg_Trans
agg_trans_data = agg_trans()

#Aggregated User
def agg_user():
    path2 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/aggregated/user/country/india/state/"
    agg_user_list=os.listdir(path2)

    columns2 = {"States":[],"Years":[],"Quarter":[],"Brands":[],"Transaction_count":[],"Percentage":[]}
    for state in agg_user_list:
        cur_states = path2 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
                cur_years = cur_states + year + "/"
                agg_quater_list = os.listdir(cur_years)

                for file in agg_quater_list:
                    cur_file = cur_years + file
                    data = open(cur_file,'r')
                    B = json.load(data)
                    
                    try:
                        for i in B['data']['usersByDevice']:
                            brand = i['brand']
                            count = i['count']
                            percentage = i['percentage']
                            columns2['Brands'].append(brand)
                            columns2['Transaction_count'].append(count)
                            columns2['Percentage'].append(percentage)
                            columns2['States'].append(state)
                            columns2['Years'].append(year)
                            columns2['Quarter'].append(int(file.strip('.json')))
                            
                    except:
                        pass
    Agg_User = pd.DataFrame(columns2) 
    return Agg_User
agg_user_data = agg_user()

#map transaction
def map_trans():
    path3 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/map/transaction/hover/country/india/state/"
    map_trans_list = os.listdir(path3)

    columns3 = {"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}
    for state in map_trans_list:
        cur_states = path3 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
            cur_years = cur_states + year + "/"
            agg_quater_list = os.listdir(cur_years)
            
            for file in agg_quater_list:
                cur_file = cur_years + file
                data = open(cur_file,'r')
                C = json.load(data)
                for i in C['data']['hoverDataList']:
                        name = i['name']
                        count = i['metric'][0]['count']
                        amount = i['metric'][0]['amount']
                        columns3['Districts'].append(name)
                        columns3['Transaction_count'].append(count)
                        columns3['Transaction_amount'].append(amount)
                        columns3['States'].append(state)
                        columns3['Years'].append(year)
                        columns3['Quarter'].append(int(file.strip('.json')))
    map_transaction = pd.DataFrame(columns3)
    return map_transaction
                        
map_transaction_data = map_trans()

#map user
def map_user():
    path4 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/map/user/hover/country/india/state/"
    map_user_list = os.listdir(path4)

    columns4 = {"States":[],"Years":[],"Quarter":[],"Districts":[],"RegisteredUsers":[],"AppOpens":[]}
    for state in map_user_list:
        cur_states = path4 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
            cur_years = cur_states + year + "/"
            agg_quater_list = os.listdir(cur_years)
            
            for file in agg_quater_list:
                cur_file = cur_years + file
                data = open(cur_file,'r')
                D = json.load(data)

                for i in D['data']['hoverData'].items():
                    District = i[0]
                    registeredUsers = i[1]['registeredUsers']
                    appOpens = i[1]['appOpens']
                    columns4['Districts'].append(District)
                    columns4['RegisteredUsers'].append(registeredUsers)
                    columns4['AppOpens'].append(appOpens)
                    columns4['States'].append(state)
                    columns4['Years'].append(year)
                    columns4['Quarter'].append(int(file.strip('.json')))
    map_user = pd.DataFrame(columns4)
    return map_user


map_user_data = map_user()

#top_transactions
def top_trans():
    path5 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/top/transaction/country/india/state/"
    top_transaction_list = os.listdir(path5)

    columns5 = {"States":[],"Years":[],"Quarter":[],"Pincode":[],"Transaction_count":[],"Transaction_amount":[]}
    for state in top_transaction_list:
        cur_states = path5 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
            cur_years = cur_states + year + "/"
            agg_quater_list = os.listdir(cur_years)
            
            for file in agg_quater_list:
                cur_file = cur_years + file
                data = open(cur_file,'r')
                E = json.load(data)

                for i in E['data']['pincodes']:
                    name = i['entityName']
                    count = i['metric']['count']
                    amount = i['metric']['amount']
                    columns5['Pincode'].append(name)
                    columns5['Transaction_count'].append(count)
                    columns5['Transaction_amount'].append(amount)
                    columns5['States'].append(state)
                    columns5['Years'].append(year)
                    columns5['Quarter'].append(int(file.strip('.json')))
    top_transaction_df = pd.DataFrame(columns5)
    return top_transaction_df


top_transaction_data = top_trans()

#top_users
def top_users():
    path6 = "C:/Users/krkar/OneDrive/Documents/Youtube/Phonepe/pulse/data/top/user/country/india/state/"
    top_user_list = os.listdir(path6)

    columns6 = {"States":[],"Years":[],"Quarter":[],"Pincode":[],"Registered_user":[]}
    for state in top_user_list:
        cur_states = path6 + state + "/"
        agg_year_list = os.listdir(cur_states)
        for year in agg_year_list:
            cur_years = cur_states + year + "/"
            agg_quater_list = os.listdir(cur_years)
            
            for file in agg_quater_list:
                cur_file = cur_years + file
                data = open(cur_file,'r')
                F = json.load(data)

                for i in F['data']['pincodes']:
                    name = i['name']
                    registeredUsers = i['registeredUsers']
                    columns6['Pincode'].append(name)
                    columns6['Registered_user'].append(registeredUsers)
                    columns6['States'].append(state)
                    columns6['Years'].append(year)
                    columns6['Quarter'].append(int(file.strip('.json')))
    top_user_df = pd.DataFrame(columns6)
    return top_user_df
top_user_data = top_users()

#agg_trans table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(agg_trans_data.columns, agg_trans_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS agg_trans ({columns})"

agg_trans_table = sql_create_table.replace("float64","float").replace("object","text").replace("int64","int")
cur.execute(agg_trans_table)
myconnect.commit()

sql_insert = "INSERT INTO agg_trans VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(0, len(agg_trans_data)):
    cur.execute(sql_insert, tuple(agg_trans_data.iloc[i]))
    myconnect.commit()

#agg_user table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(agg_user_data.columns, agg_user_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS agg_user ({columns})"

agg_user_table = sql_create_table.replace("float64","float").replace("object","text").replace("int64","int")
cur.execute(agg_user_table)
myconnect.commit()

sql_insert = "INSERT INTO agg_user VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(0, len(agg_user_data)):
    cur.execute(sql_insert, tuple(agg_user_data.iloc[i]))
    myconnect.commit()

#map_trans table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(map_transaction_data.columns, map_transaction_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS map_trans ({columns})"

map_trans_table = sql_create_table.replace("float64","float").replace("object","text").replace("int64","int")
cur.execute(map_trans_table)
myconnect.commit()

sql_insert = "INSERT INTO map_trans VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(0, len(map_transaction_data)):
    cur.execute(sql_insert, tuple(map_transaction_data.iloc[i]))
    myconnect.commit()

#map_user table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(map_user_data.columns, map_user_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS map_user ({columns})"

map_user_table = sql_create_table.replace("object","text").replace("int64","int")
cur.execute(map_user_table)
myconnect.commit()

sql_insert = "INSERT INTO map_user VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(0, len(map_user_data)):
    cur.execute(sql_insert, tuple(map_user_data.iloc[i]))
    myconnect.commit()

#top_trans table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(top_transaction_data.columns, top_transaction_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS top_trans ({columns})"

top_trans_table = sql_create_table.replace("float64","float").replace("object","text").replace("int64","int")
cur.execute(top_trans_table)
myconnect.commit()

sql_insert = "INSERT INTO top_trans VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(0, len(top_transaction_data)):
    cur.execute(sql_insert, tuple(top_transaction_data.iloc[i]))
    myconnect.commit()


#top_user table
myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

columns = ", ".join(
    f"{column_name} {dtype}"
    for column_name, dtype in zip(top_user_data.columns, top_user_data.dtypes))
sql_create_table = f"CREATE TABLE IF NOT EXISTS top_user ({columns})"

top_user_table = sql_create_table.replace("object","text").replace("int64","int")
cur.execute(top_user_table)
myconnect.commit()

sql_insert = "INSERT INTO top_user VALUES (%s, %s, %s, %s, %s)"

for i in range(0, len(top_user_data)):
    cur.execute(sql_insert, tuple(top_user_data.iloc[i]))
    myconnect.commit()

#streamlit code
st.set_page_config(page_title= "Phonepe Pulse Data Visualization",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created for PhonePe Data Visualization!
                                        Data has been cloned from Phonepe Pulse Github Repository"""})

st.sidebar.header(":wave: :violet[**Welcome to the Swathi's dashboard!**]")

with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","About"], 
                icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#dcc7f2"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
    
if selected == "Home":
    #st.image("img.png")
    st.markdown("# :blue[Data Visualization and Exploration]")
    st.markdown("## :blue[A User-Friendly Tool Using Streamlit and Plotly]")
    col1 = st.columns(1)[0]   
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :blue[Domain :] Fintech")
        st.markdown("### :blue[Technologies used :] Github-Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit and Plotly")
        st.markdown("### :blue[Overview :]  This streamlit app can be used to visualize the PhonePe pulse data and gain lots of insights on Transactions, Number of users, Top 10 state, District, Pincode. Bar charts, Pie charts and Geo map visualization are used to get insights.")
     

if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    #columns= st.columns([1,1.5],gap="large")
    colum1 = st.columns(1)[0]
    with colum1:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on PhonePe.
                - Top 10 State, District, Pincode based on Total PhonePe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on how many people use PhonePe.
                """,icon="🔍"
                )
    if Type == "Transactions":
        col1,col2,col3 = st.columns([1,1,1],gap="small")

        selected_year = st.selectbox("Select Year", list(range(2018, 2023)))
        selected_quarter = st.select_slider("Select Quarter", options=[1, 2, 3, 4])
        with col1:
            st.markdown("### :violet[State]")
            cur.execute(f"select states, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans where years = {selected_year} and quarter = {selected_quarter} group by states order by Total desc limit 10")
            df_1 = pd.DataFrame(cur.fetchall(),columns = ["States","Transaction_count","Transaction_amount"])
            fig = px.sunburst(df_1, path=['States', 'Transaction_amount', 'Transaction_count'], 
                              values='Transaction_amount', title='Top 10', hover_data=['Transaction_count'], 
                              labels={'Transaction_amount': 'Transaction Amount'})
            st.plotly_chart(fig,use_container_width=True)

        with col2:
            st.markdown("### :violet[District]")
            cur.execute(f"select districts, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Transaction_amount from map_trans where years = {selected_year} and quarter = {selected_quarter} group by districts order by Transaction_amount desc limit 10")
            df_2 = pd.DataFrame(cur.fetchall(), columns=["Districts", "Transaction_count", "Transaction_amount"])
            fig = px.sunburst(df_2, path=['Districts', 'Transaction_amount', 'Transaction_count'],
                              values="Transaction_amount", title="Top 10", hover_data=["Transaction_count"], 
                              labels={'Transaction_amount': 'Transaction_Amount'})
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            st.markdown("### :violet[Pincode]")
            cur.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total_amount from top_trans where years = {selected_year} and quarter = {selected_quarter} group by pincode order by Total_amount desc limit 10")
            df_3 = pd.DataFrame(cur.fetchall(),columns = ["Pincode","Transaction_count","Transaction_amount"])
            fig = px.pie(df_3,values = "Transaction_amount",names = "Pincode",title = "Top 10",hover_data = ['Transaction_count'],labels={'Transactions_Count':'Transactions_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        st.markdown("### :violet[Bar Chart]")
        cur.execute(f"select distinct states, sum(Transaction_count) as Total_Transactions_Count from agg_trans where years = 2018 and quarter = 1 group by states order by Total_Transactions_Count")
        df_4 = pd.DataFrame(cur.fetchall(),columns = ["States","Transaction_count"])
        fig = px.bar(df_4, y='Transaction_count', x='States', text='Transaction_count', color='States')
        fig.update_traces(texttemplate='%{text:.3s}', textposition='inside')
        fig.update_layout(uniformtext_minsize=7,uniformtext_mode='hide')
        fig.update_layout(xaxis_tickangle=-90)  
        st.plotly_chart(fig,use_container_width=True)  

    if Type == "Users":
        selected_year = st.selectbox("Select Year", list(range(2018, 2023)))
        selected_quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")

        with col1:
            st.markdown("### :violet[Brands]")
            if selected_year == 2022 and selected_quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")

            else:
                st.markdown("### :violet[Brands]")
                cur.execute(f"select brands, sum(Transaction_count) as Total_Count, avg(percentage)*100 as Avg_Percentage from agg_user where years = {selected_year} and quarter = {selected_quarter} group by brands order by Total_Count limit 10;")
                df = pd.DataFrame(cur.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.pie(df, values='Total_Users', names='Brand', 
                             title='Top 10', color='Avg_Percentage', 
                             color_discrete_sequence=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 

        with col2:
            st.markdown("### :violet[District]")
            cur.execute(f"select districts, sum(RegisteredUsers) as Total_Users, sum(appopens) as Total_Appopens from map_user where years = {selected_year} and quarter = {selected_quarter} group by districts order by Total_Users limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['Districts', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                        title='Top 10',
                        x="Total_Users",
                        y="Districts",
                        orientation='h',
                        color='Total_Users',
                        color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)

        with col3:
            st.markdown("### :violet[Pincode]")
            cur.execute(f"select Pincode, sum(Registered_user) as Total_Users from top_user where years = {selected_year} and quarter = {selected_quarter} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                        values='Total_Users',
                        names='Pincode',
                        title='Top 10',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :violet[State]")
            cur.execute(f"select states, sum(Registeredusers) as Total_Users, sum(Appopens) as Total_Appopens from map_user where years = {selected_year} and quarter = {selected_quarter} group by states order by Total_Users desc limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['States', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                            names='States',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Appopens'],
                            labels={'Total_Appopens':'Total_Appopens'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)


# MENU 3 - ABOUT
if selected == "About":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[About PhonePe Pulse:] ")
        st.write("##### On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")
        
        st.write("##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")
        
        st.markdown("### :violet[About PhonePe:] ")
        st.write("##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")
        
        
        
    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        #st.image("Pulseimg.jpg")




