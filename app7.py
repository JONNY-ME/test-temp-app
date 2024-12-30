import streamlit as st

def main():
    st.title("KodeKloud - Event Reservation Form")

    with st.form("reservation_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        event_date = st.date_input("Event Date")
        number_of_guests = st.number_input("Number of Guests", min_value=1, step=1)
        address = st.text_area("Address", placeholder="Enter your address")

        # Submit button
        submitted = st.form_submit_button("Reserve")

        if submitted:
            if name and email and address:
                st.success("Reservation successful! Thank you, {}.".format(name))
                st.write("Reservation Details:")
                st.write(f"Name: {name}")
                st.write(f"Email: {email}")
                st.write(f"Event Date: {event_date}")
                st.write(f"Number of Guests: {number_of_guests}")
                st.write(f"Address: {address}")
            else:
                st.error("Please fill in all the required fields before submitting.")

if __name__ == "__main__":
    main()
