def get_last_grades_widget(subject, grades_list):
    widgety_ocen = ''
 
    for i in range(0, len(grades_list)):
        if grades_list[i] == "1" or grades_list[i] == "1+":
            color = "#CC6666"
        elif "2" in grades_list[i]:
            color = "#9966CC"
        elif grades_list[i] == "3" or grades_list[i] == "3-" or grades_list[i] == "3+":
            color = "#CC9933"
        elif grades_list[i] == "4" or grades_list[i] == "4-" or grades_list[i] == "4+":
            color = "#3399FF"
        elif grades_list[i] == "5" or grades_list[i] == "5-" or grades_list[i] == "5+":
            color = "#33CC99"
        elif grades_list[i] == "6" or grades_list[i] == "6-":
            color = "#99CC33"
        elif grades_list[i] == "np." or grades_list[i] == "nb" or grades_list[i] == "bz":
            color = "#003366"
        else:
            color = "#6600CC"
            
            
        widgety_ocen = widgety_ocen + f'MDCard(MDLabel(text="{grades_list[i]}", font_size=24, halign="center", bold=True), size_hint=(None, None), size=("26dp", "26dp"), md_bg_color=utils.get_color_from_hex("{color}"), radius=10)' + ', '
    widget_parameters = f'MDLabel(text="{subject}", size_hint=(None, None), adaptive_height=True, adaptive_width=True), ' + widgety_ocen + 'orientation="horizontal", padding=(0, 0, 0, "10dp"), spacing="5dp"'
    
    ready_widget = f'MDBoxLayout({widget_parameters})'
    return ready_widget

def get_timetable_widget():
    pass

def get_tests_widget(nazwa_spr, data_spr, spr_color):
    if spr_color == True:
        if_color = 'theme_text_color="Custom", '
    else:
        if_color = ''
        
    ready_widget = f'MDBoxLayout(MDLabel(text="{nazwa_spr}", size_hint=(None, None), adaptive_width=True, height="20dp", {if_color}text_color=utils.get_color_from_hex("#3399FF")), MDLabel(text="{data_spr}", halign="right", height="20dp", size_hint=(1, None), {if_color}text_color=utils.get_color_from_hex("#3399FF")), orientation="horizontal", padding=(0, 0, 0, "10dp"))'
    return ready_widget

def get_homework_widget(nazwa_zadania, data_zadania, zadanie_color):
    if zadanie_color == True:
        if_color = 'theme_text_color="Custom", '
    else:
        if_color = ''
        
    ready_widget = f'MDBoxLayout(MDLabel(text="{nazwa_zadania}", size_hint=(None, None), adaptive_width=True, height="20dp", {if_color}text_color=utils.get_color_from_hex("#3399FF")), MDLabel(text="{data_zadania}", halign="right", height="20dp", size_hint=(1, None), {if_color}text_color=utils.get_color_from_hex("#3399FF")), orientation="horizontal", padding=(0, 0, 0, "10dp"))'
    return ready_widget
    


