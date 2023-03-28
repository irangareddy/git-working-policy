"""Welcome"""

import streamlit as st


def welcome_view():
    st.write("# Git Working Policy")
    st.sidebar.success("Select a option above.")

    st.markdown(
        """
        This project aims to establish a comprehensive Git working policy to ensure efficient and consistent Git usage
        within a team or organization. The policy covers various aspects of Git usage, including guidelines for checking
        out and committing code, requirements for commit metadata, signing, structure, and style.
        
        Additionally, the policy outlines a branching model that includes feature, bugfix, test, and release branches,
        as well as instructions for hotfixes and merging branches. The policy also provides guidelines for file and
        folder naming, including case sensitivity, special characters, and line endings.
        
        The project's goal is to establish a clear and unified Git workflow that promotes collaboration and productivity
        while minimizing errors and conflicts. The policy aims to facilitate the development process by providing a
        structured approach to Git usage, enabling team members to work efficiently and effectively.

        **👈 Select a option from the dropdown on the left** to try it out now and see for yourself how Git Working Policy can make your life easier! 🙌
    """
    )