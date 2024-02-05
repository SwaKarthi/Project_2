import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

myconnect = pymysql.connect(host='127.0.0.1', user='root', passwd='Sw@30', database='phonepe')
cur = myconnect.cursor()

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
    st.markdown("# :blue[Data Visualization and Exploration]")
    st.markdown("## :blue[A User-Friendly Tool Using Streamlit and Plotly]") 
    col1,col2 = st.columns([2,2],gap="small")
  
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :blue[Domain :] Fintech")
        st.markdown("### :blue[Technologies used :] Github-Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit and Plotly")
        st.markdown("### :blue[Overview :]  This streamlit app can be used to visualize the PhonePe pulse data and gain lots of insights on Transactions, Number of users, Top 10 state, District, Pincode. Bar charts, Pie charts and Geo map visualization are used to get insights.")

    with col2:
        st.write(" ")
        st.write(" ")
        video_url = "https://youtu.be/c_1H6vivsiA"
        st.video(video_url)

if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    col1,col2= st.columns([1,1.5],gap="large")
    with col1:
        selected_year = st.selectbox("Select Year", list(range(2018, 2023)))
        selected_quarter = st.select_slider("Select Quarter", options=[1, 2, 3, 4])
    with col2:
        st.info("""#### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on PhonePe.
                - Top 10 State, District, Pincode based on Total PhonePe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on how many people use PhonePe.
                """,icon="🔍")
    
    if Type == "Transactions":
        col1,col2 = st.columns([2,2],gap="large")

        st.markdown("### :violet[Geo Map Visualization]")
        cur.execute(f"select distinct states, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans where years = {selected_year} and quarter = {selected_quarter} group by states order by Total desc")
        df_geo = pd.DataFrame(cur.fetchall(), columns=["States", "Transaction_count", "Transaction_amount"])
        df_geo['Transaction_count'] = pd.to_numeric(df_geo['Transaction_count'])
        fig = px.choropleth(df_geo,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',locations='States',
            color='Transaction_count', color_continuous_scale='sunset', range_color=[0, df_geo['Transaction_count'].max()])
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)

        with col1:
            st.markdown("### :violet[State wise Transaction Count & Transaction Amount]")
            cur.execute(f"select states, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans where years = {selected_year} and quarter = {selected_quarter} group by states order by Total desc limit 10")
            df_1 = pd.DataFrame(cur.fetchall(),columns = ["States","Transaction_count","Transaction_amount"])
            fig = px.sunburst(df_1, path=['States', 'Transaction_amount', 'Transaction_count'], 
                              values='Transaction_amount', title='Top 10', hover_data=['Transaction_count'], 
                              labels={'Transaction_amount': 'Transaction Amount'})
            st.plotly_chart(fig,use_container_width=True)

        with col2:
            st.markdown("### :violet[District wise Transaction Count & Transaction Amount]")
            cur.execute(f"select districts, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Transaction_amount from map_trans where years = {selected_year} and quarter = {selected_quarter} group by districts order by Transaction_amount desc limit 10")
            df_2 = pd.DataFrame(cur.fetchall(), columns=["Districts", "Transaction_count", "Transaction_amount"])
            fig = px.sunburst(df_2, path=['Districts', 'Transaction_amount', 'Transaction_count'],
                              values="Transaction_amount", title="Top 10", hover_data=["Transaction_count"], 
                              labels={'Transaction_amount': 'Transaction_Amount'})
            st.plotly_chart(fig, use_container_width=True)

        with col1:
            st.markdown("### :violet[Pincode]")
            cur.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total_amount from top_trans where years = {selected_year} and quarter = {selected_quarter} group by pincode order by Total_amount desc limit 10")
            df_3 = pd.DataFrame(cur.fetchall(),columns = ["Pincode","Transaction_count","Transaction_amount"])
            fig = px.pie(df_3,values = "Transaction_amount",names = "Pincode",title = "Top 10",
                         hover_data = ['Transaction_count'],labels={'Transactions_Count':'Transactions_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with col2:
            st.markdown("### :violet[All States Transaction Count]")
            cur.execute(f"select distinct states, sum(Transaction_count) as Total_Transactions_Count from agg_trans where years = {selected_year} and quarter = {selected_quarter} group by states order by Total_Transactions_Count")
            df_4 = pd.DataFrame(cur.fetchall(),columns = ["States","Transaction_count"])
            fig = px.bar(df_4, y='Transaction_count', x='States', text='Transaction_count', color='States')
            fig.update_traces(texttemplate='%{text:.3s}', textposition='inside')
            fig.update_layout(uniformtext_minsize=7,uniformtext_mode='hide')
            fig.update_layout(xaxis_tickangle=-90)  
            st.plotly_chart(fig,use_container_width=True)  

    if Type == "Users":
        col1, col2 = st.columns([2, 2], gap="large")

        st.markdown("### :violet[Geo Map Visualization]")
        cur.execute(f"select distinct states, sum(Registeredusers) as Total_Users, sum(Appopens) as Total_Appopens from map_user where years = {selected_year} and quarter = {selected_quarter} group by states order by states")
        df_geo_users = pd.DataFrame(cur.fetchall(), columns=['States', 'Total_Users', 'Total_Appopens'])
        df_geo_users['Total_Users'] = pd.to_numeric(df_geo_users['Total_Users'])
        fig = px.choropleth(df_geo_users,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',locations='States',
            color='Total_Users', color_continuous_scale='sunset', range_color=[0, df_geo_users['Total_Users'].max()])
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)

        with col1:
            
            if selected_year == 2022 and selected_quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")

            else:
                st.markdown("### :violet[Brands - Total count]")
                cur.execute(f"select brands, sum(Transaction_count) as Total_Count, avg(percentage)*100 as Avg_Percentage from agg_user where years = {selected_year} and quarter = {selected_quarter} group by brands order by Total_Count limit 10;")
                df = pd.DataFrame(cur.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.pie(df, values='Total_Users', names='Brand', title='Top 10', 
                             color='Avg_Percentage', color_discrete_sequence=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True) 

        with col2:
            st.markdown("### :violet[State wise Total users and Appopens]")
            cur.execute(f"select states, sum(Registeredusers) as Total_Users, sum(Appopens) as Total_Appopens from map_user where years = {selected_year} and quarter = {selected_quarter} group by states order by Total_Users desc limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['States', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users', names='States', title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Appopens'], labels={'Total_Appopens':'Total_Appopens'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with col1:
            st.markdown("### :violet[District wise Total users and Appopens]")
            cur.execute(f"select districts, sum(RegisteredUsers) as Total_Users, sum(appopens) as Total_Appopens from map_user where years = {selected_year} and quarter = {selected_quarter} group by districts order by Total_Users limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['Districts', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.pie(df, values='Total_Users', names='Districts', title='Top 10', 
                        color_discrete_sequence=px.colors.sequential.Agsunset, hover_data=['Total_Users'])
            st.plotly_chart(fig,use_container_width=True)

        with col2:
            st.markdown("### :violet[Pincode]")
            cur.execute(f"select Pincode, sum(Registered_user) as Total_Users from top_user where years = {selected_year} and quarter = {selected_quarter} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(cur.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df, values='Total_Users', names='Pincode',title='Top 10', 
                         color_discrete_sequence=px.colors.sequential.Agsunset, hover_data=['Total_Users'])
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
        st.write(" ")
        st.write(" ")
        image_url = "https://i.ytimg.com/vi/c_1H6vivsiA/maxresdefault.jpg"
        st.image(image_url, caption='Phonepe Pulse', use_column_width=True)

    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        image_url = "https://www.bizzbuzz.news/h-upload/2021/08/30/1271432-phone-pay.jpg"
        st.image(image_url, caption='Phonepe Pulse', use_column_width=True)


