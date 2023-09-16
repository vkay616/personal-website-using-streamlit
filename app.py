import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="Vinay Khanduri | Python Developer", layout="wide")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
home_img = Image.open("images/2206.jpg")


selected = option_menu(None, ["Home", "Education", "Experience", "Projects"], 
    icons=['a', 'a', 'a', 'a'], 
    menu_icon="cast", default_index=0, orientation="horizontal")



if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h4 class='highlight'>Hi, I'm Vinay Khanduri 👋</h4>", unsafe_allow_html=True)
        
        st.markdown("<h2>A Python Developer from Greater Noida, India</h2>", unsafe_allow_html=True)

        st.write("---")

        st.markdown("<div style='text-align:justify;'> I'm passionate about solving real world problems through code! I'm proficient in <span class='highlight'>Python</span>, <span class='highlight'>JavaScript</span> and <span class='highlight'>Go</span> and have previously worked with their different frameworks like <span class='highlight'>Django</span>, <span class='highlight'>Flask</span>, <span class='highlight'>Selenium</span>, <span class='highlight'>FastAPI</span>, <span class='highlight'>TensorFlow</span>, <span class='highlight'>Streamlit</span>, <span class='highlight'>React</span>, <span class='highlight'>Mocha</span>, <span class='highlight'>Web3</span>, <span class='highlight'>Gin</span> and <span class='highlight'>Colly</span>. I'm also familiar with <span class='highlight'>SQL</span> and <span class='highlight'>NoSQL</span> databases, <span class='highlight'>Machine Learning</span> and Data Analysis tools and libraries such as <span class='highlight'>Excel</span>, <span class='highlight'>Tableau</span>, <span class='highlight'>Power BI</span> and <span class='highlight'>Plotly-Dash</span>. <br> <br> Apart from coding, the other activities that I love doing! <br> <br> 🎵 Listening to Music <br> 🎮 Gaming with Friends <br> 📖 Reading Novels/Manga <br><br> <strong><a style='color:#ff4b4b;' href='https://drive.google.com/file/d/1VawLcCmyKqRQKBlwMa0bcry28SDiPs0c/view?usp=sharing'>Click here</a> to view my resume!</strong> </div>", unsafe_allow_html=True)
        
    with col2:
        st.image(home_img, use_column_width=True, caption='Image by catalyststuff on Freepik')

    st.write("---")

    st.markdown("<h3 style='text-align:center;'>MY SKILLS</h3>", unsafe_allow_html=True)

    st.write("  \n")

    lang_col, fw_col, db_col = st.columns(3)

    with lang_col:
        st.markdown("<h6 style='text-align:center;'>Languages</h6>", unsafe_allow_html=True)
        st.markdown("<p align='center'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=py,js,go,solidity,html,css,latex,r&perline=2' /></a></p>", unsafe_allow_html=True)


    with fw_col:
        st.markdown("<h6 style='text-align:center;'>Frameworks</h6>", unsafe_allow_html=True)
        st.markdown("<p align='center'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=django,flask,react,fastapi,selenium,tensorflow,tailwind,bootstrap&perline=2' /></a></p>", unsafe_allow_html=True)


    with db_col:
        st.markdown("<h6 style='text-align:center;'>Databases</h6>", unsafe_allow_html=True)
        st.markdown("<p align='center'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=sqlite,postgres,mysql,mongodb&perline=1' /></a></p>", unsafe_allow_html=True)


    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown("<h3 style='text-align:center;'>TOOLS I USE</h3>", unsafe_allow_html=True)

    st.markdown("<p align='center'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=vscode,git,postman,gcp,linux,replit,remix,ps,ai,matlab' /></a></p>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("<h3 style='text-align:center;'>CONNECT WITH ME ON</h3>", unsafe_allow_html=True)

    st.markdown("<p align='center'><a href='https://www.linkedin.com/in/vkay616'><img src='https://skillicons.dev/icons?i=linkedin' /></a> &nbsp; <a href='https://github.com/vkay616'><img src='https://skillicons.dev/icons?i=github' /></a> &nbsp; <a href='https://twitter.com/vkay616'><img src='https://skillicons.dev/icons?i=twitter' /></a></p>", unsafe_allow_html=True)
    
    st.markdown("<p align='center'><strong>Reach out to me via <a style='color:#ff4b4b;' href='mailto:vinaykhanduri2001@gmail.com'>vinaykhanduri2001@gmail.com</a></strong></p>", unsafe_allow_html=True)




if selected == "Education":
    st.write("Education")


if selected == "Experience":
    st.write("Experience")


if selected == "Projects":
    st.write("Projects")

