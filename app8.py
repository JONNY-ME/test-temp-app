import streamlit as st

def main():
    st.title("Volunteer Contact & Participation Form")

    st.header("Part 1: Basic Contact & Participation Details")
    full_name = st.text_input("Full Name", help="Enter your legal name as it appears on your government-issued ID.")
    preferred_name = st.text_input("Preferred Name (if any)", help="If you go by a name other than your legal name, please list it here.")
    email = st.text_input("Primary Email Address", help="We will use this email to communicate all event details and updates.")
    phone_number = st.text_input("Phone Number", help="Include country code if outside the local region.")

    attendance = st.radio("Are you attending the full event or partial days?", ["Full Event", "Partial Days"])
    if attendance == "Partial Days":
        specific_days = st.text_input("If Partial Days, specify which days you will attend.")

    st.header("Part 2: Logistics & Special Requirements")
    t_shirt_size = st.selectbox("T-Shirt Size (for volunteer uniform)", ["XS", "S", "M", "L", "XL", "XXL", "Other"])
    dietary_restrictions = st.text_area("Dietary Restrictions or Allergies", help="Let us know if you have any food limitations so we can accommodate you.")

    st.subheader("Emergency Contact Information")
    emergency_contact_name = st.text_input("Name")
    emergency_contact_relationship = st.text_input("Relationship to You")
    emergency_contact_phone = st.text_input("Phone Number")

    st.header("Part 3: Stipend & Reimbursement Preferences")
    st.subheader("Bank Details")
    account_holder_name = st.text_input("Account Holder's Name", help="Please confirm the exact name on the bank account.")
    bank_name = st.text_input("Bank Name", help="Example: XYZ Bank.")
    account_type = st.radio("Type of Account", ["Checking", "Savings"])
    branch_location = st.text_input("Branch Location (optional)", help="If known, you may list the city or branch code.")
    account_number = st.text_input("Account Number", help="e.g., 123456789 (Checking).")
    routing_number = st.text_input("Routing Number", help="e.g., 987654321.")

    st.header("Part 4: Consent & Submission")
    confirm_submission = st.checkbox("I confirm that all provided information is accurate and I authorize the organization to use it strictly for volunteer coordination, stipend, and reimbursement purposes.")

    if confirm_submission:
        st.success("Thank you for submitting your details!")

if __name__ == "__main__":
    main()
