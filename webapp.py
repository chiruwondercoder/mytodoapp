import streamlit as cg
import functions

todos = functions.get_todos()

def add_todo():
    todotoget = cg.session_state["new_todo"] + "\n"
    todos.append(todotoget)
    functions.write_todos(todos)

cg.title("Your everyday TODO app!")
cg.subheader("Use this app to increase your productivity.")
cg.write("Manage your everyday task by keeping the TODO list handy \n and this app can help you achieve this.")

for index, todo in enumerate(todos):
    checkbox = cg.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del cg.session_state[todo]
        cg.experimental_rerun()

cg.text_input(label="", placeholder="Add new todo here...!", on_change=add_todo, key="new_todo")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
cg.markdown(hide_streamlit_style, unsafe_allow_html=True)

