import reflex as rx

# --- Reactive State ---
class State(rx.State):
    todos: list[str] = []
    new_todo: str = ""

    def add_todo(self):
        if self.new_todo.strip():
            self.todos.append(self.new_todo.strip())
            self.new_todo = ""

    def remove_todo(self, index: int):
        self.todos.pop(index)


# --- UI Definition ---
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("📝 To-Do List", size="6"),
            rx.hstack(
                rx.input(
                    placeholder="Add a task...",
                    value=State.new_todo,
                    on_change=State.set_new_todo,
                    width="70%",
                ),
                rx.button("Add", on_click=State.add_todo),
            ),
            rx.divider(),
            rx.foreach(
                State.todos,
                lambda todo, i: rx.hstack(
                    rx.text(todo, flex="1"),
                    rx.button("❌", color_scheme="red", on_click=lambda: State.remove_todo(i)),
                ),
            ),
            width="400px",
            spacing="4",
        ),
        height="100vh",
    )


# --- App Setup ---
app = rx.App()
app.add_page(index)