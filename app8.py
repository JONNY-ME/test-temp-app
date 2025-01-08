import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header

def main():
    st.title("🌟 Freelancer Profile Setup for Payment Processing 🌟")

    # Define session state variables to manage page navigation
    if "page" not in st.session_state:
        st.session_state.page = 1

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    if st.session_state.page == 1:
        colored_header("Welcome to Flexos!", color_name="blue-70")
        st.write(
            "Set up your profile to start receiving payments and accessing exclusive opportunities. Let’s make it quick and easy!"
        )

        st.markdown(
            "### Why Join Us?\n- **Easy Setup**: Quick onboarding process.\n- **Secure Payments**: Guaranteed payment security.\n- **Exclusive Opportunities**: Access top-tier projects."
        )

        colored_header("Personal Details", color_name="green-70")
        full_name = st.text_input(
            "Full Name", help="Enter your legal name as it appears on government-issued documents."
        )
        email = st.text_input(
            "Email Address", help="We’ll use this to send you payment notifications and updates."
        )
        country = st.text_input(
            "Country of Residence", help="Enter the name of your country of residence."
        )

        add_vertical_space(2)
        if st.button("Next »"):
            next_page()

    elif st.session_state.page == 2:
        colored_header("Tax Information", color_name="red-70")
        st.write(
            "To comply with tax regulations, we are required to collect your Tax Identification Number (TIN). This information will only be used for reporting purposes and will remain confidential."
        )

        tin = st.text_input(
            "Tax Identification Number (TIN)",
            help="Enter your TIN as issued by your local tax authority."
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("« Previous"):
                prev_page()
        with col2:
            if st.button("Next »"):
                next_page()

    elif st.session_state.page == 3:
        colored_header("Profile Preferences", color_name="red-70")
        st.markdown(
            "### Highlight Your Expertise\nSelect up to two skills that define your professional strengths."
        )
        skills = st.multiselect(
            "Professional Skills or Interests",
            ["Writing", "Design", "Programming", "Marketing", "Finance", "Consulting", "Data Analysis", "Customer Service"],
            help="Select up to three skills that best represent your expertise."
        )
        portfolio_link = st.text_input(
            "Portfolio Link (Optional)",
            help="Share a link to showcase your work (e.g., Behance, GitHub)."
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("« Previous"):
                prev_page()
        with col2:
            if st.button("Next »"):
                next_page()

    elif st.session_state.page == 4:
        colored_header("Confirm and Submit", color_name="orange-70")
        st.markdown(
            "### Final Step\nReview your information and click submit to complete your profile setup."
        )
        if st.button("✅ Submit"):
            st.success(
                "🎉 Thank you for setting up your profile! You are now ready to receive payments and explore opportunities with Flexos. 🎉"
            )

if __name__ == "__main__":
    main()
