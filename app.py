import streamlit as st

def display_menu():
    st.sidebar.title("Task Manager")
    option = st.sidebar.selectbox(
        "Choose an option:",
        ["View tasks", "Add new task", "Search for a task", "Delete task", "Exit"],
        key="menu"
    )
    return option

def view_task(tasks):
    st.subheader("View Tasks")
    if not tasks:
        st.write("No tasks available.")
    else:
        for title, content in tasks.items():
            st.write(f"**{title}**")
            st.write(f"{content}")

def add_new_task(tasks):
    st.subheader("Add New Task")
    title = st.text_input("Enter Task Title", key="add_title")
    content = st.text_area("Enter Task Content", key="add_content")
    if st.button("Add Task", key="add_button"):
        if title and content:
            tasks[title] = content
            st.success("Task added successfully.")
        else:
            st.warning("Please enter both title and content.")

def search_for_task(tasks):
    st.subheader("Search for a Task")
    search = st.text_input("Enter Task Title to Search", key="search_title")
    if st.button("Search", key="search_button"):
        if search in tasks:
            st.write(f"**{search}**")
            st.write(f"{tasks[search]}")
        else:
            st.write(f"Task '{search}' not found.")

def delete_task(tasks):
    st.subheader("Delete Task")
    delete = st.text_input("Enter Task Title to Delete", key="delete_title")
    if st.button("Delete", key="delete_button"):
        if delete in tasks:
            del tasks[delete]
            st.success("Task deleted successfully.")
        else:
            st.write(f"Task '{delete}' not found.")

def main():
    st.title("Task Manager")
    if 'tasks' not in st.session_state:
        st.session_state.tasks = {}
    
    option = display_menu()
    
    if option == "View tasks":
        view_task(st.session_state.tasks)
    elif option == "Add new task":
        add_new_task(st.session_state.tasks)
    elif option == "Search for a task":
        search_for_task(st.session_state.tasks)
    elif option == "Delete task":
        delete_task(st.session_state.tasks)
    elif option == "Exit":
        st.write("Thank you for using our task manager. Goodbye!")

if __name__ == "__main__":
    main()
