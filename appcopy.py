import streamlit as st

import pandas as pd

st.title("Teston")



class DataFrame_Loader():

    def __init__(self):
        print("Loadind DataFrame")

    def read_csv(self, data):
        self.df = pd.read_csv(data)
        return self.df



def main():
    data = st.file_uploader("Upload a Dataset", type=["csv"])


    if data is not None:
        df = load.read_csv(data)
        #st.dataframe(df.head())
        st.success("Data Frame Loaded successfully")
        df = pd.DataFrame(df)
        filtered = st.multiselect("Filter columns", options=list(df.columns), default=list(df.columns))
        st.write(df[filtered])




if __name__ == '__main__':
	load = DataFrame_Loader()


	main()

