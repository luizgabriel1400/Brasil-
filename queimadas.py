import pandas as pd
import plotly.express as px
import streamlit as st



# grafico queimadas
queimada=pd.read_csv("foco_queimadas_2024.csv"); 
grafico=px.density_mapbox(queimada, lon="Longitude", lat="Latitude", z="FRP", mapbox_style="open-street-map",
                            zoom=3, radius=11 )
grafico.update_layout(margin={"r": 0, "t": 0, "b": 0, "l": 0})

titulo_grafico=st.title("Map do numero de queimadas de 2024")
st.plotly_chart(grafico)
hora=px.line(queimada, y= "DataHora" )
st.plotly_chart(hora)
# os estados om focos de encendios e queimadas 
estados=px.bar(queimada["Estado"])
st.plotly_chart(estados)
muni=px.bar(queimada["Municipio"])
st.plotly_chart(muni)
st.write("""são 1200 casos de focos e queimadas registrados no brasil, liderado pelo o bioma da amozonia seguido cerrado eles
         são os que tem mais casos regitrados,  inlustrado no grafico abixo: """)

# grafico do biomas mais afetados pelas queimadas  
bioma=px.bar(queimada["Bioma"].value_counts())
st.plotly_chart(bioma)

# data base com os dados 
st.write("# Base de dados usado pra cria os graficos")
st.write(queimada)





