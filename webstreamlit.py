import streamlit as st

st.title("To do List")

if "Task" not in st.session_state:
    st.session_state.Task = [];

with st.form("todo_form"):
    new_task = st.text_input("New Task")
    submitted = st.form_submit_button("Add Task")

if new_task and submitted:
    st.session_state.Task.append(new_task)
    st.success(f"Added task {new_task}")

st.subheader("Avaliable Task:")

if st.session_state.Task:
    for index, task in enumerate(st.session_state.Task):
        col1, col2 = st.columns([4, 1]) 
        col1.write(f"{index+1} {task}")
        remove = col2.button("❌", key=f"remove_{index}")

        if remove:
           st.session_state.Task.pop(index)
           st.rerun()


else:
    st.info("No tasks yet. Add one above!")
