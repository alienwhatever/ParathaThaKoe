#!/usr/bin/python3
import pygame, sys

# import custom modules
from modules.menu import menu
from modules.areana import Areana
from modules.showMessage import showMessage
from modules.creditpage import creditpage

# size of pygame window
size = ([600, 500]) # list wrap into tuple because this value never change
menu_return_value = menu(pygame, sys, size)
if menu_return_value == 'play':  # display menu if user click playButton call areana function(game areana)
    if Areana(pygame, sys, size).areana() == 'showMsg': # display message if user fail
        showMessage(pygame, sys, size)

if menu_return_value == 'Credits': # display credits section by calling creditPage if user click credits button
    creditpage(pygame, sys, size)
