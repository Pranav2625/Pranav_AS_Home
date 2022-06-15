from tkinter import *
from functools import partial  # To prevent unwanted windows
 # import random


class Main_screen:
  def __init__(self, parent):

    # Formatting variables:

    # Main Screen GUI:
    self.main_frame = Frame(width = 600, height = 600, bg = "maroon",  # Both these lines are the features of 
                            pady = 10)                                 # the main window frame
    self.main_frame.grid()

    # Home Screen Heading:
    self.home_scrn_label = Label(self.main_frame, text = "Blackjack",    # Makes the title heading for the window
                                font = ("Italic", "16", "bold"),         # using a specfic font
                                bg = "gold", padx = 200, pady = 10)      # and a label colour
    self.home_scrn_label.grid(row = 0)                                   # and applies it to the interface's grid

    # Single Player button:
    self.sngle_button = Button(self.main_frame, text = "Single Player", font = "arial 10 bold",   # Creates a button for
                              padx = 10, pady = 10, command = self.single_username)               # Single player mode
    self.sngle_button.grid(row = 1, pady = 10)                                      # and puts it onto the grid

    # # Multiplayer Drop-down:
    def two_or_three():
      if variable.get() == "2 Players":                      # If 2 players selected
        two_play()                                           # goto two_play()
      if variable.get() == "3 Players":                      # If 3 players selected
        three_play()                                         # goto three_play()
    variable = StringVar(root)
    variable.set("Multiplayer")
    self.mult_drop = OptionMenu(self.main_frame, variable, "2 Players", "3 Players")     # Create the menu and it's options
    self.mult_drop.grid(row = 2, pady = 5)                                                         # and put it on the grid

    self.confirm_mult = Button(self.main_frame, text = "Confirm", font = "arial 10 bold", command = two_or_three)  # Create the confirm button
    self.confirm_mult.grid(row = 3, pady = 2)                                                        

    def two_play():                                                                          # If two players are selected...
      get_dble_username = Double_Username(self)                                              # goto the Double_Username class
      get_dble_username.dble_usrnme_text.configure(text = "Enter in usernames for the two players") # And make this the heading

    def three_play():
      print("Three players")

  def single_username(self):                                           # When the single player button is pressed
    get_sngle_usrnme = Single_Username(self)                          # Calls on the Single_Username class
    get_sngle_usrnme.sngle_usrnme_text.configure(text = "Enter in a username") # and makes the heading of the window

class Single_Username:
  def __init__(self, partner):

    partner.sngle_button.config(state = DISABLED) # Disables the confirm button when 
                                                 # while this window is open
    
    self.sngle_usrnme_win = Toplevel() # Sets up the window

    self.sngle_usrnme_win.protocol("WM_DELETE_WINDOW", partial(self.close_sngle_usrnme, partner)) # Releases confirm button 
                                                                                               # when window closed
    
    self.sngle_usrnme_frame = Frame(self.sngle_usrnme_win, width = 600, height = 600, bg = "maroon")  # Makes the frame for this window
    self.sngle_usrnme_frame.grid()

    self.sngle_usrnme_text = Label(self.sngle_usrnme_frame, text = "", font = "arial 14 bold", justify = CENTER,  # Adds the heading
                                    width = 40, bg = "orange", wrap = 250)
    self.sngle_usrnme_text.grid(row = 0)

    def prnt_sngle_usrnme():                                    # Carries out defintion if confirm is pushed
      sngle_username = self.sngle_usrnme_entry_box.get()        # Stores the input text from the entry field in this variable as string
      print("Hello", sngle_username)                         # and prints it out
    
    self.sngle_usrnme_entry_box = Entry(self.sngle_usrnme_frame, width = 20, font = "arial 14") # Creates the entry box
    self.sngle_usrnme_entry_box.grid(row = 2, pady = 10)

    self.sngle_usrnme_confirm = Button(self.sngle_usrnme_frame, text = "Confirm", bg = "gold", font = "arial 10 bold", # Creates
                                   command = prnt_sngle_usrnme)                                                     # confirm button
    self.sngle_usrnme_confirm.grid(row = 4, pady = 10)
    
    self.sngle_usrnme_back = Button(self.sngle_usrnme_frame, text = "Back", width = 10, bg = "orange",           # Creates back button
                                 font = "arial 10 bold", command = partial(self.close_sngle_usrnme, partner))
    self.sngle_usrnme_back.grid(row = 6, pady = 10)

  def close_sngle_usrnme(self, partner):             # If either the back button or window is closed
    partner.sngle_button.config(state = NORMAL)   # revert the single player button back to normal
    self.sngle_usrnme_win.destroy()               # and destroy the window


class Double_Username:
  def __init__(self, partner):

    partner.confirm_mult.config(state = DISABLED) # Confirm button disabled while window is open

    self.dble_usrnme_win = Toplevel() # Setsup window

    self.dble_usrnme_win.protocol("WM_DELETE_WINDOW", partial(self.close_dble_usrnme, partner)) # For when users closes tabs with 
                                                                                                # X button

    self.dble_usrnme_frame = Frame(self.dble_usrnme_win, width = 600, height = 600, bg = "maroon") # Frame for the window
    self.dble_usrnme_frame.grid()

    self.dble_usrnme_text = Label(self.dble_usrnme_frame, text = "", font = "arial 14 bold", # Window heading
                                  justify = CENTER, width = 40, bg = "orange", wrap = 250)
    self.dble_usrnme_text.grid(row = 0)

    def prnt_dble_usrnme():                               # When confirmed is pushed...
      dble_username1 = self.dble_usrnme_entry_box1.get()  # Store the usr input in
      dble_username2 = self.dble_usrnme_entry_box2.get()  # these two varibales
      print("Hello", dble_username1, "&", dble_username2) # and print this statement in the terminal
    
    self.dble_usrnme_entry_box1 = Entry(self.dble_usrnme_frame, width = 20, font = "arial 14") # Make two   
    self.dble_usrnme_entry_box1.grid(row = 2, pady = 10)                                       # entry
    self.dble_usrnme_entry_box2 = Entry(self.dble_usrnme_frame, width = 20, font = "arial 14") # boxes
    self.dble_usrnme_entry_box2.grid(row = 3, pady = 5)

    self.dble_usrnme_confirm = Button(self.dble_usrnme_frame, text = "Confirm", bg = "gold", # Confrim button for
                                      font = "arial 10 bold", command = prnt_dble_usrnme)    # username input
    self.dble_usrnme_confirm.grid(row = 4, pady = 10)

    self.dble_usrnme_back = Button(self.dble_usrnme_frame, text = "Back", bg = "orange",   # Back button
                                   font = "arial 10 bold", 
                                   command = partial(self.close_dble_usrnme, partner))
    self.dble_usrnme_back.grid(row = 6, pady = 10)

  def close_dble_usrnme(self, partner):            # If either back or the X button is pushed...
      partner.confirm_mult.config(state = NORMAL)  # revert the multiplayer confirm button back to normal
      self.dble_usrnme_win.destroy()               # and destroy the window
    
# main routine:
if __name__ == "__main__":
  root = Tk()
  root.title("Blackjack Home Screen")  # Name of the windows
  something = Main_screen(root)
  root.mainloop()