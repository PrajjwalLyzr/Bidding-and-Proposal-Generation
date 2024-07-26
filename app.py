import os
from utils import utils
import streamlit as st
from PIL import Image
from bidding import bidding_proposal_generation
from dotenv import load_dotenv; load_dotenv()


# Setup your config
utils.page_config()
utils.style_app()


# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Bidding and Proposal Generation")
st.markdown("This app helps you to generate Bidding and Proposal for your specific Construction Projects")

# Setting up the sidebar for input
st.sidebar.title("Bidding and Proposal Generation")
API_KEY = os.getenv('OPENAI_API_KEY')

st.sidebar.markdown('---')
utils.template_end()
utils.social_media()

col1, col2, col3 = st.columns(3)

with col1:
    project_name = st.text_input(label="Project Name")
    start_data = st.date_input(label="Start Data")
    amenities = st.text_input(label="Amenities", placeholder='Gym, Parking, Swimming Pool')
    project_manager = st.text_input(label="Project Manager Name")
    company_email = st.text_input(label="Company Email", placeholder='company@abc.com')


with col2:
    project_location = st.text_input(label="Project Location")
    end_data = st.date_input(label="End Data")
    estimated_budget = st.text_input(label="Estimated Budget", value="$")
    company_address = st.text_input(label="Company Address")

with col3:
    design_preference = st.selectbox(label="Design Preferences", options=["Traditional", "Modern"])
    number_apartments = st.text_input(label="Number Of Apartments", placeholder="Type a number...")
    company_name = st.text_input(label="Company Name")
    company_phone = st.text_input(label="Company Phone", placeholder="Phone Number")


if (project_name and project_location and design_preference and amenities and
    start_data and end_data and number_apartments and 
    project_manager and estimated_budget and company_name and 
    company_address and company_email and company_phone) != "":

    if st.button('Generate'):
        generated_output = bidding_proposal_generation(ApiKey=API_KEY,
                                                       ProjectTitle=project_name,
                                                       ProjectLocation=project_location,
                                                       StartDate=start_data,
                                                       EndDate=end_data,
                                                       Amenities=amenities,
                                                       NumberOfApartments=number_apartments,
                                                       DesignPreferences=design_preference,
                                                       EstimatedBudget=estimated_budget,
                                                       CompanyName=company_name,
                                                       ProjectManagerName=project_manager,
                                                       CompanyAddress=company_address,
                                                       CompanyPhone=company_phone,
                                                       CompanyEmail=company_email)
        
        proposal = generated_output[0]['task_output']
        if proposal:
            st.markdown('---')
            st.write(proposal)
        

