import dearpygui.dearpygui as dpg

dpg.create_context()
# Generate unique ids for all widgets we want to change in runtime
wind_id = dpg.generate_uuid()
temp_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    output = "Wind Value:"
    dpg.create_viewport(title='Custom Title', width=600, height=300)

dpg.create_viewport(title="Windchill Caculator", width=600,height=300)

with dpg.window(label="Windchill Caculator", width=600, height=300):
    dpg.add_text("Welcome to the windchill caculator")
    dpg.add_input_int(label="Wind Speed",width=100, tag=wind_id )
    dpg.add_input_int(label="Temperature", width=100, tag=wind_id")
    dpg.add_button(label="Caculate", callback=callback)
    dpg.addbutto

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()