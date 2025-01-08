import streamlit as st

def main():
    st.title("Personalised Wellness Program Registration")

    # Define session state variables to manage page navigation
    if "page" not in st.session_state:
        st.session_state.page = 1

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    if st.session_state.page == 1:
        # st.header("Welcome to [Program Name]!")
        st.write("Let’s create a wellness plan that’s uniquely yours. This form takes just a few moments.")

        st.header("Step 1: Tell Us About Yourself")
        full_name = st.text_input("Name", help="Enter your full name.")
        email = st.text_input("Email Address", help="We’ll send you updates, resources, and your personalised plan.")
        age_group = st.radio("Age Group", ["Under 18", "18-30", "31-50", "Over 50"], help="Select your age group.")
        hobbies = st.multiselect("Hobbies or Interests", ["Photography", "Hiking", "Reading", "Yoga", "Cooking", "Other"], help="Choose up to three activities you enjoy.")

        if st.button("Next"):
            next_page()

    elif st.session_state.page == 2:
        st.header("Step 2: Health & Wellness Information")
        st.write("Your Health Profile")
        st.write("To provide you with the best plan, we’d like to understand your health better.")

        diagnosed_conditions = st.radio("Do you have any diagnosed medical conditions?", ["Yes", "No"], help="Specify if you have any medical conditions.")
        if diagnosed_conditions == "Yes":
            condition_details = st.text_area("Please specify your medical conditions:")

        treatments = st.radio("Are you currently undergoing any treatments or taking medication?", ["Yes", "No"], help="Specify if you are on any treatments or medication.")
        if treatments == "Yes":
            treatment_details = st.text_area("Please specify your treatments or medications:")

        medical_history = st.text_area("Brief Medical History (Optional)", help="Share any significant health events or history (e.g., surgeries, chronic conditions).")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Next"):
                next_page()

    elif st.session_state.page == 3:
        st.header("Step 3: Consent & Privacy")
        consent = st.checkbox("I consent to the use of my health and personal information for the purpose of creating a personalised wellness plan. I understand that my data will remain confidential and securely stored in compliance with privacy laws.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Next"):
                if consent:
                    next_page()
                else:
                    st.warning("Please provide your consent to proceed.")

    elif st.session_state.page == 4:
        st.header("Step 4: Confirm and Submit")
        if st.button("Submit"):
            st.success("Thank you for registering! Your personalised wellness plan will be sent to your email shortly.")

if __name__ == "__main__":
    main()
