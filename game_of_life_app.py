import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

grid_size = 5

initial_grid = pd.DataFrame(np.zeros(shape=(grid_size, grid_size)))

st.table(initial_grid)

AgGrid(initial_grid)