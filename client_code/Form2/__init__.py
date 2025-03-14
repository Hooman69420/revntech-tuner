from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Ensure side_menu_card and close_btn are hidden at startup
        self.side_menu_card.visible = True

        if hasattr(self, "close_btn"):  # Check if close_btn exists
            self.close_btn.visible = False  

    def breadcrumbs_button_click(self, **event_args):
        """Toggles the visibility of side_menu_card and close button"""
        is_visible = not self.side_menu_card.visible
        self.side_menu_card.visible = is_visible

        if hasattr(self, "close_btn"):
            self.close_btn.visible = is_visible  

    def close_btn_click(self, **event_args):
        """Closes the side menu card"""
        self.side_menu_card.visible = False
      
        if hasattr(self, "close_btn"):
            self.close_btn.visible = False

    def close_btn(self, **event_args):
          """Button Style"""
          self.close_btn.style["position"] = "absolute"
          self.close_btn.style["top"] = "0"        
          self.close_btn.style["right"] = "0" 