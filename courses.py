class Course:
    name: str
    provider: str
    verification_link: str


    def __init__(self, n, p, v) -> None:
        self.name = n
        self.provider = p
        self.verification_link = v


courses = [

    Course(
        "IBM Data Science Professional Certificate", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/specialization/certificate/2VZF27CUSEKJ"
    ),

    Course(
        "Google Cloud Computing Foundation Program", 
        "Google", 
        "https://drive.google.com/file/d/1VZiZ37OA6kWQMOObFfSIbSqEnZnrrMJH/view"
    ),

    Course(
        "Go: The Complete Developer's Guide (Golang)", 
        "Udemy", 
        "https://www.udemy.com/certificate/UC-8eb805c6-8d1d-4e1e-9642-5d6446aab7c2/"
    ),

    Course(
        "Python and Django Full Stack Web Developer Bootcamp", 
        "Udemy", 
        "https://www.udemy.com/certificate/UC-b88f586e-be78-4316-b9e8-6e6a755baba1/"
    ),

    Course(
        "Convolutional Neural Networks", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/9HZ6H7DG4H8R"
    ),

    Course(
        "Tensorflow 2.0: Deep Learning and Artificial Intelligence", 
        "Udemy", 
        "https://www.udemy.com/certificate/UC-0e952797-5c93-4608-b7b7-e0ac17c50a90/"
    ),

    Course(
        "Machine Learning A-Z™: Hands-On Python & R in Data Science", 
        "Udemy", 
        "https://www.udemy.com/certificate/UC-2280da1f-a50f-42aa-8975-caf28647dd36/"
    ),

    Course(
        "Structuring Machine Learning Projects", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/8X5A38S3K9VW"
    ),

    Course(
        "Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/GUFHZ4BHS8FM"
    ),
        
    Course(
        "Neural Networks and Deep Learning", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/VNRSV6C6BS3X"
    ),

    Course(
        "The Complete Python Masterclass: Learn Python from Scratch", 
        "Udemy", 
        "https://www.udemy.com/certificate/UC-683f7638-6689-45c9-baa6-eaa274d08e3f/"
    ),

    Course(
        "Python Data Structures", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/TESFF2CF53JV"
    ),

    Course(
        "Programming for Everybody (Getting Started with Python)", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/LCVLYZTPHKWH"
    ),

    Course(
        "Introduction to Programming with MATLAB", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/HCE6UW2CKLFQ"
    ),

    Course(
        "Game Theory", 
        "Coursera", 
        "https://www.coursera.org/account/accomplishments/certificate/VA8F9RXTJUFQ"
    ),

    Course(
        "Career Essentials in Data Analysis by Microsoft and LinkedIn", 
        "LinkedIn", 
        "https://www.linkedin.com/learning/certificates/59086fe6c6a273a96d4f28b607e7c0795e516de7aff46bcade6241cf7b61e0bd?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "SQL and Relational Databases 101", 
        "Cognitive Class", 
        "https://courses.cognitiveclass.ai/certificates/2fbea288fde34835b6e44ffd079f4d4d"
    ),

    Course(
        "SQL for Data Analysis (2020)", 
        "LinkedIn", 
        "https://www.linkedin.com/learning/certificates/ddde539606eb99dddec8716f4acc3052454735b9fdaca932897f3d5f2abce0fa?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "Learning Excel: Data Analysis", 
        "LinkedIn", 
        "https://www.linkedin.com/learning/certificates/d9fbe2f7561c5ff5fbc3de51e952cc7d16430199685393d549523613d759f0db?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "Learning Data Analytics Part 2: Extending and Applying Core Knowledge", 
        "Coursera", 
        "https://www.linkedin.com/learning/certificates/b8b760a9c0d603e550c5c46afea208e1f6338dd9dde6ca24232cbad0659f1635?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "Learning Data Analytics: 1 Foundations", 
        "LinkedIn", 
        "https://www.linkedin.com/learning/certificates/63c278bef7eb2c734926d597ddb95142f18af52862e2d26d7169063af20046c5?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "Data Fluency: Exploring and Describing Data",
        "LinkedIn",
        "https://www.linkedin.com/learning/certificates/b405b216f3e314db69d01990a15a62a8904f7fc892737c092908c6e2d70eaab2?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "Introduction to Career Skills in Data Analytics",
        "LinkedIn",
        "https://www.linkedin.com/learning/certificates/de2660965413d280acacd6ea9b5c15bf9704a8b189eaeefd89dabebdc7651c8f?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    ),

    Course(
        "The Non-Technical Skills of Effective Data Scientists",
        "LinkedIn",
        "https://www.linkedin.com/learning/certificates/f2430994b8617490b0f27c57e38ddb4a2c0e9b03d6de5e32c80d3164cfd23f15?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_certifications_details%3BUwL2aa%2FVRUKTfFjVGx3H8g%3D%3D"
    )

]
