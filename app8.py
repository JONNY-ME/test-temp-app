import streamlit as st

def main():
    st.title("Streamline")

    # Define session state variables to manage page navigation
    if "page" not in st.session_state:
        st.session_state.page = 1

    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    if st.session_state.page == 1:
        st.header("Welcome to Streamline Subscriptions!")
        st.write("Get started with your subscription in just a few steps. Streamline Subscriptions offers you flexible and affordable plans to access premium content and exclusive features.")
        st.write("Whether you're looking for a monthly plan or a long-term commitment with added savings, we have options that fit your needs. Join our community and enjoy seamless, uninterrupted services tailored to your preferences.")

        st.header("Step 1: Basic Information")
        full_name = st.text_input("Name", help="Enter your full name.")
        email = st.text_input("Email Address", help="We'll send your confirmation and receipts to this email.")

        if st.button("Next"):
            next_page()

    elif st.session_state.page == 2:
        st.header("Step 2: Choose Your Plan")
        subscription_plan = st.selectbox("Select Your Subscription Plan:", [
            "Standard Plan", 
            "Premium Plan (Most Popular!)", 
            "Annual Plan (Best Value!)"])
        st.write("**Standard Plan ($10/month)**: Enjoy access to our basic features and services, ideal for casual users.")
        st.write("**Premium Plan ($20/month)**: Unlock premium features, exclusive content, and priority support for an enhanced experience.")
        st.write("**Annual Plan ($200/year)**: Save more with our best value plan, providing all Premium features for an entire year.")

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
        confirm_submission = st.checkbox("I authorize Streamline Subscriptions to charge my card according to my selected plan. I understand I can cancel anytime.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                prev_page()
        with col2:
            if st.button("Submit"):
                if confirm_submission:
                    st.success("Thank you for starting your subscription! Welcome to Streamline Subscriptions.")
                else:
                    st.warning("Please authorize the payment to proceed.")

if __name__ == "__main__":
    main()
