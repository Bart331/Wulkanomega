from kivy.lang import Builder
from kivymd.app import MDApp
#from kivymd.uix.label import MDIcon
from kivy.properties import StringProperty
#from kivymd.uix.list import OneLineListItem, IconLeftWidget, IconLeftWidgetWithoutTouch, OneLineIconListItem
from jakies_procedury_zamiana import get_last_grades_widget as glw
from jakies_procedury_zamiana import get_tests_widget as gtw
from jakies_procedury_zamiana import get_homework_widget as ghw
#from time import sleep
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import kivy.utils as utils
from kivy.config import Config
from kivy.clock import Clock


Config.set('kivy', 'exit_on_escape', '0')



class Tabs(MDBoxLayout, MDTabsBase):
    pass

class Wulkanomega(MDApp):
    
    last_grades_height = StringProperty('80dp')
    najblizsze_spr_height = StringProperty('80dp')
    zadania_domowe_height = StringProperty('80dp')
    
    today_lucky_number = StringProperty("--/11")
    unread_messages_count = StringProperty("0")
    procent_frekwencji = StringProperty("98,89%")
    
    grades_click_count = 0
    
    

    def resize_grades_card(self, num):
        if num == 2:
            self.last_grades_height = "120dp"
        elif num == 0 or num == 1:
            self.last_grades_height = "80dp"
        else:
            self.last_grades_height = str(120 + num * 25) + "dp"
            
    def resize_tests_card(self, num):
        if num == 2:
            self.najblizsze_spr_height = "120dp"
        elif num == 0 or num == 1:
            self.najblizsze_spr_height = "80dp"
        else:
            self.najblizsze_spr_height = str(120 + num * 15) + "dp"
            
    def resize_homowork_card(self, num):
        if num == 2:
            self.zadania_domowe = "120dp"
        elif num == 0 or num == 1:
            self.zadania_domowe_height = "80dp"
        else:
            self.zadania_domowe_height = str(120 + num * 15) + "dp"
   
    def on_start(self):
        #self.root.ids.last_grades_box.remove_widget(self.root.ids.ost_oceny_1)
        self.resize_grades_card(0)
        self.resize_tests_card(0)
        self.resize_homowork_card(1)
        
        #nazwa_spr = "Sprawdzian - fizyka"
        nazwa_spr = "Brak nadchodzących sprawdzianów"
        #data_spr = "10.07"
        data_spr = ""
        #syff = glw("Dziad", ["6", "5", "4", "3", "2", "1", "np.", "..."])
        #for _ in range(10):
        #self.root.ids.last_grades_box.add_widget(eval(syff))
        syff = glw("Brak nowych ocen", [])
        self.root.ids.last_grades_box.add_widget(eval(syff))
        
        spr_wg1 = gtw(nazwa_spr, data_spr, False)
        #spr_wg = gtw("Kartkówka - matematyka", "6.07", True)
        #for _ in range(5):
        #self.root.ids.najblizsze_sprawdziany.add_widget(eval(spr_wg))
        self.root.ids.najblizsze_sprawdziany.add_widget(eval(spr_wg1))
        
        #zadania = ghw("Język niemiecki - Setieaje12wohnundzwanzigstenarberitzwieundfunfzehn", "17.07", False)
        zadania = ghw("Język niemiecki - Z12 Ab 2", "17.07", False)
        self.root.ids.zadania_domowe.add_widget(eval(zadania))
        
    def load_grades(self):
        self.resize_grades_card(2)
        
        self.root.ids.last_grades_box.clear_widgets()
        syff = glw("Dziad", ["6", "5"])
        self.root.ids.last_grades_box.add_widget(eval(syff))
        syff = glw("Matma", ["4+", "5"])
        self.root.ids.last_grades_box.add_widget(eval(syff))
        
    def btn_press(self):
        self.root.ids.main_nav.switch_tab("oceny")
       
    def set_to_grades(self):
        global grades_click_count
        self.grades_click_count += 1
        if self.grades_click_count == 2:
            #print("dwa razy")
            self.root.ids.grades_tabs.switch_tab("Szczegóły")
            self.grades_click_count = 0
            
    def reset_grades_tab(self):
        global grades_click_count
        self.grades_click_count = 0
        
            
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("start.kv")
    
    def refresh_callback(self, *args):

        def refresh_callback(interval):
            print("refresh")
            self.load_grades()
            self.root.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)
            
    
Wulkanomega().run()



'''

https://pictogrammers.com/library/mdi/
https://kivymd.readthedocs.io/en/1.1.1/
https://www.rapidtables.com/web/color/RGB_Color.html
https://vulcan-api.readthedocs.io/en/latest/full-docs.html
padding_left, padding_top, padding_right, padding_bottom

#99CC33 6
#33CC99 5
#3399FF 4
#CC9933 3
#9966CC 2
#CC6666 1
#003366 np
#6600CC other ...
'''
