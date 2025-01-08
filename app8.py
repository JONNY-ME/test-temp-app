import streamlit as st

def main():
    st.title("Subscription Service Setup")

    # Define session state variables to manage page navigation
    if "page" not in st.session_state:
        st.session_state.page = 1

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    if st.session_state.page == 1:
        st.header("Welcome to [Service Name]!")
        st.write("Get started with your subscription in just a few steps.")

        st.header("Step 1: Basic Information")
        full_name = st.text_input("Name", help="Enter your full name.")
        email = st.text_input("Email Address", help="We'll send your confirmation and receipts to this email.")

        if st.button("Next"):
            next_page()

    elif st.session_state.page == 2:
        st.header("Step 2: Choose Your Plan")
        subscription_plan = st.radio("Select Your Subscription Plan:", ["Standard Plan", "Premium Plan (Most Popular!)", "Annual Plan (Best Value!)"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Next"):
                next_page()

    elif st.session_state.page == 3:
        st.header("Step 3: Card Details")
        st.write("To complete your subscription, securely provide your card information:")
        card_number = st.text_input("Card Number", help="e.g., 4111 1111 1111 1111.")
        expiration_date = st.text_input("Expiration Date", help="MM/YY")
        cvv = st.text_input("CVV (Security Code)", help="3 digits on the back of the card (4 for AMEX).", type="password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Next"):
                next_page()

    elif st.session_state.page == 4:
        st.header("Final Step: Confirm and Start Your Subscription")
        confirm_submission = st.checkbox("I authorize [Service Name] to charge my card according to my selected plan. I understand I can cancel anytime.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Submit"):
                if confirm_submission:
                    st.success("Thank you for starting your subscription!")
                else:
                    st.warning("Please authorize the payment to proceed.")

if __name__ == "__main__":
    main()
