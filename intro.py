## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)


# Navbar
st.set_page_config(
    page_title="Intro Generator",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ AI Intro Generator"
    "</h1>",
    unsafe_allow_html=True
)

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 24px;
    margin-top: 0;
    margin-bottom: 24px;
}
</style>
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">🎨&nbsp;&nbsp;Turn Your Blogging Ideas into a Magnetic&nbsp;&nbsp;💥<br>Create stunning intros that will grab your audience's attention and leave them wanting more!</h3>
''', unsafe_allow_html=True)


# sidebar for the user input

with st.sidebar:
    st.markdown(
        "<style>h1 {text-align: center;}</style>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<style>h1 {text-align: center; color: black;}</style>",
        unsafe_allow_html=True
    )
    st.title("Input Settings")
    
    st.markdown(
        "<style>"
        "h4 {text-align: left; color: black; margin-top: 4px;}"
        "p {text-align: left; color: black;}"
        "</style>",
        unsafe_allow_html=True
    )
    st.markdown("<h4>Enter Details for the Intro: </h4>", unsafe_allow_html=True)

    # Blog Title
    blog_title = st.text_input("Blog Title/Topic") 

    # Primary Keyword
    primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    secondary_keyword = st.text_input("Secondary Keyword")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Word Counter
    word_count = st.number_input("Word Count", min_value=250, max_value=3000, step=100)
    

    # Prompt
    prompt_parts = [
            f"""
            Please ignore all previous instructions. You are an expert copywriter who writes detailed and compelling blog articles. Can you please write a short introduction to this article on {blog_title}? The introduction length must be {word_count} words. Please use the Question, background and thesis copywriting framework to hook and grab the attention of the blog readers. In the first section ask* questions and engage the reader.
            n the second section define the background of the topic. In the third section, tell about what is going to be discussed, and what values you are going to get by reading this article/blog.
            Follow these instructions:
            1. You have a {voice_tones} tone of voice. 
            2. You have a {writing_styles} writing style. Targeted audience is {audience}.
            3. Mentions the number of words in the end of response.
            3. Avoiding jargon and complex terms.
            4. Write like a human.
            5. Focus first on creating high quality, thorough content that provides value to readers. 
            6. Making sure to incorporate Primary Keyword "{primary_keyword}" as the primary keyword and "{secondary_keyword}" as a secondary keyword. 
	        7. Your introduction should grab the reader's attention, provide context, and give a brief overview of what they can expect to learn from the post. 
	        8. Incorporate the Primary Keyword "{primary_keyword}" into your introduction in a natural and relevant way in bold format only one time, and include the Secondary Keyword "{secondary_keyword}" at least once to reinforce its importance and also in bold format.
            9. Keep paragraphs 3 sentences or less. Turn long sentences into two shorter ones.
            10. Markdown formatting where applicable
            11. Write content so that it can outrank other websites. 
            11. Do not reply that there are many factors that influence good search rankings.
            12. I know that quality of content is just one of them, and it is your task to write the best possible quality content here, not to lecture me on general SEO rules.
            13. Make sure that you don't follow ai pattern but article should be really simple and it should make sense. 
            14. Make sure to add a bit of humor and add some funny lines. Also add bold and italic
            15. write the information in your own words rather than copying and pasting from other sources also double-check for plagiarism because I need pure unique content
            """
            ]

    # Submit Button
    submit_button = st.button("Generate")




if submit_button:
    # Display the spinner
    with st.spinner("Converting desired input to prompt..."):
        # Generate the response
        response = model.generate_content(prompt_parts)
        # Write results
        st.write(response.text)
        
        
        

    # Add styling to the generated text
    st.markdown('''
        <style>
            p {
                font-family: 'Open Sans', sans-serif;
                font-size: 16px;
                line-height: 24px;
                margin-top: 0;
                margin-bottom: 24px;
            }
            strong {
                font-weight: 600;
            }
            em {
                font-style: italic;
            }
            code {
                background-color: #f5f5f5;
                border-radius: 3px;
                display: inline-block;
                font-family: 'Menlo', monospace;
                font-size: 14px;
                margin: 0 1px;
                padding: 2px 4px;
            }
        </style>
    ''', unsafe_allow_html=True)

clear_button = st.sidebar.button("Clear All")
with st.sidebar:
    st.markdown('''
        <style>
            .element-container .stButton.stBtn {
                background-color: #ffc107 !important;
                border-color: #ffc107 !important;
            }
        </style>
    ''', unsafe_allow_html=True)

    if clear_button:
        for key in st.session_state:
            if isinstance(st.session_state[key], str) and st.session_state[key] != "":
                st.session_state[key] = ""
            elif isinstance(st.session_state[key], list) and st.session_state[key] != []:
                st.session_state[key] = []
            elif isinstance(st.session_state[key], dict) and st.session_state[key] != {}:
                st.session_state[key] = {}

# Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)



