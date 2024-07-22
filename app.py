import streamlit as st

def display_menu():
 st.title = "Task Manager"
 option = st.selectbox("Choose Options:", ["View task", "Add new task","Search for a task","Delete task","Exit"])
 return option
def view_task(tasks):
    st.subheader = "View Task"
    if not tasks:
        st.write("No tasks available")
    else:
        for title, content in tasks.items():
            st.write(f" {title}")
            st.write(f"{content}")
            
def add_new_task(tasks):
    st.subheader = "Add New Task"
    title = st.text_input("Enter Task Title")
    content = st.text_area("Enter Task Content")
    if st.button("Add Tassk"):
        if title and content:
         st.success("Task added successfully")
    else:
        st.warning("Please enter both title and content")
        
def search_for_task(tasks):
    st.subheader = "Search for a Task"
    search = st.text_input("Enter Task Title")
    if st.button("Search"):
        if search in tasks:
            st.write(f"Task found: {search}")
            st.write(f"{tasks[search]}")
        else:
            st.write(f"Task '{search}' not found")
    else:
        st.warning("Please enter a task title to search")
        
def delete_task(tasks):
    st.subheader = "Delete Task"
    delete = st.text_input("Enter Task Title")
    if st.button("Delete"):
        if delete in tasks:
            del tasks[delete]
            st.success("Task deleted successfully")
        else:
            st.write(f"Task '{delete}' not found")
    else:
        st.warning("Please enter a task title to delete")

def exit_task(tasks):
    st.subheader("Exit")
    st.write("Thank you for using our task manager. Goodbye!")
    st.stop()
    
def main():
    st.title("Task Manager")
    tasks = {}
    
    while True:
        option = display_menu()
        
        if option == "View task":
            view_task(tasks)
        elif option == "Add new task":
            add_new_task(tasks)
        elif option == "Search for a Task":
            search_for_task(tasks)
        elif option == "Delete task":
            delete_task(tasks)
        elif option == "Exit":
            exit_task(tasks)
            break

if __name__ == "__main__":
    main()