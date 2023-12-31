import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image
from courses import Course, courses
from streamlit.components.v1 import html

# setting page config
st.set_page_config(page_title="Vinay Khanduri | Python Developer", layout="wide")


# function to read local css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# declaring all images used in the website
HOME_IMG = Image.open("images/2206.jpg")
VIT_LOGO = Image.open("images/vit.jpg")
BBPS_LOGO = Image.open("images/bbps.png")
UDEMY_LOGO = Image.open("images/udemy.jpeg")
COURSERA_LOGO = Image.open("images/coursera.jpeg")
LINKEDIN_LOGO = Image.open("images/linkedin.jpeg")
GOOGLE_LOGO = Image.open("images/google.jpeg")
CC_LOGO = Image.open("images/cgc.png")
NO_IMG = Image.open("images/none.jpg")
MTE_LOGO = Image.open("images/mte.jpeg")
MSRF_LOGO = Image.open("images/msrf.jpeg")
IOTAGI_LOGO = Image.open("images/iotagi.jpeg")
TSF_LOGO = Image.open("images/tsf.jpeg")


selected = option_menu(None, ["Home", "Education", "Experience", "Projects"], 
    icons=['a', 'a', 'a', 'a'], 
    menu_icon="cast", default_index=0, orientation="horizontal")



if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h4 class='highlight'>Hi, I'm Vinay Khanduri 👋</h4>", unsafe_allow_html=True)
        
        st.markdown("<h2>A Python Developer from Greater Noida, India</h2>", unsafe_allow_html=True)

        st.write("---")

        st.markdown("<div class='j-text'>I'm passionate about solving real world problems through code! I'm proficient in <span class='highlight'>Python</span>, <span class='highlight'>JavaScript</span> and <span class='highlight'>Go</span> and have previously worked with their different frameworks like <span class='highlight'>Django</span>, <span class='highlight'>Flask</span>, <span class='highlight'>Selenium</span>, <span class='highlight'>FastAPI</span>, <span class='highlight'>TensorFlow</span>, <span class='highlight'>Streamlit</span>, <span class='highlight'>React</span>, <span class='highlight'>Mocha</span>, <span class='highlight'>Web3</span>, <span class='highlight'>Gin</span> and <span class='highlight'>Colly</span>. I'm also familiar with <span class='highlight'>SQL</span> and <span class='highlight'>NoSQL</span> databases, <span class='highlight'>Machine Learning</span> and Data Analysis tools and libraries such as <span class='highlight'>Excel</span>, <span class='highlight'>Tableau</span>, <span class='highlight'>Power BI</span> and <span class='highlight'>Plotly-Dash</span>. <br> <br> Apart from coding, the other activities that I love doing! <br> <br> 🎵 Listening to Music <br> 🎮 Gaming with Friends <br> 📖 Reading Novels/Manga <br><br> <strong><a href='https://drive.google.com/file/d/1VawLcCmyKqRQKBlwMa0bcry28SDiPs0c/view?usp=sharing'>Click here</a> to view my resume!</strong> </div>", unsafe_allow_html=True)
        
    with col2:
        st.image(HOME_IMG, use_column_width=True, caption='Image by catalyststuff on Freepik')

    st.write("---")

    st.markdown("<h3>MY SKILLS</h3>", unsafe_allow_html=True)

    st.write("  \n")

    lang_col, fw_col, db_col = st.columns(3)

    with lang_col:
        st.markdown("<h6 style='text-align:center;'>Languages</h6>", unsafe_allow_html=True)
        st.markdown("<p class='centered'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=py,js,go,solidity,html,css,latex,r&perline=2' /></a></p>", unsafe_allow_html=True)


    with fw_col:
        st.markdown("<h6 style='text-align:center;'>Frameworks</h6>", unsafe_allow_html=True)
        st.markdown("<p class='centered'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=django,flask,react,fastapi,selenium,tensorflow,tailwind,bootstrap&perline=2' /></a></p>", unsafe_allow_html=True)


    with db_col:
        st.markdown("<h6 style='text-align:center;'>Databases</h6>", unsafe_allow_html=True)
        st.markdown("<p class='centered'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=sqlite,postgres,mysql,mongodb&perline=1' /></a></p>", unsafe_allow_html=True)


    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown("<h3>TOOLS I USE</h3>", unsafe_allow_html=True)

    st.write("")

    st.markdown("<p class='centered'><a href='https://skillicons.dev'><img src='https://skillicons.dev/icons?i=vscode,git,postman,gcp,linux,replit,remix,ps,ai,matlab' /></a></p>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("<h3>CONNECT WITH ME ON</h3>", unsafe_allow_html=True)

    st.write("")

    st.markdown("<p class='centered'><a href='https://www.linkedin.com/in/vkay616'><img src='https://skillicons.dev/icons?i=linkedin' /></a> &nbsp; <a href='https://github.com/vkay616'><img src='https://skillicons.dev/icons?i=github' /></a> &nbsp; <a href='https://twitter.com/vkay616'><img src='https://skillicons.dev/icons?i=twitter' /></a></p>", unsafe_allow_html=True)
    
    st.markdown("<p class='centered'><strong>Reach out to me via <a href='mailto:vinaykhanduri2001@gmail.com'>vinaykhanduri2001@gmail.com</a></strong></p>", unsafe_allow_html=True)




if selected == "Education":

    st.markdown("<h3>EDUCATION</h3> <br>", unsafe_allow_html=True)

    img_col1, detail_col1 = st.columns([1, 17])

    with img_col1:
        st.image(VIT_LOGO, use_column_width=True)

    with detail_col1:
        st.markdown("<p class='degree'><strong>Bachelor of Technology in Electronics and Instrumentation</strong><br><em>Vellore Institute of Technology, Vellore &nbsp; | &nbsp; CGPA: 7.95/10</em><br>2019 - 2023</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Relevant Courses</strong><br> 📍 Python Programming <br> 📍 Object Oriented Programming with C++ <br> 📍 Data Structures and Algorithms<br>📍 Neural Networks and Fuzzy Control<br>📍 Statistics and Probability using R<br>📍 Java", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Clubs and Activities</strong><br>📍 Core Member, Design @ <strong><a href='https://www.linkedin.com/company/the-next-chapter-vit/'>The Next Chapter</a></strong><br>📍 Core Member, Technical @ <strong><a href='https://www.linkedin.com/company/soft-computing-research-society-vit/'>Soft Computing Research Society</a></strong><br>📍 Published 2 conference papers titled <strong><a href='https://ieeexplore.ieee.org/document/9984343'>Kyphosis Disease Prediction with help of RandomizedSearchCV and AdaBoosting</a></strong> and <strong><a href='https://drive.google.com/file/d/1IE3JFF3g9hSxhW_8hX2nZKzZF-mDjw_U/view'>Short-Term Electrical Load Forecasting using ARIMA and LSTM</a></strong><br>📍 Participated in a lot of hackathons like HackHarvard, ShellHacks, Amazon ML Challenge, Flipkart Grid and other competitions like L&T's Techgium throughout my college years<br>📍 Student Volunteer @ <strong><a href='https://www.linkedin.com/company/national-youth-council-of-india/'>National Youth Council of India</a></strong>", unsafe_allow_html=True)

        st.write("---")

    img_col2, detail_col2 = st.columns([1, 17])

    with img_col2:
        st.image(BBPS_LOGO, use_column_width=True)

    with detail_col2:
        st.markdown("<p class='degree'><strong>Class XII, CBSE, Science</strong><br><em>Bal Bharati Public School, Noida &nbsp; | &nbsp; Percentage: 93.2%</em><br>2006 - 2019</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Clubs and Activities</strong><br>📍 Served in the Student Council as the Secretary of the Infotech Club during the academic year 2016-17<br>📍 Participated in and won various interschool events related to Web Designing, Graphic Designing, Film-making and Gaming<br>📍 Awarded Special Achiever certificate for getting an Olympiad Rank of 42 in Level 2 of International Informatics Olympiad 2014-15<br>📍 Won 1st prize in Dialogue Category and 3rd prize in Content Category in the North East Film Festival organized by CBSE in October 2015", unsafe_allow_html=True)


    st.write("---")

    st.markdown("<h3>ONLINE COURSE CERTIFICATIONS</h3> <br>", unsafe_allow_html=True)

    for course in courses:

        course_img_col, course_detail_col = st.columns([1, 17])

        if course.provider == "Udemy":
            img = UDEMY_LOGO

        elif course.provider == "Coursera":
            img = COURSERA_LOGO

        elif course.provider == "LinkedIn":
            img = LINKEDIN_LOGO

        elif course.provider == "Google":
            img = GOOGLE_LOGO
        
        elif course.provider == "Cognitive Class":
            img = CC_LOGO

        else:
            img = NO_IMG

        with course_img_col:
            st.image(img, use_column_width=True)

        with course_detail_col:
            st.markdown(f"<p class='degree'><strong>{course.name}</strong><br><em>{course.provider}</em><br><strong><a href='{course.verification_link}'>Verify</a></strong></p>", unsafe_allow_html=True)

            if course.name != courses[-1].name:
                st.write("---")






if selected == "Experience":

    st.markdown("<h3>INTERNSHIPS</h3><br>", unsafe_allow_html=True)
    
    e_img_col1, e_detail_col1 = st.columns([1, 17])

    with e_img_col1:
        st.image(MTE_LOGO, use_column_width=True)

    with e_detail_col1:
        st.markdown("<p class='degree'><strong>Cloud Computing Intern</strong><br><em>MedTourEasy &nbsp; | &nbsp; Remote</em><br>Oct. 2021</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Responsibilities/Tasks</strong><br>📍 Learnt about Google Cloud Essentials, Infrastructure, Kubernetes, Performing Foundational Data, ML and AI Tasks<br>📍 Completed Setting Up and Configuring a Cloud Environment in Google Cloud Qwiklab assessment as the final project during the internship with a perfect score<br>", unsafe_allow_html=True)

        st.write("---")


    e_img_col2, e_detail_col2 = st.columns([1, 17])

    with e_img_col2:
        st.image(MSRF_LOGO, use_column_width=True)

    with e_detail_col2:
        st.markdown("<p class='degree'><strong>Machine Learning Intern</strong><br><em>Madras Scientific Research Foundation &nbsp; | &nbsp; Remote</em><br>Aug. 2021 - Sep. 2021</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Responsibilities/Tasks</strong><br>📍 Authored weekly technical blogs on Python, Image Processing and Machine Learning concepts<br>📍 Worked on a research paper on the topic 'AI-based Drug Discovery & Development Process' in a team of 4 for L&T's Techgium<br>📍 Researched solutions from machine learning papers and journals, implemented machine learning and deep learning models", unsafe_allow_html=True)

        st.write("---")

    
    e_img_col3, e_detail_col3 = st.columns([1, 17])

    with e_img_col3:
        st.image(IOTAGI_LOGO, use_column_width=True)

    with e_detail_col3:
        st.markdown("<p class='degree'><strong>Machine Learning Intern</strong><br><em>IoTAGI &nbsp; | &nbsp; Remote</em><br>Jul. 2021</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Responsibilities/Tasks</strong><br>📍 Designed the working of data transfer from IoT devices to Cloud platforms and worked on processing the data from devices to derive meaningful output<br> 📍 Carried out research to integrate machine learning models in the cloud to improve supply chain management, smart city infrastructure, and home automation systems using AI-IoT", unsafe_allow_html=True)

        st.write("---")


    e_img_col4, e_detail_col4 = st.columns([1, 17])

    with e_img_col4:
        st.image(TSF_LOGO, use_column_width=True)

    with e_detail_col4:
        st.markdown("<p class='degree'><strong>Data Science and Business Analytics Intern</strong><br><em>The Sparks Foundation &nbsp; | &nbsp; Remote</em><br>Feb. 2021</p>", unsafe_allow_html=True)

        st.markdown("<strong class='highlight'>Responsibilities/Tasks</strong><br>📍 Worked on supervised, unsupervised machine learning & EDA tasks using Python and Tableau", unsafe_allow_html=True)






if selected == "Projects":
    
    st.markdown("<h3>PROJECTS</h3><br>", unsafe_allow_html=True)


    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.markdown("<div class='project'><h5 class='centered'>AutoML App</h5><p class='centered tmn highlight'><em>Python, Streamlit, PyCaret, Pandas Profiling</em></p><p class='j-text'>Built and deployed a Streamlit app where the user can upload data and automate the EDA and ML model training process.</p><p class='centered'><strong><a href='https://automl-app-616.streamlit.app/'>View Site</a> &nbsp; | &nbsp; <a href='https://github.com/vkay616/AutoML-app-using-streamlit'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p2:
        st.markdown("<div class='project'><h5 class='centered'>Library Management System</h5><p class='centered tmn highlight'><em>Python, Django, Bootstrap</em></p><p class='j-text'>A library management system where the user can login/logout, issue and return books.</p><br><p class='centered'><strong><a href='https://vkay616.pythonanywhere.com/'>View Site</a> &nbsp; | &nbsp; <a href='https://github.com/vkay616/library-management-website-Django'>View Code</a></strong></p></div>", unsafe_allow_html=True)


    with p3:
        st.markdown("<div class='project'><h5 class='centered'>Notes App</h5><p class='centered tmn highlight'><em>Python, Django, JavaScript, React, CSS</em></p><p class='j-text'>A note taking application, where the user can perform CRUD operations like creating, editing, deleting and viewing notes.</p><p class='centered'><strong><a href='https://github.com/vkay616/django-react-notes-app'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p4:
        st.markdown("<div class='project'><h5 class='centered'>Stock Monitoring Dashboard</h5><p class='centered tmn highlight'><em>Python, Plotly-Dash, Scikit-Learn, TensorFlow</em></p><p class='j-text'>A stock monitoring dashboard which updates in real-time by scraping data from Google Finance website.</p><p class='centered'><strong><a href='https://github.com/vkay616/stock-price-monitoring-dashboard-using-plotly-dash'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    st.write("")

   
   
   
   
    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.markdown("<div class='project'><h5 class='centered'>Books API</h5><p class='centered tmn highlight'><em>Go, Gin, Colly</em></p><p class='j-text'>A simple API built using Gin Framework. It has 3 endpoints, to GET all books, to GET book by its ID and the last one to POST new book.</p><p class='centered'><strong><a href='https://github.com/vkay616/BooksAPI-using-Go'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p2:
        st.markdown("<div class='project'><h5 class='centered'>Stock Market Simulator</h5><p class='centered tmn highlight'><em>Python, Flask, TailwindCSS</em></p><p class='j-text'>Built a stock market simulator where users can choose to buy/sell stocks whose prices are changed by a random value every second.</p><p class='centered'><strong><a href='https://github.com/vkay616/library-management-website-Django'>View Code</a></strong></p></div>", unsafe_allow_html=True)


    with p3:
        st.markdown("<div class='project'><h5 class='centered'>Todo App</h5><p class='centered tmn highlight'><em>Python, Django, Flask</em></p><p class='j-text'>A todo web app where the user can perform basic CRUD operations like create, edit, view and delete tasks.</p><p class='centered'><strong><a href='https://github.com/vkay616/todo-app-using-Flask'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p4:
        st.markdown("<div class='project'><h5 class='centered'>Kyphosis Disease Prediction</h5><p class='centered tmn highlight'><em>Python, Scikit-Learn, LaTeX</em></p><p class='j-text'>Applied ML algorithms with feature scaling methods like Power Transform and Quantile Transform to predict kyphosis in children.</p><p class='centered'><strong><a href='https://ieeexplore.ieee.org/document/9984343'>View Paper</a> &nbsp; | &nbsp; <a href='https://github.com/vkay616/kyphosis-disease-prediction-using-RandomizedSearchCV-and-AdaBoost'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    st.write("")
    
    
    
    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.markdown("<div class='project'><h5 class='centered'>Electrical Load Forecasting</h5><p class='centered tmn highlight'><em>Python, Scikit-Learn, TensorFlow, Statsmodel</em></p><p class='j-text'>Engineered a short-term load forecasting model using ARIMA and LSTM, and compared its performance with traditional ML models.</p><p class='centered'><strong><a href='https://drive.google.com/file/d/1IE3JFF3g9hSxhW_8hX2nZKzZF-mDjw_U/view'>View Paper</a></strong></p></div>", unsafe_allow_html=True)

    with p2:
        st.markdown("<div class='project'><h5 class='centered'>Singapore Buildings' Info Extractor</h5><p class='centered tmn highlight'><em>Python, Selenium, Pillow, Pytesseract</em></p><p class='j-text'>Built a scraper to fetch the allowed limit of floors, type of buildings for a specific postal code in Singapore from ura.gov.sg/maps.</p><p class='centered'><strong><a href='https://github.com/vkay616/ura-singapore-land-information-scraper'>View Code</a></strong></p></div>", unsafe_allow_html=True)


    with p3:
        st.markdown("<div class='project'><h5 class='centered'>Real-Time Gender Detection</h5><p class='centered tmn highlight'><em>Python, OpenCV, TensorFlow</em></p><p class='j-text'>An app that can detect a person's gender in real-time. The model was trained using a dataset of around 2500 images.</p><p class='centered'><strong><a href='https://github.com/vkay616/real-time-gender-detection'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p4:
        st.markdown("<div class='project'><h5 class='centered'>Student Management System</h5><p class='centered tmn highlight'><em>Python, SQLite, Tkinter</em></p><p class='j-text'>A GUI based student management system where the user can perform CRUD operations on a students database.</p><p class='centered'><strong><a href='https://github.com/vkay616/student-management-system-using-sqlite-and-tkinter'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    st.write("")


    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.markdown("<div class='project'><h5 class='centered'>Lottery Smart Contract App</h5><p class='centered tmn highlight'><em>Solidity, JavaScript, React, Mocha</em></p><p class='j-text'>Built & deployed a tested smart contract on Sepolia Test Network. Players can enter lottery by paying min. 0.01 ether.</p><p class='centered'><strong><a href='https://github.com/vkay616/lottery-contract-react-app'>View Code</a></strong></p></div>", unsafe_allow_html=True)

    with p2:
        st.markdown("<div class='project'><h5 class='centered'>File Upload App</h5><p class='centered tmn highlight'><em>Python, Flask</em></p><p class='j-text'>A file uploading app (pdf and txt only) with user authentication using Flask Login.</p><br><p class='centered'><strong><a href='https://github.com/vkay616/flask-file-upload-app-with-user-authentication'>View Code</a></strong></p></div>", unsafe_allow_html=True)


    with p3:
        pass

    with p4:
        pass

