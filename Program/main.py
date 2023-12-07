import faulthandler

faulthandler.enable()
from NutritionProgram import dashboard, home_screen

home_window = home_screen.HomeScreen(
    width=500, height=500, appearance_mode="light", color_theme="green"
)
home_window.show_homescreen()

dash_board = dashboard.Dashboard(
    width=1380,
    height=720,
    appearance="dark",
    theme_color="green",
    userName=home_window.get_user_enrollment_id(),
)

dash_board.show_dashboard()

print("Program exited successfully.")
