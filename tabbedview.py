from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty

from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from elecengpy import elementfile as ef
import re



class CustomTab(TabbedPanel):
    pass

class EdgeTab(TabbedPanel):
    resistance = StringProperty("TBC")
    def cable_calcs(self):
        cable = ef.cableclass()
        size = re.findall(r"[-+]?\d*\.\d+|\d+", self.ids.btn_size.text)
        size = size[0]
        cable.changesize(size)
        if 'PVC' in (self.ids.btn_insulation.text):
            cable.changeinsulation('pvc')
        elif 'XLPE' in self.ids.btn_insulation.text:
            cable.changeinsulation('pvc')
        if 'single' in (self.ids.btn_core.text):
            cable.changecore('single core')
        elif 'Multi' in self.ids.btn_core.text:
            cable.changecore('multicore')
        self.resistance = str(cable.resistance)

    pass
