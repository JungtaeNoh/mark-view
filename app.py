import streamlit as st
view = [50, 100, 70]
st.write('# Mark')
st.write('## raw data')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
mark = pd.Series(view)
mark