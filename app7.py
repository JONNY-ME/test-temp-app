import streamlit as st

# Sidebar Navigation
st.sidebar.title("Sophia Carter")

st.sidebar.image("img/download.jpeg")
st.sidebar.markdown("**Business Analyst**")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/sophiacarter) | [Email](mailto:paexternal228@oaisb.info)")

# Main Page Content
st.title("Sophia Carter")
st.subheader("Business Analyst Portfolio")
st.markdown("""
Analytical and detail-oriented Business Analyst with 5+ years of experience in driving business solutions through data-driven decision-making, stakeholder engagement, and process optimization.
""")

# About Section
st.header("About Me")
st.markdown("""
I specialize in transforming complex business challenges into actionable solutions. With expertise in data analysis, Agile methodologies, and stakeholder management, I aim to optimize processes and deliver measurable results for organizations.
""")

# Skills Section
st.header("Skills")
st.write("""
- **Business Process Modeling**  
- **Requirements Gathering and Analysis**  
- **Data Visualization (Power BI, Tableau)**  
- **SQL and Advanced Excel**  
- **Agile and Scrum Methodologies**  
- **Risk Assessment and Mitigation**  
- **Stakeholder Engagement**  
- **Change Management**
""")

# Work Experience Section
st.header("Work Experience")

st.subheader("Senior Business Analyst | ABC Tech Solutions")
st.write("**Jan 2020 – Present | Berlin, Germany**")
st.markdown("""
- Collaborated with cross-functional teams to deliver business transformation projects worth €2M+.  
- Designed and implemented data visualization dashboards using Tableau, reducing reporting time by 30%.  
- Developed process maps and workflows to streamline client onboarding, reducing cycle time by 20%.  
""")

st.subheader("Business Analyst | Innovate Analytics")
st.write("**June 2017 – Dec 2019 | Hamburg, Germany**")
st.markdown("""
- Automated recurring reports, saving 25+ hours/month for the analytics team.  
- Facilitated Agile ceremonies as a Scrum Master, enhancing project delivery timelines by 10%.  
""")

st.subheader("Junior Business Analyst | DataBridge Consulting")
st.write("**Aug 2015 – May 2017 | Munich, Germany**")
st.markdown("""
- Conducted market research to identify business opportunities, supporting revenue growth of €500K annually.  
- Assisted in creating business cases and feasibility studies for new initiatives.  
""")

# Education Section
st.header("Education")

st.subheader("Master of Business Administration (MBA)")
st.write("**Technical University of Munich | Graduated: 2015**")

st.subheader("Bachelor of Economics and Business Administration")
st.write("**University of Frankfurt | Graduated: 2013**")

# Certifications Section
st.header("Certifications")
st.write("""
- **Certified Business Analysis Professional (CBAP)**  
- **Scrum Master Certified (SMC)**  
- **Tableau Desktop Specialist**
""")

# Contact Section
st.header("Contact Me")
st.markdown("""
- **Email**: [paexternal228@oaisb.info](mailto:paexternal228@oaisb.info)  
- **LinkedIn**: [linkedin.com/in/sophiacarter](https://linkedin.com/in/sophiacarter)  
""")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 Sophia Carter | Portfolio created with Streamlit")
