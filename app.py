import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image
from courses import all_courses

st.set_page_config(page_title="Vinay Khanduri | Python Developer", layout="wide")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
home_img = Image.open("images/2206.jpg")
vit_img = Image.open("images/vit.jpg")
bbps_img = Image.open("images/bbps.png")
udemy_img = Image.open("images/udemy.jpeg")
coursera_img = Image.open("images/coursera.jpeg")
linkedin_img = Image.open("images/linkedin.jpeg")
google_img = Image.open("images/google.jpeg")


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
    st.markdown("<h3 style='text-align:center;'>EDUCATION</h3> <br>", unsafe_allow_html=True)

    img_col1, detail_col1 = st.columns([1, 17])

    with img_col1:
        st.image(vit_img, use_column_width=True)

    with detail_col1:
        st.markdown("<p class='degree'><strong>Bachelor of Technology in Electronics and Instrumentation</strong><br><em>Vellore Institute of Technology, Vellore &nbsp; | &nbsp; CGPA: 7.95/10</em><br>2019 - 2023</p>", unsafe_allow_html=True)

        st.markdown("<strong>Relevant Courses</strong><br> 📍 Python Programming <br> 📍 Object Oriented Programming with C++ <br> 📍 Data Structures and Algorithms<br>📍 Neural Networks and Fuzzy Control<br>📍 Statistics and Probability using R<br>📍 Java", unsafe_allow_html=True)

        st.markdown("<strong>Clubs and Activities</strong><br>📍 Core Member, Design @ <strong><a style='color:#ff4b4b;' href='https://www.linkedin.com/company/the-next-chapter-vit/'>The Next Chapter</a></strong><br>📍 Core Member, Technical @ <strong><a style='color:#ff4b4b;' href='https://www.linkedin.com/company/soft-computing-research-society-vit/'>Soft Computing Research Society</a></strong><br>📍 Published 2 conference papers titled <strong><a style='color:#ff4b4b;' href='https://ieeexplore.ieee.org/document/9984343'>Kyphosis Disease Prediction with help of RandomizedSearchCV and AdaBoosting</a></strong> and <strong><a style='color:#ff4b4b;' href='https://drive.google.com/file/d/1IE3JFF3g9hSxhW_8hX2nZKzZF-mDjw_U/view'>Short-Term Electrical Load Forecasting using ARIMA and LSTM</a></strong><br>📍 Participated in a lot of hackathons like HackHarvard, ShellHacks, Amazon ML Challenge, Flipkart Grid and other competitions like L&T's Techgium throughout my college years<br>📍 Student Volunteer @ <strong><a href='https://www.linkedin.com/company/national-youth-council-of-india/' style='color: #ff4b4b;'>National Youth Council of India</a></strong>", unsafe_allow_html=True)

        st.write("---")

    img_col2, detail_col2 = st.columns([1, 17])

    with img_col2:
        st.image(bbps_img, use_column_width=True)

    with detail_col2:
        st.markdown("<p class='degree'><strong>Class XII, CBSE, Science</strong><br><em>Bal Bharati Public School, Noida &nbsp; | &nbsp; Percentage: 93.2%</em><br>2006 - 2019</p>", unsafe_allow_html=True)

        st.markdown("<strong>Clubs and Activities</strong><br>📍 Served in the Student Council as the Secretary of the Infotech Club during the academic year 2016-17<br>📍 Participated in and won various interschool events related to Web Designing, Graphic Designing, Film-making and Gaming<br>📍 Awarded Special Achiever certificate for getting an Olympiad Rank of 42 in Level 2 of International Informatics Olympiad 2014-15<br>📍 Won 1st prize in Dialogue Category and 3rd prize in Content Category in the North East Film Festival organized by CBSE in October 2015", unsafe_allow_html=True)


    st.write("---")

    st.markdown("<h3 style='text-align:center;'>ONLINE COURSE CERTIFICATIONS</h3> <br>", unsafe_allow_html=True)

    for course in all_courses:
        course_img_col, course_detail_col = st.columns([1, 17])
        if course.get("provider") == "Udemy":
            img = udemy_img
        elif course.get("provider") == "Coursera":
            img = coursera_img
        elif course.get("provider") == "LinkedIn":
            img = linkedin_img
        elif course.get("provider") == "Google":
            img = google_img
        else:
            img = None

        with course_img_col:
            st.image(img, use_column_width=True)

        with course_detail_col:
            st.markdown(f"<p class='degree'><strong>{course.get('name')}</strong><br><em>{course.get('provider')}</em><br><strong><a href='{course.get('verification link')}' style='color: #ff4b4b;'>Verify</a></strong></p>", unsafe_allow_html=True)

            
            st.write("---")






if selected == "Experience":
    st.write("Experience")


if selected == "Projects":
    st.write("Projects")

