import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="Badminton News Update", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jrpzvtqz.json")
img_player = Image.open("images/badminton.PNG")
img_contact_form = Image.open("images/foto.jpeg")
img_lottie_animation = Image.open("images/ginting.jpg")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Welcome!")
        st.title("Badminton Update")
        st.write(
        """Berisi Informasi Terbaru seputar Badminton Dunia."""
    )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("SEPUTAR BADMINTON")
        st.write("##")
        st.write(
            """
            Jika kamu ingin mengetahui berita terbaru seputar bulutangkis kamu bisa mengunjungi website ini,
            Karena di Website ini akan ada berita terbaru Setiap harinya.
            mulai dari Kalender Tournament Badminton,Seputar Atlet,Ranking BWF Terbaru,dll
            """
        )
        st.write("[Learn More >](https://pbsi.id/)")
    with right_column:
        st.image(img_player)





#program studi kasus 1


import streamlit as st

st.title("Peringkat Dunia Atlet Badminton")

# Create a list of animals
Rank_Pemain  = [
    {"Nama": "VIKTOR AXELSEN", "Point":114006 , "Turnamen": 14, "Negara" : "DENMARK" ,"Kategori" : "Tunggal Putra" },
    {"Nama": "LEE ZII JIA", "Point":76588 , "Turnamen": 15, "Negara" : "MALAYSIA" ,"Kategori" : "Tunggal Putra" },
    {"Nama": "ANTHONY GINTING", "Point":76299 , "Turnamen": 17, "Negara" : "INDONESIA" ,"Kategori" : "Tunggal Putra" },
    {"Nama": "JONATAN CHRISTIE", "Point":75812 , "Turnamen": 18, "Negara" : "INDONESIA" ,"Kategori" : "Tunggal Putra" },
    {"Nama": "CHOU TIEN CHEN", "Point":75466 , "Turnamen": 16, "Negara" : "CHINESE TAIPEI" ,"Kategori" : "Tunggal Putra" },

    {"Nama": "FAJAR ALFIAN/RIAN ARDIANTO", "Point":92855 , "Turnamen": 18, "Negara" : "INDONESIA","Kategori" : "Ganda Putra" },
    {"Nama": "HENDRA SETIAWAN/MOHAMMAD AHSAN", "Point":80255, "Turnamen": 17, "Negara" : "INDONESIA","Kategori" : "Ganda Putra" },
	{"Nama": "AARON CHIA/SOH WOOI YIK", "Point":80203, "Turnamen": 18, "Negara" : "MALAYASIA","Kategori" : "Ganda Putra" },
	{"Nama": "TAKURO HOKI/YUGO KOBAYASHI", "Point":74740, "Turnamen": 15, "Negara" : "JAPAN","Kategori" : "Ganda Putra" },
	{"Nama": "LIU YU CHEN/OU XUAN YI", "Point":72422, "Turnamen": 18, "Negara" : "CHINA","Kategori" : "Ganda Putra" },
	
	
	{"Nama": "AKANE YAMAGUCI", "Point":102613, "Turnamen": 14, "Negara" : "JAPAN" ,"Kategori" : "Tunggal Putri" },
	{"Nama": "TAI TZU YING", "Point":91745, "Turnamen": 15, "Negara" : "CHINESE TAIPEI" ,"Kategori" : "Tunggal Putri" },
	{"Nama": "CHEN YU FEI", "Point":91556, "Turnamen": 16, "Negara" : "CHINA" ,"Kategori" : "Tunggal Putri" },
	{"Nama": "AN SE YOUNG", "Point":91453, "Turnamen": 16, "Negara" : "CHINA" ,"Kategori" : "Tunggal Putri" },
	{"Nama": "HE BING JIAO", "Point":81284, "Turnamen": 17, "Negara" : "CHINA" ,"Kategori" : "Tunggal Putri" },
	

	{"Nama": "CHEN QING CHEN/JIA YI FAN", "Point":104816, "Turnamen": 15, "Negara" : "CHINA" ,"Kategori" : "Ganda Putri" },
	{"Nama": "NAMI MATSUYAMA/CHIHARU SHIDA", "Point":81913, "Turnamen": 13, "Negara" : "JAPAN" ,"Kategori" : "Ganda Putri" },
	{"Nama": "ZHANG SHU XIAN/ZHENG YU", "Point":76758, "Turnamen": 19, "Negara" : "CHINA" ,"Kategori" : "Ganda Putri" },
	{"Nama": "KIM HYE JEONG/JEONG NA EUN", "Point":75390, "Turnamen": 17, "Negara" : "KOREA" ,"Kategori" : "Ganda Putri" },
	{"Nama": "APRIYANI RAHAYU/SITI FADIA", "Point":70300, "Turnamen": 10, "Negara" : "INDONESIA" ,"Kategori" : "Ganda Putri" },
	
	
	{"Nama": "ZHENG SI WEI/HUANG YA QIONG", "Point":112400, "Turnamen": 13, "Negara" : "CHINA" ,"Kategori" : "Ganda Campuran" },
	{"Nama": "WANG YI LYU/HUANG DONG PING", "Point":82120, "Turnamen": 14, "Negara" : "CHINA" ,"Kategori" : "Ganda Campuran" },
	{"Nama": "YUTA WATANABE/ARISA HIGASHINO", "Point":81320, "Turnamen": 11, "Negara" : "JAPAN" ,"Kategori" : "Ganda Campuran" },
	{"Nama": "DECHAPOL PUAVARANUKROH/SAPSIREE TAERATTANACHAI", "Point":80870, "Turnamen": 14, "Negara" : "THAILAND" ,"Kategori" : "Ganda Campuran" },
	{"Nama": "THOM GICQUEL/DELPHINE DELRUE", "Point":66250, "Turnamen": 14, "Negara" : "FRANCE" ,"Kategori" : "Ganda Campuran" }
]

# Use the map function 
if st.button("Rank Pemain Seluruh Kategori"):
    animals_in_kg = map(lambda x: {"Nama": x["Nama"], "Point": x["Point"], "Turnamen": x["Turnamen"],"Negara": x["Negara"],"Kategori": x["Kategori"]}, Rank_Pemain)
    st.table(animals_in_kg)
# Use the filter function 
if st.button("Rank Pemain Tunggal Putra"):
    filter_TunggalPutra = filter(lambda x: x["Kategori"] == "Tunggal Putra", Rank_Pemain)
    st.table(filter_TunggalPutra)

if st.button("Rank Pemain Ganda Putra"):
    filter_GandaPutra = filter(lambda x: x["Kategori"] == "Ganda Putra", Rank_Pemain)
    st.table(filter_GandaPutra)

if st.button("Rank Pemain Tunggal Putri"):
    filter_TunggalPutri = filter(lambda x: x["Kategori"] == "Tunggal Putri", Rank_Pemain)
    st.table(filter_TunggalPutri)

if st.button("Rank Pemain Ganda Putri"):
    filter_GandaPutri = filter(lambda x: x["Kategori"] == "Ganda Putri", Rank_Pemain)
    st.table(filter_GandaPutri)

if st.button("Rank Pemain Ganda Campuran"):
    filter_GandaCampuran = filter(lambda x: x["Kategori"] == "Ganda Campuran", Rank_Pemain)
    st.table(filter_GandaCampuran)

Turnamen = st.sidebar.slider("Select minimum turnamen", 0, 20, 2)
if st.button("Filter by Turnamen"):
    filter_Turnamen = filter(lambda x: x["Turnamen"] >= Turnamen, Rank_Pemain)
    st.table(filter_Turnamen)


# Use the sorted function to sort 
if st.button("Sort by Turnamen"):
    sorted_Turnamen = sorted(Rank_Pemain, key=lambda x: x["Turnamen"])
    st.table(sorted_Turnamen)

if st.button("Sort by Point"):
    sorted_Point = sorted(Rank_Pemain, key=lambda x: x["Point"])
    st.table(sorted_Point)
    



# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Streaming dan Highlight Pertandingan Badminton ")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Home favourite Anthony Sinisuka Ginting encounters an in-form Shi Yu Qi")
        st.write(
            """
            BWF TV is the official channel of the Badminton World Federation (BWF), where we bring to you live, catch-up and delayed streaming of the big events on the HSBC BWF World Tour,
             as well as the majors like the TotalEnergies BWF Sudirman Cup Finals, TotalEnergies BWF Thomas and Uber Cup Finals and the TotalEnergies BWF World Championships.
             Plus enjoy a range of other exclusive content including the latest highlights and interviews as well as our top-rating magazine show Badminton Unlimited.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/JGeMaf0v6_Q)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Denmark Open 2022 | Chia/Soh (MAS) [4] vs. Gideon/Sukamuljo (INA) [2] | SF")
        st.write(
            """
            Denmark Open 2022 | Super 750,Men's Doubles | Semifinals
Chia/Soh (MAS) [4] vs. Gideon/Sukamuljo (INA) [2]
#BWFWorldTour #DenmarkOpen2022 ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=t4M57CBd5eA)")


