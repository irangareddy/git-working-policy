import streamlit as st
import re

regex_pattern = r"^[a-zA-Z]+\w*(\s+[a-zA-Z0-9]+\w*)*$"


def validate_branch_name(s):
    if len(s.split()) > 3:
        return False, "Branch names should not be no more than two words for best practice."
    elif not re.match(regex_pattern, s):
        return False, "Invalid branch name."
    return True, "Valid branch name."


def branch_name_view():
    st.title('Branch Naming Standards')

    option = st.selectbox(
        'Branch Type',
        ('Feature', 'Bug', 'Temp'),
        format_func=lambda x: {
            'Feature': 'Create a new feature or user story',
            'Bug': 'Fix a bug or issue',
            'Temp': 'Create a temporary branch for experimentation or testing',
        }[x]
    )

    branch_name = st.text_input('Branch Name', '')
    st.caption("""
    - Enter a branch name with only alphabets or alphanumeric characters
    - Use word spacing only, no special characters like :red[new-branch, fix_branch]
    - Must start with at least one alphabet character and followed by zero or more alphanumeric characters
    - Followed by zero or more occurrences of a space and one or more alphabetic or alphanumeric characters, and zero or more alphanumeric characters
    """)
    valid, message = validate_branch_name(branch_name)
    if not valid:
        st.error(message, icon="🚨")
    ticket = st.text_input('Ticket Name', '')
    st.caption("Some examples of valid ticket names styles: :blue[CMEM-1211, ECC-3223, JIRA-122, RNN-212]")
    if option is not None and branch_name and ticket:
        proper_name = generate_branch_name(branch_type=option, name=branch_name, ticket_number=ticket)
        st.write("The proper branch name is")
        st.success(proper_name)


def generate_branch_name(branch_type, name, ticket_number):
    # Enforce camel case for name argument
    name = proper_naming(name)

    if branch_type == "Feature":
        return f"feature/{name}-{ticket_number}"
    elif branch_type == "Bug":
        return f"bugfix/{name}-{ticket_number}"
    elif branch_type == "Temp":
        return f"temp/{name}"
    else:
        raise ValueError(f"Invalid branch type: {branch_type}")


def proper_naming(name):
    # Split the string into individual words

    words = name.split()

    # Capitalize the first letter of each word except for the first one
    capitalized_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]

    # Concatenate the words back together to form a camel case string
    camel_case_string = ''.join(capitalized_words)

    return camel_case_string
