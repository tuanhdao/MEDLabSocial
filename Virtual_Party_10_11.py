#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 11, 2022, at 14:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Virtual Party'  # from the Builder filename that created this script
expInfo = {
    'Study ID': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Study ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tuanh\\Dropbox\\Reprogrammed IG\\Virtual_Party_10_6_no_trigger.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
wellcome_image = visual.ImageStim(
    win=win,
    name='wellcome_image', 
    image='images/welcome.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_1 = visual.Rect(
    win=win, name='polygon_1',
    width=(1, 0.25)[0], height=(1, 0.25)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from welcome_bold
welcome_text.bold = 'True'
mouse = event.Mouse()

# --- Initialize components for Routine "Introduction_1" ---
intro_1 = visual.ImageStim(
    win=win,
    name='intro_1', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
intro_text_1 = visual.TextStim(win=win, name='intro_text_1',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
intro_1_key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_2
trialList=data.importConditions('Trials.xlsx')
next_intro_1 = visual.TextStim(win=win, name='next_intro_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Introduction_2" ---
intro_2 = visual.ImageStim(
    win=win,
    name='intro_2', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
intro_key_resp_2 = keyboard.Keyboard()
intro_text_2 = visual.TextStim(win=win, name='intro_text_2',
    text='The game includes 5 rounds where you will learn more and more about the other people playing the game. At the end, there will be a virtual party for the most-liked players. Players who get enough likes across the game \nwill be invited to the party, but people who are less liked will not be included.  First, let’s set up your profile so that the other players can learn about you...\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
next_intro_2 = visual.TextStim(win=win, name='next_intro_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Participant_name" ---
name_question = visual.TextStim(win=win, name='name_question',
    text='What is your name?',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
name_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='name_enter',
     autoLog=True,
)
button_name = visual.Rect(
    win=win, name='button_name',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit_name = visual.TextStim(win=win, name='submit_name',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_name = event.Mouse(win=win)
x, y = [None, None]
mouse_name.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_name
ptp_name = name_enter.text
ptp_nameContainer = []
# Run 'Begin Experiment' code from remove_name
expInfo['name_enter.text']= None

# --- Initialize components for Routine "Participant_age" ---
age_question = visual.TextStim(win=win, name='age_question',
    text='How old are you? ',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
age_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='age_enter',
     autoLog=True,
)
mouse_age = event.Mouse(win=win)
x, y = [None, None]
mouse_age.mouseClock = core.Clock()
button_age = visual.Rect(
    win=win, name='button_age',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
submit_age = visual.TextStim(win=win, name='submit_age',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
reminder = visual.TextStim(win=win, name='reminder',
    text='Please only enter a number.',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Set experiment start values for variable component ptp_age
ptp_age = age_enter.text
ptp_ageContainer = []

# --- Initialize components for Routine "Participant_hometown" ---
hometown_question = visual.TextStim(win=win, name='hometown_question',
    text='What is your hometown?',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
hometown_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='hometown_enter',
     autoLog=True,
)
mouse_home = event.Mouse(win=win)
x, y = [None, None]
mouse_home.mouseClock = core.Clock()
button_home = visual.Rect(
    win=win, name='button_home',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
submit_home = visual.TextStim(win=win, name='submit_home',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
# Set experiment start values for variable component ptp_hometown
ptp_hometown = hometown_enter.text
ptp_hometownContainer = []

# --- Initialize components for Routine "Participant_interest" ---
interest_question = visual.TextStim(win=win, name='interest_question',
    text='What are some things you are interested in?',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
interest_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='interest_enter',
     autoLog=True,
)
mouse_interest = event.Mouse(win=win)
x, y = [None, None]
mouse_interest.mouseClock = core.Clock()
button_interest = visual.Rect(
    win=win, name='button_interest',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
submit_interest = visual.TextStim(win=win, name='submit_interest',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
# Set experiment start values for variable component ptp_interest
ptp_interest = interest_enter.text
ptp_interestContainer = []

# --- Initialize components for Routine "Participant_school" ---
school_question = visual.TextStim(win=win, name='school_question',
    text='What school do you go to?',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
school_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='school_enter',
     autoLog=True,
)
mouse_school = event.Mouse(win=win)
x, y = [None, None]
mouse_school.mouseClock = core.Clock()
button_school = visual.Rect(
    win=win, name='button_school',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
submit_school = visual.TextStim(win=win, name='submit_school',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
# Set experiment start values for variable component ptp_school
ptp_school = school_enter.text
ptp_schoolContainer = []

# --- Initialize components for Routine "Participant_profile" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
background_profile = visual.Rect(
    win=win, name='background_profile',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border = visual.Rect(
    win=win, name='border',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(-0.5, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
subject_image = visual.ImageStim(
    win=win,
    name='subject_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.15), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
part_response = visual.TextStim(win=win, name='part_response',
    text='',
    font='Open Sans',
    pos=(0.1, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
part_prompts = visual.TextStim(win=win, name='part_prompts',
    text='Age:\nHometown:\nInterests:\nSchool:',
    font='Arial',
    pos=(-0.11, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
part_name = visual.TextStim(win=win, name='part_name',
    text='',
    font='Arial',
    pos=(-0.11, -0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
next = keyboard.Keyboard()
next_text = visual.TextStim(win=win, name='next_text',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "Waiting" ---
wait_1 = visual.ImageStim(
    win=win,
    name='wait_1', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_wait = visual.Rect(
    win=win, name='polygon_wait',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
wait_text_1 = visual.TextStim(win=win, name='wait_text_1',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
load_1 = visual.ImageStim(
    win=win,
    name='load_1', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Introduction_3" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_intro_3 = visual.Rect(
    win=win, name='polygon_intro_3',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
intro_text_3 = visual.TextStim(win=win, name='intro_text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
intro_key_resp_3 = keyboard.Keyboard()
next_intro_3 = visual.TextStim(win=win, name='next_intro_3',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Coplayer_profile_loader" ---
# Run 'Begin Experiment' code from cop_info_loader
# empty lists to hold stimuli
names = []
ages = []
hometowns = []
interests = []
photos = []
votes = []
schools = []


# --- Initialize components for Routine "Coplayer_profile_shuffler" ---

# --- Initialize components for Routine "Coplayer_profiles" ---
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_coplayer = visual.Rect(
    win=win, name='polygon_coplayer',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_coplayer = visual.Rect(
    win=win, name='border_coplayer',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(-0.5, 0.15), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
# Run 'Begin Experiment' code from code_cop_profile
cop_age_st = str()

curr_item = -1
cop_img = visual.ImageStim(
    win=win,
    name='cop_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.15), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
cop_resp_show = visual.TextStim(win=win, name='cop_resp_show',
    text='',
    font='Arial',
    pos=(0.1, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
cop_prompts_show = visual.TextStim(win=win, name='cop_prompts_show',
    text='',
    font='Arial',
    pos=(-0.11, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
cop_vote_show = visual.TextStim(win=win, name='cop_vote_show',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color=[0.0000, 0.0000, 0.0000], colorSpace='rgb', opacity=0.0, 
    languageStyle='LTR',
    depth=-7.0);
cop_name_show = visual.TextStim(win=win, name='cop_name_show',
    text='',
    font='Arial',
    pos=(-0.11, -0.04), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_cop_profile = keyboard.Keyboard()
next_text_cop_profile = visual.TextStim(win=win, name='next_text_cop_profile',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Vote_store" ---

# --- Initialize components for Routine "Introduction_4" ---
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_intro_4 = visual.Rect(
    win=win, name='polygon_intro_4',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
intro_text_4 = visual.TextStim(win=win, name='intro_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()
next_intro_4 = visual.TextStim(win=win, name='next_intro_4',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Introduction_5" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_intro_5 = visual.Rect(
    win=win, name='polygon_intro_5',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()
thumbs_up = visual.ImageStim(
    win=win,
    name='thumbs_up', 
    image='images/Like.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
thumbs_down = visual.ImageStim(
    win=win,
    name='thumbs_down', 
    image='images/dislike.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
feedback_like = visual.TextStim(win=win, name='feedback_like',
    text='Great news!\nThis means the person liked you.',
    font='Arial',
    pos=(-.29, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
feedback_dislike = visual.TextStim(win=win, name='feedback_dislike',
    text='Oh no!\nThis means the person disliked you.',
    font='Arial',
    pos=(.29, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
next_3 = visual.TextStim(win=win, name='next_3',
    text='Press space to continue. ',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "Introduction_6" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_intro_6 = visual.Rect(
    win=win, name='polygon_intro_6',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_10 = keyboard.Keyboard()
next_intro6 = visual.TextStim(win=win, name='next_intro6',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Practice_1a" ---
prac_image_1 = visual.ImageStim(
    win=win,
    name='prac_image_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
like_prac_button_1 = visual.Rect(
    win=win, name='like_prac_button_1',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
like_prac_text_1 = visual.TextStim(win=win, name='like_prac_text_1',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
dislike_prac_button_1 = visual.Rect(
    win=win, name='dislike_prac_button_1',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
dislike_prac_text_1 = visual.TextStim(win=win, name='dislike_prac_text_1',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
player_1 = visual.TextStim(win=win, name='player_1',
    text='',
    font='Arial',
    pos=(-0.2, 0.34), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
click_prac_1 = event.Mouse(win=win)
x, y = [None, None]
click_prac_1.mouseClock = core.Clock()
vote_question_2 = visual.TextStim(win=win, name='vote_question_2',
    text='Do you like or dislike Player 1? ',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "Practice_1b" ---
wait = visual.TextStim(win=win, name='wait',
    text='Compiling votes, your feedback\nwill be presented soon...',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_3 = visual.ImageStim(
    win=win,
    name='load_white1_3', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_prac_1 = visual.TextStim(win=win, name='fixation_prac_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Practice_1c" ---
like_prac = visual.ImageStim(
    win=win,
    name='like_prac', 
    image='images/thumb-up.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Practice_1d" ---
wait_2 = visual.TextStim(win=win, name='wait_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Practice_2a" ---
prac_image_2 = visual.ImageStim(
    win=win,
    name='prac_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
like_prac_button_2 = visual.Rect(
    win=win, name='like_prac_button_2',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
like_prac_text_2 = visual.TextStim(win=win, name='like_prac_text_2',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
dislike_prac_button_2 = visual.Rect(
    win=win, name='dislike_prac_button_2',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
dislike_prac_text_2 = visual.TextStim(win=win, name='dislike_prac_text_2',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
player_2 = visual.TextStim(win=win, name='player_2',
    text='',
    font='Arial',
    pos=(-0.2, 0.34), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
click_prac_2 = event.Mouse(win=win)
x, y = [None, None]
click_prac_2.mouseClock = core.Clock()
vote_question = visual.TextStim(win=win, name='vote_question',
    text='Do you like or dislike Player 2? ',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "Practice_2b" ---
wait_3 = visual.TextStim(win=win, name='wait_3',
    text='Compiling votes, your feedback\nwill be presented soon...',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_4 = visual.ImageStim(
    win=win,
    name='load_white1_4', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_prac_2 = visual.TextStim(win=win, name='fixation_prac_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Practice_2c" ---
dislike_prac = visual.ImageStim(
    win=win,
    name='dislike_prac', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Practice_2d" ---
wait_4 = visual.TextStim(win=win, name='wait_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Introduction_7" ---
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_9 = visual.Rect(
    win=win, name='polygon_9',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_9 = keyboard.Keyboard()
next_intro7 = visual.TextStim(win=win, name='next_intro7',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Player_profiles_voting_style" ---
border_2 = visual.Rect(
    win=win, name='border_2',
    width=(0.21, 0.31)[0], height=(0.21, 0.31)[1],
    ori=0.0, pos=(-0.4, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
coplayer_image_2 = visual.ImageStim(
    win=win,
    name='coplayer_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cop_prompts = visual.TextBox2(
     win, text='Name:\nAge:\nHometown:\nInterests:\nSchool:', font='Arial',
     pos=(-0.15, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cop_prompts',
     autoLog=True,
)
cop_response = visual.TextStim(win=win, name='cop_response',
    text='',
    font='Arial',
    pos=(0.45, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
# Run 'Begin Experiment' code from capitalization_cop
cop_age_st = str()

# set a to -1
a = -1
like_real_button_1 = visual.Rect(
    win=win, name='like_real_button_1',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
like_real_text_1 = visual.TextStim(win=win, name='like_real_text_1',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
dislike_real_button_1 = visual.Rect(
    win=win, name='dislike_real_button_1',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
dislike_real_text_1 = visual.TextStim(win=win, name='dislike_real_text_1',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
click_real_1 = event.Mouse(win=win)
x, y = [None, None]
click_real_1.mouseClock = core.Clock()
vote_question_3 = visual.TextStim(win=win, name='vote_question_3',
    text='',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Waiting_vote" ---
wait_5 = visual.TextStim(win=win, name='wait_5',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1 = visual.ImageStim(
    win=win,
    name='load_white1', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_r_1 = visual.TextStim(win=win, name='fixation_r_1',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Cop_vote" ---
# Run 'Begin Experiment' code from code_thumb
save_vote = ''
play_round = ''
vote_image = visual.ImageStim(
    win=win,
    name='vote_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Waiting_vote_3" ---
wait_7 = visual.TextStim(win=win, name='wait_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Waiting_3" ---
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Most_vote_1" ---
most_pic_1 = visual.ImageStim(
    win=win,
    name='most_pic_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_8 = visual.Rect(
    win=win, name='border_8',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_9 = visual.Rect(
    win=win, name='border_9',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
most_vote_1 = visual.ImageStim(
    win=win,
    name='most_vote_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_most_1 = visual.TextStim(win=win, name='name_most_1',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_most_1 = visual.TextStim(win=win, name='next_most_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_most1 = keyboard.Keyboard()
# Run 'Begin Experiment' code from most_votes_code
name_most_1.bold = 'True'
name_most_1.text.upper()
next_most_1.bold = 'True'

# create random index numbers for most/least player
most_least_index = []
for n in range(0, 11):
   most_least_index.append(n)
  
shuffle(most_least_index)
m = most_least_index[0]
l = most_least_index[1]
    
    
    

# --- Initialize components for Routine "Waiting_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Least_vote_1" ---
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border4_4 = visual.Rect(
    win=win, name='border4_4',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_6 = visual.Rect(
    win=win, name='border_6',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
least_vote_1 = visual.ImageStim(
    win=win,
    name='least_vote_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_least_1 = visual.TextStim(win=win, name='name_least_1',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_least_1 = visual.TextStim(win=win, name='next_least_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_least1 = keyboard.Keyboard()
# Run 'Begin Experiment' code from least_code_1
name_least_1.bold = 'True'
next_least_1.bold = 'True'

# --- Initialize components for Routine "round_1" ---
image_36 = visual.ImageStim(
    win=win,
    name='image_36', 
    image='images/round1.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_24 = visual.Rect(
    win=win, name='polygon_24',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_27 = visual.TextStim(win=win, name='text_27',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_23 = keyboard.Keyboard()
next_intro3_4 = visual.TextStim(win=win, name='next_intro3_4',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Poll_loader" ---
# Run 'Begin Experiment' code from code_poll_loader
poll_1 = []
poll_2 = []
poll_3 = []
poll_4 = []

# --- Initialize components for Routine "Introduction_9" ---
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_15 = visual.Rect(
    win=win, name='polygon_15',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_15 = visual.TextStim(win=win, name='text_15',
    text='It’s time to learn more about the players in this game.\nEveryone will be asked a poll question and see each other’s responses.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
next_intro7_6 = visual.TextStim(win=win, name='next_intro7_6',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_17 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_19
next_intro7_6.bold = 'True'

# --- Initialize components for Routine "Poll_q1" ---
poll_question_1 = visual.TextStim(win=win, name='poll_question_1',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
poll_enter_1 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='poll_enter_1',
     autoLog=True,
)
button5 = visual.Rect(
    win=win, name='button5',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit5 = visual.TextStim(win=win, name='submit5',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse5 = event.Mouse(win=win)
x, y = [None, None]
mouse5.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_poll_1
ptp_poll_1 = poll_enter_1.text
ptp_poll_1Container = []

# --- Initialize components for Routine "Waiting_5" ---
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Introduction_10" ---
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_18 = keyboard.Keyboard()
next_intro3_2 = visual.TextStim(win=win, name='next_intro3_2',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "poll_resp_1_1" ---
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_11 = visual.Rect(
    win=win, name='polygon_11',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_11 = keyboard.Keyboard()
poll_next_1_1 = visual.TextStim(win=win, name='poll_next_1_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_1_1_names = visual.TextStim(win=win, name='poll_1_1_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_1_1_responses = visual.TextStim(win=win, name='poll_1_1_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_1
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "poll_resp_1_2" ---
image_42 = visual.ImageStim(
    win=win,
    name='image_42', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_30 = visual.Rect(
    win=win, name='polygon_30',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_29 = keyboard.Keyboard()
poll_next_1_2 = visual.TextStim(win=win, name='poll_next_1_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_1_2_names = visual.TextStim(win=win, name='poll_1_2_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_1_2_responses = visual.TextStim(win=win, name='poll_1_2_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_5
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "Introduction_11" ---
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_19 = keyboard.Keyboard()
next_intro3_3 = visual.TextStim(win=win, name='next_intro3_3',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Player_profiles_voting_style_2" ---
border_4 = visual.Rect(
    win=win, name='border_4',
    width=(0.21, 0.31)[0], height=(0.21, 0.31)[1],
    ori=0.0, pos=(-0.4, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from capitalization_cop_2
cop_age_st = str()

# set b to -1
b = -1
coplayer_image = visual.ImageStim(
    win=win,
    name='coplayer_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cop_prompts_2 = visual.TextBox2(
     win, text='Name:\nAge:\nHometown:\nInterests:\nSchool:', font='Arial',
     pos=(-0.15, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cop_prompts_2',
     autoLog=True,
)
cop_response_2 = visual.TextStim(win=win, name='cop_response_2',
    text='',
    font='Arial',
    pos=(0.45, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
like_real_button_2 = visual.Rect(
    win=win, name='like_real_button_2',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
like_real_text_2 = visual.TextStim(win=win, name='like_real_text_2',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
dislike_real_button_2 = visual.Rect(
    win=win, name='dislike_real_button_2',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
dislike_real_text_2 = visual.TextStim(win=win, name='dislike_real_text_2',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
click_real_2 = event.Mouse(win=win)
x, y = [None, None]
click_real_2.mouseClock = core.Clock()
vote_question_4 = visual.TextStim(win=win, name='vote_question_4',
    text='',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Waiting_vote_2" ---
wait_6 = visual.TextStim(win=win, name='wait_6',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_2 = visual.ImageStim(
    win=win,
    name='load_white1_2', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_r_2 = visual.TextStim(win=win, name='fixation_r_2',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Cop_vote_2" ---
vote_image_second = visual.ImageStim(
    win=win,
    name='vote_image_second', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Waiting_vote_3" ---
wait_7 = visual.TextStim(win=win, name='wait_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Waiting_3" ---
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Most_vote_2" ---
most_pic = visual.ImageStim(
    win=win,
    name='most_pic', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_14 = visual.Rect(
    win=win, name='border_14',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_15 = visual.Rect(
    win=win, name='border_15',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
most_vote_2 = visual.ImageStim(
    win=win,
    name='most_vote_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_most_2 = visual.TextStim(win=win, name='name_most_2',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_most_2 = visual.TextStim(win=win, name='next_most_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_most2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from most_votes_2
name_most_2.bold = 'True'
name_most_2.text.upper()
next_most_2.bold = 'True'

# --- Initialize components for Routine "Waiting_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Least_vote_2" ---
image_30 = visual.ImageStim(
    win=win,
    name='image_30', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border4_5 = visual.Rect(
    win=win, name='border4_5',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_13 = visual.Rect(
    win=win, name='border_13',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
least_vote_2 = visual.ImageStim(
    win=win,
    name='least_vote_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_least_2 = visual.TextStim(win=win, name='name_least_2',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_least_2 = visual.TextStim(win=win, name='next_least_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_least2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from least_votes_2
name_least_2.bold = 'True'
next_least_2.bold = 'True'

# --- Initialize components for Routine "round_2" ---
image_37 = visual.ImageStim(
    win=win,
    name='image_37', 
    image='images/round2.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_25 = visual.Rect(
    win=win, name='polygon_25',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_28 = visual.TextStim(win=win, name='text_28',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_24 = keyboard.Keyboard()
next_intro3_5 = visual.TextStim(win=win, name='next_intro3_5',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Introduction_12" ---
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_19 = visual.Rect(
    win=win, name='polygon_19',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_18 = visual.TextStim(win=win, name='text_18',
    text="Let's learn more about the players.\nEveryone will answer the next poll question and see each other’s responses.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
next_intro7_7 = visual.TextStim(win=win, name='next_intro7_7',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_20 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_22
next_intro7_7.bold = 'True'

# --- Initialize components for Routine "Poll_q2" ---
poll_question_2 = visual.TextStim(win=win, name='poll_question_2',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
poll_enter_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='poll_enter_2',
     autoLog=True,
)
button5_2 = visual.Rect(
    win=win, name='button5_2',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit5_2 = visual.TextStim(win=win, name='submit5_2',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse5_2 = event.Mouse(win=win)
x, y = [None, None]
mouse5_2.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_poll_2
ptp_poll_2 = poll_enter_2.text
ptp_poll_2Container = []

# --- Initialize components for Routine "Waiting_5" ---
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Introduction_10" ---
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_18 = keyboard.Keyboard()
next_intro3_2 = visual.TextStim(win=win, name='next_intro3_2',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "poll_resp_2_1" ---
image_43 = visual.ImageStim(
    win=win,
    name='image_43', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp = keyboard.Keyboard()
poll_next_2_1 = visual.TextStim(win=win, name='poll_next_2_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_2_1_names = visual.TextStim(win=win, name='poll_2_1_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_2_1_responses = visual.TextStim(win=win, name='poll_2_1_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "poll_resp_2_2" ---
image_44 = visual.ImageStim(
    win=win,
    name='image_44', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_31 = visual.Rect(
    win=win, name='polygon_31',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_30 = keyboard.Keyboard()
poll_next_2_2 = visual.TextStim(win=win, name='poll_next_2_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_2_2_names = visual.TextStim(win=win, name='poll_2_2_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_2_2_responses = visual.TextStim(win=win, name='poll_2_2_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_6
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "Introduction_11" ---
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_19 = keyboard.Keyboard()
next_intro3_3 = visual.TextStim(win=win, name='next_intro3_3',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Player_profiles_voting_style_3" ---
border_10 = visual.Rect(
    win=win, name='border_10',
    width=(0.21, 0.31)[0], height=(0.21, 0.31)[1],
    ori=0.0, pos=(-0.4, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from capitalization_cop_3
cop_age_st = str()

# set c to -1
c = -1
coplayer_image_3 = visual.ImageStim(
    win=win,
    name='coplayer_image_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cop_prompts_3 = visual.TextBox2(
     win, text='Name:\nAge:\nHometown:\nInterests:\nSchool:', font='Arial',
     pos=(-0.15, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cop_prompts_3',
     autoLog=True,
)
cop_response_3 = visual.TextStim(win=win, name='cop_response_3',
    text='',
    font='Arial',
    pos=(0.45, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
like_real_button_3 = visual.Rect(
    win=win, name='like_real_button_3',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
like_real_text_3 = visual.TextStim(win=win, name='like_real_text_3',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
dislike_real_button_3 = visual.Rect(
    win=win, name='dislike_real_button_3',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
dislike_real_text_3 = visual.TextStim(win=win, name='dislike_real_text_3',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
click_real_3 = event.Mouse(win=win)
x, y = [None, None]
click_real_3.mouseClock = core.Clock()
vote_question_5 = visual.TextStim(win=win, name='vote_question_5',
    text='',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Waiting_vote_2" ---
wait_6 = visual.TextStim(win=win, name='wait_6',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_2 = visual.ImageStim(
    win=win,
    name='load_white1_2', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_r_2 = visual.TextStim(win=win, name='fixation_r_2',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Cop_vote_3" ---
vote_image_third = visual.ImageStim(
    win=win,
    name='vote_image_third', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Waiting_vote_3" ---
wait_7 = visual.TextStim(win=win, name='wait_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Waiting_3" ---
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Most_vote_3" ---
most_pic_2 = visual.ImageStim(
    win=win,
    name='most_pic_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_16 = visual.Rect(
    win=win, name='border_16',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_17 = visual.Rect(
    win=win, name='border_17',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
most_vote_3 = visual.ImageStim(
    win=win,
    name='most_vote_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_most_3 = visual.TextStim(win=win, name='name_most_3',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_most_3 = visual.TextStim(win=win, name='next_most_3',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_most3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from most_votes_3
name_most_3.bold = 'True'
name_most_3.text.upper()
next_most_3.bold = 'True'


    
    

# --- Initialize components for Routine "Waiting_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Least_vote_3" ---
image_31 = visual.ImageStim(
    win=win,
    name='image_31', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border4_6 = visual.Rect(
    win=win, name='border4_6',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_18 = visual.Rect(
    win=win, name='border_18',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
least_vote_3 = visual.ImageStim(
    win=win,
    name='least_vote_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_least_3 = visual.TextStim(win=win, name='name_least_3',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_least_3 = visual.TextStim(win=win, name='next_least_3',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_least3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from least_votes_3
name_least_3.bold = 'True'
next_least_3.bold = 'True'

# --- Initialize components for Routine "round_3" ---
image_38 = visual.ImageStim(
    win=win,
    name='image_38', 
    image='images/round3.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_26 = visual.Rect(
    win=win, name='polygon_26',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_29 = visual.TextStim(win=win, name='text_29',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_25 = keyboard.Keyboard()
next_intro3_6 = visual.TextStim(win=win, name='next_intro3_6',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Introduction_12" ---
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_19 = visual.Rect(
    win=win, name='polygon_19',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_18 = visual.TextStim(win=win, name='text_18',
    text="Let's learn more about the players.\nEveryone will answer the next poll question and see each other’s responses.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
next_intro7_7 = visual.TextStim(win=win, name='next_intro7_7',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_20 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_22
next_intro7_7.bold = 'True'

# --- Initialize components for Routine "Poll_q3" ---
poll_question_3 = visual.TextStim(win=win, name='poll_question_3',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
poll_enter_3 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='poll_enter_3',
     autoLog=True,
)
button5_3 = visual.Rect(
    win=win, name='button5_3',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit5_3 = visual.TextStim(win=win, name='submit5_3',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse5_3 = event.Mouse(win=win)
x, y = [None, None]
mouse5_3.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_poll_3
ptp_poll_3 = poll_enter_3.text
ptp_poll_3Container = []

# --- Initialize components for Routine "Waiting_5" ---
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Introduction_10" ---
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_18 = keyboard.Keyboard()
next_intro3_2 = visual.TextStim(win=win, name='next_intro3_2',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "poll_resp_3_1" ---
image_46 = visual.ImageStim(
    win=win,
    name='image_46', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_3 = keyboard.Keyboard()
poll_next_3_1 = visual.TextStim(win=win, name='poll_next_3_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_3_1_names = visual.TextStim(win=win, name='poll_3_1_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_3_1_responses = visual.TextStim(win=win, name='poll_3_1_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_8
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "pol_resp_3_2" ---
image_45 = visual.ImageStim(
    win=win,
    name='image_45', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_32 = visual.Rect(
    win=win, name='polygon_32',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_31 = keyboard.Keyboard()
poll_next_3_2 = visual.TextStim(win=win, name='poll_next_3_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_3_2_names = visual.TextStim(win=win, name='poll_3_2_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_3_2_responses = visual.TextStim(win=win, name='poll_3_2_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_7
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "Introduction_11" ---
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_19 = keyboard.Keyboard()
next_intro3_3 = visual.TextStim(win=win, name='next_intro3_3',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Player_profiles_voting_style_4" ---
border_11 = visual.Rect(
    win=win, name='border_11',
    width=(0.21, 0.31)[0], height=(0.21, 0.31)[1],
    ori=0.0, pos=(-0.4, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from capitalization_cop_4
cop_age_st = str()

# set d to -1
d = -1
coplayer_image_4 = visual.ImageStim(
    win=win,
    name='coplayer_image_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cop_prompts_4 = visual.TextBox2(
     win, text='Name:\nAge:\nHometown:\nInterests:\nSchool:', font='Arial',
     pos=(-0.15, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cop_prompts_4',
     autoLog=True,
)
cop_response_4 = visual.TextStim(win=win, name='cop_response_4',
    text='',
    font='Arial',
    pos=(0.45, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
like_real_button_4 = visual.Rect(
    win=win, name='like_real_button_4',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
like_real_text_4 = visual.TextStim(win=win, name='like_real_text_4',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
dislike_real_button_4 = visual.Rect(
    win=win, name='dislike_real_button_4',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
dislike_real_text_4 = visual.TextStim(win=win, name='dislike_real_text_4',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
click_real_4 = event.Mouse(win=win)
x, y = [None, None]
click_real_4.mouseClock = core.Clock()
vote_question_6 = visual.TextStim(win=win, name='vote_question_6',
    text='',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Waiting_vote_2" ---
wait_6 = visual.TextStim(win=win, name='wait_6',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_2 = visual.ImageStim(
    win=win,
    name='load_white1_2', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_r_2 = visual.TextStim(win=win, name='fixation_r_2',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Cop_vote_4" ---
vote_image_4 = visual.ImageStim(
    win=win,
    name='vote_image_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Waiting_vote_3" ---
wait_7 = visual.TextStim(win=win, name='wait_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Waiting_3" ---
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Most_vote_4" ---
most_pic_3 = visual.ImageStim(
    win=win,
    name='most_pic_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_20 = visual.Rect(
    win=win, name='border_20',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_21 = visual.Rect(
    win=win, name='border_21',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
most_vote_4 = visual.ImageStim(
    win=win,
    name='most_vote_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_most_4 = visual.TextStim(win=win, name='name_most_4',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_most_4 = visual.TextStim(win=win, name='next_most_4',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_most4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from most_votes_4
name_most_4.bold = 'True'
name_most_4.text.upper()
next_most_4.bold = 'True'


    

# --- Initialize components for Routine "Waiting_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Least_vote_4" ---
image_32 = visual.ImageStim(
    win=win,
    name='image_32', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border4_7 = visual.Rect(
    win=win, name='border4_7',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_19 = visual.Rect(
    win=win, name='border_19',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
least_vote_4 = visual.ImageStim(
    win=win,
    name='least_vote_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_least_4 = visual.TextStim(win=win, name='name_least_4',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_least_4 = visual.TextStim(win=win, name='next_least_4',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_least4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from least_votes_4
name_least_4.bold = 'True'
next_least_4.bold = 'True'

# --- Initialize components for Routine "round_4" ---
image_39 = visual.ImageStim(
    win=win,
    name='image_39', 
    image='images/round4.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_27 = visual.Rect(
    win=win, name='polygon_27',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_30 = visual.TextStim(win=win, name='text_30',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_26 = keyboard.Keyboard()
next_intro3_7 = visual.TextStim(win=win, name='next_intro3_7',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Introduction_12" ---
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_19 = visual.Rect(
    win=win, name='polygon_19',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_18 = visual.TextStim(win=win, name='text_18',
    text="Let's learn more about the players.\nEveryone will answer the next poll question and see each other’s responses.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
next_intro7_7 = visual.TextStim(win=win, name='next_intro7_7',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_20 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_22
next_intro7_7.bold = 'True'

# --- Initialize components for Routine "Poll_q4" ---
poll_question_4 = visual.TextStim(win=win, name='poll_question_4',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
poll_enter_4 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='poll_enter_4',
     autoLog=True,
)
button5_4 = visual.Rect(
    win=win, name='button5_4',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit5_4 = visual.TextStim(win=win, name='submit5_4',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse5_4 = event.Mouse(win=win)
x, y = [None, None]
mouse5_4.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_poll_4
ptp_poll_4 = poll_enter_4.text
ptp_poll_4Container = []

# --- Initialize components for Routine "Waiting_5" ---
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Introduction_10" ---
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_18 = keyboard.Keyboard()
next_intro3_2 = visual.TextStim(win=win, name='next_intro3_2',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "poll_resp_4_1" ---
image_47 = visual.ImageStim(
    win=win,
    name='image_47', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_6 = keyboard.Keyboard()
poll_next_4_1 = visual.TextStim(win=win, name='poll_next_4_1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_4_1_names = visual.TextStim(win=win, name='poll_4_1_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_4_1_responses = visual.TextStim(win=win, name='poll_4_1_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_9
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "pol_resp_4_2" ---
image_48 = visual.ImageStim(
    win=win,
    name='image_48', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_33 = visual.Rect(
    win=win, name='polygon_33',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
key_resp_32 = keyboard.Keyboard()
poll_next_4_2 = visual.TextStim(win=win, name='poll_next_4_2',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
poll_4_2_names = visual.TextStim(win=win, name='poll_4_2_names',
    text='',
    font='Arial',
    pos=(-0.15, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
poll_4_2_responses = visual.TextStim(win=win, name='poll_4_2_responses',
    text='',
    font='Arial',
    pos=(0.05, 0.025), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
# Run 'Begin Experiment' code from poll_code_10
trialList=data.importConditions('Trials.xlsx')

# --- Initialize components for Routine "Introduction_11" ---
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_19 = keyboard.Keyboard()
next_intro3_3 = visual.TextStim(win=win, name='next_intro3_3',
    text='',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Player_profiles_voting_style_5" ---
border_12 = visual.Rect(
    win=win, name='border_12',
    width=(0.21, 0.31)[0], height=(0.21, 0.31)[1],
    ori=0.0, pos=(-0.4, 0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from capitalization_cop_5
cop_age_st = str()

# set e to -1
e = -1
coplayer_image_5 = visual.ImageStim(
    win=win,
    name='coplayer_image_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.2), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cop_prompts_5 = visual.TextBox2(
     win, text='Name:\nAge:\nHometown:\nInterests:\nSchool:', font='Arial',
     pos=(-0.15, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cop_prompts_5',
     autoLog=True,
)
cop_response_5 = visual.TextStim(win=win, name='cop_response_5',
    text='',
    font='Arial',
    pos=(0.45, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
like_real_button_5 = visual.Rect(
    win=win, name='like_real_button_5',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(-0.4, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
like_real_text_5 = visual.TextStim(win=win, name='like_real_text_5',
    text='Like ',
    font='Arial',
    pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
dislike_real_button_5 = visual.Rect(
    win=win, name='dislike_real_button_5',
    width=(0.21, 0.07)[0], height=(0.21, 0.07)[1],
    ori=0.0, pos=(0.39, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
dislike_real_text_5 = visual.TextStim(win=win, name='dislike_real_text_5',
    text='Dislike ',
    font='Arial',
    pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
click_real_5 = event.Mouse(win=win)
x, y = [None, None]
click_real_5.mouseClock = core.Clock()
vote_question_7 = visual.TextStim(win=win, name='vote_question_7',
    text='',
    font='Open Sans',
    pos=(0, -.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "Waiting_vote_2" ---
wait_6 = visual.TextStim(win=win, name='wait_6',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
load_white1_2 = visual.ImageStim(
    win=win,
    name='load_white1_2', 
    image='images/load_white.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation_r_2 = visual.TextStim(win=win, name='fixation_r_2',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Cop_vote_5" ---
vote_image_5 = visual.ImageStim(
    win=win,
    name='vote_image_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Waiting_vote_3" ---
wait_7 = visual.TextStim(win=win, name='wait_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Waiting_3" ---
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_12 = visual.Rect(
    win=win, name='polygon_12',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Most_vote_5" ---
most_pic_4 = visual.ImageStim(
    win=win,
    name='most_pic_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_22 = visual.Rect(
    win=win, name='border_22',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_23 = visual.Rect(
    win=win, name='border_23',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
most_vote_5 = visual.ImageStim(
    win=win,
    name='most_vote_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_most_5 = visual.TextStim(win=win, name='name_most_5',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_most_5 = visual.TextStim(win=win, name='next_most_5',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_most5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from most_votes_5
name_most_5.bold = 'True'
name_most_5.text.upper()
next_most_5.bold = 'True'


# --- Initialize components for Routine "Waiting_4" ---
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='images/background_gen.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Least_vote_5" ---
image_33 = visual.ImageStim(
    win=win,
    name='image_33', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border4_8 = visual.Rect(
    win=win, name='border4_8',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_24 = visual.Rect(
    win=win, name='border_24',
    width=(0.22, 0.32)[0], height=(0.22, 0.32)[1],
    ori=0.0, pos=(0, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
least_vote_5 = visual.ImageStim(
    win=win,
    name='least_vote_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
name_least_5 = visual.TextStim(win=win, name='name_least_5',
    text='',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
next_least_5 = visual.TextStim(win=win, name='next_least_5',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_least5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from least_votes_5
name_least_5.bold = 'True'
next_least_5.bold = 'True'

# --- Initialize components for Routine "Waiting_6" ---
image_34 = visual.ImageStim(
    win=win,
    name='image_34', 
    image='images/round5.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
polygon_23 = visual.Rect(
    win=win, name='polygon_23',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.8, depth=-1.0, interpolate=True)
text_19 = visual.TextStim(win=win, name='text_19',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_15 = keyboard.Keyboard()
image_35 = visual.ImageStim(
    win=win,
    name='image_35', 
    image='images/load-icon-png-7945.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "Result" ---
party_pic = visual.ImageStim(
    win=win,
    name='party_pic', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_25 = visual.Rect(
    win=win, name='border_25',
    width=(1.5, 0.75)[0], height=(1.5, 0.75)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.9, depth=-1.0, interpolate=True)
border_26 = visual.Rect(
    win=win, name='border_26',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
winner_1 = visual.ImageStim(
    win=win,
    name='winner_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
winner_n1 = visual.TextStim(win=win, name='winner_n1',
    text='',
    font='Arial',
    pos=(-0.5, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
winner_n2 = visual.TextStim(win=win, name='winner_n2',
    text='',
    font='Arial',
    pos=(-0.3, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
winner_n3 = visual.TextStim(win=win, name='winner_n3',
    text='',
    font='Arial',
    pos=(-0.1, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
winner_n4 = visual.TextStim(win=win, name='winner_n4',
    text='',
    font='Arial',
    pos=(0.1, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
winner_n5 = visual.TextStim(win=win, name='winner_n5',
    text='',
    font='Arial',
    pos=(0.3, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
winner_n6 = visual.TextStim(win=win, name='winner_n6',
    text='',
    font='Arial',
    pos=(0.5, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
next_result1 = visual.TextStim(win=win, name='next_result1',
    text='Press space to continue.',
    font='Arial',
    pos=(0, -0.30), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
next_result = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_31
next_result1.bold = 'True'
winner_n1.bold = 'True'
winner_n2.bold = 'True'
winner_n3.bold = 'True'
winner_n4.bold = 'True'
winner_n5.bold = 'True'
winner_n6.bold = 'True'
    
border_27 = visual.Rect(
    win=win, name='border_27',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(-0.3, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-13.0, interpolate=True)
winner_2 = visual.ImageStim(
    win=win,
    name='winner_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
border_28 = visual.Rect(
    win=win, name='border_28',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(-0.1, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-15.0, interpolate=True)
winner_3 = visual.ImageStim(
    win=win,
    name='winner_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.1, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
border_29 = visual.Rect(
    win=win, name='border_29',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(0.1, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-17.0, interpolate=True)
winner_4 = visual.ImageStim(
    win=win,
    name='winner_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.1, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
border_30 = visual.Rect(
    win=win, name='border_30',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(0.3, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-19.0, interpolate=True)
winner_5 = visual.ImageStim(
    win=win,
    name='winner_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
border_31 = visual.Rect(
    win=win, name='border_31',
    width=(0.19, 0.28)[0], height=(0.19, 0.28)[1],
    ori=0.0, pos=(0.5, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-21.0, interpolate=True)
winner_6 = visual.ImageStim(
    win=win,
    name='winner_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.5, 0.1), size=(0.18, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
text_24 = visual.TextStim(win=win, name='text_24',
    text='CONGRATULATIONS!  You are invited!',
    font='Arial',
    pos=(0, -0.19), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
# Run 'Begin Experiment' code from code_14
text_24.bold = 'True'

# --- Initialize components for Routine "Chat" ---
chat_q = visual.TextStim(win=win, name='chat_q',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
chat_enter = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='chat_enter',
     autoLog=True,
)
button5_5 = visual.Rect(
    win=win, name='button5_5',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0, -0.2), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
submit5_5 = visual.TextStim(win=win, name='submit5_5',
    text='Click here to submit',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse5_5 = event.Mouse(win=win)
x, y = [None, None]
mouse5_5.mouseClock = core.Clock()
# Set experiment start values for variable component ptp_chat_enter
ptp_chat_enter = chat_enter.text
ptp_chat_enterContainer = []

# --- Initialize components for Routine "comment_final" ---
image_party2 = visual.ImageStim(
    win=win,
    name='image_party2', 
    image='images/background_party.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
border_33 = visual.Rect(
    win=win, name='border_33',
    width=(2, 1.5)[0], height=(2, 1.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.8, depth=-1.0, interpolate=True)
text_26 = visual.TextStim(win=win, name='text_26',
    text='',
    font='Arial',
    units='pix', pos=[0,0], height=50.0, wrapWidth=1000.0, ori=1.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
see_chats = visual.ImageStim(
    win=win,
    name='see_chats', 
    image='images/chats.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "postq_1" ---
header1 = visual.TextStim(win=win, name='header1',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate = visual.TextStim(win=win, name='indicate',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions1 = visual.TextStim(win=win, name='instructions1',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
interested_slider = visual.Slider(win=win, name='interested_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
distressed_slider = visual.Slider(win=win, name='distressed_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
excited_slider = visual.Slider(win=win, name='excited_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
interested = visual.TextStim(win=win, name='interested',
    text='Interested',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
distressed = visual.TextStim(win=win, name='distressed',
    text='Distressed',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
excited = visual.TextStim(win=win, name='excited',
    text='Excited',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q1 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code1
header1.bold = 'True'
instructions1.bold= 'True'
interested.bold = 'True'
distressed.bold = 'True'
excited.bold = 'True'

# --- Initialize components for Routine "postq_2" ---
header2 = visual.TextStim(win=win, name='header2',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_2 = visual.TextStim(win=win, name='indicate_2',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
upset_slider = visual.Slider(win=win, name='upset_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
strong_slider = visual.Slider(win=win, name='strong_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
guilty_slider = visual.Slider(win=win, name='guilty_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
upset = visual.TextStim(win=win, name='upset',
    text='Upset',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
strong = visual.TextStim(win=win, name='strong',
    text='Strong',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
guilty = visual.TextStim(win=win, name='guilty',
    text='Guilty',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code2
header2.bold = 'True'
instructions2.bold= 'True'
upset.bold = 'True'
strong.bold = 'True'
guilty.bold = 'True'

# --- Initialize components for Routine "postq_3" ---
header3 = visual.TextStim(win=win, name='header3',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_3 = visual.TextStim(win=win, name='indicate_3',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions3 = visual.TextStim(win=win, name='instructions3',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
scared_slider_2 = visual.Slider(win=win, name='scared_slider_2',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
hostile_slider = visual.Slider(win=win, name='hostile_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
enthu_slider_2 = visual.Slider(win=win, name='enthu_slider_2',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
scared = visual.TextStim(win=win, name='scared',
    text='Scared',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
hostile = visual.TextStim(win=win, name='hostile',
    text='Hostile',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
enthusiastic = visual.TextStim(win=win, name='enthusiastic',
    text='Enthusiastic',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code3
header3.bold = 'True'
instructions3.bold= 'True'
scared.bold = 'True'
hostile.bold = 'True'
enthusiastic.bold = 'True'

# --- Initialize components for Routine "postq_4" ---
header4 = visual.TextStim(win=win, name='header4',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_4 = visual.TextStim(win=win, name='indicate_4',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions4 = visual.TextStim(win=win, name='instructions4',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
proud_slider = visual.Slider(win=win, name='proud_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
irritable_slider = visual.Slider(win=win, name='irritable_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
alert_slider = visual.Slider(win=win, name='alert_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
proud = visual.TextStim(win=win, name='proud',
    text='Proud',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
irritable = visual.TextStim(win=win, name='irritable',
    text='Irritable',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
alert = visual.TextStim(win=win, name='alert',
    text='Alert',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code4
header4.bold = 'True'
instructions4.bold= 'True'
proud.bold = 'True'
irritable.bold = 'True'
alert.bold = 'True'

# --- Initialize components for Routine "postq_5" ---
header5 = visual.TextStim(win=win, name='header5',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate5 = visual.TextStim(win=win, name='indicate5',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions5 = visual.TextStim(win=win, name='instructions5',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ashamed_slider = visual.Slider(win=win, name='ashamed_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
inspired_slider = visual.Slider(win=win, name='inspired_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
nervous_slider = visual.Slider(win=win, name='nervous_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
ashamed = visual.TextStim(win=win, name='ashamed',
    text='Ashamed',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
inspired = visual.TextStim(win=win, name='inspired',
    text='Inspired',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
nervous = visual.TextStim(win=win, name='nervous',
    text='Nervous',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q5 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code5
header5.bold = 'True'
instructions5.bold= 'True'
ashamed.bold = 'True'
inspired.bold = 'True'
nervous.bold = 'True'

# --- Initialize components for Routine "postq_6" ---
header6 = visual.TextStim(win=win, name='header6',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_6 = visual.TextStim(win=win, name='indicate_6',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions6 = visual.TextStim(win=win, name='instructions6',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
determined_slider = visual.Slider(win=win, name='determined_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
attentive_slider = visual.Slider(win=win, name='attentive_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
jittery_slider = visual.Slider(win=win, name='jittery_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.21), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-5, readOnly=False)
determined = visual.TextStim(win=win, name='determined',
    text='Determined',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
attentive = visual.TextStim(win=win, name='attentive',
    text='Attentive',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
jittery = visual.TextStim(win=win, name='jittery',
    text='Jittery',
    font='Arial',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
next_q6 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code6
header6.bold = 'True'
instructions6.bold= 'True'
determined.bold = 'True'
attentive.bold = 'True'
jittery.bold = 'True'

# --- Initialize components for Routine "postq_7" ---
header7 = visual.TextStim(win=win, name='header7',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_7 = visual.TextStim(win=win, name='indicate_7',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions7 = visual.TextStim(win=win, name='instructions7',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
active_slider = visual.Slider(win=win, name='active_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
afraid_slider = visual.Slider(win=win, name='afraid_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
active = visual.TextStim(win=win, name='active',
    text='Active',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
afraid = visual.TextStim(win=win, name='afraid',
    text='Afraid',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
next_q7 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code7
header7.bold = 'True'
instructions7.bold= 'True'
active.bold = 'True'
afraid.bold = 'True'

# --- Initialize components for Routine "postq_8" ---
header8 = visual.TextStim(win=win, name='header8',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_8 = visual.TextStim(win=win, name='indicate_8',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions8 = visual.TextStim(win=win, name='instructions8',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
believe_slider_1 = visual.Slider(win=win, name='believe_slider_1',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
believe_slider_2 = visual.Slider(win=win, name='believe_slider_2',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
believe_1 = visual.TextStim(win=win, name='believe_1',
    text='I believed I was interacting with other teens/young adults.',
    font='Arial',
    pos=(0, 0.21), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
believe_2 = visual.TextStim(win=win, name='believe_2',
    text='I thought the other players were real people my age.',
    font='Arial',
    pos=(0, 0.021), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
next_8 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code8
header8.bold = 'True'
instructions8.bold= 'True'
believe_1.bold = 'True'
believe_2.bold = 'True'


# --- Initialize components for Routine "postq_9" ---
header9 = visual.TextStim(win=win, name='header9',
    text='',
    font='Arial',
    pos=(0, 0.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
indicate_9 = visual.TextStim(win=win, name='indicate_9',
    text='',
    font='Arial',
    pos=(0, 0.32), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructions9 = visual.TextStim(win=win, name='instructions9',
    text='Use the mouse to pick the options that represent how you feel, then press space to submit.',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
bother_slider = visual.Slider(win=win, name='bother_slider',
    startValue=None, size=(1.0, 0.03), pos=(0, 0.15), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-3, readOnly=False)
happy_slider_3 = visual.Slider(win=win, name='happy_slider_3',
    startValue=None, size=(1.0, 0.03), pos=(0, -0.03), units=None,
    labels=["Very slightly or not at all","A little","Moderately","Quite a bit","Extremely"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='white', lineColor='white', colorSpace='rgb',
    font='Arial', labelHeight=0.02,
    flip=False, ori=0.0, depth=-4, readOnly=False)
bother = visual.TextStim(win=win, name='bother',
    text='It bothered me when other players disliked me.',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
happy = visual.TextStim(win=win, name='happy',
    text='It made me happy when other players liked me.',
    font='Arial',
    pos=(0, 0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
next_9 = keyboard.Keyboard()
# Run 'Begin Experiment' code from postq_code9
header8.bold = 'True'
instructions8.bold= 'True'
bother.bold = 'True'
happy.bold = 'True'


# --- Initialize components for Routine "done" ---
done_text = visual.TextStim(win=win, name='done_text',
    text='Thank you for participating! \nThe experiment is done.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from done_code
done_text.bold = 'True'

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [wellcome_image, polygon_1, welcome_text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wellcome_image* updates
    if wellcome_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wellcome_image.frameNStart = frameN  # exact frame index
        wellcome_image.tStart = t  # local t and not account for scr refresh
        wellcome_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wellcome_image, 'tStartRefresh')  # time at next scr refresh
        wellcome_image.setAutoDraw(True)
    if wellcome_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wellcome_image.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            wellcome_image.tStop = t  # not accounting for scr refresh
            wellcome_image.frameNStop = frameN  # exact frame index
            wellcome_image.setAutoDraw(False)
    
    # *polygon_1* updates
    if polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_1.frameNStart = frameN  # exact frame index
        polygon_1.tStart = t  # local t and not account for scr refresh
        polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_1, 'tStartRefresh')  # time at next scr refresh
        polygon_1.setAutoDraw(True)
    if polygon_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_1.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            polygon_1.tStop = t  # not accounting for scr refresh
            polygon_1.frameNStop = frameN  # exact frame index
            polygon_1.setAutoDraw(False)
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Introduction_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_text_1.setText('For this game, you will be connecting to a research social media platform used for studies of how teens/young adults make decisions about their peers.  You will be playing a game with other teens/young adults participating in research studies where you get to know each other and make decisions about who you like and don’t like to see who makes it to a virtual party. You will also see how the other players voted for you. \n')
intro_1_key_resp.keys = []
intro_1_key_resp.rt = []
_intro_1_key_resp_allKeys = []
# Run 'Begin Routine' code from code_2
next_intro_1.bold = 'True'
# keep track of which components have finished
Introduction_1Components = [intro_1, polygon_2, intro_text_1, intro_1_key_resp, next_intro_1]
for thisComponent in Introduction_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_1* updates
    if intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1.frameNStart = frameN  # exact frame index
        intro_1.tStart = t  # local t and not account for scr refresh
        intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1, 'tStartRefresh')  # time at next scr refresh
        intro_1.setAutoDraw(True)
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *intro_text_1* updates
    if intro_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text_1.frameNStart = frameN  # exact frame index
        intro_text_1.tStart = t  # local t and not account for scr refresh
        intro_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text_1, 'tStartRefresh')  # time at next scr refresh
        intro_text_1.setAutoDraw(True)
    
    # *intro_1_key_resp* updates
    waitOnFlip = False
    if intro_1_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1_key_resp.frameNStart = frameN  # exact frame index
        intro_1_key_resp.tStart = t  # local t and not account for scr refresh
        intro_1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1_key_resp, 'tStartRefresh')  # time at next scr refresh
        intro_1_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_1_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_1_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_1_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_1_key_resp_allKeys.extend(theseKeys)
        if len(_intro_1_key_resp_allKeys):
            intro_1_key_resp.keys = _intro_1_key_resp_allKeys[-1].name  # just the last key pressed
            intro_1_key_resp.rt = _intro_1_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro_1* updates
    if next_intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro_1.frameNStart = frameN  # exact frame index
        next_intro_1.tStart = t  # local t and not account for scr refresh
        next_intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro_1, 'tStartRefresh')  # time at next scr refresh
        next_intro_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_1" ---
for thisComponent in Introduction_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_1_key_resp.keys in ['', [], None]:  # No response was made
    intro_1_key_resp.keys = None
thisExp.addData('intro_1_key_resp.keys',intro_1_key_resp.keys)
if intro_1_key_resp.keys != None:  # we had a response
    thisExp.addData('intro_1_key_resp.rt', intro_1_key_resp.rt)
thisExp.nextEntry()
# the Routine "Introduction_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp_2.keys = []
intro_key_resp_2.rt = []
_intro_key_resp_2_allKeys = []
# Run 'Begin Routine' code from code_7
next_intro_2.bold = 'True'
# keep track of which components have finished
Introduction_2Components = [intro_2, polygon_3, intro_key_resp_2, intro_text_2, next_intro_2]
for thisComponent in Introduction_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_2* updates
    if intro_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_2.frameNStart = frameN  # exact frame index
        intro_2.tStart = t  # local t and not account for scr refresh
        intro_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_2, 'tStartRefresh')  # time at next scr refresh
        intro_2.setAutoDraw(True)
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *intro_key_resp_2* updates
    waitOnFlip = False
    if intro_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp_2.frameNStart = frameN  # exact frame index
        intro_key_resp_2.tStart = t  # local t and not account for scr refresh
        intro_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp_2, 'tStartRefresh')  # time at next scr refresh
        intro_key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_resp_2_allKeys.extend(theseKeys)
        if len(_intro_key_resp_2_allKeys):
            intro_key_resp_2.keys = _intro_key_resp_2_allKeys[-1].name  # just the last key pressed
            intro_key_resp_2.rt = _intro_key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intro_text_2* updates
    if intro_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text_2.frameNStart = frameN  # exact frame index
        intro_text_2.tStart = t  # local t and not account for scr refresh
        intro_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text_2, 'tStartRefresh')  # time at next scr refresh
        intro_text_2.setAutoDraw(True)
    
    # *next_intro_2* updates
    if next_intro_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro_2.frameNStart = frameN  # exact frame index
        next_intro_2.tStart = t  # local t and not account for scr refresh
        next_intro_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro_2, 'tStartRefresh')  # time at next scr refresh
        next_intro_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_2" ---
for thisComponent in Introduction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp_2.keys in ['', [], None]:  # No response was made
    intro_key_resp_2.keys = None
thisExp.addData('intro_key_resp_2.keys',intro_key_resp_2.keys)
if intro_key_resp_2.keys != None:  # we had a response
    thisExp.addData('intro_key_resp_2.rt', intro_key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Introduction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_name" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
name_enter.reset()
name_enter.setText('')
# setup some python lists for storing info about the mouse_name
mouse_name.clicked_name = []
gotValidClick = False  # until a click is received
ptp_name = name_enter.text  # Set routine start values for ptp_name
# keep track of which components have finished
Participant_nameComponents = [name_question, name_enter, button_name, submit_name, mouse_name]
for thisComponent in Participant_nameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_name" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *name_question* updates
    if name_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_question.frameNStart = frameN  # exact frame index
        name_question.tStart = t  # local t and not account for scr refresh
        name_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_question, 'tStartRefresh')  # time at next scr refresh
        name_question.setAutoDraw(True)
    
    # *name_enter* updates
    if name_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_enter.frameNStart = frameN  # exact frame index
        name_enter.tStart = t  # local t and not account for scr refresh
        name_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_enter, 'tStartRefresh')  # time at next scr refresh
        name_enter.setAutoDraw(True)
    
    # *button_name* updates
    if button_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_name.frameNStart = frameN  # exact frame index
        button_name.tStart = t  # local t and not account for scr refresh
        button_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_name, 'tStartRefresh')  # time at next scr refresh
        button_name.setAutoDraw(True)
    
    # *submit_name* updates
    if submit_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit_name.frameNStart = frameN  # exact frame index
        submit_name.tStart = t  # local t and not account for scr refresh
        submit_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_name, 'tStartRefresh')  # time at next scr refresh
        submit_name.setAutoDraw(True)
    # *mouse_name* updates
    if mouse_name.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_name.frameNStart = frameN  # exact frame index
        mouse_name.tStart = t  # local t and not account for scr refresh
        mouse_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_name, 'tStartRefresh')  # time at next scr refresh
        mouse_name.status = STARTED
        mouse_name.mouseClock.reset()
        prevButtonState = mouse_name.getPressed()  # if button is down already this ISN'T a new click
    if mouse_name.status == STARTED:  # only update if started and not finished!
        buttons = mouse_name.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button_name)
                    clickableList = button_name
                except:
                    clickableList = [button_name]
                for obj in clickableList:
                    if obj.contains(mouse_name):
                        gotValidClick = True
                        mouse_name.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_name = name_enter.text  # Set frame start values for ptp_name
    ptp_nameContainer.append(ptp_name)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_nameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_name" ---
for thisComponent in Participant_nameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('name_enter.text',name_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_name.frameStartVal', ptp_nameContainer[0])  # Save start frame value
# Run 'End Routine' code from capitalization_name
if ptp_name.isalpha() and (ptp_name.islower() or (len(ptp_name) > 2 and ptp_name.isupper())):
    ptp_name = ptp_name.lower().capitalize()
ptp_name.strip()
# the Routine "Participant_name" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_age" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
age_enter.reset()
age_enter.setText('')
# setup some python lists for storing info about the mouse_age
mouse_age.clicked_name = []
gotValidClick = False  # until a click is received
ptp_age = age_enter.text  # Set routine start values for ptp_age
# keep track of which components have finished
Participant_ageComponents = [age_question, age_enter, mouse_age, button_age, submit_age, reminder]
for thisComponent in Participant_ageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_age" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *age_question* updates
    if age_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_question.frameNStart = frameN  # exact frame index
        age_question.tStart = t  # local t and not account for scr refresh
        age_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_question, 'tStartRefresh')  # time at next scr refresh
        age_question.setAutoDraw(True)
    
    # *age_enter* updates
    if age_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_enter.frameNStart = frameN  # exact frame index
        age_enter.tStart = t  # local t and not account for scr refresh
        age_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_enter, 'tStartRefresh')  # time at next scr refresh
        age_enter.setAutoDraw(True)
    # *mouse_age* updates
    if mouse_age.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_age.frameNStart = frameN  # exact frame index
        mouse_age.tStart = t  # local t and not account for scr refresh
        mouse_age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_age, 'tStartRefresh')  # time at next scr refresh
        mouse_age.status = STARTED
        mouse_age.mouseClock.reset()
        prevButtonState = mouse_age.getPressed()  # if button is down already this ISN'T a new click
    if mouse_age.status == STARTED:  # only update if started and not finished!
        buttons = mouse_age.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button_age)
                    clickableList = button_age
                except:
                    clickableList = [button_age]
                for obj in clickableList:
                    if obj.contains(mouse_age):
                        gotValidClick = True
                        mouse_age.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button_age* updates
    if button_age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_age.frameNStart = frameN  # exact frame index
        button_age.tStart = t  # local t and not account for scr refresh
        button_age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_age, 'tStartRefresh')  # time at next scr refresh
        button_age.setAutoDraw(True)
    
    # *submit_age* updates
    if submit_age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit_age.frameNStart = frameN  # exact frame index
        submit_age.tStart = t  # local t and not account for scr refresh
        submit_age.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_age, 'tStartRefresh')  # time at next scr refresh
        submit_age.setAutoDraw(True)
    
    # *reminder* updates
    if reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        reminder.frameNStart = frameN  # exact frame index
        reminder.tStart = t  # local t and not account for scr refresh
        reminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reminder, 'tStartRefresh')  # time at next scr refresh
        reminder.setAutoDraw(True)
    ptp_age = age_enter.text  # Set frame start values for ptp_age
    ptp_ageContainer.append(ptp_age)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_ageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_age" ---
for thisComponent in Participant_ageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('age_enter.text',age_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_age.frameStartVal', ptp_ageContainer[0])  # Save start frame value
# the Routine "Participant_age" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_hometown" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
hometown_enter.reset()
hometown_enter.setText('')
# setup some python lists for storing info about the mouse_home
mouse_home.clicked_name = []
gotValidClick = False  # until a click is received
ptp_hometown = hometown_enter.text  # Set routine start values for ptp_hometown
# keep track of which components have finished
Participant_hometownComponents = [hometown_question, hometown_enter, mouse_home, button_home, submit_home]
for thisComponent in Participant_hometownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_hometown" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hometown_question* updates
    if hometown_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hometown_question.frameNStart = frameN  # exact frame index
        hometown_question.tStart = t  # local t and not account for scr refresh
        hometown_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hometown_question, 'tStartRefresh')  # time at next scr refresh
        hometown_question.setAutoDraw(True)
    
    # *hometown_enter* updates
    if hometown_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hometown_enter.frameNStart = frameN  # exact frame index
        hometown_enter.tStart = t  # local t and not account for scr refresh
        hometown_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hometown_enter, 'tStartRefresh')  # time at next scr refresh
        hometown_enter.setAutoDraw(True)
    # *mouse_home* updates
    if mouse_home.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_home.frameNStart = frameN  # exact frame index
        mouse_home.tStart = t  # local t and not account for scr refresh
        mouse_home.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_home, 'tStartRefresh')  # time at next scr refresh
        mouse_home.status = STARTED
        mouse_home.mouseClock.reset()
        prevButtonState = mouse_home.getPressed()  # if button is down already this ISN'T a new click
    if mouse_home.status == STARTED:  # only update if started and not finished!
        buttons = mouse_home.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button_home)
                    clickableList = button_home
                except:
                    clickableList = [button_home]
                for obj in clickableList:
                    if obj.contains(mouse_home):
                        gotValidClick = True
                        mouse_home.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button_home* updates
    if button_home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_home.frameNStart = frameN  # exact frame index
        button_home.tStart = t  # local t and not account for scr refresh
        button_home.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_home, 'tStartRefresh')  # time at next scr refresh
        button_home.setAutoDraw(True)
    
    # *submit_home* updates
    if submit_home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit_home.frameNStart = frameN  # exact frame index
        submit_home.tStart = t  # local t and not account for scr refresh
        submit_home.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_home, 'tStartRefresh')  # time at next scr refresh
        submit_home.setAutoDraw(True)
    ptp_hometown = hometown_enter.text  # Set frame start values for ptp_hometown
    ptp_hometownContainer.append(ptp_hometown)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_hometownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_hometown" ---
for thisComponent in Participant_hometownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hometown_enter.text',hometown_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_hometown.frameStartVal', ptp_hometownContainer[0])  # Save start frame value
# Run 'End Routine' code from capitalization_2
if ptp_hometown.isalpha() and (ptp_hometown.islower() or (len(ptp_hometown) > 2 and ptp_hometown.isupper())):
    ptp_hometown = ptp_hometown.lower().capitalize()
# the Routine "Participant_hometown" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_interest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
interest_enter.reset()
interest_enter.setText('')
# setup some python lists for storing info about the mouse_interest
mouse_interest.clicked_name = []
gotValidClick = False  # until a click is received
ptp_interest = interest_enter.text  # Set routine start values for ptp_interest
# keep track of which components have finished
Participant_interestComponents = [interest_question, interest_enter, mouse_interest, button_interest, submit_interest]
for thisComponent in Participant_interestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_interest" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interest_question* updates
    if interest_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interest_question.frameNStart = frameN  # exact frame index
        interest_question.tStart = t  # local t and not account for scr refresh
        interest_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interest_question, 'tStartRefresh')  # time at next scr refresh
        interest_question.setAutoDraw(True)
    
    # *interest_enter* updates
    if interest_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interest_enter.frameNStart = frameN  # exact frame index
        interest_enter.tStart = t  # local t and not account for scr refresh
        interest_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interest_enter, 'tStartRefresh')  # time at next scr refresh
        interest_enter.setAutoDraw(True)
    # *mouse_interest* updates
    if mouse_interest.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_interest.frameNStart = frameN  # exact frame index
        mouse_interest.tStart = t  # local t and not account for scr refresh
        mouse_interest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_interest, 'tStartRefresh')  # time at next scr refresh
        mouse_interest.status = STARTED
        mouse_interest.mouseClock.reset()
        prevButtonState = mouse_interest.getPressed()  # if button is down already this ISN'T a new click
    if mouse_interest.status == STARTED:  # only update if started and not finished!
        buttons = mouse_interest.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button_interest)
                    clickableList = button_interest
                except:
                    clickableList = [button_interest]
                for obj in clickableList:
                    if obj.contains(mouse_interest):
                        gotValidClick = True
                        mouse_interest.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button_interest* updates
    if button_interest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_interest.frameNStart = frameN  # exact frame index
        button_interest.tStart = t  # local t and not account for scr refresh
        button_interest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_interest, 'tStartRefresh')  # time at next scr refresh
        button_interest.setAutoDraw(True)
    
    # *submit_interest* updates
    if submit_interest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit_interest.frameNStart = frameN  # exact frame index
        submit_interest.tStart = t  # local t and not account for scr refresh
        submit_interest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_interest, 'tStartRefresh')  # time at next scr refresh
        submit_interest.setAutoDraw(True)
    ptp_interest = interest_enter.text  # Set frame start values for ptp_interest
    ptp_interestContainer.append(ptp_interest)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_interestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_interest" ---
for thisComponent in Participant_interestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interest_enter.text',interest_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_interest.frameStartVal', ptp_interestContainer[0])  # Save start frame value
# the Routine "Participant_interest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_school" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
school_enter.reset()
school_enter.setText('')
# setup some python lists for storing info about the mouse_school
mouse_school.clicked_name = []
gotValidClick = False  # until a click is received
ptp_school = school_enter.text  # Set routine start values for ptp_school
# keep track of which components have finished
Participant_schoolComponents = [school_question, school_enter, mouse_school, button_school, submit_school]
for thisComponent in Participant_schoolComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_school" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *school_question* updates
    if school_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        school_question.frameNStart = frameN  # exact frame index
        school_question.tStart = t  # local t and not account for scr refresh
        school_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(school_question, 'tStartRefresh')  # time at next scr refresh
        school_question.setAutoDraw(True)
    
    # *school_enter* updates
    if school_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        school_enter.frameNStart = frameN  # exact frame index
        school_enter.tStart = t  # local t and not account for scr refresh
        school_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(school_enter, 'tStartRefresh')  # time at next scr refresh
        school_enter.setAutoDraw(True)
    # *mouse_school* updates
    if mouse_school.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_school.frameNStart = frameN  # exact frame index
        mouse_school.tStart = t  # local t and not account for scr refresh
        mouse_school.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_school, 'tStartRefresh')  # time at next scr refresh
        mouse_school.status = STARTED
        mouse_school.mouseClock.reset()
        prevButtonState = mouse_school.getPressed()  # if button is down already this ISN'T a new click
    if mouse_school.status == STARTED:  # only update if started and not finished!
        buttons = mouse_school.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button_school)
                    clickableList = button_school
                except:
                    clickableList = [button_school]
                for obj in clickableList:
                    if obj.contains(mouse_school):
                        gotValidClick = True
                        mouse_school.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button_school* updates
    if button_school.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_school.frameNStart = frameN  # exact frame index
        button_school.tStart = t  # local t and not account for scr refresh
        button_school.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_school, 'tStartRefresh')  # time at next scr refresh
        button_school.setAutoDraw(True)
    
    # *submit_school* updates
    if submit_school.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit_school.frameNStart = frameN  # exact frame index
        submit_school.tStart = t  # local t and not account for scr refresh
        submit_school.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_school, 'tStartRefresh')  # time at next scr refresh
        submit_school.setAutoDraw(True)
    ptp_school = school_enter.text  # Set frame start values for ptp_school
    ptp_schoolContainer.append(ptp_school)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_schoolComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_school" ---
for thisComponent in Participant_schoolComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('school_enter.text',school_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_school.routineEndVal', ptp_school)  # Save end routine value
thisExp.addData('ptp_school.frameStartVal', ptp_schoolContainer[0])  # Save start frame value
# the Routine "Participant_school" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Participant_profile" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
subject_image.setImage('images/subject.jpg')
# Run 'Begin Routine' code from code
part_response.alignText = 'left'
part_prompts.alignText = 'left'
part_name.alignText = 'left'
part_name.bold = 'True'
next_text.bold = 'True'
next.keys = []
next.rt = []
_next_allKeys = []
# keep track of which components have finished
Participant_profileComponents = [image_4, background_profile, border, subject_image, part_response, part_prompts, part_name, next, next_text]
for thisComponent in Participant_profileComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Participant_profile" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *background_profile* updates
    if background_profile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        background_profile.frameNStart = frameN  # exact frame index
        background_profile.tStart = t  # local t and not account for scr refresh
        background_profile.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(background_profile, 'tStartRefresh')  # time at next scr refresh
        background_profile.setAutoDraw(True)
    
    # *border* updates
    if border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border.frameNStart = frameN  # exact frame index
        border.tStart = t  # local t and not account for scr refresh
        border.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border, 'tStartRefresh')  # time at next scr refresh
        border.setAutoDraw(True)
    
    # *subject_image* updates
    if subject_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        subject_image.frameNStart = frameN  # exact frame index
        subject_image.tStart = t  # local t and not account for scr refresh
        subject_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(subject_image, 'tStartRefresh')  # time at next scr refresh
        subject_image.setAutoDraw(True)
    
    # *part_response* updates
    if part_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part_response.frameNStart = frameN  # exact frame index
        part_response.tStart = t  # local t and not account for scr refresh
        part_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part_response, 'tStartRefresh')  # time at next scr refresh
        part_response.setAutoDraw(True)
    if part_response.status == STARTED:  # only update if drawing
        part_response.setText(ptp_age + '\n' + ptp_hometown + '\n' + ptp_interest
+ '\n' + ptp_school, log=False)
    
    # *part_prompts* updates
    if part_prompts.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part_prompts.frameNStart = frameN  # exact frame index
        part_prompts.tStart = t  # local t and not account for scr refresh
        part_prompts.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part_prompts, 'tStartRefresh')  # time at next scr refresh
        part_prompts.setAutoDraw(True)
    
    # *part_name* updates
    if part_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part_name.frameNStart = frameN  # exact frame index
        part_name.tStart = t  # local t and not account for scr refresh
        part_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part_name, 'tStartRefresh')  # time at next scr refresh
        part_name.setAutoDraw(True)
    if part_name.status == STARTED:  # only update if drawing
        part_name.setText(ptp_name, log=False)
    
    # *next* updates
    waitOnFlip = False
    if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next.frameNStart = frameN  # exact frame index
        next.tStart = t  # local t and not account for scr refresh
        next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
        next.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next.status == STARTED and not waitOnFlip:
        theseKeys = next.getKeys(keyList=['space'], waitRelease=False)
        _next_allKeys.extend(theseKeys)
        if len(_next_allKeys):
            next.keys = _next_allKeys[-1].name  # just the last key pressed
            next.rt = _next_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text* updates
    if next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text.frameNStart = frameN  # exact frame index
        next_text.tStart = t  # local t and not account for scr refresh
        next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
        next_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_profileComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Participant_profile" ---
for thisComponent in Participant_profileComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Participant_profile" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
wait_text_1.setText('Waiting for others to connect to the social media platform...')
# keep track of which components have finished
WaitingComponents = [wait_1, polygon_wait, wait_text_1, load_1]
for thisComponent in WaitingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_1* updates
    if wait_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_1.frameNStart = frameN  # exact frame index
        wait_1.tStart = t  # local t and not account for scr refresh
        wait_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_1, 'tStartRefresh')  # time at next scr refresh
        wait_1.setAutoDraw(True)
    if wait_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_1.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            wait_1.tStop = t  # not accounting for scr refresh
            wait_1.frameNStop = frameN  # exact frame index
            wait_1.setAutoDraw(False)
    
    # *polygon_wait* updates
    if polygon_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_wait.frameNStart = frameN  # exact frame index
        polygon_wait.tStart = t  # local t and not account for scr refresh
        polygon_wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_wait, 'tStartRefresh')  # time at next scr refresh
        polygon_wait.setAutoDraw(True)
    if polygon_wait.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_wait.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_wait.tStop = t  # not accounting for scr refresh
            polygon_wait.frameNStop = frameN  # exact frame index
            polygon_wait.setAutoDraw(False)
    
    # *wait_text_1* updates
    if wait_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_text_1.frameNStart = frameN  # exact frame index
        wait_text_1.tStart = t  # local t and not account for scr refresh
        wait_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_text_1, 'tStartRefresh')  # time at next scr refresh
        wait_text_1.setAutoDraw(True)
    if wait_text_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_text_1.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            wait_text_1.tStop = t  # not accounting for scr refresh
            wait_text_1.frameNStop = frameN  # exact frame index
            wait_text_1.setAutoDraw(False)
    
    # *load_1* updates
    if load_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        load_1.frameNStart = frameN  # exact frame index
        load_1.tStart = t  # local t and not account for scr refresh
        load_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(load_1, 'tStartRefresh')  # time at next scr refresh
        load_1.setAutoDraw(True)
    if load_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > load_1.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            load_1.tStop = t  # not accounting for scr refresh
            load_1.frameNStop = frameN  # exact frame index
            load_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting" ---
for thisComponent in WaitingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Introduction_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_text_3.setText('All players are connected now. Take some time to get to know the other people playing the game with you.\n')
intro_key_resp_3.keys = []
intro_key_resp_3.rt = []
_intro_key_resp_3_allKeys = []
# Run 'Begin Routine' code from code_10
next_intro_3.bold = True
# keep track of which components have finished
Introduction_3Components = [image_3, polygon_intro_3, intro_text_3, intro_key_resp_3, next_intro_3]
for thisComponent in Introduction_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *polygon_intro_3* updates
    if polygon_intro_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_intro_3.frameNStart = frameN  # exact frame index
        polygon_intro_3.tStart = t  # local t and not account for scr refresh
        polygon_intro_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_intro_3, 'tStartRefresh')  # time at next scr refresh
        polygon_intro_3.setAutoDraw(True)
    
    # *intro_text_3* updates
    if intro_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text_3.frameNStart = frameN  # exact frame index
        intro_text_3.tStart = t  # local t and not account for scr refresh
        intro_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text_3, 'tStartRefresh')  # time at next scr refresh
        intro_text_3.setAutoDraw(True)
    
    # *intro_key_resp_3* updates
    waitOnFlip = False
    if intro_key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp_3.frameNStart = frameN  # exact frame index
        intro_key_resp_3.tStart = t  # local t and not account for scr refresh
        intro_key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp_3, 'tStartRefresh')  # time at next scr refresh
        intro_key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_resp_3_allKeys.extend(theseKeys)
        if len(_intro_key_resp_3_allKeys):
            intro_key_resp_3.keys = _intro_key_resp_3_allKeys[-1].name  # just the last key pressed
            intro_key_resp_3.rt = _intro_key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro_3* updates
    if next_intro_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro_3.frameNStart = frameN  # exact frame index
        next_intro_3.tStart = t  # local t and not account for scr refresh
        next_intro_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro_3, 'tStartRefresh')  # time at next scr refresh
        next_intro_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_3" ---
for thisComponent in Introduction_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
cop_info_loader_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='cop_info_loader_loop')
thisExp.addLoop(cop_info_loader_loop)  # add the loop to the experiment
thisCop_info_loader_loop = cop_info_loader_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCop_info_loader_loop.rgb)
if thisCop_info_loader_loop != None:
    for paramName in thisCop_info_loader_loop:
        exec('{} = thisCop_info_loader_loop[paramName]'.format(paramName))

for thisCop_info_loader_loop in cop_info_loader_loop:
    currentLoop = cop_info_loader_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCop_info_loader_loop.rgb)
    if thisCop_info_loader_loop != None:
        for paramName in thisCop_info_loader_loop:
            exec('{} = thisCop_info_loader_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Coplayer_profile_loader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from cop_info_loader
    # add information into lists
    names.append(cop_name)
    ages.append(cop_age)
    hometowns.append(cop_hometown)
    interests.append(cop_interests)
    photos.append(cop_photo)
    votes.append(cop_vote)
    schools.append(cop_school)
    # keep track of which components have finished
    Coplayer_profile_loaderComponents = []
    for thisComponent in Coplayer_profile_loaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Coplayer_profile_loader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Coplayer_profile_loaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Coplayer_profile_loader" ---
    for thisComponent in Coplayer_profile_loaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Coplayer_profile_loader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'cop_info_loader_loop'


# --- Prepare to start Routine "Coplayer_profile_shuffler" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from info_shuffler
shuffle(names)
shuffle(ages)
shuffle(hometowns)
shuffle(interests)
shuffle(photos)
shuffle(votes)
shuffle(schools)

# keep track of which components have finished
Coplayer_profile_shufflerComponents = []
for thisComponent in Coplayer_profile_shufflerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Coplayer_profile_shuffler" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Coplayer_profile_shufflerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Coplayer_profile_shuffler" ---
for thisComponent in Coplayer_profile_shufflerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Coplayer_profile_shuffler" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
coplayers_show = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='coplayers_show')
thisExp.addLoop(coplayers_show)  # add the loop to the experiment
thisCoplayers_show = coplayers_show.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCoplayers_show.rgb)
if thisCoplayers_show != None:
    for paramName in thisCoplayers_show:
        exec('{} = thisCoplayers_show[paramName]'.format(paramName))

for thisCoplayers_show in coplayers_show:
    currentLoop = coplayers_show
    # abbreviate parameter names if possible (e.g. rgb = thisCoplayers_show.rgb)
    if thisCoplayers_show != None:
        for paramName in thisCoplayers_show:
            exec('{} = thisCoplayers_show[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Coplayer_profiles" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image_5.setImage('images/background_profiles.jpeg')
    # Run 'Begin Routine' code from code_cop_profile
    cop_resp_show.alignText = 'left'
    cop_prompts_show.alignText = 'left'
    cop_name_show.alignText = 'left'
    cop_name_show.bold = 'True'
    next_text_cop_profile.bold = 'True'
    
    curr_item += 1
    
    # assign current profiles
    cop_name = names[curr_item]
    cop_age = ages[curr_item]
    cop_hometown = hometowns[curr_item]
    cop_interests = interests[curr_item]
    cop_photo = photos[curr_item]
    cop_school = schools[curr_item]
    
    print(cop_name)
    print(cop_age)
    print(cop_hometown)
    print(cop_interests)
    print(cop_school)
    cop_img.setImage(cop_photo)
    cop_resp_show.setText(str(cop_age) + '\n' + cop_hometown + '\n' + cop_interests + '\n' + cop_school)
    cop_prompts_show.setText('Age:\nHometown:\nInterests:\nSchool:')
    cop_vote_show.setText(cop_vote)
    cop_name_show.setText(cop_name)
    next_cop_profile.keys = []
    next_cop_profile.rt = []
    _next_cop_profile_allKeys = []
    # keep track of which components have finished
    Coplayer_profilesComponents = [image_5, polygon_coplayer, border_coplayer, cop_img, cop_resp_show, cop_prompts_show, cop_vote_show, cop_name_show, next_cop_profile, next_text_cop_profile]
    for thisComponent in Coplayer_profilesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Coplayer_profiles" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        
        # *polygon_coplayer* updates
        if polygon_coplayer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_coplayer.frameNStart = frameN  # exact frame index
            polygon_coplayer.tStart = t  # local t and not account for scr refresh
            polygon_coplayer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_coplayer, 'tStartRefresh')  # time at next scr refresh
            polygon_coplayer.setAutoDraw(True)
        
        # *border_coplayer* updates
        if border_coplayer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_coplayer.frameNStart = frameN  # exact frame index
            border_coplayer.tStart = t  # local t and not account for scr refresh
            border_coplayer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_coplayer, 'tStartRefresh')  # time at next scr refresh
            border_coplayer.setAutoDraw(True)
        
        # *cop_img* updates
        if cop_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_img.frameNStart = frameN  # exact frame index
            cop_img.tStart = t  # local t and not account for scr refresh
            cop_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_img, 'tStartRefresh')  # time at next scr refresh
            cop_img.setAutoDraw(True)
        
        # *cop_resp_show* updates
        if cop_resp_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_resp_show.frameNStart = frameN  # exact frame index
            cop_resp_show.tStart = t  # local t and not account for scr refresh
            cop_resp_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_resp_show, 'tStartRefresh')  # time at next scr refresh
            cop_resp_show.setAutoDraw(True)
        
        # *cop_prompts_show* updates
        if cop_prompts_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts_show.frameNStart = frameN  # exact frame index
            cop_prompts_show.tStart = t  # local t and not account for scr refresh
            cop_prompts_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts_show, 'tStartRefresh')  # time at next scr refresh
            cop_prompts_show.setAutoDraw(True)
        
        # *cop_vote_show* updates
        if cop_vote_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_vote_show.frameNStart = frameN  # exact frame index
            cop_vote_show.tStart = t  # local t and not account for scr refresh
            cop_vote_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_vote_show, 'tStartRefresh')  # time at next scr refresh
            cop_vote_show.setAutoDraw(True)
        
        # *cop_name_show* updates
        if cop_name_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_name_show.frameNStart = frameN  # exact frame index
            cop_name_show.tStart = t  # local t and not account for scr refresh
            cop_name_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_name_show, 'tStartRefresh')  # time at next scr refresh
            cop_name_show.setAutoDraw(True)
        
        # *next_cop_profile* updates
        waitOnFlip = False
        if next_cop_profile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_cop_profile.frameNStart = frameN  # exact frame index
            next_cop_profile.tStart = t  # local t and not account for scr refresh
            next_cop_profile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_cop_profile, 'tStartRefresh')  # time at next scr refresh
            next_cop_profile.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(next_cop_profile.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(next_cop_profile.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if next_cop_profile.status == STARTED and not waitOnFlip:
            theseKeys = next_cop_profile.getKeys(keyList=['space'], waitRelease=False)
            _next_cop_profile_allKeys.extend(theseKeys)
            if len(_next_cop_profile_allKeys):
                next_cop_profile.keys = _next_cop_profile_allKeys[-1].name  # just the last key pressed
                next_cop_profile.rt = _next_cop_profile_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *next_text_cop_profile* updates
        if next_text_cop_profile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_text_cop_profile.frameNStart = frameN  # exact frame index
            next_text_cop_profile.tStart = t  # local t and not account for scr refresh
            next_text_cop_profile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_text_cop_profile, 'tStartRefresh')  # time at next scr refresh
            next_text_cop_profile.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Coplayer_profilesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Coplayer_profiles" ---
    for thisComponent in Coplayer_profilesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_cop_profile
    print(photos)
    print(names)
    print(interests)
    print(hometowns)
    # the Routine "Coplayer_profiles" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'coplayers_show'

# get names of stimulus parameters
if coplayers_show.trialList in ([], [None], None):
    params = []
else:
    params = coplayers_show.trialList[0].keys()
# save data for this loop
coplayers_show.saveAsExcel(filename + '.xlsx', sheetName='coplayers_show',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
coplayers_show.saveAsText(filename + 'coplayers_show.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Vote_store" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from vote_store

#already have assigned lists
vote_cop1 = votes[0]
vote_cop2 = votes[1]
vote_cop3 = votes[2]
vote_cop4 = votes[3]
vote_cop5 = votes[4]
vote_cop6 = votes[5]
vote_cop7 = votes[6]
vote_cop8 = votes[7]
vote_cop9 = votes[8]
vote_cop10 = votes[9]
vote_cop11 = votes[10]
vote_cop12 = votes[11]

# seperate by ','
vote_split_cop1 = vote_cop1.split(',')
vote_split_cop2 = vote_cop2.split(',')
vote_split_cop3 = vote_cop3.split(',')
vote_split_cop4 = vote_cop4.split(',')
vote_split_cop5 = vote_cop5.split(',')
vote_split_cop6 = vote_cop6.split(',')
vote_split_cop7 = vote_cop7.split(',')
vote_split_cop8 = vote_cop8.split(',')
vote_split_cop9 = vote_cop9.split(',')
vote_split_cop10 = vote_cop10.split(',')
vote_split_cop11 = vote_cop11.split(',')
vote_split_cop12 = vote_cop12.split(',')


# create a new empty list
vote_all = []

#append lists to new list
vote_all.append(vote_split_cop1)
vote_all.append(vote_split_cop2)
vote_all.append(vote_split_cop3)
vote_all.append(vote_split_cop4)
vote_all.append(vote_split_cop5)
vote_all.append(vote_split_cop6)
vote_all.append(vote_split_cop7)
vote_all.append(vote_split_cop8)
vote_all.append(vote_split_cop9)
vote_all.append(vote_split_cop10)
vote_all.append(vote_split_cop11)
vote_all.append(vote_split_cop12)

# got vote pattern lists for every coplayer
#print(vote_split_cop1)
#print(vote_split_cop2)
#print(vote_split_cop3)
#print(vote_split_cop4)
#print(vote_split_cop5)
#print(vote_split_cop6)
#print(vote_split_cop7)
#print(vote_split_cop8)
#print(vote_split_cop9)
#print(vote_split_cop10)
#print(vote_split_cop11)

# check final vote_all
print(vote_all)
# keep track of which components have finished
Vote_storeComponents = []
for thisComponent in Vote_storeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Vote_store" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Vote_storeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Vote_store" ---
for thisComponent in Vote_storeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Vote_store" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_text_4.setText("Now, we want to hear from YOU about which players you like and which players you dislike, based on the information you have so far.  You will see each player’s profile again and this time click 'Like' if you like that person and 'Dislike' if you dislike that person. \n")
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# Run 'Begin Routine' code from code_11
next_intro_4.bold = True
# keep track of which components have finished
Introduction_4Components = [image_6, polygon_intro_4, intro_text_4, key_resp_4, next_intro_4]
for thisComponent in Introduction_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *polygon_intro_4* updates
    if polygon_intro_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_intro_4.frameNStart = frameN  # exact frame index
        polygon_intro_4.tStart = t  # local t and not account for scr refresh
        polygon_intro_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_intro_4, 'tStartRefresh')  # time at next scr refresh
        polygon_intro_4.setAutoDraw(True)
    
    # *intro_text_4* updates
    if intro_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text_4.frameNStart = frameN  # exact frame index
        intro_text_4.tStart = t  # local t and not account for scr refresh
        intro_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text_4, 'tStartRefresh')  # time at next scr refresh
        intro_text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro_4* updates
    if next_intro_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro_4.frameNStart = frameN  # exact frame index
        next_intro_4.tStart = t  # local t and not account for scr refresh
        next_intro_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro_4, 'tStartRefresh')  # time at next scr refresh
        next_intro_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_4" ---
for thisComponent in Introduction_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Introduction_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_5.setText('While you are voting on each player, the same person is also voting on you. After you both make your selections, you will find out how they voted for you. The feedback will look like this:\n\n')
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# Run 'Begin Routine' code from bold_text_thumbs
next_3.bold = 'True'
# keep track of which components have finished
Introduction_5Components = [image_7, polygon_intro_5, text_5, key_resp_5, thumbs_up, thumbs_down, feedback_like, feedback_dislike, next_3]
for thisComponent in Introduction_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *polygon_intro_5* updates
    if polygon_intro_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_intro_5.frameNStart = frameN  # exact frame index
        polygon_intro_5.tStart = t  # local t and not account for scr refresh
        polygon_intro_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_intro_5, 'tStartRefresh')  # time at next scr refresh
        polygon_intro_5.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *thumbs_up* updates
    if thumbs_up.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thumbs_up.frameNStart = frameN  # exact frame index
        thumbs_up.tStart = t  # local t and not account for scr refresh
        thumbs_up.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thumbs_up, 'tStartRefresh')  # time at next scr refresh
        thumbs_up.setAutoDraw(True)
    
    # *thumbs_down* updates
    if thumbs_down.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thumbs_down.frameNStart = frameN  # exact frame index
        thumbs_down.tStart = t  # local t and not account for scr refresh
        thumbs_down.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thumbs_down, 'tStartRefresh')  # time at next scr refresh
        thumbs_down.setAutoDraw(True)
    
    # *feedback_like* updates
    if feedback_like.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_like.frameNStart = frameN  # exact frame index
        feedback_like.tStart = t  # local t and not account for scr refresh
        feedback_like.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_like, 'tStartRefresh')  # time at next scr refresh
        feedback_like.setAutoDraw(True)
    
    # *feedback_dislike* updates
    if feedback_dislike.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_dislike.frameNStart = frameN  # exact frame index
        feedback_dislike.tStart = t  # local t and not account for scr refresh
        feedback_dislike.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_dislike, 'tStartRefresh')  # time at next scr refresh
        feedback_dislike.setAutoDraw(True)
    
    # *next_3* updates
    if next_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_3.frameNStart = frameN  # exact frame index
        next_3.tStart = t  # local t and not account for scr refresh
        next_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_3, 'tStartRefresh')  # time at next scr refresh
        next_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_5" ---
for thisComponent in Introduction_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_10.setText('Remember there will be 5 rounds so you can change your votes in future rounds and you may find that other players change their votes for you as well.\n\nFirst, let’s do some practice trials to make sure it’s clear how voting works.\n\n')
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# Run 'Begin Routine' code from bold_intro_next
next_intro6.bold = True
# keep track of which components have finished
Introduction_6Components = [image_13, polygon_intro_6, text_10, key_resp_10, next_intro6]
for thisComponent in Introduction_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        image_13.setAutoDraw(True)
    
    # *polygon_intro_6* updates
    if polygon_intro_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_intro_6.frameNStart = frameN  # exact frame index
        polygon_intro_6.tStart = t  # local t and not account for scr refresh
        polygon_intro_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_intro_6, 'tStartRefresh')  # time at next scr refresh
        polygon_intro_6.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro6* updates
    if next_intro6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro6.frameNStart = frameN  # exact frame index
        next_intro6.tStart = t  # local t and not account for scr refresh
        next_intro6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro6, 'tStartRefresh')  # time at next scr refresh
        next_intro6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_6" ---
for thisComponent in Introduction_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Practice_1a" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
prac_image_1.setImage('images/practice.png')
player_1.setText('Player 1')
# Run 'Begin Routine' code from bold_prac_1
player_1.bold = 'True'

# setup some python lists for storing info about the click_prac_1
click_prac_1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Practice_1aComponents = [prac_image_1, like_prac_button_1, like_prac_text_1, dislike_prac_button_1, dislike_prac_text_1, player_1, click_prac_1, vote_question_2]
for thisComponent in Practice_1aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_1a" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_image_1* updates
    if prac_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_image_1.frameNStart = frameN  # exact frame index
        prac_image_1.tStart = t  # local t and not account for scr refresh
        prac_image_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_image_1, 'tStartRefresh')  # time at next scr refresh
        prac_image_1.setAutoDraw(True)
    
    # *like_prac_button_1* updates
    if like_prac_button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_prac_button_1.frameNStart = frameN  # exact frame index
        like_prac_button_1.tStart = t  # local t and not account for scr refresh
        like_prac_button_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_prac_button_1, 'tStartRefresh')  # time at next scr refresh
        like_prac_button_1.setAutoDraw(True)
    
    # *like_prac_text_1* updates
    if like_prac_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_prac_text_1.frameNStart = frameN  # exact frame index
        like_prac_text_1.tStart = t  # local t and not account for scr refresh
        like_prac_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_prac_text_1, 'tStartRefresh')  # time at next scr refresh
        like_prac_text_1.setAutoDraw(True)
    
    # *dislike_prac_button_1* updates
    if dislike_prac_button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dislike_prac_button_1.frameNStart = frameN  # exact frame index
        dislike_prac_button_1.tStart = t  # local t and not account for scr refresh
        dislike_prac_button_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dislike_prac_button_1, 'tStartRefresh')  # time at next scr refresh
        dislike_prac_button_1.setAutoDraw(True)
    
    # *dislike_prac_text_1* updates
    if dislike_prac_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dislike_prac_text_1.frameNStart = frameN  # exact frame index
        dislike_prac_text_1.tStart = t  # local t and not account for scr refresh
        dislike_prac_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dislike_prac_text_1, 'tStartRefresh')  # time at next scr refresh
        dislike_prac_text_1.setAutoDraw(True)
    
    # *player_1* updates
    if player_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        player_1.frameNStart = frameN  # exact frame index
        player_1.tStart = t  # local t and not account for scr refresh
        player_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(player_1, 'tStartRefresh')  # time at next scr refresh
        player_1.setAutoDraw(True)
    # *click_prac_1* updates
    if click_prac_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        click_prac_1.frameNStart = frameN  # exact frame index
        click_prac_1.tStart = t  # local t and not account for scr refresh
        click_prac_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click_prac_1, 'tStartRefresh')  # time at next scr refresh
        click_prac_1.status = STARTED
        click_prac_1.mouseClock.reset()
        prevButtonState = click_prac_1.getPressed()  # if button is down already this ISN'T a new click
    if click_prac_1.status == STARTED:  # only update if started and not finished!
        buttons = click_prac_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([like_prac_button_1, dislike_prac_button_1])
                    clickableList = [like_prac_button_1, dislike_prac_button_1]
                except:
                    clickableList = [[like_prac_button_1, dislike_prac_button_1]]
                for obj in clickableList:
                    if obj.contains(click_prac_1):
                        gotValidClick = True
                        click_prac_1.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *vote_question_2* updates
    if vote_question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vote_question_2.frameNStart = frameN  # exact frame index
        vote_question_2.tStart = t  # local t and not account for scr refresh
        vote_question_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vote_question_2, 'tStartRefresh')  # time at next scr refresh
        vote_question_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_1aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_1a" ---
for thisComponent in Practice_1aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Practice_1a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Practice_1b" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_1bComponents = [wait, load_white1_3, fixation_prac_1]
for thisComponent in Practice_1bComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_1b" ---
while continueRoutine and routineTimer.getTime() < 2.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait* updates
    if wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait.frameNStart = frameN  # exact frame index
        wait.tStart = t  # local t and not account for scr refresh
        wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
        wait.setAutoDraw(True)
    if wait.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            wait.tStop = t  # not accounting for scr refresh
            wait.frameNStop = frameN  # exact frame index
            wait.setAutoDraw(False)
    
    # *load_white1_3* updates
    if load_white1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        load_white1_3.frameNStart = frameN  # exact frame index
        load_white1_3.tStart = t  # local t and not account for scr refresh
        load_white1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(load_white1_3, 'tStartRefresh')  # time at next scr refresh
        load_white1_3.setAutoDraw(True)
    if load_white1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > load_white1_3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            load_white1_3.tStop = t  # not accounting for scr refresh
            load_white1_3.frameNStop = frameN  # exact frame index
            load_white1_3.setAutoDraw(False)
    
    # *fixation_prac_1* updates
    if fixation_prac_1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_prac_1.frameNStart = frameN  # exact frame index
        fixation_prac_1.tStart = t  # local t and not account for scr refresh
        fixation_prac_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_prac_1, 'tStartRefresh')  # time at next scr refresh
        fixation_prac_1.setAutoDraw(True)
    if fixation_prac_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_prac_1.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            fixation_prac_1.tStop = t  # not accounting for scr refresh
            fixation_prac_1.frameNStop = frameN  # exact frame index
            fixation_prac_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_1bComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_1b" ---
for thisComponent in Practice_1bComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.500000)

# --- Prepare to start Routine "Practice_1c" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_1cComponents = [like_prac]
for thisComponent in Practice_1cComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_1c" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *like_prac* updates
    if like_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_prac.frameNStart = frameN  # exact frame index
        like_prac.tStart = t  # local t and not account for scr refresh
        like_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_prac, 'tStartRefresh')  # time at next scr refresh
        like_prac.setAutoDraw(True)
    if like_prac.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > like_prac.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            like_prac.tStop = t  # not accounting for scr refresh
            like_prac.frameNStop = frameN  # exact frame index
            like_prac.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_1cComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_1c" ---
for thisComponent in Practice_1cComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Practice_1d" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_1dComponents = [wait_2]
for thisComponent in Practice_1dComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_1d" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_2* updates
    if wait_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_2.frameNStart = frameN  # exact frame index
        wait_2.tStart = t  # local t and not account for scr refresh
        wait_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_2, 'tStartRefresh')  # time at next scr refresh
        wait_2.setAutoDraw(True)
    if wait_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            wait_2.tStop = t  # not accounting for scr refresh
            wait_2.frameNStop = frameN  # exact frame index
            wait_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_1dComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_1d" ---
for thisComponent in Practice_1dComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Practice_2a" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
prac_image_2.setImage('images/practice.png')
player_2.setText('Player 2')
# Run 'Begin Routine' code from code_9
player_2.bold = 'True'
# setup some python lists for storing info about the click_prac_2
click_prac_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Practice_2aComponents = [prac_image_2, like_prac_button_2, like_prac_text_2, dislike_prac_button_2, dislike_prac_text_2, player_2, click_prac_2, vote_question]
for thisComponent in Practice_2aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_2a" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_image_2* updates
    if prac_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_image_2.frameNStart = frameN  # exact frame index
        prac_image_2.tStart = t  # local t and not account for scr refresh
        prac_image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_image_2, 'tStartRefresh')  # time at next scr refresh
        prac_image_2.setAutoDraw(True)
    
    # *like_prac_button_2* updates
    if like_prac_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_prac_button_2.frameNStart = frameN  # exact frame index
        like_prac_button_2.tStart = t  # local t and not account for scr refresh
        like_prac_button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_prac_button_2, 'tStartRefresh')  # time at next scr refresh
        like_prac_button_2.setAutoDraw(True)
    
    # *like_prac_text_2* updates
    if like_prac_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_prac_text_2.frameNStart = frameN  # exact frame index
        like_prac_text_2.tStart = t  # local t and not account for scr refresh
        like_prac_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_prac_text_2, 'tStartRefresh')  # time at next scr refresh
        like_prac_text_2.setAutoDraw(True)
    
    # *dislike_prac_button_2* updates
    if dislike_prac_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dislike_prac_button_2.frameNStart = frameN  # exact frame index
        dislike_prac_button_2.tStart = t  # local t and not account for scr refresh
        dislike_prac_button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dislike_prac_button_2, 'tStartRefresh')  # time at next scr refresh
        dislike_prac_button_2.setAutoDraw(True)
    
    # *dislike_prac_text_2* updates
    if dislike_prac_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dislike_prac_text_2.frameNStart = frameN  # exact frame index
        dislike_prac_text_2.tStart = t  # local t and not account for scr refresh
        dislike_prac_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dislike_prac_text_2, 'tStartRefresh')  # time at next scr refresh
        dislike_prac_text_2.setAutoDraw(True)
    
    # *player_2* updates
    if player_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        player_2.frameNStart = frameN  # exact frame index
        player_2.tStart = t  # local t and not account for scr refresh
        player_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(player_2, 'tStartRefresh')  # time at next scr refresh
        player_2.setAutoDraw(True)
    # *click_prac_2* updates
    if click_prac_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        click_prac_2.frameNStart = frameN  # exact frame index
        click_prac_2.tStart = t  # local t and not account for scr refresh
        click_prac_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click_prac_2, 'tStartRefresh')  # time at next scr refresh
        click_prac_2.status = STARTED
        click_prac_2.mouseClock.reset()
        prevButtonState = click_prac_2.getPressed()  # if button is down already this ISN'T a new click
    if click_prac_2.status == STARTED:  # only update if started and not finished!
        buttons = click_prac_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([like_prac_button_2, dislike_prac_button_2])
                    clickableList = [like_prac_button_2, dislike_prac_button_2]
                except:
                    clickableList = [[like_prac_button_2, dislike_prac_button_2]]
                for obj in clickableList:
                    if obj.contains(click_prac_2):
                        gotValidClick = True
                        click_prac_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *vote_question* updates
    if vote_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vote_question.frameNStart = frameN  # exact frame index
        vote_question.tStart = t  # local t and not account for scr refresh
        vote_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vote_question, 'tStartRefresh')  # time at next scr refresh
        vote_question.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_2aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_2a" ---
for thisComponent in Practice_2aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Practice_2a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Practice_2b" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_2bComponents = [wait_3, load_white1_4, fixation_prac_2]
for thisComponent in Practice_2bComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_2b" ---
while continueRoutine and routineTimer.getTime() < 2.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_3* updates
    if wait_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_3.frameNStart = frameN  # exact frame index
        wait_3.tStart = t  # local t and not account for scr refresh
        wait_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_3, 'tStartRefresh')  # time at next scr refresh
        wait_3.setAutoDraw(True)
    if wait_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_3.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            wait_3.tStop = t  # not accounting for scr refresh
            wait_3.frameNStop = frameN  # exact frame index
            wait_3.setAutoDraw(False)
    
    # *load_white1_4* updates
    if load_white1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        load_white1_4.frameNStart = frameN  # exact frame index
        load_white1_4.tStart = t  # local t and not account for scr refresh
        load_white1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(load_white1_4, 'tStartRefresh')  # time at next scr refresh
        load_white1_4.setAutoDraw(True)
    if load_white1_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > load_white1_4.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            load_white1_4.tStop = t  # not accounting for scr refresh
            load_white1_4.frameNStop = frameN  # exact frame index
            load_white1_4.setAutoDraw(False)
    
    # *fixation_prac_2* updates
    if fixation_prac_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_prac_2.frameNStart = frameN  # exact frame index
        fixation_prac_2.tStart = t  # local t and not account for scr refresh
        fixation_prac_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_prac_2, 'tStartRefresh')  # time at next scr refresh
        fixation_prac_2.setAutoDraw(True)
    if fixation_prac_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_prac_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            fixation_prac_2.tStop = t  # not accounting for scr refresh
            fixation_prac_2.frameNStop = frameN  # exact frame index
            fixation_prac_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_2bComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_2b" ---
for thisComponent in Practice_2bComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.500000)

# --- Prepare to start Routine "Practice_2c" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
dislike_prac.setImage('images/thumb-down.png')
# keep track of which components have finished
Practice_2cComponents = [dislike_prac]
for thisComponent in Practice_2cComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_2c" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *dislike_prac* updates
    if dislike_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dislike_prac.frameNStart = frameN  # exact frame index
        dislike_prac.tStart = t  # local t and not account for scr refresh
        dislike_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dislike_prac, 'tStartRefresh')  # time at next scr refresh
        dislike_prac.setAutoDraw(True)
    if dislike_prac.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dislike_prac.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            dislike_prac.tStop = t  # not accounting for scr refresh
            dislike_prac.frameNStop = frameN  # exact frame index
            dislike_prac.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_2cComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_2c" ---
for thisComponent in Practice_2cComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Practice_2d" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_2dComponents = [wait_4]
for thisComponent in Practice_2dComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_2d" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_4* updates
    if wait_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_4.frameNStart = frameN  # exact frame index
        wait_4.tStart = t  # local t and not account for scr refresh
        wait_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_4, 'tStartRefresh')  # time at next scr refresh
        wait_4.setAutoDraw(True)
    if wait_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_4.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            wait_4.tStop = t  # not accounting for scr refresh
            wait_4.frameNStop = frameN  # exact frame index
            wait_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_2dComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_2d" ---
for thisComponent in Practice_2dComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "Introduction_7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_9.setText('Now it’s time to vote for real.')
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# Run 'Begin Routine' code from bold_intro_7
next_intro7.bold = True
# keep track of which components have finished
Introduction_7Components = [image_12, polygon_9, text_9, key_resp_9, next_intro7]
for thisComponent in Introduction_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    
    # *polygon_9* updates
    if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_9.frameNStart = frameN  # exact frame index
        polygon_9.tStart = t  # local t and not account for scr refresh
        polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
        polygon_9.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro7* updates
    if next_intro7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro7.frameNStart = frameN  # exact frame index
        next_intro7.tStart = t  # local t and not account for scr refresh
        next_intro7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro7, 'tStartRefresh')  # time at next scr refresh
        next_intro7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_7" ---
for thisComponent in Introduction_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
voting_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='voting_1')
thisExp.addLoop(voting_1)  # add the loop to the experiment
thisVoting_1 = voting_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVoting_1.rgb)
if thisVoting_1 != None:
    for paramName in thisVoting_1:
        exec('{} = thisVoting_1[paramName]'.format(paramName))

for thisVoting_1 in voting_1:
    currentLoop = voting_1
    # abbreviate parameter names if possible (e.g. rgb = thisVoting_1.rgb)
    if thisVoting_1 != None:
        for paramName in thisVoting_1:
            exec('{} = thisVoting_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Player_profiles_voting_style" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    coplayer_image_2.setImage(photos[a])
    cop_prompts.reset()
    cop_response.setText(names[a] + '\n' + str(ages[a]) + '\n' + hometowns[a] + '\n' + interests[a] + '\n' + schools[a])
    # Run 'Begin Routine' code from capitalization_cop
    cop_response.alignText = 'left'
    cop_age_st = (str(cop_age))
    cop_prompts.alignText = 'left'
    
    # increment i for each loop
    a = a + 1
    print(a)
    
    # setup some python lists for storing info about the click_real_1
    click_real_1.clicked_name = []
    gotValidClick = False  # until a click is received
    vote_question_3.setText('Do you like or dislike ' + names[a] + '?')
    # keep track of which components have finished
    Player_profiles_voting_styleComponents = [border_2, coplayer_image_2, cop_prompts, cop_response, like_real_button_1, like_real_text_1, dislike_real_button_1, dislike_real_text_1, click_real_1, vote_question_3]
    for thisComponent in Player_profiles_voting_styleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Player_profiles_voting_style" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *border_2* updates
        if border_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_2.frameNStart = frameN  # exact frame index
            border_2.tStart = t  # local t and not account for scr refresh
            border_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_2, 'tStartRefresh')  # time at next scr refresh
            border_2.setAutoDraw(True)
        
        # *coplayer_image_2* updates
        if coplayer_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            coplayer_image_2.frameNStart = frameN  # exact frame index
            coplayer_image_2.tStart = t  # local t and not account for scr refresh
            coplayer_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(coplayer_image_2, 'tStartRefresh')  # time at next scr refresh
            coplayer_image_2.setAutoDraw(True)
        
        # *cop_prompts* updates
        if cop_prompts.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts.frameNStart = frameN  # exact frame index
            cop_prompts.tStart = t  # local t and not account for scr refresh
            cop_prompts.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts, 'tStartRefresh')  # time at next scr refresh
            cop_prompts.setAutoDraw(True)
        
        # *cop_response* updates
        if cop_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_response.frameNStart = frameN  # exact frame index
            cop_response.tStart = t  # local t and not account for scr refresh
            cop_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_response, 'tStartRefresh')  # time at next scr refresh
            cop_response.setAutoDraw(True)
        # Run 'Each Frame' code from capitalization_cop
        cop_prompts.alignText = 'left'
        
        # *like_real_button_1* updates
        if like_real_button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_button_1.frameNStart = frameN  # exact frame index
            like_real_button_1.tStart = t  # local t and not account for scr refresh
            like_real_button_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_button_1, 'tStartRefresh')  # time at next scr refresh
            like_real_button_1.setAutoDraw(True)
        
        # *like_real_text_1* updates
        if like_real_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_text_1.frameNStart = frameN  # exact frame index
            like_real_text_1.tStart = t  # local t and not account for scr refresh
            like_real_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_text_1, 'tStartRefresh')  # time at next scr refresh
            like_real_text_1.setAutoDraw(True)
        
        # *dislike_real_button_1* updates
        if dislike_real_button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_button_1.frameNStart = frameN  # exact frame index
            dislike_real_button_1.tStart = t  # local t and not account for scr refresh
            dislike_real_button_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_button_1, 'tStartRefresh')  # time at next scr refresh
            dislike_real_button_1.setAutoDraw(True)
        
        # *dislike_real_text_1* updates
        if dislike_real_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_text_1.frameNStart = frameN  # exact frame index
            dislike_real_text_1.tStart = t  # local t and not account for scr refresh
            dislike_real_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_text_1, 'tStartRefresh')  # time at next scr refresh
            dislike_real_text_1.setAutoDraw(True)
        # *click_real_1* updates
        if click_real_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            click_real_1.frameNStart = frameN  # exact frame index
            click_real_1.tStart = t  # local t and not account for scr refresh
            click_real_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_real_1, 'tStartRefresh')  # time at next scr refresh
            click_real_1.status = STARTED
            click_real_1.mouseClock.reset()
            prevButtonState = click_real_1.getPressed()  # if button is down already this ISN'T a new click
        if click_real_1.status == STARTED:  # only update if started and not finished!
            buttons = click_real_1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([like_real_button_1, dislike_real_button_1])
                        clickableList = [like_real_button_1, dislike_real_button_1]
                    except:
                        clickableList = [[like_real_button_1, dislike_real_button_1]]
                    for obj in clickableList:
                        if obj.contains(click_real_1):
                            gotValidClick = True
                            click_real_1.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *vote_question_3* updates
        if vote_question_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_question_3.frameNStart = frameN  # exact frame index
            vote_question_3.tStart = t  # local t and not account for scr refresh
            vote_question_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_question_3, 'tStartRefresh')  # time at next scr refresh
            vote_question_3.setAutoDraw(True)
        # Run 'Each Frame' code from ptp_vote_1
        ptp_v = ''
        if mouse.isPressedIn(like_real_button_1):
            ptp_v="Like"
        elif mouse.isPressedIn(dislike_real_button_1):
            ptp_v ="Dislike"
        voting_1.addData('Participant_vote', ptp_v)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Player_profiles_voting_styleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Player_profiles_voting_style" ---
    for thisComponent in Player_profiles_voting_styleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for voting_1 (TrialHandler)
    # the Routine "Player_profiles_voting_style" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting_vote" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_5.setText('Compiling votes, your feedback\nwill be presented soon...')
    # keep track of which components have finished
    Waiting_voteComponents = [wait_5, load_white1, fixation_r_1]
    for thisComponent in Waiting_voteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_5* updates
        if wait_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_5.frameNStart = frameN  # exact frame index
            wait_5.tStart = t  # local t and not account for scr refresh
            wait_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_5, 'tStartRefresh')  # time at next scr refresh
            wait_5.setAutoDraw(True)
        if wait_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_5.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                wait_5.tStop = t  # not accounting for scr refresh
                wait_5.frameNStop = frameN  # exact frame index
                wait_5.setAutoDraw(False)
        
        # *load_white1* updates
        if load_white1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            load_white1.frameNStart = frameN  # exact frame index
            load_white1.tStart = t  # local t and not account for scr refresh
            load_white1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_white1, 'tStartRefresh')  # time at next scr refresh
            load_white1.setAutoDraw(True)
        if load_white1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > load_white1.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                load_white1.tStop = t  # not accounting for scr refresh
                load_white1.frameNStop = frameN  # exact frame index
                load_white1.setAutoDraw(False)
        
        # *fixation_r_1* updates
        if fixation_r_1.status == NOT_STARTED and tThisFlip >= vote_duration-frameTolerance:
            # keep track of start time/frame for later
            fixation_r_1.frameNStart = frameN  # exact frame index
            fixation_r_1.tStart = t  # local t and not account for scr refresh
            fixation_r_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_r_1, 'tStartRefresh')  # time at next scr refresh
            fixation_r_1.setAutoDraw(True)
        if fixation_r_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_r_1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_r_1.tStop = t  # not accounting for scr refresh
                fixation_r_1.frameNStop = frameN  # exact frame index
                fixation_r_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_voteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote" ---
    for thisComponent in Waiting_voteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Waiting_vote" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cop_vote" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_thumb
    if vote_all[a][0] == '1':
        image_thumb = 'images/thumb-up.png'
        save_vote = 'Like'
        play_round = '1'
        cop_type = vote_all[a][5]
    else:
        image_thumb = 'images/thumb-down.png'
        save_vote = 'Dislike'
        play_round = '1'
        cop_type = vote_all[a][5]
    voting_1.addData('Study ID', expInfo['Study ID'])
    voting_1.addData('Coplayer_vote', save_vote)
    voting_1.addData('Round', play_round)
    voting_1.addData('Coplayer_type', cop_type)
    
    vote_image.setImage(image_thumb)
    # keep track of which components have finished
    Cop_voteComponents = [vote_image]
    for thisComponent in Cop_voteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cop_vote" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vote_image* updates
        if vote_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            vote_image.frameNStart = frameN  # exact frame index
            vote_image.tStart = t  # local t and not account for scr refresh
            vote_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_image, 'tStartRefresh')  # time at next scr refresh
            vote_image.setAutoDraw(True)
        if vote_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vote_image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                vote_image.tStop = t  # not accounting for scr refresh
                vote_image.frameNStop = frameN  # exact frame index
                vote_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cop_voteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cop_vote" ---
    for thisComponent in Cop_voteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Waiting_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_7.setText('+')
    # keep track of which components have finished
    Waiting_vote_3Components = [wait_7]
    for thisComponent in Waiting_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_7* updates
        if wait_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_7.frameNStart = frameN  # exact frame index
            wait_7.tStart = t  # local t and not account for scr refresh
            wait_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_7, 'tStartRefresh')  # time at next scr refresh
            wait_7.setAutoDraw(True)
        if wait_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wait_7.tStop = t  # not accounting for scr refresh
                wait_7.frameNStop = frameN  # exact frame index
                wait_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_3" ---
    for thisComponent in Waiting_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'voting_1'

# get names of stimulus parameters
if voting_1.trialList in ([], [None], None):
    params = []
else:
    params = voting_1.trialList[0].keys()
# save data for this loop
voting_1.saveAsExcel(filename + '.xlsx', sheetName='voting_1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
voting_1.saveAsText(filename + 'voting_1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Waiting_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_12.setText('Let’s find out who got the MOST like votes this round...')
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Waiting_3Components = [image_15, polygon_12, text_12, key_resp_12, image_16]
for thisComponent in Waiting_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_3" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            image_15.setAutoDraw(False)
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    if polygon_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_12.tStop = t  # not accounting for scr refresh
            polygon_12.frameNStop = frameN  # exact frame index
            polygon_12.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            text_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            image_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_3" ---
for thisComponent in Waiting_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Most_vote_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
most_pic_1.setImage('images/background_mostvote.jpg')
most_vote_1.setImage(photos[m])
name_most_1.setText(names[m])
next_most1.keys = []
next_most1.rt = []
_next_most1_allKeys = []
# keep track of which components have finished
Most_vote_1Components = [most_pic_1, border_8, border_9, most_vote_1, name_most_1, next_most_1, next_most1]
for thisComponent in Most_vote_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Most_vote_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *most_pic_1* updates
    if most_pic_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_pic_1.frameNStart = frameN  # exact frame index
        most_pic_1.tStart = t  # local t and not account for scr refresh
        most_pic_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_pic_1, 'tStartRefresh')  # time at next scr refresh
        most_pic_1.setAutoDraw(True)
    
    # *border_8* updates
    if border_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_8.frameNStart = frameN  # exact frame index
        border_8.tStart = t  # local t and not account for scr refresh
        border_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_8, 'tStartRefresh')  # time at next scr refresh
        border_8.setAutoDraw(True)
    
    # *border_9* updates
    if border_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_9.frameNStart = frameN  # exact frame index
        border_9.tStart = t  # local t and not account for scr refresh
        border_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_9, 'tStartRefresh')  # time at next scr refresh
        border_9.setAutoDraw(True)
    
    # *most_vote_1* updates
    if most_vote_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_vote_1.frameNStart = frameN  # exact frame index
        most_vote_1.tStart = t  # local t and not account for scr refresh
        most_vote_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_vote_1, 'tStartRefresh')  # time at next scr refresh
        most_vote_1.setAutoDraw(True)
    
    # *name_most_1* updates
    if name_most_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_most_1.frameNStart = frameN  # exact frame index
        name_most_1.tStart = t  # local t and not account for scr refresh
        name_most_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_most_1, 'tStartRefresh')  # time at next scr refresh
        name_most_1.setAutoDraw(True)
    
    # *next_most_1* updates
    if next_most_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most_1.frameNStart = frameN  # exact frame index
        next_most_1.tStart = t  # local t and not account for scr refresh
        next_most_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most_1, 'tStartRefresh')  # time at next scr refresh
        next_most_1.setAutoDraw(True)
    
    # *next_most1* updates
    waitOnFlip = False
    if next_most1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most1.frameNStart = frameN  # exact frame index
        next_most1.tStart = t  # local t and not account for scr refresh
        next_most1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most1, 'tStartRefresh')  # time at next scr refresh
        next_most1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_most1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_most1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_most1.status == STARTED and not waitOnFlip:
        theseKeys = next_most1.getKeys(keyList=['space'], waitRelease=False)
        _next_most1_allKeys.extend(theseKeys)
        if len(_next_most1_allKeys):
            next_most1.keys = _next_most1_allKeys[-1].name  # just the last key pressed
            next_most1.rt = _next_most1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Most_vote_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Most_vote_1" ---
for thisComponent in Most_vote_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Most_vote_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_13.setText('Let’s find out who got the LEAST like votes this round...')
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Waiting_4Components = [image_17, polygon_13, text_13, key_resp_14, image_18]
for thisComponent in Waiting_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_4" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            image_17.setAutoDraw(False)
    
    # *polygon_13* updates
    if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.tStart = t  # local t and not account for scr refresh
        polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
        polygon_13.setAutoDraw(True)
    if polygon_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_13.tStop = t  # not accounting for scr refresh
            polygon_13.frameNStop = frameN  # exact frame index
            polygon_13.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            text_13.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            image_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_4" ---
for thisComponent in Waiting_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Least_vote_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image_20.setImage('images/sad.png')
least_vote_1.setImage(photos[l])
name_least_1.setText(names[l])
next_least1.keys = []
next_least1.rt = []
_next_least1_allKeys = []
# keep track of which components have finished
Least_vote_1Components = [image_20, border4_4, border_6, least_vote_1, name_least_1, next_least_1, next_least1]
for thisComponent in Least_vote_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Least_vote_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_20* updates
    if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_20.frameNStart = frameN  # exact frame index
        image_20.tStart = t  # local t and not account for scr refresh
        image_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
        image_20.setAutoDraw(True)
    
    # *border4_4* updates
    if border4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border4_4.frameNStart = frameN  # exact frame index
        border4_4.tStart = t  # local t and not account for scr refresh
        border4_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border4_4, 'tStartRefresh')  # time at next scr refresh
        border4_4.setAutoDraw(True)
    
    # *border_6* updates
    if border_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_6.frameNStart = frameN  # exact frame index
        border_6.tStart = t  # local t and not account for scr refresh
        border_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_6, 'tStartRefresh')  # time at next scr refresh
        border_6.setAutoDraw(True)
    
    # *least_vote_1* updates
    if least_vote_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        least_vote_1.frameNStart = frameN  # exact frame index
        least_vote_1.tStart = t  # local t and not account for scr refresh
        least_vote_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(least_vote_1, 'tStartRefresh')  # time at next scr refresh
        least_vote_1.setAutoDraw(True)
    
    # *name_least_1* updates
    if name_least_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_least_1.frameNStart = frameN  # exact frame index
        name_least_1.tStart = t  # local t and not account for scr refresh
        name_least_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_least_1, 'tStartRefresh')  # time at next scr refresh
        name_least_1.setAutoDraw(True)
    
    # *next_least_1* updates
    if next_least_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least_1.frameNStart = frameN  # exact frame index
        next_least_1.tStart = t  # local t and not account for scr refresh
        next_least_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least_1, 'tStartRefresh')  # time at next scr refresh
        next_least_1.setAutoDraw(True)
    
    # *next_least1* updates
    waitOnFlip = False
    if next_least1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least1.frameNStart = frameN  # exact frame index
        next_least1.tStart = t  # local t and not account for scr refresh
        next_least1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least1, 'tStartRefresh')  # time at next scr refresh
        next_least1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_least1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_least1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_least1.status == STARTED and not waitOnFlip:
        theseKeys = next_least1.getKeys(keyList=['space'], waitRelease=False)
        _next_least1_allKeys.extend(theseKeys)
        if len(_next_least1_allKeys):
            next_least1.keys = _next_least1_allKeys[-1].name  # just the last key pressed
            next_least1.rt = _next_least1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Least_vote_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Least_vote_1" ---
for thisComponent in Least_vote_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from least_code_1
# create random index numbers for most/least player
m = most_least_index[2]
l = most_least_index[3]
# the Routine "Least_vote_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "round_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_27.setText('Time to move on to the next round. We are getting closer to the virtual party! Let’s see if you will be invited.')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
next_intro3_4.setText('Press space to continue.')
# Run 'Begin Routine' code from code_32
next_intro3_4.bold = 'True'
# keep track of which components have finished
round_1Components = [image_36, polygon_24, text_27, key_resp_23, next_intro3_4]
for thisComponent in round_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "round_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_36* updates
    if image_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_36.frameNStart = frameN  # exact frame index
        image_36.tStart = t  # local t and not account for scr refresh
        image_36.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_36, 'tStartRefresh')  # time at next scr refresh
        image_36.setAutoDraw(True)
    
    # *polygon_24* updates
    if polygon_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_24.frameNStart = frameN  # exact frame index
        polygon_24.tStart = t  # local t and not account for scr refresh
        polygon_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_24, 'tStartRefresh')  # time at next scr refresh
        polygon_24.setAutoDraw(True)
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    
    # *key_resp_23* updates
    waitOnFlip = False
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_4* updates
    if next_intro3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_4.frameNStart = frameN  # exact frame index
        next_intro3_4.tStart = t  # local t and not account for scr refresh
        next_intro3_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_4, 'tStartRefresh')  # time at next scr refresh
        next_intro3_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "round_1" ---
for thisComponent in round_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "round_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
poll_load = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='poll_load')
thisExp.addLoop(poll_load)  # add the loop to the experiment
thisPoll_load = poll_load.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPoll_load.rgb)
if thisPoll_load != None:
    for paramName in thisPoll_load:
        exec('{} = thisPoll_load[paramName]'.format(paramName))

for thisPoll_load in poll_load:
    currentLoop = poll_load
    # abbreviate parameter names if possible (e.g. rgb = thisPoll_load.rgb)
    if thisPoll_load != None:
        for paramName in thisPoll_load:
            exec('{} = thisPoll_load[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Poll_loader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_poll_loader
    poll_1.append(cop_poll1)
    poll_2.append(cop_poll2)
    poll_3.append(cop_poll3)
    poll_4.append(cop_poll4)
    
    shuffle(poll_1)
    shuffle(poll_2)
    shuffle(poll_3)
    shuffle(poll_4)
    # keep track of which components have finished
    Poll_loaderComponents = []
    for thisComponent in Poll_loaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Poll_loader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Poll_loaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Poll_loader" ---
    for thisComponent in Poll_loaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Poll_loader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'poll_load'

# get names of stimulus parameters
if poll_load.trialList in ([], [None], None):
    params = []
else:
    params = poll_load.trialList[0].keys()
# save data for this loop
poll_load.saveAsExcel(filename + '.xlsx', sheetName='poll_load',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
poll_load.saveAsText(filename + 'poll_load.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Introduction_9" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_17.keys = []
key_resp_17.rt = []
_key_resp_17_allKeys = []
# keep track of which components have finished
Introduction_9Components = [image_22, polygon_15, text_15, next_intro7_6, key_resp_17]
for thisComponent in Introduction_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_9" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_22* updates
    if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_22.frameNStart = frameN  # exact frame index
        image_22.tStart = t  # local t and not account for scr refresh
        image_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
        image_22.setAutoDraw(True)
    
    # *polygon_15* updates
    if polygon_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_15.frameNStart = frameN  # exact frame index
        polygon_15.tStart = t  # local t and not account for scr refresh
        polygon_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
        polygon_15.setAutoDraw(True)
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *next_intro7_6* updates
    if next_intro7_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro7_6.frameNStart = frameN  # exact frame index
        next_intro7_6.tStart = t  # local t and not account for scr refresh
        next_intro7_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro7_6, 'tStartRefresh')  # time at next scr refresh
        next_intro7_6.setAutoDraw(True)
    
    # *key_resp_17* updates
    waitOnFlip = False
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_17_allKeys.extend(theseKeys)
        if len(_key_resp_17_allKeys):
            key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
            key_resp_17.rt = _key_resp_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_9" ---
for thisComponent in Introduction_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Poll_q1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
poll_question_1.setText('What is your favorite movie?')
poll_enter_1.reset()
poll_enter_1.setText('')
# setup some python lists for storing info about the mouse5
mouse5.clicked_name = []
gotValidClick = False  # until a click is received
ptp_poll_1 = poll_enter_1.text  # Set routine start values for ptp_poll_1
# keep track of which components have finished
Poll_q1Components = [poll_question_1, poll_enter_1, button5, submit5, mouse5]
for thisComponent in Poll_q1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Poll_q1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *poll_question_1* updates
    if poll_question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_question_1.frameNStart = frameN  # exact frame index
        poll_question_1.tStart = t  # local t and not account for scr refresh
        poll_question_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_question_1, 'tStartRefresh')  # time at next scr refresh
        poll_question_1.setAutoDraw(True)
    
    # *poll_enter_1* updates
    if poll_enter_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_enter_1.frameNStart = frameN  # exact frame index
        poll_enter_1.tStart = t  # local t and not account for scr refresh
        poll_enter_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_enter_1, 'tStartRefresh')  # time at next scr refresh
        poll_enter_1.setAutoDraw(True)
    
    # *button5* updates
    if button5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button5.frameNStart = frameN  # exact frame index
        button5.tStart = t  # local t and not account for scr refresh
        button5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5, 'tStartRefresh')  # time at next scr refresh
        button5.setAutoDraw(True)
    
    # *submit5* updates
    if submit5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit5.frameNStart = frameN  # exact frame index
        submit5.tStart = t  # local t and not account for scr refresh
        submit5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit5, 'tStartRefresh')  # time at next scr refresh
        submit5.setAutoDraw(True)
    # *mouse5* updates
    if mouse5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5.frameNStart = frameN  # exact frame index
        mouse5.tStart = t  # local t and not account for scr refresh
        mouse5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5, 'tStartRefresh')  # time at next scr refresh
        mouse5.status = STARTED
        mouse5.mouseClock.reset()
        prevButtonState = mouse5.getPressed()  # if button is down already this ISN'T a new click
    if mouse5.status == STARTED:  # only update if started and not finished!
        buttons = mouse5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button5)
                    clickableList = button5
                except:
                    clickableList = [button5]
                for obj in clickableList:
                    if obj.contains(mouse5):
                        gotValidClick = True
                        mouse5.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_poll_1 = poll_enter_1.text  # Set frame start values for ptp_poll_1
    ptp_poll_1Container.append(ptp_poll_1)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Poll_q1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Poll_q1" ---
for thisComponent in Poll_q1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('poll_enter_1.text',poll_enter_1.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_poll_1.routineEndVal', ptp_poll_1)  # Save end routine value
# the Routine "Poll_q1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_11.setText('Waiting for others to answer the poll question...')
# keep track of which components have finished
Waiting_5Components = [image_19, polygon_16, text_11, image_23]
for thisComponent in Waiting_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_5" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            image_19.setAutoDraw(False)
    
    # *polygon_16* updates
    if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_16.frameNStart = frameN  # exact frame index
        polygon_16.tStart = t  # local t and not account for scr refresh
        polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
        polygon_16.setAutoDraw(True)
    if polygon_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_16.tStop = t  # not accounting for scr refresh
            polygon_16.frameNStop = frameN  # exact frame index
            polygon_16.setAutoDraw(False)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            text_11.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            image_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_5" ---
for thisComponent in Waiting_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Introduction_10" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_16.setText("All players have answered the poll question now.\n\nLet's see the responses!")
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
next_intro3_2.setText('Press space to continue.')
# Run 'Begin Routine' code from code_20
next_intro3_2.bold = 'True'
# keep track of which components have finished
Introduction_10Components = [image_24, polygon_17, text_16, key_resp_18, next_intro3_2]
for thisComponent in Introduction_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_10" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *polygon_17* updates
    if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.tStart = t  # local t and not account for scr refresh
        polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
        polygon_17.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_2* updates
    if next_intro3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_2.frameNStart = frameN  # exact frame index
        next_intro3_2.tStart = t  # local t and not account for scr refresh
        next_intro3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_2, 'tStartRefresh')  # time at next scr refresh
        next_intro3_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_10" ---
for thisComponent in Introduction_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_1_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
poll_1_1_names.setText(ptp_name +':' + '\n'+ names[0]+':' +'\n'+ names[1]+':'+'\n'+ names[2]+':'+'\n'+ names[3]+':' +'\n'+ names[4]+':' +'\n'+ names[5]+':'+'\n'+ names[6]+':')
poll_1_1_responses.setText(ptp_poll_1 +'\n' + poll_1[0] +'\n'+ poll_1[1] +'\n'+ poll_1[2] +'\n'+ poll_1[3] +'\n'+ poll_1[4] +'\n'+ poll_1[5] +'\n'+ poll_1[6])
# Run 'Begin Routine' code from poll_code_1
poll_next_1_1.bold = 'True'
poll_1_1_names.alignText = 'Left'
poll_1_1_names.bold = 'True'
poll_1_1_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_1_1Components = [image_14, polygon_11, key_resp_11, poll_next_1_1, poll_1_1_names, poll_1_1_responses]
for thisComponent in poll_resp_1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_1_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_14* updates
    if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_14.frameNStart = frameN  # exact frame index
        image_14.tStart = t  # local t and not account for scr refresh
        image_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
        image_14.setAutoDraw(True)
    
    # *polygon_11* updates
    if polygon_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_11.frameNStart = frameN  # exact frame index
        polygon_11.tStart = t  # local t and not account for scr refresh
        polygon_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
        polygon_11.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_1_1* updates
    if poll_next_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_1_1.frameNStart = frameN  # exact frame index
        poll_next_1_1.tStart = t  # local t and not account for scr refresh
        poll_next_1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_1_1, 'tStartRefresh')  # time at next scr refresh
        poll_next_1_1.setAutoDraw(True)
    
    # *poll_1_1_names* updates
    if poll_1_1_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_1_1_names.frameNStart = frameN  # exact frame index
        poll_1_1_names.tStart = t  # local t and not account for scr refresh
        poll_1_1_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_1_1_names, 'tStartRefresh')  # time at next scr refresh
        poll_1_1_names.setAutoDraw(True)
    
    # *poll_1_1_responses* updates
    if poll_1_1_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_1_1_responses.frameNStart = frameN  # exact frame index
        poll_1_1_responses.tStart = t  # local t and not account for scr refresh
        poll_1_1_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_1_1_responses, 'tStartRefresh')  # time at next scr refresh
        poll_1_1_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_1_1" ---
for thisComponent in poll_resp_1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_1_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_29.keys = []
key_resp_29.rt = []
_key_resp_29_allKeys = []
poll_1_2_names.setText(names[7]+':' +'\n'+ names[8]+':'+'\n'+ names[9]+':'+'\n'+ names[10]+':' +'\n'+ names[11]+':')
poll_1_2_responses.setText(poll_1[7] +'\n'+ poll_1[8] +'\n'+ poll_1[9] +'\n'+ poll_1[10] +'\n'+ poll_1[11] )
# Run 'Begin Routine' code from poll_code_5
poll_next_1_2.bold = 'True'
poll_1_2_names.alignText = 'Left'
poll_1_2_names.bold = 'True'
poll_1_2_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_1_2Components = [image_42, polygon_30, key_resp_29, poll_next_1_2, poll_1_2_names, poll_1_2_responses]
for thisComponent in poll_resp_1_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_1_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_42* updates
    if image_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_42.frameNStart = frameN  # exact frame index
        image_42.tStart = t  # local t and not account for scr refresh
        image_42.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_42, 'tStartRefresh')  # time at next scr refresh
        image_42.setAutoDraw(True)
    
    # *polygon_30* updates
    if polygon_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_30.frameNStart = frameN  # exact frame index
        polygon_30.tStart = t  # local t and not account for scr refresh
        polygon_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_30, 'tStartRefresh')  # time at next scr refresh
        polygon_30.setAutoDraw(True)
    
    # *key_resp_29* updates
    waitOnFlip = False
    if key_resp_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_29.frameNStart = frameN  # exact frame index
        key_resp_29.tStart = t  # local t and not account for scr refresh
        key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
        key_resp_29.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_29.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_29.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_29_allKeys.extend(theseKeys)
        if len(_key_resp_29_allKeys):
            key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
            key_resp_29.rt = _key_resp_29_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_1_2* updates
    if poll_next_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_1_2.frameNStart = frameN  # exact frame index
        poll_next_1_2.tStart = t  # local t and not account for scr refresh
        poll_next_1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_1_2, 'tStartRefresh')  # time at next scr refresh
        poll_next_1_2.setAutoDraw(True)
    
    # *poll_1_2_names* updates
    if poll_1_2_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_1_2_names.frameNStart = frameN  # exact frame index
        poll_1_2_names.tStart = t  # local t and not account for scr refresh
        poll_1_2_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_1_2_names, 'tStartRefresh')  # time at next scr refresh
        poll_1_2_names.setAutoDraw(True)
    
    # *poll_1_2_responses* updates
    if poll_1_2_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_1_2_responses.frameNStart = frameN  # exact frame index
        poll_1_2_responses.tStart = t  # local t and not account for scr refresh
        poll_1_2_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_1_2_responses, 'tStartRefresh')  # time at next scr refresh
        poll_1_2_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_1_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_1_2" ---
for thisComponent in poll_resp_1_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_1_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_11" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_17.setText('Time to move on to the next round. We are getting closer to the virtual party! \n\nLet’s see if you will be invited. ')
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
next_intro3_3.setText('Press space to continue.')
# Run 'Begin Routine' code from code_21
next_intro3_3.bold = 'True'
# keep track of which components have finished
Introduction_11Components = [image_25, polygon_18, text_17, key_resp_19, next_intro3_3]
for thisComponent in Introduction_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_11" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    
    # *polygon_18* updates
    if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.tStart = t  # local t and not account for scr refresh
        polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
        polygon_18.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_3* updates
    if next_intro3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_3.frameNStart = frameN  # exact frame index
        next_intro3_3.tStart = t  # local t and not account for scr refresh
        next_intro3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_3, 'tStartRefresh')  # time at next scr refresh
        next_intro3_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_11" ---
for thisComponent in Introduction_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
voting_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='voting_2')
thisExp.addLoop(voting_2)  # add the loop to the experiment
thisVoting_2 = voting_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVoting_2.rgb)
if thisVoting_2 != None:
    for paramName in thisVoting_2:
        exec('{} = thisVoting_2[paramName]'.format(paramName))

for thisVoting_2 in voting_2:
    currentLoop = voting_2
    # abbreviate parameter names if possible (e.g. rgb = thisVoting_2.rgb)
    if thisVoting_2 != None:
        for paramName in thisVoting_2:
            exec('{} = thisVoting_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Player_profiles_voting_style_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from capitalization_cop_2
    cop_response_2.alignText = 'left'
    cop_prompts_2.alignText = 'left'
    
    
    # increment b for each loop
    b = b + 1
    
    coplayer_image.setImage(photos[b])
    cop_prompts_2.reset()
    cop_response_2.setText(names[b] + '\n' + str(ages[b]) + '\n' + hometowns[b] + '\n' + interests[b] + '\n' + schools[b])
    # setup some python lists for storing info about the click_real_2
    click_real_2.clicked_name = []
    gotValidClick = False  # until a click is received
    vote_question_4.setText('Do you like or dislike ' + names[b] + '?')
    # keep track of which components have finished
    Player_profiles_voting_style_2Components = [border_4, coplayer_image, cop_prompts_2, cop_response_2, like_real_button_2, like_real_text_2, dislike_real_button_2, dislike_real_text_2, click_real_2, vote_question_4]
    for thisComponent in Player_profiles_voting_style_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Player_profiles_voting_style_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *border_4* updates
        if border_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_4.frameNStart = frameN  # exact frame index
            border_4.tStart = t  # local t and not account for scr refresh
            border_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_4, 'tStartRefresh')  # time at next scr refresh
            border_4.setAutoDraw(True)
        
        # *coplayer_image* updates
        if coplayer_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            coplayer_image.frameNStart = frameN  # exact frame index
            coplayer_image.tStart = t  # local t and not account for scr refresh
            coplayer_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(coplayer_image, 'tStartRefresh')  # time at next scr refresh
            coplayer_image.setAutoDraw(True)
        
        # *cop_prompts_2* updates
        if cop_prompts_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts_2.frameNStart = frameN  # exact frame index
            cop_prompts_2.tStart = t  # local t and not account for scr refresh
            cop_prompts_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts_2, 'tStartRefresh')  # time at next scr refresh
            cop_prompts_2.setAutoDraw(True)
        
        # *cop_response_2* updates
        if cop_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_response_2.frameNStart = frameN  # exact frame index
            cop_response_2.tStart = t  # local t and not account for scr refresh
            cop_response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_response_2, 'tStartRefresh')  # time at next scr refresh
            cop_response_2.setAutoDraw(True)
        
        # *like_real_button_2* updates
        if like_real_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_button_2.frameNStart = frameN  # exact frame index
            like_real_button_2.tStart = t  # local t and not account for scr refresh
            like_real_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_button_2, 'tStartRefresh')  # time at next scr refresh
            like_real_button_2.setAutoDraw(True)
        
        # *like_real_text_2* updates
        if like_real_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_text_2.frameNStart = frameN  # exact frame index
            like_real_text_2.tStart = t  # local t and not account for scr refresh
            like_real_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'like_real_text_2.started')
            like_real_text_2.setAutoDraw(True)
        
        # *dislike_real_button_2* updates
        if dislike_real_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_button_2.frameNStart = frameN  # exact frame index
            dislike_real_button_2.tStart = t  # local t and not account for scr refresh
            dislike_real_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_button_2, 'tStartRefresh')  # time at next scr refresh
            dislike_real_button_2.setAutoDraw(True)
        
        # *dislike_real_text_2* updates
        if dislike_real_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_text_2.frameNStart = frameN  # exact frame index
            dislike_real_text_2.tStart = t  # local t and not account for scr refresh
            dislike_real_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_text_2, 'tStartRefresh')  # time at next scr refresh
            dislike_real_text_2.setAutoDraw(True)
        # *click_real_2* updates
        if click_real_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            click_real_2.frameNStart = frameN  # exact frame index
            click_real_2.tStart = t  # local t and not account for scr refresh
            click_real_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_real_2, 'tStartRefresh')  # time at next scr refresh
            click_real_2.status = STARTED
            click_real_2.mouseClock.reset()
            prevButtonState = click_real_2.getPressed()  # if button is down already this ISN'T a new click
        if click_real_2.status == STARTED:  # only update if started and not finished!
            buttons = click_real_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([like_real_button_2, dislike_real_button_2])
                        clickableList = [like_real_button_2, dislike_real_button_2]
                    except:
                        clickableList = [[like_real_button_2, dislike_real_button_2]]
                    for obj in clickableList:
                        if obj.contains(click_real_2):
                            gotValidClick = True
                            click_real_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *vote_question_4* updates
        if vote_question_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_question_4.frameNStart = frameN  # exact frame index
            vote_question_4.tStart = t  # local t and not account for scr refresh
            vote_question_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_question_4, 'tStartRefresh')  # time at next scr refresh
            vote_question_4.setAutoDraw(True)
        # Run 'Each Frame' code from ptp_vote_2
        ptp_v = ''
        if mouse.isPressedIn(like_real_button_2):
            ptp_v="Like"
        elif mouse.isPressedIn(dislike_real_button_2):
            ptp_v ="Dislike"
        voting_2.addData('Participant_vote', ptp_v)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Player_profiles_voting_style_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Player_profiles_voting_style_2" ---
    for thisComponent in Player_profiles_voting_style_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for voting_2 (TrialHandler)
    # the Routine "Player_profiles_voting_style_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting_vote_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_6.setText('Compiling votes, your feedback\nwill be presented soon...')
    # keep track of which components have finished
    Waiting_vote_2Components = [wait_6, load_white1_2, fixation_r_2]
    for thisComponent in Waiting_vote_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_6* updates
        if wait_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_6.frameNStart = frameN  # exact frame index
            wait_6.tStart = t  # local t and not account for scr refresh
            wait_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_6, 'tStartRefresh')  # time at next scr refresh
            wait_6.setAutoDraw(True)
        if wait_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_6.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                wait_6.tStop = t  # not accounting for scr refresh
                wait_6.frameNStop = frameN  # exact frame index
                wait_6.setAutoDraw(False)
        
        # *load_white1_2* updates
        if load_white1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            load_white1_2.frameNStart = frameN  # exact frame index
            load_white1_2.tStart = t  # local t and not account for scr refresh
            load_white1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_white1_2, 'tStartRefresh')  # time at next scr refresh
            load_white1_2.setAutoDraw(True)
        if load_white1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > load_white1_2.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                load_white1_2.tStop = t  # not accounting for scr refresh
                load_white1_2.frameNStop = frameN  # exact frame index
                load_white1_2.setAutoDraw(False)
        
        # *fixation_r_2* updates
        if fixation_r_2.status == NOT_STARTED and tThisFlip >= vote_duration-frameTolerance:
            # keep track of start time/frame for later
            fixation_r_2.frameNStart = frameN  # exact frame index
            fixation_r_2.tStart = t  # local t and not account for scr refresh
            fixation_r_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_r_2, 'tStartRefresh')  # time at next scr refresh
            fixation_r_2.setAutoDraw(True)
        if fixation_r_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_r_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_r_2.tStop = t  # not accounting for scr refresh
                fixation_r_2.frameNStop = frameN  # exact frame index
                fixation_r_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_2" ---
    for thisComponent in Waiting_vote_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Waiting_vote_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cop_vote_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    vote_image_second.setImage(image_thumb)
    # Run 'Begin Routine' code from code_thumb_2
    if vote_all[b][1] == '1':
        image_thumb = 'images/thumb-up.png'
        save_vote = 'Like'
        play_round = '2'
        cop_type = vote_all[b][5]
    else:
        image_thumb = 'images/thumb-down.png'
        save_vote = 'Dislike'
        play_round = '2'
        cop_type = vote_all[b][5]
    voting_2.addData('Study ID', expInfo['Study ID'])
    voting_2.addData('Coplayer_vote', save_vote)
    voting_2.addData('Round', play_round)
    voting_2.addData('Coplayer_type', cop_type)
    # keep track of which components have finished
    Cop_vote_2Components = [vote_image_second]
    for thisComponent in Cop_vote_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cop_vote_2" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vote_image_second* updates
        if vote_image_second.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_image_second.frameNStart = frameN  # exact frame index
            vote_image_second.tStart = t  # local t and not account for scr refresh
            vote_image_second.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_image_second, 'tStartRefresh')  # time at next scr refresh
            vote_image_second.setAutoDraw(True)
        if vote_image_second.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vote_image_second.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                vote_image_second.tStop = t  # not accounting for scr refresh
                vote_image_second.frameNStop = frameN  # exact frame index
                vote_image_second.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cop_vote_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cop_vote_2" ---
    for thisComponent in Cop_vote_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Waiting_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_7.setText('+')
    # keep track of which components have finished
    Waiting_vote_3Components = [wait_7]
    for thisComponent in Waiting_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_7* updates
        if wait_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_7.frameNStart = frameN  # exact frame index
            wait_7.tStart = t  # local t and not account for scr refresh
            wait_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_7, 'tStartRefresh')  # time at next scr refresh
            wait_7.setAutoDraw(True)
        if wait_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wait_7.tStop = t  # not accounting for scr refresh
                wait_7.frameNStop = frameN  # exact frame index
                wait_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_3" ---
    for thisComponent in Waiting_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'voting_2'

# get names of stimulus parameters
if voting_2.trialList in ([], [None], None):
    params = []
else:
    params = voting_2.trialList[0].keys()
# save data for this loop
voting_2.saveAsExcel(filename + '.xlsx', sheetName='voting_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
voting_2.saveAsText(filename + 'voting_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Waiting_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_12.setText('Let’s find out who got the MOST like votes this round...')
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Waiting_3Components = [image_15, polygon_12, text_12, key_resp_12, image_16]
for thisComponent in Waiting_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_3" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            image_15.setAutoDraw(False)
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    if polygon_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_12.tStop = t  # not accounting for scr refresh
            polygon_12.frameNStop = frameN  # exact frame index
            polygon_12.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            text_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            image_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_3" ---
for thisComponent in Waiting_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Most_vote_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
most_pic.setImage('images/background_mostvote.jpg')
most_vote_2.setImage(photos[m])
name_most_2.setText(names[m])
next_most2.keys = []
next_most2.rt = []
_next_most2_allKeys = []
# keep track of which components have finished
Most_vote_2Components = [most_pic, border_14, border_15, most_vote_2, name_most_2, next_most_2, next_most2]
for thisComponent in Most_vote_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Most_vote_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *most_pic* updates
    if most_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_pic.frameNStart = frameN  # exact frame index
        most_pic.tStart = t  # local t and not account for scr refresh
        most_pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_pic, 'tStartRefresh')  # time at next scr refresh
        most_pic.setAutoDraw(True)
    
    # *border_14* updates
    if border_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_14.frameNStart = frameN  # exact frame index
        border_14.tStart = t  # local t and not account for scr refresh
        border_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_14, 'tStartRefresh')  # time at next scr refresh
        border_14.setAutoDraw(True)
    
    # *border_15* updates
    if border_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_15.frameNStart = frameN  # exact frame index
        border_15.tStart = t  # local t and not account for scr refresh
        border_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_15, 'tStartRefresh')  # time at next scr refresh
        border_15.setAutoDraw(True)
    
    # *most_vote_2* updates
    if most_vote_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_vote_2.frameNStart = frameN  # exact frame index
        most_vote_2.tStart = t  # local t and not account for scr refresh
        most_vote_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_vote_2, 'tStartRefresh')  # time at next scr refresh
        most_vote_2.setAutoDraw(True)
    
    # *name_most_2* updates
    if name_most_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_most_2.frameNStart = frameN  # exact frame index
        name_most_2.tStart = t  # local t and not account for scr refresh
        name_most_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_most_2, 'tStartRefresh')  # time at next scr refresh
        name_most_2.setAutoDraw(True)
    
    # *next_most_2* updates
    if next_most_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most_2.frameNStart = frameN  # exact frame index
        next_most_2.tStart = t  # local t and not account for scr refresh
        next_most_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most_2, 'tStartRefresh')  # time at next scr refresh
        next_most_2.setAutoDraw(True)
    
    # *next_most2* updates
    waitOnFlip = False
    if next_most2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most2.frameNStart = frameN  # exact frame index
        next_most2.tStart = t  # local t and not account for scr refresh
        next_most2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most2, 'tStartRefresh')  # time at next scr refresh
        next_most2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_most2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_most2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_most2.status == STARTED and not waitOnFlip:
        theseKeys = next_most2.getKeys(keyList=['space'], waitRelease=False)
        _next_most2_allKeys.extend(theseKeys)
        if len(_next_most2_allKeys):
            next_most2.keys = _next_most2_allKeys[-1].name  # just the last key pressed
            next_most2.rt = _next_most2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Most_vote_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Most_vote_2" ---
for thisComponent in Most_vote_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Most_vote_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_13.setText('Let’s find out who got the LEAST like votes this round...')
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Waiting_4Components = [image_17, polygon_13, text_13, key_resp_14, image_18]
for thisComponent in Waiting_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_4" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            image_17.setAutoDraw(False)
    
    # *polygon_13* updates
    if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.tStart = t  # local t and not account for scr refresh
        polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
        polygon_13.setAutoDraw(True)
    if polygon_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_13.tStop = t  # not accounting for scr refresh
            polygon_13.frameNStop = frameN  # exact frame index
            polygon_13.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            text_13.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            image_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_4" ---
for thisComponent in Waiting_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Least_vote_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image_30.setImage('images/sad.jpg')
least_vote_2.setImage(photos[l])
name_least_2.setText(names[l])
next_least2.keys = []
next_least2.rt = []
_next_least2_allKeys = []
# keep track of which components have finished
Least_vote_2Components = [image_30, border4_5, border_13, least_vote_2, name_least_2, next_least_2, next_least2]
for thisComponent in Least_vote_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Least_vote_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_30* updates
    if image_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_30.frameNStart = frameN  # exact frame index
        image_30.tStart = t  # local t and not account for scr refresh
        image_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
        image_30.setAutoDraw(True)
    
    # *border4_5* updates
    if border4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border4_5.frameNStart = frameN  # exact frame index
        border4_5.tStart = t  # local t and not account for scr refresh
        border4_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border4_5, 'tStartRefresh')  # time at next scr refresh
        border4_5.setAutoDraw(True)
    
    # *border_13* updates
    if border_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_13.frameNStart = frameN  # exact frame index
        border_13.tStart = t  # local t and not account for scr refresh
        border_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_13, 'tStartRefresh')  # time at next scr refresh
        border_13.setAutoDraw(True)
    
    # *least_vote_2* updates
    if least_vote_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        least_vote_2.frameNStart = frameN  # exact frame index
        least_vote_2.tStart = t  # local t and not account for scr refresh
        least_vote_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(least_vote_2, 'tStartRefresh')  # time at next scr refresh
        least_vote_2.setAutoDraw(True)
    
    # *name_least_2* updates
    if name_least_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_least_2.frameNStart = frameN  # exact frame index
        name_least_2.tStart = t  # local t and not account for scr refresh
        name_least_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_least_2, 'tStartRefresh')  # time at next scr refresh
        name_least_2.setAutoDraw(True)
    
    # *next_least_2* updates
    if next_least_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least_2.frameNStart = frameN  # exact frame index
        next_least_2.tStart = t  # local t and not account for scr refresh
        next_least_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least_2, 'tStartRefresh')  # time at next scr refresh
        next_least_2.setAutoDraw(True)
    
    # *next_least2* updates
    waitOnFlip = False
    if next_least2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least2.frameNStart = frameN  # exact frame index
        next_least2.tStart = t  # local t and not account for scr refresh
        next_least2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least2, 'tStartRefresh')  # time at next scr refresh
        next_least2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_least2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_least2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_least2.status == STARTED and not waitOnFlip:
        theseKeys = next_least2.getKeys(keyList=['space'], waitRelease=False)
        _next_least2_allKeys.extend(theseKeys)
        if len(_next_least2_allKeys):
            next_least2.keys = _next_least2_allKeys[-1].name  # just the last key pressed
            next_least2.rt = _next_least2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Least_vote_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Least_vote_2" ---
for thisComponent in Least_vote_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from least_votes_2
# create random index numbers for most/least player
m = most_least_index[4]
l = most_least_index[5]
    
# the Routine "Least_vote_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "round_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_28.setText('Time to move on to the next round. We are getting closer to the virtual party! Let’s see if you will be invited.')
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
next_intro3_5.setText('Press space to continue.')
# Run 'Begin Routine' code from code_33
next_intro3_5.bold = 'True'
# keep track of which components have finished
round_2Components = [image_37, polygon_25, text_28, key_resp_24, next_intro3_5]
for thisComponent in round_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "round_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_37* updates
    if image_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_37.frameNStart = frameN  # exact frame index
        image_37.tStart = t  # local t and not account for scr refresh
        image_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_37, 'tStartRefresh')  # time at next scr refresh
        image_37.setAutoDraw(True)
    
    # *polygon_25* updates
    if polygon_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_25.frameNStart = frameN  # exact frame index
        polygon_25.tStart = t  # local t and not account for scr refresh
        polygon_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_25, 'tStartRefresh')  # time at next scr refresh
        polygon_25.setAutoDraw(True)
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_5* updates
    if next_intro3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_5.frameNStart = frameN  # exact frame index
        next_intro3_5.tStart = t  # local t and not account for scr refresh
        next_intro3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_5, 'tStartRefresh')  # time at next scr refresh
        next_intro3_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "round_2" ---
for thisComponent in round_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "round_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_12" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
Introduction_12Components = [image_26, polygon_19, text_18, next_intro7_7, key_resp_20]
for thisComponent in Introduction_12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_12" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_26* updates
    if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_26.frameNStart = frameN  # exact frame index
        image_26.tStart = t  # local t and not account for scr refresh
        image_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
        image_26.setAutoDraw(True)
    
    # *polygon_19* updates
    if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_19.frameNStart = frameN  # exact frame index
        polygon_19.tStart = t  # local t and not account for scr refresh
        polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
        polygon_19.setAutoDraw(True)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # *next_intro7_7* updates
    if next_intro7_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro7_7.frameNStart = frameN  # exact frame index
        next_intro7_7.tStart = t  # local t and not account for scr refresh
        next_intro7_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro7_7, 'tStartRefresh')  # time at next scr refresh
        next_intro7_7.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_12" ---
for thisComponent in Introduction_12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Poll_q2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
poll_question_2.setText("If money didn't matter, what would be your dream job?")
poll_enter_2.reset()
poll_enter_2.setText('')
# setup some python lists for storing info about the mouse5_2
mouse5_2.clicked_name = []
gotValidClick = False  # until a click is received
ptp_poll_2 = poll_enter_2.text  # Set routine start values for ptp_poll_2
# keep track of which components have finished
Poll_q2Components = [poll_question_2, poll_enter_2, button5_2, submit5_2, mouse5_2]
for thisComponent in Poll_q2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Poll_q2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *poll_question_2* updates
    if poll_question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_question_2.frameNStart = frameN  # exact frame index
        poll_question_2.tStart = t  # local t and not account for scr refresh
        poll_question_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_question_2, 'tStartRefresh')  # time at next scr refresh
        poll_question_2.setAutoDraw(True)
    
    # *poll_enter_2* updates
    if poll_enter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_enter_2.frameNStart = frameN  # exact frame index
        poll_enter_2.tStart = t  # local t and not account for scr refresh
        poll_enter_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_enter_2, 'tStartRefresh')  # time at next scr refresh
        poll_enter_2.setAutoDraw(True)
    
    # *button5_2* updates
    if button5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button5_2.frameNStart = frameN  # exact frame index
        button5_2.tStart = t  # local t and not account for scr refresh
        button5_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5_2, 'tStartRefresh')  # time at next scr refresh
        button5_2.setAutoDraw(True)
    
    # *submit5_2* updates
    if submit5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit5_2.frameNStart = frameN  # exact frame index
        submit5_2.tStart = t  # local t and not account for scr refresh
        submit5_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit5_2, 'tStartRefresh')  # time at next scr refresh
        submit5_2.setAutoDraw(True)
    # *mouse5_2* updates
    if mouse5_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5_2.frameNStart = frameN  # exact frame index
        mouse5_2.tStart = t  # local t and not account for scr refresh
        mouse5_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5_2, 'tStartRefresh')  # time at next scr refresh
        mouse5_2.status = STARTED
        mouse5_2.mouseClock.reset()
        prevButtonState = mouse5_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse5_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse5_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button5)
                    clickableList = button5
                except:
                    clickableList = [button5]
                for obj in clickableList:
                    if obj.contains(mouse5_2):
                        gotValidClick = True
                        mouse5_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_poll_2 = poll_enter_2.text  # Set frame start values for ptp_poll_2
    ptp_poll_2Container.append(ptp_poll_2)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Poll_q2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Poll_q2" ---
for thisComponent in Poll_q2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('poll_enter_2.text',poll_enter_2.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_poll_2.routineEndVal', ptp_poll_2)  # Save end routine value
# the Routine "Poll_q2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_11.setText('Waiting for others to answer the poll question...')
# keep track of which components have finished
Waiting_5Components = [image_19, polygon_16, text_11, image_23]
for thisComponent in Waiting_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_5" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            image_19.setAutoDraw(False)
    
    # *polygon_16* updates
    if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_16.frameNStart = frameN  # exact frame index
        polygon_16.tStart = t  # local t and not account for scr refresh
        polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
        polygon_16.setAutoDraw(True)
    if polygon_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_16.tStop = t  # not accounting for scr refresh
            polygon_16.frameNStop = frameN  # exact frame index
            polygon_16.setAutoDraw(False)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            text_11.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            image_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_5" ---
for thisComponent in Waiting_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Introduction_10" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_16.setText("All players have answered the poll question now.\n\nLet's see the responses!")
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
next_intro3_2.setText('Press space to continue.')
# Run 'Begin Routine' code from code_20
next_intro3_2.bold = 'True'
# keep track of which components have finished
Introduction_10Components = [image_24, polygon_17, text_16, key_resp_18, next_intro3_2]
for thisComponent in Introduction_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_10" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *polygon_17* updates
    if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.tStart = t  # local t and not account for scr refresh
        polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
        polygon_17.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_2* updates
    if next_intro3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_2.frameNStart = frameN  # exact frame index
        next_intro3_2.tStart = t  # local t and not account for scr refresh
        next_intro3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_2, 'tStartRefresh')  # time at next scr refresh
        next_intro3_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_10" ---
for thisComponent in Introduction_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_2_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
poll_2_1_names.setText(ptp_name +':' + '\n'+ names[0]+':' +'\n'+ names[1]+':'+'\n'+ names[2]+':'+'\n'+ names[3]+':' +'\n'+ names[4]+':' +'\n'+ names[5]+':'+'\n'+ names[6]+':')
poll_2_1_responses.setText(ptp_poll_2 +'\n' + poll_2[0] +'\n'+ poll_2[1] +'\n'+ poll_2[2] +'\n'+ poll_2[3] +'\n'+ poll_2[4] +'\n'+ poll_2[5] +'\n'+ poll_2[6])
# Run 'Begin Routine' code from poll_code
poll_next_2_1.bold = 'True'
poll_2_1_names.alignText = 'Left'
poll_2_1_names.bold = 'True'
poll_2_1_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_2_1Components = [image_43, polygon, key_resp, poll_next_2_1, poll_2_1_names, poll_2_1_responses]
for thisComponent in poll_resp_2_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_2_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_43* updates
    if image_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_43.frameNStart = frameN  # exact frame index
        image_43.tStart = t  # local t and not account for scr refresh
        image_43.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_43, 'tStartRefresh')  # time at next scr refresh
        image_43.setAutoDraw(True)
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_2_1* updates
    if poll_next_2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_2_1.frameNStart = frameN  # exact frame index
        poll_next_2_1.tStart = t  # local t and not account for scr refresh
        poll_next_2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_2_1, 'tStartRefresh')  # time at next scr refresh
        poll_next_2_1.setAutoDraw(True)
    
    # *poll_2_1_names* updates
    if poll_2_1_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_2_1_names.frameNStart = frameN  # exact frame index
        poll_2_1_names.tStart = t  # local t and not account for scr refresh
        poll_2_1_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_2_1_names, 'tStartRefresh')  # time at next scr refresh
        poll_2_1_names.setAutoDraw(True)
    
    # *poll_2_1_responses* updates
    if poll_2_1_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_2_1_responses.frameNStart = frameN  # exact frame index
        poll_2_1_responses.tStart = t  # local t and not account for scr refresh
        poll_2_1_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_2_1_responses, 'tStartRefresh')  # time at next scr refresh
        poll_2_1_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_2_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_2_1" ---
for thisComponent in poll_resp_2_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_2_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_2_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_30.keys = []
key_resp_30.rt = []
_key_resp_30_allKeys = []
poll_2_2_names.setText(names[7]+':' +'\n'+ names[8]+':'+'\n'+ names[9]+':'+'\n'+ names[10]+':' +'\n'+ names[11]+':')
poll_2_2_responses.setText(poll_2[7] +'\n'+ poll_2[8] +'\n'+ poll_2[9] +'\n'+ poll_2[10] +'\n'+ poll_2[11] )
# Run 'Begin Routine' code from poll_code_6
poll_next_2_2.bold = 'True'
poll_2_2_names.alignText = 'Left'
poll_2_2_names.bold = 'True'
poll_2_2_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_2_2Components = [image_44, polygon_31, key_resp_30, poll_next_2_2, poll_2_2_names, poll_2_2_responses]
for thisComponent in poll_resp_2_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_2_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_44* updates
    if image_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_44.frameNStart = frameN  # exact frame index
        image_44.tStart = t  # local t and not account for scr refresh
        image_44.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_44, 'tStartRefresh')  # time at next scr refresh
        image_44.setAutoDraw(True)
    
    # *polygon_31* updates
    if polygon_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_31.frameNStart = frameN  # exact frame index
        polygon_31.tStart = t  # local t and not account for scr refresh
        polygon_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_31, 'tStartRefresh')  # time at next scr refresh
        polygon_31.setAutoDraw(True)
    
    # *key_resp_30* updates
    waitOnFlip = False
    if key_resp_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_30.frameNStart = frameN  # exact frame index
        key_resp_30.tStart = t  # local t and not account for scr refresh
        key_resp_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_30, 'tStartRefresh')  # time at next scr refresh
        key_resp_30.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_30.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_30.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_30_allKeys.extend(theseKeys)
        if len(_key_resp_30_allKeys):
            key_resp_30.keys = _key_resp_30_allKeys[-1].name  # just the last key pressed
            key_resp_30.rt = _key_resp_30_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_2_2* updates
    if poll_next_2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_2_2.frameNStart = frameN  # exact frame index
        poll_next_2_2.tStart = t  # local t and not account for scr refresh
        poll_next_2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_2_2, 'tStartRefresh')  # time at next scr refresh
        poll_next_2_2.setAutoDraw(True)
    
    # *poll_2_2_names* updates
    if poll_2_2_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_2_2_names.frameNStart = frameN  # exact frame index
        poll_2_2_names.tStart = t  # local t and not account for scr refresh
        poll_2_2_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_2_2_names, 'tStartRefresh')  # time at next scr refresh
        poll_2_2_names.setAutoDraw(True)
    
    # *poll_2_2_responses* updates
    if poll_2_2_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_2_2_responses.frameNStart = frameN  # exact frame index
        poll_2_2_responses.tStart = t  # local t and not account for scr refresh
        poll_2_2_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_2_2_responses, 'tStartRefresh')  # time at next scr refresh
        poll_2_2_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_2_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_2_2" ---
for thisComponent in poll_resp_2_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_2_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_11" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_17.setText('Time to move on to the next round. We are getting closer to the virtual party! \n\nLet’s see if you will be invited. ')
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
next_intro3_3.setText('Press space to continue.')
# Run 'Begin Routine' code from code_21
next_intro3_3.bold = 'True'
# keep track of which components have finished
Introduction_11Components = [image_25, polygon_18, text_17, key_resp_19, next_intro3_3]
for thisComponent in Introduction_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_11" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    
    # *polygon_18* updates
    if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.tStart = t  # local t and not account for scr refresh
        polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
        polygon_18.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_3* updates
    if next_intro3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_3.frameNStart = frameN  # exact frame index
        next_intro3_3.tStart = t  # local t and not account for scr refresh
        next_intro3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_3, 'tStartRefresh')  # time at next scr refresh
        next_intro3_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_11" ---
for thisComponent in Introduction_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
voting_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='voting_3')
thisExp.addLoop(voting_3)  # add the loop to the experiment
thisVoting_3 = voting_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVoting_3.rgb)
if thisVoting_3 != None:
    for paramName in thisVoting_3:
        exec('{} = thisVoting_3[paramName]'.format(paramName))

for thisVoting_3 in voting_3:
    currentLoop = voting_3
    # abbreviate parameter names if possible (e.g. rgb = thisVoting_3.rgb)
    if thisVoting_3 != None:
        for paramName in thisVoting_3:
            exec('{} = thisVoting_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Player_profiles_voting_style_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from capitalization_cop_3
    cop_response_3.alignText = 'left'
    cop_prompts_3.alignText = 'left'
    
    
    # increment i for each loop
    c = c + 1
    
    coplayer_image_3.setImage(photos[c])
    cop_prompts_3.reset()
    cop_response_3.setText(names[c] + '\n' + str(ages[c]) + '\n' + hometowns[c] + '\n' + interests[c] + '\n' + schools[c])
    # setup some python lists for storing info about the click_real_3
    click_real_3.clicked_name = []
    gotValidClick = False  # until a click is received
    vote_question_5.setText('Do you like or dislike ' + names[c] + '?')
    # keep track of which components have finished
    Player_profiles_voting_style_3Components = [border_10, coplayer_image_3, cop_prompts_3, cop_response_3, like_real_button_3, like_real_text_3, dislike_real_button_3, dislike_real_text_3, click_real_3, vote_question_5]
    for thisComponent in Player_profiles_voting_style_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Player_profiles_voting_style_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *border_10* updates
        if border_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_10.frameNStart = frameN  # exact frame index
            border_10.tStart = t  # local t and not account for scr refresh
            border_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_10, 'tStartRefresh')  # time at next scr refresh
            border_10.setAutoDraw(True)
        
        # *coplayer_image_3* updates
        if coplayer_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            coplayer_image_3.frameNStart = frameN  # exact frame index
            coplayer_image_3.tStart = t  # local t and not account for scr refresh
            coplayer_image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(coplayer_image_3, 'tStartRefresh')  # time at next scr refresh
            coplayer_image_3.setAutoDraw(True)
        
        # *cop_prompts_3* updates
        if cop_prompts_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts_3.frameNStart = frameN  # exact frame index
            cop_prompts_3.tStart = t  # local t and not account for scr refresh
            cop_prompts_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts_3, 'tStartRefresh')  # time at next scr refresh
            cop_prompts_3.setAutoDraw(True)
        
        # *cop_response_3* updates
        if cop_response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_response_3.frameNStart = frameN  # exact frame index
            cop_response_3.tStart = t  # local t and not account for scr refresh
            cop_response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_response_3, 'tStartRefresh')  # time at next scr refresh
            cop_response_3.setAutoDraw(True)
        
        # *like_real_button_3* updates
        if like_real_button_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_button_3.frameNStart = frameN  # exact frame index
            like_real_button_3.tStart = t  # local t and not account for scr refresh
            like_real_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_button_3, 'tStartRefresh')  # time at next scr refresh
            like_real_button_3.setAutoDraw(True)
        
        # *like_real_text_3* updates
        if like_real_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_text_3.frameNStart = frameN  # exact frame index
            like_real_text_3.tStart = t  # local t and not account for scr refresh
            like_real_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_text_3, 'tStartRefresh')  # time at next scr refresh
            like_real_text_3.setAutoDraw(True)
        
        # *dislike_real_button_3* updates
        if dislike_real_button_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_button_3.frameNStart = frameN  # exact frame index
            dislike_real_button_3.tStart = t  # local t and not account for scr refresh
            dislike_real_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_button_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dislike_real_button_3.started')
            dislike_real_button_3.setAutoDraw(True)
        
        # *dislike_real_text_3* updates
        if dislike_real_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_text_3.frameNStart = frameN  # exact frame index
            dislike_real_text_3.tStart = t  # local t and not account for scr refresh
            dislike_real_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_text_3, 'tStartRefresh')  # time at next scr refresh
            dislike_real_text_3.setAutoDraw(True)
        # *click_real_3* updates
        if click_real_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            click_real_3.frameNStart = frameN  # exact frame index
            click_real_3.tStart = t  # local t and not account for scr refresh
            click_real_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_real_3, 'tStartRefresh')  # time at next scr refresh
            click_real_3.status = STARTED
            click_real_3.mouseClock.reset()
            prevButtonState = click_real_3.getPressed()  # if button is down already this ISN'T a new click
        if click_real_3.status == STARTED:  # only update if started and not finished!
            buttons = click_real_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([like_real_button_3, dislike_real_button_3])
                        clickableList = [like_real_button_3, dislike_real_button_3]
                    except:
                        clickableList = [[like_real_button_3, dislike_real_button_3]]
                    for obj in clickableList:
                        if obj.contains(click_real_3):
                            gotValidClick = True
                            click_real_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *vote_question_5* updates
        if vote_question_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_question_5.frameNStart = frameN  # exact frame index
            vote_question_5.tStart = t  # local t and not account for scr refresh
            vote_question_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_question_5, 'tStartRefresh')  # time at next scr refresh
            vote_question_5.setAutoDraw(True)
        # Run 'Each Frame' code from ptp_vote_3
        ptp_v = ''
        if mouse.isPressedIn(like_real_button_3):
            ptp_v="Like"
        elif mouse.isPressedIn(dislike_real_button_3):
            ptp_v ="Dislike"
        voting_3.addData('Participant_vote', ptp_v)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Player_profiles_voting_style_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Player_profiles_voting_style_3" ---
    for thisComponent in Player_profiles_voting_style_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for voting_3 (TrialHandler)
    # the Routine "Player_profiles_voting_style_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting_vote_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_6.setText('Compiling votes, your feedback\nwill be presented soon...')
    # keep track of which components have finished
    Waiting_vote_2Components = [wait_6, load_white1_2, fixation_r_2]
    for thisComponent in Waiting_vote_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_6* updates
        if wait_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_6.frameNStart = frameN  # exact frame index
            wait_6.tStart = t  # local t and not account for scr refresh
            wait_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_6, 'tStartRefresh')  # time at next scr refresh
            wait_6.setAutoDraw(True)
        if wait_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_6.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                wait_6.tStop = t  # not accounting for scr refresh
                wait_6.frameNStop = frameN  # exact frame index
                wait_6.setAutoDraw(False)
        
        # *load_white1_2* updates
        if load_white1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            load_white1_2.frameNStart = frameN  # exact frame index
            load_white1_2.tStart = t  # local t and not account for scr refresh
            load_white1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_white1_2, 'tStartRefresh')  # time at next scr refresh
            load_white1_2.setAutoDraw(True)
        if load_white1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > load_white1_2.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                load_white1_2.tStop = t  # not accounting for scr refresh
                load_white1_2.frameNStop = frameN  # exact frame index
                load_white1_2.setAutoDraw(False)
        
        # *fixation_r_2* updates
        if fixation_r_2.status == NOT_STARTED and tThisFlip >= vote_duration-frameTolerance:
            # keep track of start time/frame for later
            fixation_r_2.frameNStart = frameN  # exact frame index
            fixation_r_2.tStart = t  # local t and not account for scr refresh
            fixation_r_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_r_2, 'tStartRefresh')  # time at next scr refresh
            fixation_r_2.setAutoDraw(True)
        if fixation_r_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_r_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_r_2.tStop = t  # not accounting for scr refresh
                fixation_r_2.frameNStop = frameN  # exact frame index
                fixation_r_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_2" ---
    for thisComponent in Waiting_vote_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Waiting_vote_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cop_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_thumb_3
    if vote_all[c][2] == '1':
        image_thumb = 'images/thumb-up.png'
        save_vote = 'Like'
        play_round = '3'
        cop_type = vote_all[c][5]
    else:
        image_thumb = 'images/thumb-down.png'
        save_vote = 'Dislike'
        play_round = '3'
        cop_type = vote_all[c][5]
    voting_3.addData('Study ID', expInfo['Study ID'])
    voting_3.addData('Coplayer_vote', save_vote)
    voting_3.addData('Round', play_round)
    voting_3.addData('Coplayer_type', cop_type)
    vote_image_third.setImage(image_thumb)
    # keep track of which components have finished
    Cop_vote_3Components = [vote_image_third]
    for thisComponent in Cop_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cop_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vote_image_third* updates
        if vote_image_third.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_image_third.frameNStart = frameN  # exact frame index
            vote_image_third.tStart = t  # local t and not account for scr refresh
            vote_image_third.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_image_third, 'tStartRefresh')  # time at next scr refresh
            vote_image_third.setAutoDraw(True)
        if vote_image_third.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vote_image_third.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                vote_image_third.tStop = t  # not accounting for scr refresh
                vote_image_third.frameNStop = frameN  # exact frame index
                vote_image_third.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cop_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cop_vote_3" ---
    for thisComponent in Cop_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Waiting_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_7.setText('+')
    # keep track of which components have finished
    Waiting_vote_3Components = [wait_7]
    for thisComponent in Waiting_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_7* updates
        if wait_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_7.frameNStart = frameN  # exact frame index
            wait_7.tStart = t  # local t and not account for scr refresh
            wait_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_7, 'tStartRefresh')  # time at next scr refresh
            wait_7.setAutoDraw(True)
        if wait_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wait_7.tStop = t  # not accounting for scr refresh
                wait_7.frameNStop = frameN  # exact frame index
                wait_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_3" ---
    for thisComponent in Waiting_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'voting_3'

# get names of stimulus parameters
if voting_3.trialList in ([], [None], None):
    params = []
else:
    params = voting_3.trialList[0].keys()
# save data for this loop
voting_3.saveAsExcel(filename + '.xlsx', sheetName='voting_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
voting_3.saveAsText(filename + 'voting_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Waiting_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_12.setText('Let’s find out who got the MOST like votes this round...')
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Waiting_3Components = [image_15, polygon_12, text_12, key_resp_12, image_16]
for thisComponent in Waiting_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_3" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            image_15.setAutoDraw(False)
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    if polygon_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_12.tStop = t  # not accounting for scr refresh
            polygon_12.frameNStop = frameN  # exact frame index
            polygon_12.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            text_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            image_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_3" ---
for thisComponent in Waiting_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Most_vote_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
most_pic_2.setImage('images/background_mostvote.jpg')
most_vote_3.setImage(photos[m])
name_most_3.setText(names[m])
next_most3.keys = []
next_most3.rt = []
_next_most3_allKeys = []
# keep track of which components have finished
Most_vote_3Components = [most_pic_2, border_16, border_17, most_vote_3, name_most_3, next_most_3, next_most3]
for thisComponent in Most_vote_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Most_vote_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *most_pic_2* updates
    if most_pic_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_pic_2.frameNStart = frameN  # exact frame index
        most_pic_2.tStart = t  # local t and not account for scr refresh
        most_pic_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_pic_2, 'tStartRefresh')  # time at next scr refresh
        most_pic_2.setAutoDraw(True)
    
    # *border_16* updates
    if border_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_16.frameNStart = frameN  # exact frame index
        border_16.tStart = t  # local t and not account for scr refresh
        border_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_16, 'tStartRefresh')  # time at next scr refresh
        border_16.setAutoDraw(True)
    
    # *border_17* updates
    if border_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_17.frameNStart = frameN  # exact frame index
        border_17.tStart = t  # local t and not account for scr refresh
        border_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_17, 'tStartRefresh')  # time at next scr refresh
        border_17.setAutoDraw(True)
    
    # *most_vote_3* updates
    if most_vote_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_vote_3.frameNStart = frameN  # exact frame index
        most_vote_3.tStart = t  # local t and not account for scr refresh
        most_vote_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_vote_3, 'tStartRefresh')  # time at next scr refresh
        most_vote_3.setAutoDraw(True)
    
    # *name_most_3* updates
    if name_most_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_most_3.frameNStart = frameN  # exact frame index
        name_most_3.tStart = t  # local t and not account for scr refresh
        name_most_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_most_3, 'tStartRefresh')  # time at next scr refresh
        name_most_3.setAutoDraw(True)
    
    # *next_most_3* updates
    if next_most_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most_3.frameNStart = frameN  # exact frame index
        next_most_3.tStart = t  # local t and not account for scr refresh
        next_most_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most_3, 'tStartRefresh')  # time at next scr refresh
        next_most_3.setAutoDraw(True)
    
    # *next_most3* updates
    waitOnFlip = False
    if next_most3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most3.frameNStart = frameN  # exact frame index
        next_most3.tStart = t  # local t and not account for scr refresh
        next_most3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most3, 'tStartRefresh')  # time at next scr refresh
        next_most3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_most3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_most3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_most3.status == STARTED and not waitOnFlip:
        theseKeys = next_most3.getKeys(keyList=['space'], waitRelease=False)
        _next_most3_allKeys.extend(theseKeys)
        if len(_next_most3_allKeys):
            next_most3.keys = _next_most3_allKeys[-1].name  # just the last key pressed
            next_most3.rt = _next_most3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Most_vote_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Most_vote_3" ---
for thisComponent in Most_vote_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Most_vote_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_13.setText('Let’s find out who got the LEAST like votes this round...')
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Waiting_4Components = [image_17, polygon_13, text_13, key_resp_14, image_18]
for thisComponent in Waiting_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_4" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            image_17.setAutoDraw(False)
    
    # *polygon_13* updates
    if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.tStart = t  # local t and not account for scr refresh
        polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
        polygon_13.setAutoDraw(True)
    if polygon_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_13.tStop = t  # not accounting for scr refresh
            polygon_13.frameNStop = frameN  # exact frame index
            polygon_13.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            text_13.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            image_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_4" ---
for thisComponent in Waiting_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Least_vote_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image_31.setImage('images/sad.jpg')
least_vote_3.setImage(photos[l])
name_least_3.setText(names[l])
next_least3.keys = []
next_least3.rt = []
_next_least3_allKeys = []
# keep track of which components have finished
Least_vote_3Components = [image_31, border4_6, border_18, least_vote_3, name_least_3, next_least_3, next_least3]
for thisComponent in Least_vote_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Least_vote_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_31* updates
    if image_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_31.frameNStart = frameN  # exact frame index
        image_31.tStart = t  # local t and not account for scr refresh
        image_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_31, 'tStartRefresh')  # time at next scr refresh
        image_31.setAutoDraw(True)
    
    # *border4_6* updates
    if border4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border4_6.frameNStart = frameN  # exact frame index
        border4_6.tStart = t  # local t and not account for scr refresh
        border4_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border4_6, 'tStartRefresh')  # time at next scr refresh
        border4_6.setAutoDraw(True)
    
    # *border_18* updates
    if border_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_18.frameNStart = frameN  # exact frame index
        border_18.tStart = t  # local t and not account for scr refresh
        border_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_18, 'tStartRefresh')  # time at next scr refresh
        border_18.setAutoDraw(True)
    
    # *least_vote_3* updates
    if least_vote_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        least_vote_3.frameNStart = frameN  # exact frame index
        least_vote_3.tStart = t  # local t and not account for scr refresh
        least_vote_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(least_vote_3, 'tStartRefresh')  # time at next scr refresh
        least_vote_3.setAutoDraw(True)
    
    # *name_least_3* updates
    if name_least_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_least_3.frameNStart = frameN  # exact frame index
        name_least_3.tStart = t  # local t and not account for scr refresh
        name_least_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_least_3, 'tStartRefresh')  # time at next scr refresh
        name_least_3.setAutoDraw(True)
    
    # *next_least_3* updates
    if next_least_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least_3.frameNStart = frameN  # exact frame index
        next_least_3.tStart = t  # local t and not account for scr refresh
        next_least_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least_3, 'tStartRefresh')  # time at next scr refresh
        next_least_3.setAutoDraw(True)
    
    # *next_least3* updates
    waitOnFlip = False
    if next_least3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least3.frameNStart = frameN  # exact frame index
        next_least3.tStart = t  # local t and not account for scr refresh
        next_least3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least3, 'tStartRefresh')  # time at next scr refresh
        next_least3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_least3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_least3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_least3.status == STARTED and not waitOnFlip:
        theseKeys = next_least3.getKeys(keyList=['space'], waitRelease=False)
        _next_least3_allKeys.extend(theseKeys)
        if len(_next_least3_allKeys):
            next_least3.keys = _next_least3_allKeys[-1].name  # just the last key pressed
            next_least3.rt = _next_least3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Least_vote_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Least_vote_3" ---
for thisComponent in Least_vote_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from least_votes_3
# create random index numbers for most/least player
m = most_least_index[6]
l = most_least_index[7]
    
    
# the Routine "Least_vote_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "round_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_29.setText('Time to move on to the next round. We are getting closer to the virtual party! Let’s see if you will be invited.')
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
next_intro3_6.setText('Press space to continue.')
# Run 'Begin Routine' code from code_34
next_intro3_6.bold = 'True'
# keep track of which components have finished
round_3Components = [image_38, polygon_26, text_29, key_resp_25, next_intro3_6]
for thisComponent in round_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "round_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_38* updates
    if image_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_38.frameNStart = frameN  # exact frame index
        image_38.tStart = t  # local t and not account for scr refresh
        image_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_38, 'tStartRefresh')  # time at next scr refresh
        image_38.setAutoDraw(True)
    
    # *polygon_26* updates
    if polygon_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_26.frameNStart = frameN  # exact frame index
        polygon_26.tStart = t  # local t and not account for scr refresh
        polygon_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_26, 'tStartRefresh')  # time at next scr refresh
        polygon_26.setAutoDraw(True)
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_6* updates
    if next_intro3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_6.frameNStart = frameN  # exact frame index
        next_intro3_6.tStart = t  # local t and not account for scr refresh
        next_intro3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_6, 'tStartRefresh')  # time at next scr refresh
        next_intro3_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "round_3" ---
for thisComponent in round_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "round_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_12" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
Introduction_12Components = [image_26, polygon_19, text_18, next_intro7_7, key_resp_20]
for thisComponent in Introduction_12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_12" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_26* updates
    if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_26.frameNStart = frameN  # exact frame index
        image_26.tStart = t  # local t and not account for scr refresh
        image_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
        image_26.setAutoDraw(True)
    
    # *polygon_19* updates
    if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_19.frameNStart = frameN  # exact frame index
        polygon_19.tStart = t  # local t and not account for scr refresh
        polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
        polygon_19.setAutoDraw(True)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # *next_intro7_7* updates
    if next_intro7_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro7_7.frameNStart = frameN  # exact frame index
        next_intro7_7.tStart = t  # local t and not account for scr refresh
        next_intro7_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro7_7, 'tStartRefresh')  # time at next scr refresh
        next_intro7_7.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_12" ---
for thisComponent in Introduction_12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Poll_q3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
poll_question_3.setText('If you had a whole day to do whatever you wanted, what would you do?')
poll_enter_3.reset()
poll_enter_3.setText('')
# setup some python lists for storing info about the mouse5_3
mouse5_3.clicked_name = []
gotValidClick = False  # until a click is received
ptp_poll_3 = poll_enter_3.text  # Set routine start values for ptp_poll_3
# keep track of which components have finished
Poll_q3Components = [poll_question_3, poll_enter_3, button5_3, submit5_3, mouse5_3]
for thisComponent in Poll_q3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Poll_q3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *poll_question_3* updates
    if poll_question_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_question_3.frameNStart = frameN  # exact frame index
        poll_question_3.tStart = t  # local t and not account for scr refresh
        poll_question_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_question_3, 'tStartRefresh')  # time at next scr refresh
        poll_question_3.setAutoDraw(True)
    
    # *poll_enter_3* updates
    if poll_enter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_enter_3.frameNStart = frameN  # exact frame index
        poll_enter_3.tStart = t  # local t and not account for scr refresh
        poll_enter_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_enter_3, 'tStartRefresh')  # time at next scr refresh
        poll_enter_3.setAutoDraw(True)
    
    # *button5_3* updates
    if button5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button5_3.frameNStart = frameN  # exact frame index
        button5_3.tStart = t  # local t and not account for scr refresh
        button5_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5_3, 'tStartRefresh')  # time at next scr refresh
        button5_3.setAutoDraw(True)
    
    # *submit5_3* updates
    if submit5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit5_3.frameNStart = frameN  # exact frame index
        submit5_3.tStart = t  # local t and not account for scr refresh
        submit5_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit5_3, 'tStartRefresh')  # time at next scr refresh
        submit5_3.setAutoDraw(True)
    # *mouse5_3* updates
    if mouse5_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5_3.frameNStart = frameN  # exact frame index
        mouse5_3.tStart = t  # local t and not account for scr refresh
        mouse5_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5_3, 'tStartRefresh')  # time at next scr refresh
        mouse5_3.status = STARTED
        mouse5_3.mouseClock.reset()
        prevButtonState = mouse5_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse5_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse5_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button5_3)
                    clickableList = button5_3
                except:
                    clickableList = [button5_3]
                for obj in clickableList:
                    if obj.contains(mouse5_3):
                        gotValidClick = True
                        mouse5_3.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_poll_3 = poll_enter_3.text  # Set frame start values for ptp_poll_3
    ptp_poll_3Container.append(ptp_poll_3)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Poll_q3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Poll_q3" ---
for thisComponent in Poll_q3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('poll_enter_3.text',poll_enter_3.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_poll_3.routineEndVal', ptp_poll_3)  # Save end routine value
# the Routine "Poll_q3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_11.setText('Waiting for others to answer the poll question...')
# keep track of which components have finished
Waiting_5Components = [image_19, polygon_16, text_11, image_23]
for thisComponent in Waiting_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_5" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            image_19.setAutoDraw(False)
    
    # *polygon_16* updates
    if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_16.frameNStart = frameN  # exact frame index
        polygon_16.tStart = t  # local t and not account for scr refresh
        polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
        polygon_16.setAutoDraw(True)
    if polygon_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_16.tStop = t  # not accounting for scr refresh
            polygon_16.frameNStop = frameN  # exact frame index
            polygon_16.setAutoDraw(False)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            text_11.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            image_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_5" ---
for thisComponent in Waiting_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Introduction_10" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_16.setText("All players have answered the poll question now.\n\nLet's see the responses!")
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
next_intro3_2.setText('Press space to continue.')
# Run 'Begin Routine' code from code_20
next_intro3_2.bold = 'True'
# keep track of which components have finished
Introduction_10Components = [image_24, polygon_17, text_16, key_resp_18, next_intro3_2]
for thisComponent in Introduction_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_10" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *polygon_17* updates
    if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.tStart = t  # local t and not account for scr refresh
        polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
        polygon_17.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_2* updates
    if next_intro3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_2.frameNStart = frameN  # exact frame index
        next_intro3_2.tStart = t  # local t and not account for scr refresh
        next_intro3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_2, 'tStartRefresh')  # time at next scr refresh
        next_intro3_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_10" ---
for thisComponent in Introduction_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_3_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
poll_3_1_names.setText(ptp_name +':' + '\n'+ names[0]+':' +'\n'+ names[1]+':'+'\n'+ names[2]+':'+'\n'+ names[3]+':' +'\n'+ names[4]+':' +'\n'+ names[5]+':'+'\n'+ names[6]+':')
poll_3_1_responses.setText(ptp_poll_3 +'\n' + poll_3[0] +'\n'+ poll_3[1] +'\n'+ poll_3[2] +'\n'+ poll_3[3] +'\n'+ poll_3[4] +'\n'+ poll_3[5] +'\n'+ poll_3[6])
# Run 'Begin Routine' code from poll_code_8
poll_next_3_1.bold = 'True'
poll_3_1_names.alignText = 'Left'
poll_3_1_names.bold = 'True'
poll_3_1_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_3_1Components = [image_46, polygon_5, key_resp_3, poll_next_3_1, poll_3_1_names, poll_3_1_responses]
for thisComponent in poll_resp_3_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_3_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_46* updates
    if image_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_46.frameNStart = frameN  # exact frame index
        image_46.tStart = t  # local t and not account for scr refresh
        image_46.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_46, 'tStartRefresh')  # time at next scr refresh
        image_46.setAutoDraw(True)
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_3_1* updates
    if poll_next_3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_3_1.frameNStart = frameN  # exact frame index
        poll_next_3_1.tStart = t  # local t and not account for scr refresh
        poll_next_3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_3_1, 'tStartRefresh')  # time at next scr refresh
        poll_next_3_1.setAutoDraw(True)
    
    # *poll_3_1_names* updates
    if poll_3_1_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_3_1_names.frameNStart = frameN  # exact frame index
        poll_3_1_names.tStart = t  # local t and not account for scr refresh
        poll_3_1_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_3_1_names, 'tStartRefresh')  # time at next scr refresh
        poll_3_1_names.setAutoDraw(True)
    
    # *poll_3_1_responses* updates
    if poll_3_1_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_3_1_responses.frameNStart = frameN  # exact frame index
        poll_3_1_responses.tStart = t  # local t and not account for scr refresh
        poll_3_1_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_3_1_responses, 'tStartRefresh')  # time at next scr refresh
        poll_3_1_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_3_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_3_1" ---
for thisComponent in poll_resp_3_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_3_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pol_resp_3_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_31.keys = []
key_resp_31.rt = []
_key_resp_31_allKeys = []
poll_3_2_names.setText(names[7]+':' +'\n'+ names[8]+':'+'\n'+ names[9]+':'+'\n'+ names[10]+':' +'\n'+ names[11]+':')
poll_3_2_responses.setText(poll_3[7] +'\n'+ poll_3[8] +'\n'+ poll_3[9] +'\n'+ poll_3[10] +'\n'+ poll_3[11] )
# Run 'Begin Routine' code from poll_code_7
poll_next_3_2.bold = 'True'
poll_3_2_names.alignText = 'Left'
poll_3_2_names.bold = 'True'
poll_3_2_responses.alignText = 'Left'

# keep track of which components have finished
pol_resp_3_2Components = [image_45, polygon_32, key_resp_31, poll_next_3_2, poll_3_2_names, poll_3_2_responses]
for thisComponent in pol_resp_3_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pol_resp_3_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_45* updates
    if image_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_45.frameNStart = frameN  # exact frame index
        image_45.tStart = t  # local t and not account for scr refresh
        image_45.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_45, 'tStartRefresh')  # time at next scr refresh
        image_45.setAutoDraw(True)
    
    # *polygon_32* updates
    if polygon_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_32.frameNStart = frameN  # exact frame index
        polygon_32.tStart = t  # local t and not account for scr refresh
        polygon_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_32, 'tStartRefresh')  # time at next scr refresh
        polygon_32.setAutoDraw(True)
    
    # *key_resp_31* updates
    waitOnFlip = False
    if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_31.frameNStart = frameN  # exact frame index
        key_resp_31.tStart = t  # local t and not account for scr refresh
        key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
        key_resp_31.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_31.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_31.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_31_allKeys.extend(theseKeys)
        if len(_key_resp_31_allKeys):
            key_resp_31.keys = _key_resp_31_allKeys[-1].name  # just the last key pressed
            key_resp_31.rt = _key_resp_31_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_3_2* updates
    if poll_next_3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_3_2.frameNStart = frameN  # exact frame index
        poll_next_3_2.tStart = t  # local t and not account for scr refresh
        poll_next_3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_3_2, 'tStartRefresh')  # time at next scr refresh
        poll_next_3_2.setAutoDraw(True)
    
    # *poll_3_2_names* updates
    if poll_3_2_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_3_2_names.frameNStart = frameN  # exact frame index
        poll_3_2_names.tStart = t  # local t and not account for scr refresh
        poll_3_2_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_3_2_names, 'tStartRefresh')  # time at next scr refresh
        poll_3_2_names.setAutoDraw(True)
    
    # *poll_3_2_responses* updates
    if poll_3_2_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_3_2_responses.frameNStart = frameN  # exact frame index
        poll_3_2_responses.tStart = t  # local t and not account for scr refresh
        poll_3_2_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_3_2_responses, 'tStartRefresh')  # time at next scr refresh
        poll_3_2_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pol_resp_3_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pol_resp_3_2" ---
for thisComponent in pol_resp_3_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pol_resp_3_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_11" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_17.setText('Time to move on to the next round. We are getting closer to the virtual party! \n\nLet’s see if you will be invited. ')
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
next_intro3_3.setText('Press space to continue.')
# Run 'Begin Routine' code from code_21
next_intro3_3.bold = 'True'
# keep track of which components have finished
Introduction_11Components = [image_25, polygon_18, text_17, key_resp_19, next_intro3_3]
for thisComponent in Introduction_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_11" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    
    # *polygon_18* updates
    if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.tStart = t  # local t and not account for scr refresh
        polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
        polygon_18.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_3* updates
    if next_intro3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_3.frameNStart = frameN  # exact frame index
        next_intro3_3.tStart = t  # local t and not account for scr refresh
        next_intro3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_3, 'tStartRefresh')  # time at next scr refresh
        next_intro3_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_11" ---
for thisComponent in Introduction_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
voting_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='voting_4')
thisExp.addLoop(voting_4)  # add the loop to the experiment
thisVoting_4 = voting_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVoting_4.rgb)
if thisVoting_4 != None:
    for paramName in thisVoting_4:
        exec('{} = thisVoting_4[paramName]'.format(paramName))

for thisVoting_4 in voting_4:
    currentLoop = voting_4
    # abbreviate parameter names if possible (e.g. rgb = thisVoting_4.rgb)
    if thisVoting_4 != None:
        for paramName in thisVoting_4:
            exec('{} = thisVoting_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Player_profiles_voting_style_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from capitalization_cop_4
    cop_response_4.alignText = 'left'
    cop_prompts_4.alignText = 'left'
    
    
    # increment i for each loop
    d = d + 1
    
    coplayer_image_4.setImage(photos[d])
    cop_prompts_4.reset()
    cop_response_4.setText(names[d] + '\n' + str(ages[d]) + '\n' + hometowns[d] + '\n' + interests[d] + '\n' + schools[d])
    # setup some python lists for storing info about the click_real_4
    click_real_4.clicked_name = []
    gotValidClick = False  # until a click is received
    vote_question_6.setText('Do you like or dislike ' + names[d] + '?')
    # keep track of which components have finished
    Player_profiles_voting_style_4Components = [border_11, coplayer_image_4, cop_prompts_4, cop_response_4, like_real_button_4, like_real_text_4, dislike_real_button_4, dislike_real_text_4, click_real_4, vote_question_6]
    for thisComponent in Player_profiles_voting_style_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Player_profiles_voting_style_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *border_11* updates
        if border_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_11.frameNStart = frameN  # exact frame index
            border_11.tStart = t  # local t and not account for scr refresh
            border_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_11, 'tStartRefresh')  # time at next scr refresh
            border_11.setAutoDraw(True)
        
        # *coplayer_image_4* updates
        if coplayer_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            coplayer_image_4.frameNStart = frameN  # exact frame index
            coplayer_image_4.tStart = t  # local t and not account for scr refresh
            coplayer_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(coplayer_image_4, 'tStartRefresh')  # time at next scr refresh
            coplayer_image_4.setAutoDraw(True)
        
        # *cop_prompts_4* updates
        if cop_prompts_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts_4.frameNStart = frameN  # exact frame index
            cop_prompts_4.tStart = t  # local t and not account for scr refresh
            cop_prompts_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts_4, 'tStartRefresh')  # time at next scr refresh
            cop_prompts_4.setAutoDraw(True)
        
        # *cop_response_4* updates
        if cop_response_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_response_4.frameNStart = frameN  # exact frame index
            cop_response_4.tStart = t  # local t and not account for scr refresh
            cop_response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_response_4, 'tStartRefresh')  # time at next scr refresh
            cop_response_4.setAutoDraw(True)
        
        # *like_real_button_4* updates
        if like_real_button_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_button_4.frameNStart = frameN  # exact frame index
            like_real_button_4.tStart = t  # local t and not account for scr refresh
            like_real_button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_button_4, 'tStartRefresh')  # time at next scr refresh
            like_real_button_4.setAutoDraw(True)
        
        # *like_real_text_4* updates
        if like_real_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_text_4.frameNStart = frameN  # exact frame index
            like_real_text_4.tStart = t  # local t and not account for scr refresh
            like_real_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_text_4, 'tStartRefresh')  # time at next scr refresh
            like_real_text_4.setAutoDraw(True)
        
        # *dislike_real_button_4* updates
        if dislike_real_button_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_button_4.frameNStart = frameN  # exact frame index
            dislike_real_button_4.tStart = t  # local t and not account for scr refresh
            dislike_real_button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_button_4, 'tStartRefresh')  # time at next scr refresh
            dislike_real_button_4.setAutoDraw(True)
        
        # *dislike_real_text_4* updates
        if dislike_real_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_text_4.frameNStart = frameN  # exact frame index
            dislike_real_text_4.tStart = t  # local t and not account for scr refresh
            dislike_real_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_text_4, 'tStartRefresh')  # time at next scr refresh
            dislike_real_text_4.setAutoDraw(True)
        # *click_real_4* updates
        if click_real_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            click_real_4.frameNStart = frameN  # exact frame index
            click_real_4.tStart = t  # local t and not account for scr refresh
            click_real_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_real_4, 'tStartRefresh')  # time at next scr refresh
            click_real_4.status = STARTED
            click_real_4.mouseClock.reset()
            prevButtonState = click_real_4.getPressed()  # if button is down already this ISN'T a new click
        if click_real_4.status == STARTED:  # only update if started and not finished!
            buttons = click_real_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([like_real_button_4, dislike_real_button_4])
                        clickableList = [like_real_button_4, dislike_real_button_4]
                    except:
                        clickableList = [[like_real_button_4, dislike_real_button_4]]
                    for obj in clickableList:
                        if obj.contains(click_real_4):
                            gotValidClick = True
                            click_real_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *vote_question_6* updates
        if vote_question_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_question_6.frameNStart = frameN  # exact frame index
            vote_question_6.tStart = t  # local t and not account for scr refresh
            vote_question_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_question_6, 'tStartRefresh')  # time at next scr refresh
            vote_question_6.setAutoDraw(True)
        # Run 'Each Frame' code from ptp_vote_4
        ptp_v = ''
        if mouse.isPressedIn(like_real_button_4):
            ptp_v="Like"
        elif mouse.isPressedIn(dislike_real_button_4):
            ptp_v ="Dislike"
        voting_4.addData('Participant_vote', ptp_v)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Player_profiles_voting_style_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Player_profiles_voting_style_4" ---
    for thisComponent in Player_profiles_voting_style_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for voting_4 (TrialHandler)
    # the Routine "Player_profiles_voting_style_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting_vote_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_6.setText('Compiling votes, your feedback\nwill be presented soon...')
    # keep track of which components have finished
    Waiting_vote_2Components = [wait_6, load_white1_2, fixation_r_2]
    for thisComponent in Waiting_vote_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_6* updates
        if wait_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_6.frameNStart = frameN  # exact frame index
            wait_6.tStart = t  # local t and not account for scr refresh
            wait_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_6, 'tStartRefresh')  # time at next scr refresh
            wait_6.setAutoDraw(True)
        if wait_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_6.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                wait_6.tStop = t  # not accounting for scr refresh
                wait_6.frameNStop = frameN  # exact frame index
                wait_6.setAutoDraw(False)
        
        # *load_white1_2* updates
        if load_white1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            load_white1_2.frameNStart = frameN  # exact frame index
            load_white1_2.tStart = t  # local t and not account for scr refresh
            load_white1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_white1_2, 'tStartRefresh')  # time at next scr refresh
            load_white1_2.setAutoDraw(True)
        if load_white1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > load_white1_2.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                load_white1_2.tStop = t  # not accounting for scr refresh
                load_white1_2.frameNStop = frameN  # exact frame index
                load_white1_2.setAutoDraw(False)
        
        # *fixation_r_2* updates
        if fixation_r_2.status == NOT_STARTED and tThisFlip >= vote_duration-frameTolerance:
            # keep track of start time/frame for later
            fixation_r_2.frameNStart = frameN  # exact frame index
            fixation_r_2.tStart = t  # local t and not account for scr refresh
            fixation_r_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_r_2, 'tStartRefresh')  # time at next scr refresh
            fixation_r_2.setAutoDraw(True)
        if fixation_r_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_r_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_r_2.tStop = t  # not accounting for scr refresh
                fixation_r_2.frameNStop = frameN  # exact frame index
                fixation_r_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_2" ---
    for thisComponent in Waiting_vote_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Waiting_vote_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cop_vote_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_thumb_4
    if vote_all[d][3] == '1':
        image_thumb = 'images/thumb-up.png'
        save_vote = 'Like'
        play_round = '4'
        cop_type = vote_all[d][5]
    else:
        image_thumb = 'images/thumb-down.png'
        save_vote = 'Dislike'
        play_round = '4'
        cop_type = vote_all[d][5]
    voting_4.addData('Study ID', expInfo['Study ID'])
    voting_4.addData('Coplayer_vote', save_vote)
    voting_4.addData('Round', play_round)
    voting_4.addData('Coplayer_type', cop_type)
    vote_image_4.setImage(image_thumb)
    # keep track of which components have finished
    Cop_vote_4Components = [vote_image_4]
    for thisComponent in Cop_vote_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cop_vote_4" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vote_image_4* updates
        if vote_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_image_4.frameNStart = frameN  # exact frame index
            vote_image_4.tStart = t  # local t and not account for scr refresh
            vote_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_image_4, 'tStartRefresh')  # time at next scr refresh
            vote_image_4.setAutoDraw(True)
        if vote_image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vote_image_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                vote_image_4.tStop = t  # not accounting for scr refresh
                vote_image_4.frameNStop = frameN  # exact frame index
                vote_image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cop_vote_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cop_vote_4" ---
    for thisComponent in Cop_vote_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Waiting_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_7.setText('+')
    # keep track of which components have finished
    Waiting_vote_3Components = [wait_7]
    for thisComponent in Waiting_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_7* updates
        if wait_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_7.frameNStart = frameN  # exact frame index
            wait_7.tStart = t  # local t and not account for scr refresh
            wait_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_7, 'tStartRefresh')  # time at next scr refresh
            wait_7.setAutoDraw(True)
        if wait_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wait_7.tStop = t  # not accounting for scr refresh
                wait_7.frameNStop = frameN  # exact frame index
                wait_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_3" ---
    for thisComponent in Waiting_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'voting_4'

# get names of stimulus parameters
if voting_4.trialList in ([], [None], None):
    params = []
else:
    params = voting_4.trialList[0].keys()
# save data for this loop
voting_4.saveAsExcel(filename + '.xlsx', sheetName='voting_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
voting_4.saveAsText(filename + 'voting_4.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Waiting_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_12.setText('Let’s find out who got the MOST like votes this round...')
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Waiting_3Components = [image_15, polygon_12, text_12, key_resp_12, image_16]
for thisComponent in Waiting_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_3" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            image_15.setAutoDraw(False)
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    if polygon_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_12.tStop = t  # not accounting for scr refresh
            polygon_12.frameNStop = frameN  # exact frame index
            polygon_12.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            text_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            image_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_3" ---
for thisComponent in Waiting_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Most_vote_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
most_pic_3.setImage('images/background_mostvote.jpg')
most_vote_4.setImage(photos[m])
name_most_4.setText(names[m])
next_most4.keys = []
next_most4.rt = []
_next_most4_allKeys = []
# keep track of which components have finished
Most_vote_4Components = [most_pic_3, border_20, border_21, most_vote_4, name_most_4, next_most_4, next_most4]
for thisComponent in Most_vote_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Most_vote_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *most_pic_3* updates
    if most_pic_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_pic_3.frameNStart = frameN  # exact frame index
        most_pic_3.tStart = t  # local t and not account for scr refresh
        most_pic_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_pic_3, 'tStartRefresh')  # time at next scr refresh
        most_pic_3.setAutoDraw(True)
    
    # *border_20* updates
    if border_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_20.frameNStart = frameN  # exact frame index
        border_20.tStart = t  # local t and not account for scr refresh
        border_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_20, 'tStartRefresh')  # time at next scr refresh
        border_20.setAutoDraw(True)
    
    # *border_21* updates
    if border_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_21.frameNStart = frameN  # exact frame index
        border_21.tStart = t  # local t and not account for scr refresh
        border_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_21, 'tStartRefresh')  # time at next scr refresh
        border_21.setAutoDraw(True)
    
    # *most_vote_4* updates
    if most_vote_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_vote_4.frameNStart = frameN  # exact frame index
        most_vote_4.tStart = t  # local t and not account for scr refresh
        most_vote_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_vote_4, 'tStartRefresh')  # time at next scr refresh
        most_vote_4.setAutoDraw(True)
    
    # *name_most_4* updates
    if name_most_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_most_4.frameNStart = frameN  # exact frame index
        name_most_4.tStart = t  # local t and not account for scr refresh
        name_most_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_most_4, 'tStartRefresh')  # time at next scr refresh
        name_most_4.setAutoDraw(True)
    
    # *next_most_4* updates
    if next_most_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most_4.frameNStart = frameN  # exact frame index
        next_most_4.tStart = t  # local t and not account for scr refresh
        next_most_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most_4, 'tStartRefresh')  # time at next scr refresh
        next_most_4.setAutoDraw(True)
    
    # *next_most4* updates
    waitOnFlip = False
    if next_most4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most4.frameNStart = frameN  # exact frame index
        next_most4.tStart = t  # local t and not account for scr refresh
        next_most4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most4, 'tStartRefresh')  # time at next scr refresh
        next_most4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_most4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_most4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_most4.status == STARTED and not waitOnFlip:
        theseKeys = next_most4.getKeys(keyList=['space'], waitRelease=False)
        _next_most4_allKeys.extend(theseKeys)
        if len(_next_most4_allKeys):
            next_most4.keys = _next_most4_allKeys[-1].name  # just the last key pressed
            next_most4.rt = _next_most4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Most_vote_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Most_vote_4" ---
for thisComponent in Most_vote_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Most_vote_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_13.setText('Let’s find out who got the LEAST like votes this round...')
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Waiting_4Components = [image_17, polygon_13, text_13, key_resp_14, image_18]
for thisComponent in Waiting_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_4" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            image_17.setAutoDraw(False)
    
    # *polygon_13* updates
    if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.tStart = t  # local t and not account for scr refresh
        polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
        polygon_13.setAutoDraw(True)
    if polygon_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_13.tStop = t  # not accounting for scr refresh
            polygon_13.frameNStop = frameN  # exact frame index
            polygon_13.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            text_13.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            image_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_4" ---
for thisComponent in Waiting_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Least_vote_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image_32.setImage('images/sad.jpg')
least_vote_4.setImage(photos[l])
name_least_4.setText(names[l])
next_least4.keys = []
next_least4.rt = []
_next_least4_allKeys = []
# keep track of which components have finished
Least_vote_4Components = [image_32, border4_7, border_19, least_vote_4, name_least_4, next_least_4, next_least4]
for thisComponent in Least_vote_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Least_vote_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_32* updates
    if image_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_32.frameNStart = frameN  # exact frame index
        image_32.tStart = t  # local t and not account for scr refresh
        image_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_32, 'tStartRefresh')  # time at next scr refresh
        image_32.setAutoDraw(True)
    
    # *border4_7* updates
    if border4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border4_7.frameNStart = frameN  # exact frame index
        border4_7.tStart = t  # local t and not account for scr refresh
        border4_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border4_7, 'tStartRefresh')  # time at next scr refresh
        border4_7.setAutoDraw(True)
    
    # *border_19* updates
    if border_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_19.frameNStart = frameN  # exact frame index
        border_19.tStart = t  # local t and not account for scr refresh
        border_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_19, 'tStartRefresh')  # time at next scr refresh
        border_19.setAutoDraw(True)
    
    # *least_vote_4* updates
    if least_vote_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        least_vote_4.frameNStart = frameN  # exact frame index
        least_vote_4.tStart = t  # local t and not account for scr refresh
        least_vote_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(least_vote_4, 'tStartRefresh')  # time at next scr refresh
        least_vote_4.setAutoDraw(True)
    
    # *name_least_4* updates
    if name_least_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_least_4.frameNStart = frameN  # exact frame index
        name_least_4.tStart = t  # local t and not account for scr refresh
        name_least_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_least_4, 'tStartRefresh')  # time at next scr refresh
        name_least_4.setAutoDraw(True)
    
    # *next_least_4* updates
    if next_least_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least_4.frameNStart = frameN  # exact frame index
        next_least_4.tStart = t  # local t and not account for scr refresh
        next_least_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least_4, 'tStartRefresh')  # time at next scr refresh
        next_least_4.setAutoDraw(True)
    
    # *next_least4* updates
    waitOnFlip = False
    if next_least4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least4.frameNStart = frameN  # exact frame index
        next_least4.tStart = t  # local t and not account for scr refresh
        next_least4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least4, 'tStartRefresh')  # time at next scr refresh
        next_least4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_least4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_least4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_least4.status == STARTED and not waitOnFlip:
        theseKeys = next_least4.getKeys(keyList=['space'], waitRelease=False)
        _next_least4_allKeys.extend(theseKeys)
        if len(_next_least4_allKeys):
            next_least4.keys = _next_least4_allKeys[-1].name  # just the last key pressed
            next_least4.rt = _next_least4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Least_vote_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Least_vote_4" ---
for thisComponent in Least_vote_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from least_votes_4
# create random index numbers for most/least player
m = most_least_index[8]
l = most_least_index[9]
    
    
# the Routine "Least_vote_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "round_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_30.setText('Time to move on to the next round. We are getting closer to the virtual party! Let’s see if you will be invited.')
key_resp_26.keys = []
key_resp_26.rt = []
_key_resp_26_allKeys = []
next_intro3_7.setText('Press space to continue.')
# Run 'Begin Routine' code from code_35
next_intro3_7.bold = 'True'
# keep track of which components have finished
round_4Components = [image_39, polygon_27, text_30, key_resp_26, next_intro3_7]
for thisComponent in round_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "round_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_39* updates
    if image_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_39.frameNStart = frameN  # exact frame index
        image_39.tStart = t  # local t and not account for scr refresh
        image_39.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_39, 'tStartRefresh')  # time at next scr refresh
        image_39.setAutoDraw(True)
    
    # *polygon_27* updates
    if polygon_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_27.frameNStart = frameN  # exact frame index
        polygon_27.tStart = t  # local t and not account for scr refresh
        polygon_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_27, 'tStartRefresh')  # time at next scr refresh
        polygon_27.setAutoDraw(True)
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    
    # *key_resp_26* updates
    waitOnFlip = False
    if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_26.frameNStart = frameN  # exact frame index
        key_resp_26.tStart = t  # local t and not account for scr refresh
        key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
        key_resp_26.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_26.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_26.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_26_allKeys.extend(theseKeys)
        if len(_key_resp_26_allKeys):
            key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
            key_resp_26.rt = _key_resp_26_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_7* updates
    if next_intro3_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_7.frameNStart = frameN  # exact frame index
        next_intro3_7.tStart = t  # local t and not account for scr refresh
        next_intro3_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_7, 'tStartRefresh')  # time at next scr refresh
        next_intro3_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in round_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "round_4" ---
for thisComponent in round_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "round_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_12" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
Introduction_12Components = [image_26, polygon_19, text_18, next_intro7_7, key_resp_20]
for thisComponent in Introduction_12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_12" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_26* updates
    if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_26.frameNStart = frameN  # exact frame index
        image_26.tStart = t  # local t and not account for scr refresh
        image_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
        image_26.setAutoDraw(True)
    
    # *polygon_19* updates
    if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_19.frameNStart = frameN  # exact frame index
        polygon_19.tStart = t  # local t and not account for scr refresh
        polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
        polygon_19.setAutoDraw(True)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # *next_intro7_7* updates
    if next_intro7_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro7_7.frameNStart = frameN  # exact frame index
        next_intro7_7.tStart = t  # local t and not account for scr refresh
        next_intro7_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro7_7, 'tStartRefresh')  # time at next scr refresh
        next_intro7_7.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_12" ---
for thisComponent in Introduction_12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Poll_q4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
poll_question_4.setText('What is your least favorite class?')
poll_enter_4.reset()
poll_enter_4.setText('')
# setup some python lists for storing info about the mouse5_4
mouse5_4.clicked_name = []
gotValidClick = False  # until a click is received
ptp_poll_4 = poll_enter_4.text  # Set routine start values for ptp_poll_4
# keep track of which components have finished
Poll_q4Components = [poll_question_4, poll_enter_4, button5_4, submit5_4, mouse5_4]
for thisComponent in Poll_q4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Poll_q4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *poll_question_4* updates
    if poll_question_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_question_4.frameNStart = frameN  # exact frame index
        poll_question_4.tStart = t  # local t and not account for scr refresh
        poll_question_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_question_4, 'tStartRefresh')  # time at next scr refresh
        poll_question_4.setAutoDraw(True)
    
    # *poll_enter_4* updates
    if poll_enter_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_enter_4.frameNStart = frameN  # exact frame index
        poll_enter_4.tStart = t  # local t and not account for scr refresh
        poll_enter_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_enter_4, 'tStartRefresh')  # time at next scr refresh
        poll_enter_4.setAutoDraw(True)
    
    # *button5_4* updates
    if button5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button5_4.frameNStart = frameN  # exact frame index
        button5_4.tStart = t  # local t and not account for scr refresh
        button5_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5_4, 'tStartRefresh')  # time at next scr refresh
        button5_4.setAutoDraw(True)
    
    # *submit5_4* updates
    if submit5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit5_4.frameNStart = frameN  # exact frame index
        submit5_4.tStart = t  # local t and not account for scr refresh
        submit5_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit5_4, 'tStartRefresh')  # time at next scr refresh
        submit5_4.setAutoDraw(True)
    # *mouse5_4* updates
    if mouse5_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5_4.frameNStart = frameN  # exact frame index
        mouse5_4.tStart = t  # local t and not account for scr refresh
        mouse5_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5_4, 'tStartRefresh')  # time at next scr refresh
        mouse5_4.status = STARTED
        mouse5_4.mouseClock.reset()
        prevButtonState = mouse5_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse5_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse5_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button5_4)
                    clickableList = button5_4
                except:
                    clickableList = [button5_4]
                for obj in clickableList:
                    if obj.contains(mouse5_4):
                        gotValidClick = True
                        mouse5_4.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_poll_4 = poll_enter_4.text  # Set frame start values for ptp_poll_4
    ptp_poll_4Container.append(ptp_poll_4)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Poll_q4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Poll_q4" ---
for thisComponent in Poll_q4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('poll_enter_4.text',poll_enter_4.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_poll_4.routineEndVal', ptp_poll_4)  # Save end routine value
# the Routine "Poll_q4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_11.setText('Waiting for others to answer the poll question...')
# keep track of which components have finished
Waiting_5Components = [image_19, polygon_16, text_11, image_23]
for thisComponent in Waiting_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_5" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            image_19.setAutoDraw(False)
    
    # *polygon_16* updates
    if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_16.frameNStart = frameN  # exact frame index
        polygon_16.tStart = t  # local t and not account for scr refresh
        polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
        polygon_16.setAutoDraw(True)
    if polygon_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_16.tStop = t  # not accounting for scr refresh
            polygon_16.frameNStop = frameN  # exact frame index
            polygon_16.setAutoDraw(False)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            text_11.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            image_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_5" ---
for thisComponent in Waiting_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Introduction_10" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_16.setText("All players have answered the poll question now.\n\nLet's see the responses!")
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
next_intro3_2.setText('Press space to continue.')
# Run 'Begin Routine' code from code_20
next_intro3_2.bold = 'True'
# keep track of which components have finished
Introduction_10Components = [image_24, polygon_17, text_16, key_resp_18, next_intro3_2]
for thisComponent in Introduction_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_10" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *polygon_17* updates
    if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.tStart = t  # local t and not account for scr refresh
        polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
        polygon_17.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_2* updates
    if next_intro3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_2.frameNStart = frameN  # exact frame index
        next_intro3_2.tStart = t  # local t and not account for scr refresh
        next_intro3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_2, 'tStartRefresh')  # time at next scr refresh
        next_intro3_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_10" ---
for thisComponent in Introduction_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "poll_resp_4_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
poll_4_1_names.setText(ptp_name +':' + '\n'+ names[0]+':' +'\n'+ names[1]+':'+'\n'+ names[2]+':'+'\n'+ names[3]+':' +'\n'+ names[4]+':' +'\n'+ names[5]+':'+'\n'+ names[6]+':')
poll_4_1_responses.setText(ptp_poll_4 +'\n' + poll_4[0] +'\n'+ poll_4[1] +'\n'+ poll_4[2] +'\n'+ poll_4[3] +'\n'+ poll_4[4] +'\n'+ poll_4[5] +'\n'+ poll_4[6])
# Run 'Begin Routine' code from poll_code_9
poll_next_4_1.bold = 'True'
poll_4_1_names.alignText = 'Left'
poll_4_1_names.bold = 'True'
poll_4_1_responses.alignText = 'Left'

# keep track of which components have finished
poll_resp_4_1Components = [image_47, polygon_6, key_resp_6, poll_next_4_1, poll_4_1_names, poll_4_1_responses]
for thisComponent in poll_resp_4_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "poll_resp_4_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_47* updates
    if image_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_47.frameNStart = frameN  # exact frame index
        image_47.tStart = t  # local t and not account for scr refresh
        image_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_47, 'tStartRefresh')  # time at next scr refresh
        image_47.setAutoDraw(True)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_4_1* updates
    if poll_next_4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_4_1.frameNStart = frameN  # exact frame index
        poll_next_4_1.tStart = t  # local t and not account for scr refresh
        poll_next_4_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_4_1, 'tStartRefresh')  # time at next scr refresh
        poll_next_4_1.setAutoDraw(True)
    
    # *poll_4_1_names* updates
    if poll_4_1_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_4_1_names.frameNStart = frameN  # exact frame index
        poll_4_1_names.tStart = t  # local t and not account for scr refresh
        poll_4_1_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_4_1_names, 'tStartRefresh')  # time at next scr refresh
        poll_4_1_names.setAutoDraw(True)
    
    # *poll_4_1_responses* updates
    if poll_4_1_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_4_1_responses.frameNStart = frameN  # exact frame index
        poll_4_1_responses.tStart = t  # local t and not account for scr refresh
        poll_4_1_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_4_1_responses, 'tStartRefresh')  # time at next scr refresh
        poll_4_1_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poll_resp_4_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "poll_resp_4_1" ---
for thisComponent in poll_resp_4_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "poll_resp_4_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pol_resp_4_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_32.keys = []
key_resp_32.rt = []
_key_resp_32_allKeys = []
poll_4_2_names.setText(names[7]+':' +'\n'+ names[8]+':'+'\n'+ names[9]+':'+'\n'+ names[10]+':' +'\n'+ names[11]+':')
poll_4_2_responses.setText(poll_4[7] +'\n'+ poll_4[8] +'\n'+ poll_4[9] +'\n'+ poll_4[10] +'\n'+ poll_4[11] )
# Run 'Begin Routine' code from poll_code_10
poll_next_4_2.bold = 'True'
poll_4_2_names.alignText = 'Left'
poll_4_2_names.bold = 'True'
poll_4_2_responses.alignText = 'Left'

# keep track of which components have finished
pol_resp_4_2Components = [image_48, polygon_33, key_resp_32, poll_next_4_2, poll_4_2_names, poll_4_2_responses]
for thisComponent in pol_resp_4_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pol_resp_4_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_48* updates
    if image_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_48.frameNStart = frameN  # exact frame index
        image_48.tStart = t  # local t and not account for scr refresh
        image_48.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_48, 'tStartRefresh')  # time at next scr refresh
        image_48.setAutoDraw(True)
    
    # *polygon_33* updates
    if polygon_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_33.frameNStart = frameN  # exact frame index
        polygon_33.tStart = t  # local t and not account for scr refresh
        polygon_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_33, 'tStartRefresh')  # time at next scr refresh
        polygon_33.setAutoDraw(True)
    
    # *key_resp_32* updates
    waitOnFlip = False
    if key_resp_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_32.frameNStart = frameN  # exact frame index
        key_resp_32.tStart = t  # local t and not account for scr refresh
        key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
        key_resp_32.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_32.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_32.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_32_allKeys.extend(theseKeys)
        if len(_key_resp_32_allKeys):
            key_resp_32.keys = _key_resp_32_allKeys[-1].name  # just the last key pressed
            key_resp_32.rt = _key_resp_32_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *poll_next_4_2* updates
    if poll_next_4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_next_4_2.frameNStart = frameN  # exact frame index
        poll_next_4_2.tStart = t  # local t and not account for scr refresh
        poll_next_4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_next_4_2, 'tStartRefresh')  # time at next scr refresh
        poll_next_4_2.setAutoDraw(True)
    
    # *poll_4_2_names* updates
    if poll_4_2_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_4_2_names.frameNStart = frameN  # exact frame index
        poll_4_2_names.tStart = t  # local t and not account for scr refresh
        poll_4_2_names.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_4_2_names, 'tStartRefresh')  # time at next scr refresh
        poll_4_2_names.setAutoDraw(True)
    
    # *poll_4_2_responses* updates
    if poll_4_2_responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poll_4_2_responses.frameNStart = frameN  # exact frame index
        poll_4_2_responses.tStart = t  # local t and not account for scr refresh
        poll_4_2_responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poll_4_2_responses, 'tStartRefresh')  # time at next scr refresh
        poll_4_2_responses.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pol_resp_4_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pol_resp_4_2" ---
for thisComponent in pol_resp_4_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pol_resp_4_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Introduction_11" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_17.setText('Time to move on to the next round. We are getting closer to the virtual party! \n\nLet’s see if you will be invited. ')
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
next_intro3_3.setText('Press space to continue.')
# Run 'Begin Routine' code from code_21
next_intro3_3.bold = 'True'
# keep track of which components have finished
Introduction_11Components = [image_25, polygon_18, text_17, key_resp_19, next_intro3_3]
for thisComponent in Introduction_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Introduction_11" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    
    # *polygon_18* updates
    if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.tStart = t  # local t and not account for scr refresh
        polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
        polygon_18.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_intro3_3* updates
    if next_intro3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_intro3_3.frameNStart = frameN  # exact frame index
        next_intro3_3.tStart = t  # local t and not account for scr refresh
        next_intro3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_intro3_3, 'tStartRefresh')  # time at next scr refresh
        next_intro3_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_11" ---
for thisComponent in Introduction_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
voting_5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials.xlsx'),
    seed=None, name='voting_5')
thisExp.addLoop(voting_5)  # add the loop to the experiment
thisVoting_5 = voting_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVoting_5.rgb)
if thisVoting_5 != None:
    for paramName in thisVoting_5:
        exec('{} = thisVoting_5[paramName]'.format(paramName))

for thisVoting_5 in voting_5:
    currentLoop = voting_5
    # abbreviate parameter names if possible (e.g. rgb = thisVoting_5.rgb)
    if thisVoting_5 != None:
        for paramName in thisVoting_5:
            exec('{} = thisVoting_5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Player_profiles_voting_style_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from capitalization_cop_5
    cop_response_5.alignText = 'left'
    cop_prompts_5.alignText = 'left'
    
    
    # increment e for each loop
    e = e + 1
    
    coplayer_image_5.setImage(photos[e])
    cop_prompts_5.reset()
    cop_response_5.setText(names[e] + '\n' + str(ages[e]) + '\n' + hometowns[e] + '\n' + interests[e] + '\n' + schools[e])
    # setup some python lists for storing info about the click_real_5
    click_real_5.clicked_name = []
    gotValidClick = False  # until a click is received
    vote_question_7.setText('Do you like or dislike ' + names[e] + '?')
    # keep track of which components have finished
    Player_profiles_voting_style_5Components = [border_12, coplayer_image_5, cop_prompts_5, cop_response_5, like_real_button_5, like_real_text_5, dislike_real_button_5, dislike_real_text_5, click_real_5, vote_question_7]
    for thisComponent in Player_profiles_voting_style_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Player_profiles_voting_style_5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *border_12* updates
        if border_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border_12.frameNStart = frameN  # exact frame index
            border_12.tStart = t  # local t and not account for scr refresh
            border_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border_12, 'tStartRefresh')  # time at next scr refresh
            border_12.setAutoDraw(True)
        
        # *coplayer_image_5* updates
        if coplayer_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            coplayer_image_5.frameNStart = frameN  # exact frame index
            coplayer_image_5.tStart = t  # local t and not account for scr refresh
            coplayer_image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(coplayer_image_5, 'tStartRefresh')  # time at next scr refresh
            coplayer_image_5.setAutoDraw(True)
        
        # *cop_prompts_5* updates
        if cop_prompts_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_prompts_5.frameNStart = frameN  # exact frame index
            cop_prompts_5.tStart = t  # local t and not account for scr refresh
            cop_prompts_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_prompts_5, 'tStartRefresh')  # time at next scr refresh
            cop_prompts_5.setAutoDraw(True)
        
        # *cop_response_5* updates
        if cop_response_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cop_response_5.frameNStart = frameN  # exact frame index
            cop_response_5.tStart = t  # local t and not account for scr refresh
            cop_response_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cop_response_5, 'tStartRefresh')  # time at next scr refresh
            cop_response_5.setAutoDraw(True)
        
        # *like_real_button_5* updates
        if like_real_button_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_button_5.frameNStart = frameN  # exact frame index
            like_real_button_5.tStart = t  # local t and not account for scr refresh
            like_real_button_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_button_5, 'tStartRefresh')  # time at next scr refresh
            like_real_button_5.setAutoDraw(True)
        
        # *like_real_text_5* updates
        if like_real_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_real_text_5.frameNStart = frameN  # exact frame index
            like_real_text_5.tStart = t  # local t and not account for scr refresh
            like_real_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_real_text_5, 'tStartRefresh')  # time at next scr refresh
            like_real_text_5.setAutoDraw(True)
        
        # *dislike_real_button_5* updates
        if dislike_real_button_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_button_5.frameNStart = frameN  # exact frame index
            dislike_real_button_5.tStart = t  # local t and not account for scr refresh
            dislike_real_button_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_button_5, 'tStartRefresh')  # time at next scr refresh
            dislike_real_button_5.setAutoDraw(True)
        
        # *dislike_real_text_5* updates
        if dislike_real_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dislike_real_text_5.frameNStart = frameN  # exact frame index
            dislike_real_text_5.tStart = t  # local t and not account for scr refresh
            dislike_real_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dislike_real_text_5, 'tStartRefresh')  # time at next scr refresh
            dislike_real_text_5.setAutoDraw(True)
        # *click_real_5* updates
        if click_real_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            click_real_5.frameNStart = frameN  # exact frame index
            click_real_5.tStart = t  # local t and not account for scr refresh
            click_real_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_real_5, 'tStartRefresh')  # time at next scr refresh
            click_real_5.status = STARTED
            click_real_5.mouseClock.reset()
            prevButtonState = click_real_5.getPressed()  # if button is down already this ISN'T a new click
        if click_real_5.status == STARTED:  # only update if started and not finished!
            buttons = click_real_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([like_real_button_5, dislike_real_button_5])
                        clickableList = [like_real_button_5, dislike_real_button_5]
                    except:
                        clickableList = [[like_real_button_5, dislike_real_button_5]]
                    for obj in clickableList:
                        if obj.contains(click_real_5):
                            gotValidClick = True
                            click_real_5.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *vote_question_7* updates
        if vote_question_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_question_7.frameNStart = frameN  # exact frame index
            vote_question_7.tStart = t  # local t and not account for scr refresh
            vote_question_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_question_7, 'tStartRefresh')  # time at next scr refresh
            vote_question_7.setAutoDraw(True)
        # Run 'Each Frame' code from ptp_vote_5
        ptp_v = ''
        if mouse.isPressedIn(like_real_button_5):
            ptp_v="Like"
        elif mouse.isPressedIn(dislike_real_button_5):
            ptp_v ="Dislike"
        voting_5.addData('Participant_vote', ptp_v)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Player_profiles_voting_style_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Player_profiles_voting_style_5" ---
    for thisComponent in Player_profiles_voting_style_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for voting_5 (TrialHandler)
    # the Routine "Player_profiles_voting_style_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting_vote_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_6.setText('Compiling votes, your feedback\nwill be presented soon...')
    # keep track of which components have finished
    Waiting_vote_2Components = [wait_6, load_white1_2, fixation_r_2]
    for thisComponent in Waiting_vote_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_6* updates
        if wait_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_6.frameNStart = frameN  # exact frame index
            wait_6.tStart = t  # local t and not account for scr refresh
            wait_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_6, 'tStartRefresh')  # time at next scr refresh
            wait_6.setAutoDraw(True)
        if wait_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_6.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                wait_6.tStop = t  # not accounting for scr refresh
                wait_6.frameNStop = frameN  # exact frame index
                wait_6.setAutoDraw(False)
        
        # *load_white1_2* updates
        if load_white1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            load_white1_2.frameNStart = frameN  # exact frame index
            load_white1_2.tStart = t  # local t and not account for scr refresh
            load_white1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(load_white1_2, 'tStartRefresh')  # time at next scr refresh
            load_white1_2.setAutoDraw(True)
        if load_white1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > load_white1_2.tStartRefresh + vote_duration-frameTolerance:
                # keep track of stop time/frame for later
                load_white1_2.tStop = t  # not accounting for scr refresh
                load_white1_2.frameNStop = frameN  # exact frame index
                load_white1_2.setAutoDraw(False)
        
        # *fixation_r_2* updates
        if fixation_r_2.status == NOT_STARTED and tThisFlip >= vote_duration-frameTolerance:
            # keep track of start time/frame for later
            fixation_r_2.frameNStart = frameN  # exact frame index
            fixation_r_2.tStart = t  # local t and not account for scr refresh
            fixation_r_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_r_2, 'tStartRefresh')  # time at next scr refresh
            fixation_r_2.setAutoDraw(True)
        if fixation_r_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_r_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_r_2.tStop = t  # not accounting for scr refresh
                fixation_r_2.frameNStop = frameN  # exact frame index
                fixation_r_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_2" ---
    for thisComponent in Waiting_vote_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Waiting_vote_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cop_vote_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_thumb_5
    if vote_all[e][4] == '1':
        image_thumb = 'images/thumb-up.png'
        save_vote = 'Like'
        play_round = '5'
        cop_type = vote_all[e][5]
    else:
        image_thumb = 'images/thumb-down.png'
        save_vote = 'Dislike'
        play_round = '5'
        cop_type = vote_all[e][5]
    voting_5.addData('Study ID', expInfo['Study ID'])
    voting_5.addData('Coplayer_vote', save_vote)
    voting_5.addData('Round', play_round)
    voting_5.addData('Coplayer_type', cop_type)
    vote_image_5.setImage(image_thumb)
    # keep track of which components have finished
    Cop_vote_5Components = [vote_image_5]
    for thisComponent in Cop_vote_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cop_vote_5" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vote_image_5* updates
        if vote_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vote_image_5.frameNStart = frameN  # exact frame index
            vote_image_5.tStart = t  # local t and not account for scr refresh
            vote_image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vote_image_5, 'tStartRefresh')  # time at next scr refresh
            vote_image_5.setAutoDraw(True)
        if vote_image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vote_image_5.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                vote_image_5.tStop = t  # not accounting for scr refresh
                vote_image_5.frameNStop = frameN  # exact frame index
                vote_image_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cop_vote_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cop_vote_5" ---
    for thisComponent in Cop_vote_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Waiting_vote_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_7.setText('+')
    # keep track of which components have finished
    Waiting_vote_3Components = [wait_7]
    for thisComponent in Waiting_vote_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting_vote_3" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_7* updates
        if wait_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_7.frameNStart = frameN  # exact frame index
            wait_7.tStart = t  # local t and not account for scr refresh
            wait_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_7, 'tStartRefresh')  # time at next scr refresh
            wait_7.setAutoDraw(True)
        if wait_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wait_7.tStop = t  # not accounting for scr refresh
                wait_7.frameNStop = frameN  # exact frame index
                wait_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting_vote_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting_vote_3" ---
    for thisComponent in Waiting_vote_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'voting_5'

# get names of stimulus parameters
if voting_5.trialList in ([], [None], None):
    params = []
else:
    params = voting_5.trialList[0].keys()
# save data for this loop
voting_5.saveAsExcel(filename + '.xlsx', sheetName='voting_5',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
voting_5.saveAsText(filename + 'voting_5.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Waiting_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_12.setText('Let’s find out who got the MOST like votes this round...')
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
Waiting_3Components = [image_15, polygon_12, text_12, key_resp_12, image_16]
for thisComponent in Waiting_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_3" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            image_15.setAutoDraw(False)
    
    # *polygon_12* updates
    if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.tStart = t  # local t and not account for scr refresh
        polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
        polygon_12.setAutoDraw(True)
    if polygon_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_12.tStop = t  # not accounting for scr refresh
            polygon_12.frameNStop = frameN  # exact frame index
            polygon_12.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            text_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=None, waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            image_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_3" ---
for thisComponent in Waiting_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Most_vote_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
most_pic_4.setImage('images/background_mostvote.jpg')
most_vote_5.setImage(photos[m])
name_most_5.setText(names[m])
next_most5.keys = []
next_most5.rt = []
_next_most5_allKeys = []
# keep track of which components have finished
Most_vote_5Components = [most_pic_4, border_22, border_23, most_vote_5, name_most_5, next_most_5, next_most5]
for thisComponent in Most_vote_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Most_vote_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *most_pic_4* updates
    if most_pic_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_pic_4.frameNStart = frameN  # exact frame index
        most_pic_4.tStart = t  # local t and not account for scr refresh
        most_pic_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_pic_4, 'tStartRefresh')  # time at next scr refresh
        most_pic_4.setAutoDraw(True)
    
    # *border_22* updates
    if border_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_22.frameNStart = frameN  # exact frame index
        border_22.tStart = t  # local t and not account for scr refresh
        border_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_22, 'tStartRefresh')  # time at next scr refresh
        border_22.setAutoDraw(True)
    
    # *border_23* updates
    if border_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_23.frameNStart = frameN  # exact frame index
        border_23.tStart = t  # local t and not account for scr refresh
        border_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_23, 'tStartRefresh')  # time at next scr refresh
        border_23.setAutoDraw(True)
    
    # *most_vote_5* updates
    if most_vote_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        most_vote_5.frameNStart = frameN  # exact frame index
        most_vote_5.tStart = t  # local t and not account for scr refresh
        most_vote_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(most_vote_5, 'tStartRefresh')  # time at next scr refresh
        most_vote_5.setAutoDraw(True)
    
    # *name_most_5* updates
    if name_most_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_most_5.frameNStart = frameN  # exact frame index
        name_most_5.tStart = t  # local t and not account for scr refresh
        name_most_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_most_5, 'tStartRefresh')  # time at next scr refresh
        name_most_5.setAutoDraw(True)
    
    # *next_most_5* updates
    if next_most_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most_5.frameNStart = frameN  # exact frame index
        next_most_5.tStart = t  # local t and not account for scr refresh
        next_most_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most_5, 'tStartRefresh')  # time at next scr refresh
        next_most_5.setAutoDraw(True)
    
    # *next_most5* updates
    waitOnFlip = False
    if next_most5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_most5.frameNStart = frameN  # exact frame index
        next_most5.tStart = t  # local t and not account for scr refresh
        next_most5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_most5, 'tStartRefresh')  # time at next scr refresh
        next_most5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_most5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_most5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_most5.status == STARTED and not waitOnFlip:
        theseKeys = next_most5.getKeys(keyList=['space'], waitRelease=False)
        _next_most5_allKeys.extend(theseKeys)
        if len(_next_most5_allKeys):
            next_most5.keys = _next_most5_allKeys[-1].name  # just the last key pressed
            next_most5.rt = _next_most5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Most_vote_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Most_vote_5" ---
for thisComponent in Most_vote_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Most_vote_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_13.setText('Let’s find out who got the LEAST like votes this round...')
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Waiting_4Components = [image_17, polygon_13, text_13, key_resp_14, image_18]
for thisComponent in Waiting_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_4" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            image_17.setAutoDraw(False)
    
    # *polygon_13* updates
    if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.tStart = t  # local t and not account for scr refresh
        polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
        polygon_13.setAutoDraw(True)
    if polygon_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_13.tStop = t  # not accounting for scr refresh
            polygon_13.frameNStop = frameN  # exact frame index
            polygon_13.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            text_13.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=None, waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            image_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_4" ---
for thisComponent in Waiting_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Least_vote_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
image_33.setImage('images/sad.jpg')
least_vote_5.setImage(photos[l])
name_least_5.setText(names[l])
next_least5.keys = []
next_least5.rt = []
_next_least5_allKeys = []
# keep track of which components have finished
Least_vote_5Components = [image_33, border4_8, border_24, least_vote_5, name_least_5, next_least_5, next_least5]
for thisComponent in Least_vote_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Least_vote_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_33* updates
    if image_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_33.frameNStart = frameN  # exact frame index
        image_33.tStart = t  # local t and not account for scr refresh
        image_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_33, 'tStartRefresh')  # time at next scr refresh
        image_33.setAutoDraw(True)
    
    # *border4_8* updates
    if border4_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border4_8.frameNStart = frameN  # exact frame index
        border4_8.tStart = t  # local t and not account for scr refresh
        border4_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border4_8, 'tStartRefresh')  # time at next scr refresh
        border4_8.setAutoDraw(True)
    
    # *border_24* updates
    if border_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_24.frameNStart = frameN  # exact frame index
        border_24.tStart = t  # local t and not account for scr refresh
        border_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_24, 'tStartRefresh')  # time at next scr refresh
        border_24.setAutoDraw(True)
    
    # *least_vote_5* updates
    if least_vote_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        least_vote_5.frameNStart = frameN  # exact frame index
        least_vote_5.tStart = t  # local t and not account for scr refresh
        least_vote_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(least_vote_5, 'tStartRefresh')  # time at next scr refresh
        least_vote_5.setAutoDraw(True)
    
    # *name_least_5* updates
    if name_least_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_least_5.frameNStart = frameN  # exact frame index
        name_least_5.tStart = t  # local t and not account for scr refresh
        name_least_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_least_5, 'tStartRefresh')  # time at next scr refresh
        name_least_5.setAutoDraw(True)
    
    # *next_least_5* updates
    if next_least_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least_5.frameNStart = frameN  # exact frame index
        next_least_5.tStart = t  # local t and not account for scr refresh
        next_least_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least_5, 'tStartRefresh')  # time at next scr refresh
        next_least_5.setAutoDraw(True)
    
    # *next_least5* updates
    waitOnFlip = False
    if next_least5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_least5.frameNStart = frameN  # exact frame index
        next_least5.tStart = t  # local t and not account for scr refresh
        next_least5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_least5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'next_least5.started')
        next_least5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_least5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_least5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_least5.status == STARTED and not waitOnFlip:
        theseKeys = next_least5.getKeys(keyList=['space'], waitRelease=False)
        _next_least5_allKeys.extend(theseKeys)
        if len(_next_least5_allKeys):
            next_least5.keys = _next_least5_allKeys[-1].name  # just the last key pressed
            next_least5.rt = _next_least5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Least_vote_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Least_vote_5" ---
for thisComponent in Least_vote_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if next_least5.keys in ['', [], None]:  # No response was made
    next_least5.keys = None
thisExp.addData('next_least5.keys',next_least5.keys)
if next_least5.keys != None:  # we had a response
    thisExp.addData('next_least5.rt', next_least5.rt)
thisExp.nextEntry()
# the Routine "Least_vote_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Waiting_6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_19.setText('Ok, the votes are in and it’s time to find out who is invited to the party… ')
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
Waiting_6Components = [image_34, polygon_23, text_19, key_resp_15, image_35]
for thisComponent in Waiting_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Waiting_6" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_34* updates
    if image_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_34.frameNStart = frameN  # exact frame index
        image_34.tStart = t  # local t and not account for scr refresh
        image_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_34, 'tStartRefresh')  # time at next scr refresh
        image_34.setAutoDraw(True)
    if image_34.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_34.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_34.tStop = t  # not accounting for scr refresh
            image_34.frameNStop = frameN  # exact frame index
            image_34.setAutoDraw(False)
    
    # *polygon_23* updates
    if polygon_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_23.frameNStart = frameN  # exact frame index
        polygon_23.tStart = t  # local t and not account for scr refresh
        polygon_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_23, 'tStartRefresh')  # time at next scr refresh
        polygon_23.setAutoDraw(True)
    if polygon_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_23.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_23.tStop = t  # not accounting for scr refresh
            polygon_23.frameNStop = frameN  # exact frame index
            polygon_23.setAutoDraw(False)
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    if text_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_19.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_19.tStop = t  # not accounting for scr refresh
            text_19.frameNStop = frameN  # exact frame index
            text_19.setAutoDraw(False)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_15.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_15.tStop = t  # not accounting for scr refresh
            key_resp_15.frameNStop = frameN  # exact frame index
            key_resp_15.status = FINISHED
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=None, waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_35* updates
    if image_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_35.frameNStart = frameN  # exact frame index
        image_35.tStart = t  # local t and not account for scr refresh
        image_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_35, 'tStartRefresh')  # time at next scr refresh
        image_35.setAutoDraw(True)
    if image_35.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_35.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_35.tStop = t  # not accounting for scr refresh
            image_35.frameNStop = frameN  # exact frame index
            image_35.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Waiting_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Waiting_6" ---
for thisComponent in Waiting_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Result" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
party_pic.setImage('images/background_party.jpg')
winner_1.setImage(photos[most_least_index[0]])
winner_n1.setText(names[most_least_index[0]])
winner_n2.setText(names[most_least_index[2]])
winner_n3.setText(names[most_least_index[4]])
winner_n4.setText(names[most_least_index[6]])
winner_n5.setText(names[most_least_index[8]])
winner_n6.setText(ptp_name)
next_result.keys = []
next_result.rt = []
_next_result_allKeys = []
winner_2.setImage(photos[most_least_index[4]])
winner_3.setImage(photos[most_least_index[2]])
winner_4.setImage(photos[most_least_index[6]])
winner_5.setImage(photos[most_least_index[8]])
winner_6.setImage('images/subject.jpg')
# keep track of which components have finished
ResultComponents = [party_pic, border_25, border_26, winner_1, winner_n1, winner_n2, winner_n3, winner_n4, winner_n5, winner_n6, next_result1, next_result, border_27, winner_2, border_28, winner_3, border_29, winner_4, border_30, winner_5, border_31, winner_6, text_24]
for thisComponent in ResultComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Result" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *party_pic* updates
    if party_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        party_pic.frameNStart = frameN  # exact frame index
        party_pic.tStart = t  # local t and not account for scr refresh
        party_pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(party_pic, 'tStartRefresh')  # time at next scr refresh
        party_pic.setAutoDraw(True)
    
    # *border_25* updates
    if border_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_25.frameNStart = frameN  # exact frame index
        border_25.tStart = t  # local t and not account for scr refresh
        border_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_25, 'tStartRefresh')  # time at next scr refresh
        border_25.setAutoDraw(True)
    
    # *border_26* updates
    if border_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_26.frameNStart = frameN  # exact frame index
        border_26.tStart = t  # local t and not account for scr refresh
        border_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_26, 'tStartRefresh')  # time at next scr refresh
        border_26.setAutoDraw(True)
    
    # *winner_1* updates
    if winner_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_1.frameNStart = frameN  # exact frame index
        winner_1.tStart = t  # local t and not account for scr refresh
        winner_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_1, 'tStartRefresh')  # time at next scr refresh
        winner_1.setAutoDraw(True)
    
    # *winner_n1* updates
    if winner_n1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n1.frameNStart = frameN  # exact frame index
        winner_n1.tStart = t  # local t and not account for scr refresh
        winner_n1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n1, 'tStartRefresh')  # time at next scr refresh
        winner_n1.setAutoDraw(True)
    
    # *winner_n2* updates
    if winner_n2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n2.frameNStart = frameN  # exact frame index
        winner_n2.tStart = t  # local t and not account for scr refresh
        winner_n2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n2, 'tStartRefresh')  # time at next scr refresh
        winner_n2.setAutoDraw(True)
    
    # *winner_n3* updates
    if winner_n3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n3.frameNStart = frameN  # exact frame index
        winner_n3.tStart = t  # local t and not account for scr refresh
        winner_n3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n3, 'tStartRefresh')  # time at next scr refresh
        winner_n3.setAutoDraw(True)
    
    # *winner_n4* updates
    if winner_n4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n4.frameNStart = frameN  # exact frame index
        winner_n4.tStart = t  # local t and not account for scr refresh
        winner_n4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n4, 'tStartRefresh')  # time at next scr refresh
        winner_n4.setAutoDraw(True)
    
    # *winner_n5* updates
    if winner_n5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n5.frameNStart = frameN  # exact frame index
        winner_n5.tStart = t  # local t and not account for scr refresh
        winner_n5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n5, 'tStartRefresh')  # time at next scr refresh
        winner_n5.setAutoDraw(True)
    
    # *winner_n6* updates
    if winner_n6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_n6.frameNStart = frameN  # exact frame index
        winner_n6.tStart = t  # local t and not account for scr refresh
        winner_n6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_n6, 'tStartRefresh')  # time at next scr refresh
        winner_n6.setAutoDraw(True)
    
    # *next_result1* updates
    if next_result1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_result1.frameNStart = frameN  # exact frame index
        next_result1.tStart = t  # local t and not account for scr refresh
        next_result1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_result1, 'tStartRefresh')  # time at next scr refresh
        next_result1.setAutoDraw(True)
    
    # *next_result* updates
    waitOnFlip = False
    if next_result.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_result.frameNStart = frameN  # exact frame index
        next_result.tStart = t  # local t and not account for scr refresh
        next_result.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_result, 'tStartRefresh')  # time at next scr refresh
        next_result.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_result.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_result.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_result.status == STARTED and not waitOnFlip:
        theseKeys = next_result.getKeys(keyList=['space'], waitRelease=False)
        _next_result_allKeys.extend(theseKeys)
        if len(_next_result_allKeys):
            next_result.keys = _next_result_allKeys[-1].name  # just the last key pressed
            next_result.rt = _next_result_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *border_27* updates
    if border_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_27.frameNStart = frameN  # exact frame index
        border_27.tStart = t  # local t and not account for scr refresh
        border_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_27, 'tStartRefresh')  # time at next scr refresh
        border_27.setAutoDraw(True)
    
    # *winner_2* updates
    if winner_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_2.frameNStart = frameN  # exact frame index
        winner_2.tStart = t  # local t and not account for scr refresh
        winner_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_2, 'tStartRefresh')  # time at next scr refresh
        winner_2.setAutoDraw(True)
    
    # *border_28* updates
    if border_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_28.frameNStart = frameN  # exact frame index
        border_28.tStart = t  # local t and not account for scr refresh
        border_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_28, 'tStartRefresh')  # time at next scr refresh
        border_28.setAutoDraw(True)
    
    # *winner_3* updates
    if winner_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_3.frameNStart = frameN  # exact frame index
        winner_3.tStart = t  # local t and not account for scr refresh
        winner_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_3, 'tStartRefresh')  # time at next scr refresh
        winner_3.setAutoDraw(True)
    
    # *border_29* updates
    if border_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_29.frameNStart = frameN  # exact frame index
        border_29.tStart = t  # local t and not account for scr refresh
        border_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_29, 'tStartRefresh')  # time at next scr refresh
        border_29.setAutoDraw(True)
    
    # *winner_4* updates
    if winner_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_4.frameNStart = frameN  # exact frame index
        winner_4.tStart = t  # local t and not account for scr refresh
        winner_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_4, 'tStartRefresh')  # time at next scr refresh
        winner_4.setAutoDraw(True)
    
    # *border_30* updates
    if border_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_30.frameNStart = frameN  # exact frame index
        border_30.tStart = t  # local t and not account for scr refresh
        border_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_30, 'tStartRefresh')  # time at next scr refresh
        border_30.setAutoDraw(True)
    
    # *winner_5* updates
    if winner_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_5.frameNStart = frameN  # exact frame index
        winner_5.tStart = t  # local t and not account for scr refresh
        winner_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_5, 'tStartRefresh')  # time at next scr refresh
        winner_5.setAutoDraw(True)
    
    # *border_31* updates
    if border_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_31.frameNStart = frameN  # exact frame index
        border_31.tStart = t  # local t and not account for scr refresh
        border_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_31, 'tStartRefresh')  # time at next scr refresh
        border_31.setAutoDraw(True)
    
    # *winner_6* updates
    if winner_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        winner_6.frameNStart = frameN  # exact frame index
        winner_6.tStart = t  # local t and not account for scr refresh
        winner_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(winner_6, 'tStartRefresh')  # time at next scr refresh
        winner_6.setAutoDraw(True)
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ResultComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Result" ---
for thisComponent in ResultComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Result" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Chat" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
chat_q.setText('Lastly you get a chance to chat with each other! You will see what your friends are saying and you can add your own comments HERE:')
chat_enter.reset()
chat_enter.setText('')
# setup some python lists for storing info about the mouse5_5
mouse5_5.clicked_name = []
gotValidClick = False  # until a click is received
ptp_chat_enter = chat_enter.text  # Set routine start values for ptp_chat_enter
# keep track of which components have finished
ChatComponents = [chat_q, chat_enter, button5_5, submit5_5, mouse5_5]
for thisComponent in ChatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Chat" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *chat_q* updates
    if chat_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        chat_q.frameNStart = frameN  # exact frame index
        chat_q.tStart = t  # local t and not account for scr refresh
        chat_q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(chat_q, 'tStartRefresh')  # time at next scr refresh
        chat_q.setAutoDraw(True)
    
    # *chat_enter* updates
    if chat_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        chat_enter.frameNStart = frameN  # exact frame index
        chat_enter.tStart = t  # local t and not account for scr refresh
        chat_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(chat_enter, 'tStartRefresh')  # time at next scr refresh
        chat_enter.setAutoDraw(True)
    
    # *button5_5* updates
    if button5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button5_5.frameNStart = frameN  # exact frame index
        button5_5.tStart = t  # local t and not account for scr refresh
        button5_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5_5, 'tStartRefresh')  # time at next scr refresh
        button5_5.setAutoDraw(True)
    
    # *submit5_5* updates
    if submit5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submit5_5.frameNStart = frameN  # exact frame index
        submit5_5.tStart = t  # local t and not account for scr refresh
        submit5_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit5_5, 'tStartRefresh')  # time at next scr refresh
        submit5_5.setAutoDraw(True)
    # *mouse5_5* updates
    if mouse5_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5_5.frameNStart = frameN  # exact frame index
        mouse5_5.tStart = t  # local t and not account for scr refresh
        mouse5_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5_5, 'tStartRefresh')  # time at next scr refresh
        mouse5_5.status = STARTED
        mouse5_5.mouseClock.reset()
        prevButtonState = mouse5_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse5_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse5_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(button5_5)
                    clickableList = button5_5
                except:
                    clickableList = [button5_5]
                for obj in clickableList:
                    if obj.contains(mouse5_5):
                        gotValidClick = True
                        mouse5_5.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    ptp_chat_enter = chat_enter.text  # Set frame start values for ptp_chat_enter
    ptp_chat_enterContainer.append(ptp_chat_enter)  # Save frame values
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ChatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Chat" ---
for thisComponent in ChatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('chat_enter.text',chat_enter.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('ptp_chat_enter.routineEndVal', ptp_chat_enter)  # Save end routine value
# the Routine "Chat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "comment_final" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_8
text_26.alignText = 'Left'
text_26.bold = 'True'
# keep track of which components have finished
comment_finalComponents = [image_party2, border_33, text_26, see_chats]
for thisComponent in comment_finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "comment_final" ---
while continueRoutine and routineTimer.getTime() < 15.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_party2* updates
    if image_party2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_party2.frameNStart = frameN  # exact frame index
        image_party2.tStart = t  # local t and not account for scr refresh
        image_party2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_party2, 'tStartRefresh')  # time at next scr refresh
        image_party2.setAutoDraw(True)
    if image_party2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_party2.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            image_party2.tStop = t  # not accounting for scr refresh
            image_party2.frameNStop = frameN  # exact frame index
            image_party2.setAutoDraw(False)
    
    # *border_33* updates
    if border_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        border_33.frameNStart = frameN  # exact frame index
        border_33.tStart = t  # local t and not account for scr refresh
        border_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(border_33, 'tStartRefresh')  # time at next scr refresh
        border_33.setAutoDraw(True)
    if border_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > border_33.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            border_33.tStop = t  # not accounting for scr refresh
            border_33.frameNStop = frameN  # exact frame index
            border_33.setAutoDraw(False)
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    if text_26.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 30-frameTolerance:
            # keep track of stop time/frame for later
            text_26.tStop = t  # not accounting for scr refresh
            text_26.frameNStop = frameN  # exact frame index
            text_26.setAutoDraw(False)
    if text_26.status == STARTED:  # only update if drawing
        text_26.setPos([50, 5-frameN], log=False)
        text_26.setOri(0.0, log=False)
        text_26.setText(names[most_least_index[0]] + ': ' + 'Yay'+'\n' + names[most_least_index[2]] + ': ' + 'We did it, team!'+'\n' + names[most_least_index[4]] + ': ' + 'I want those nachos'+'\n' + names[most_least_index[6]] + ': ' + 'Is this for real???'+'\n' + names[most_least_index[8]] + ': ' + 'Yay'+'\n' + ptp_name + ': ' + ptp_chat_enter

, log=False)
        text_26.setFlip('None', log=False)
    
    # *see_chats* updates
    if see_chats.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        see_chats.frameNStart = frameN  # exact frame index
        see_chats.tStart = t  # local t and not account for scr refresh
        see_chats.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(see_chats, 'tStartRefresh')  # time at next scr refresh
        see_chats.setAutoDraw(True)
    if see_chats.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > see_chats.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            see_chats.tStop = t  # not accounting for scr refresh
            see_chats.frameNStop = frameN  # exact frame index
            see_chats.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in comment_finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "comment_final" ---
for thisComponent in comment_finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.000000)

# --- Prepare to start Routine "postq_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header1.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate.setText('Indicate the way you felt playing this game:\n')
interested_slider.reset()
distressed_slider.reset()
excited_slider.reset()
next_q1.keys = []
next_q1.rt = []
_next_q1_allKeys = []
# keep track of which components have finished
postq_1Components = [header1, indicate, instructions1, interested_slider, distressed_slider, excited_slider, interested, distressed, excited, next_q1]
for thisComponent in postq_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header1* updates
    if header1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header1.frameNStart = frameN  # exact frame index
        header1.tStart = t  # local t and not account for scr refresh
        header1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header1, 'tStartRefresh')  # time at next scr refresh
        header1.setAutoDraw(True)
    
    # *indicate* updates
    if indicate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate.frameNStart = frameN  # exact frame index
        indicate.tStart = t  # local t and not account for scr refresh
        indicate.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate, 'tStartRefresh')  # time at next scr refresh
        indicate.setAutoDraw(True)
    
    # *instructions1* updates
    if instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1.frameNStart = frameN  # exact frame index
        instructions1.tStart = t  # local t and not account for scr refresh
        instructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1, 'tStartRefresh')  # time at next scr refresh
        instructions1.setAutoDraw(True)
    
    # *interested_slider* updates
    if interested_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interested_slider.frameNStart = frameN  # exact frame index
        interested_slider.tStart = t  # local t and not account for scr refresh
        interested_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interested_slider, 'tStartRefresh')  # time at next scr refresh
        interested_slider.setAutoDraw(True)
    
    # *distressed_slider* updates
    if distressed_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        distressed_slider.frameNStart = frameN  # exact frame index
        distressed_slider.tStart = t  # local t and not account for scr refresh
        distressed_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(distressed_slider, 'tStartRefresh')  # time at next scr refresh
        distressed_slider.setAutoDraw(True)
    
    # *excited_slider* updates
    if excited_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        excited_slider.frameNStart = frameN  # exact frame index
        excited_slider.tStart = t  # local t and not account for scr refresh
        excited_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(excited_slider, 'tStartRefresh')  # time at next scr refresh
        excited_slider.setAutoDraw(True)
    
    # *interested* updates
    if interested.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interested.frameNStart = frameN  # exact frame index
        interested.tStart = t  # local t and not account for scr refresh
        interested.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interested, 'tStartRefresh')  # time at next scr refresh
        interested.setAutoDraw(True)
    
    # *distressed* updates
    if distressed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        distressed.frameNStart = frameN  # exact frame index
        distressed.tStart = t  # local t and not account for scr refresh
        distressed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(distressed, 'tStartRefresh')  # time at next scr refresh
        distressed.setAutoDraw(True)
    
    # *excited* updates
    if excited.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        excited.frameNStart = frameN  # exact frame index
        excited.tStart = t  # local t and not account for scr refresh
        excited.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(excited, 'tStartRefresh')  # time at next scr refresh
        excited.setAutoDraw(True)
    
    # *next_q1* updates
    waitOnFlip = False
    if next_q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q1.frameNStart = frameN  # exact frame index
        next_q1.tStart = t  # local t and not account for scr refresh
        next_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q1, 'tStartRefresh')  # time at next scr refresh
        next_q1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q1.status == STARTED and not waitOnFlip:
        theseKeys = next_q1.getKeys(keyList=['space'], waitRelease=False)
        _next_q1_allKeys.extend(theseKeys)
        if len(_next_q1_allKeys):
            next_q1.keys = _next_q1_allKeys[-1].name  # just the last key pressed
            next_q1.rt = _next_q1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_1" ---
for thisComponent in postq_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('interested_slider.response', interested_slider.getRating())
thisExp.addData('distressed_slider.response', distressed_slider.getRating())
thisExp.addData('excited_slider.response', excited_slider.getRating())
# the Routine "postq_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header2.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_2.setText('Indicate the way you felt playing this game:\n')
upset_slider.reset()
strong_slider.reset()
guilty_slider.reset()
next_q2.keys = []
next_q2.rt = []
_next_q2_allKeys = []
# keep track of which components have finished
postq_2Components = [header2, indicate_2, instructions2, upset_slider, strong_slider, guilty_slider, upset, strong, guilty, next_q2]
for thisComponent in postq_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header2* updates
    if header2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header2.frameNStart = frameN  # exact frame index
        header2.tStart = t  # local t and not account for scr refresh
        header2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header2, 'tStartRefresh')  # time at next scr refresh
        header2.setAutoDraw(True)
    
    # *indicate_2* updates
    if indicate_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_2.frameNStart = frameN  # exact frame index
        indicate_2.tStart = t  # local t and not account for scr refresh
        indicate_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_2, 'tStartRefresh')  # time at next scr refresh
        indicate_2.setAutoDraw(True)
    
    # *instructions2* updates
    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
        instructions2.setAutoDraw(True)
    
    # *upset_slider* updates
    if upset_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        upset_slider.frameNStart = frameN  # exact frame index
        upset_slider.tStart = t  # local t and not account for scr refresh
        upset_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(upset_slider, 'tStartRefresh')  # time at next scr refresh
        upset_slider.setAutoDraw(True)
    
    # *strong_slider* updates
    if strong_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        strong_slider.frameNStart = frameN  # exact frame index
        strong_slider.tStart = t  # local t and not account for scr refresh
        strong_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(strong_slider, 'tStartRefresh')  # time at next scr refresh
        strong_slider.setAutoDraw(True)
    
    # *guilty_slider* updates
    if guilty_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        guilty_slider.frameNStart = frameN  # exact frame index
        guilty_slider.tStart = t  # local t and not account for scr refresh
        guilty_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(guilty_slider, 'tStartRefresh')  # time at next scr refresh
        guilty_slider.setAutoDraw(True)
    
    # *upset* updates
    if upset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        upset.frameNStart = frameN  # exact frame index
        upset.tStart = t  # local t and not account for scr refresh
        upset.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(upset, 'tStartRefresh')  # time at next scr refresh
        upset.setAutoDraw(True)
    
    # *strong* updates
    if strong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        strong.frameNStart = frameN  # exact frame index
        strong.tStart = t  # local t and not account for scr refresh
        strong.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(strong, 'tStartRefresh')  # time at next scr refresh
        strong.setAutoDraw(True)
    
    # *guilty* updates
    if guilty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        guilty.frameNStart = frameN  # exact frame index
        guilty.tStart = t  # local t and not account for scr refresh
        guilty.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(guilty, 'tStartRefresh')  # time at next scr refresh
        guilty.setAutoDraw(True)
    
    # *next_q2* updates
    waitOnFlip = False
    if next_q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q2.frameNStart = frameN  # exact frame index
        next_q2.tStart = t  # local t and not account for scr refresh
        next_q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q2, 'tStartRefresh')  # time at next scr refresh
        next_q2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q2.status == STARTED and not waitOnFlip:
        theseKeys = next_q2.getKeys(keyList=['space'], waitRelease=False)
        _next_q2_allKeys.extend(theseKeys)
        if len(_next_q2_allKeys):
            next_q2.keys = _next_q2_allKeys[-1].name  # just the last key pressed
            next_q2.rt = _next_q2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_2" ---
for thisComponent in postq_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('upset_slider.response', upset_slider.getRating())
thisExp.addData('strong_slider.response', strong_slider.getRating())
thisExp.addData('guilty_slider.response', guilty_slider.getRating())
# the Routine "postq_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header3.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_3.setText('Indicate the way you felt playing this game:\n')
scared_slider_2.reset()
hostile_slider.reset()
enthu_slider_2.reset()
next_q3.keys = []
next_q3.rt = []
_next_q3_allKeys = []
# keep track of which components have finished
postq_3Components = [header3, indicate_3, instructions3, scared_slider_2, hostile_slider, enthu_slider_2, scared, hostile, enthusiastic, next_q3]
for thisComponent in postq_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header3* updates
    if header3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header3.frameNStart = frameN  # exact frame index
        header3.tStart = t  # local t and not account for scr refresh
        header3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header3, 'tStartRefresh')  # time at next scr refresh
        header3.setAutoDraw(True)
    
    # *indicate_3* updates
    if indicate_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_3.frameNStart = frameN  # exact frame index
        indicate_3.tStart = t  # local t and not account for scr refresh
        indicate_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_3, 'tStartRefresh')  # time at next scr refresh
        indicate_3.setAutoDraw(True)
    
    # *instructions3* updates
    if instructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3.frameNStart = frameN  # exact frame index
        instructions3.tStart = t  # local t and not account for scr refresh
        instructions3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3, 'tStartRefresh')  # time at next scr refresh
        instructions3.setAutoDraw(True)
    
    # *scared_slider_2* updates
    if scared_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scared_slider_2.frameNStart = frameN  # exact frame index
        scared_slider_2.tStart = t  # local t and not account for scr refresh
        scared_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scared_slider_2, 'tStartRefresh')  # time at next scr refresh
        scared_slider_2.setAutoDraw(True)
    
    # *hostile_slider* updates
    if hostile_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hostile_slider.frameNStart = frameN  # exact frame index
        hostile_slider.tStart = t  # local t and not account for scr refresh
        hostile_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hostile_slider, 'tStartRefresh')  # time at next scr refresh
        hostile_slider.setAutoDraw(True)
    
    # *enthu_slider_2* updates
    if enthu_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enthu_slider_2.frameNStart = frameN  # exact frame index
        enthu_slider_2.tStart = t  # local t and not account for scr refresh
        enthu_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enthu_slider_2, 'tStartRefresh')  # time at next scr refresh
        enthu_slider_2.setAutoDraw(True)
    
    # *scared* updates
    if scared.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scared.frameNStart = frameN  # exact frame index
        scared.tStart = t  # local t and not account for scr refresh
        scared.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scared, 'tStartRefresh')  # time at next scr refresh
        scared.setAutoDraw(True)
    
    # *hostile* updates
    if hostile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hostile.frameNStart = frameN  # exact frame index
        hostile.tStart = t  # local t and not account for scr refresh
        hostile.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hostile, 'tStartRefresh')  # time at next scr refresh
        hostile.setAutoDraw(True)
    
    # *enthusiastic* updates
    if enthusiastic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enthusiastic.frameNStart = frameN  # exact frame index
        enthusiastic.tStart = t  # local t and not account for scr refresh
        enthusiastic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enthusiastic, 'tStartRefresh')  # time at next scr refresh
        enthusiastic.setAutoDraw(True)
    
    # *next_q3* updates
    waitOnFlip = False
    if next_q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q3.frameNStart = frameN  # exact frame index
        next_q3.tStart = t  # local t and not account for scr refresh
        next_q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q3, 'tStartRefresh')  # time at next scr refresh
        next_q3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q3.status == STARTED and not waitOnFlip:
        theseKeys = next_q3.getKeys(keyList=['space'], waitRelease=False)
        _next_q3_allKeys.extend(theseKeys)
        if len(_next_q3_allKeys):
            next_q3.keys = _next_q3_allKeys[-1].name  # just the last key pressed
            next_q3.rt = _next_q3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_3" ---
for thisComponent in postq_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('scared_slider_2.response', scared_slider_2.getRating())
thisExp.addData('hostile_slider.response', hostile_slider.getRating())
thisExp.addData('enthu_slider_2.response', enthu_slider_2.getRating())
# the Routine "postq_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header4.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_4.setText('Indicate the way you felt playing this game:\n')
proud_slider.reset()
irritable_slider.reset()
alert_slider.reset()
next_q4.keys = []
next_q4.rt = []
_next_q4_allKeys = []
# keep track of which components have finished
postq_4Components = [header4, indicate_4, instructions4, proud_slider, irritable_slider, alert_slider, proud, irritable, alert, next_q4]
for thisComponent in postq_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header4* updates
    if header4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header4.frameNStart = frameN  # exact frame index
        header4.tStart = t  # local t and not account for scr refresh
        header4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header4, 'tStartRefresh')  # time at next scr refresh
        header4.setAutoDraw(True)
    
    # *indicate_4* updates
    if indicate_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_4.frameNStart = frameN  # exact frame index
        indicate_4.tStart = t  # local t and not account for scr refresh
        indicate_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_4, 'tStartRefresh')  # time at next scr refresh
        indicate_4.setAutoDraw(True)
    
    # *instructions4* updates
    if instructions4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions4.frameNStart = frameN  # exact frame index
        instructions4.tStart = t  # local t and not account for scr refresh
        instructions4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions4, 'tStartRefresh')  # time at next scr refresh
        instructions4.setAutoDraw(True)
    
    # *proud_slider* updates
    if proud_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proud_slider.frameNStart = frameN  # exact frame index
        proud_slider.tStart = t  # local t and not account for scr refresh
        proud_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proud_slider, 'tStartRefresh')  # time at next scr refresh
        proud_slider.setAutoDraw(True)
    
    # *irritable_slider* updates
    if irritable_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        irritable_slider.frameNStart = frameN  # exact frame index
        irritable_slider.tStart = t  # local t and not account for scr refresh
        irritable_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(irritable_slider, 'tStartRefresh')  # time at next scr refresh
        irritable_slider.setAutoDraw(True)
    
    # *alert_slider* updates
    if alert_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        alert_slider.frameNStart = frameN  # exact frame index
        alert_slider.tStart = t  # local t and not account for scr refresh
        alert_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alert_slider, 'tStartRefresh')  # time at next scr refresh
        alert_slider.setAutoDraw(True)
    
    # *proud* updates
    if proud.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proud.frameNStart = frameN  # exact frame index
        proud.tStart = t  # local t and not account for scr refresh
        proud.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proud, 'tStartRefresh')  # time at next scr refresh
        proud.setAutoDraw(True)
    
    # *irritable* updates
    if irritable.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        irritable.frameNStart = frameN  # exact frame index
        irritable.tStart = t  # local t and not account for scr refresh
        irritable.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(irritable, 'tStartRefresh')  # time at next scr refresh
        irritable.setAutoDraw(True)
    
    # *alert* updates
    if alert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        alert.frameNStart = frameN  # exact frame index
        alert.tStart = t  # local t and not account for scr refresh
        alert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alert, 'tStartRefresh')  # time at next scr refresh
        alert.setAutoDraw(True)
    
    # *next_q4* updates
    waitOnFlip = False
    if next_q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q4.frameNStart = frameN  # exact frame index
        next_q4.tStart = t  # local t and not account for scr refresh
        next_q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'next_q4.started')
        next_q4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q4.status == STARTED and not waitOnFlip:
        theseKeys = next_q4.getKeys(keyList=['space'], waitRelease=False)
        _next_q4_allKeys.extend(theseKeys)
        if len(_next_q4_allKeys):
            next_q4.keys = _next_q4_allKeys[-1].name  # just the last key pressed
            next_q4.rt = _next_q4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_4" ---
for thisComponent in postq_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('proud_slider.response', proud_slider.getRating())
thisExp.addData('irritable_slider.response', irritable_slider.getRating())
thisExp.addData('alert_slider.response', alert_slider.getRating())
# the Routine "postq_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header5.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate5.setText('Indicate the way you felt playing this game:\n')
ashamed_slider.reset()
inspired_slider.reset()
nervous_slider.reset()
next_q5.keys = []
next_q5.rt = []
_next_q5_allKeys = []
# keep track of which components have finished
postq_5Components = [header5, indicate5, instructions5, ashamed_slider, inspired_slider, nervous_slider, ashamed, inspired, nervous, next_q5]
for thisComponent in postq_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header5* updates
    if header5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header5.frameNStart = frameN  # exact frame index
        header5.tStart = t  # local t and not account for scr refresh
        header5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header5, 'tStartRefresh')  # time at next scr refresh
        header5.setAutoDraw(True)
    
    # *indicate5* updates
    if indicate5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate5.frameNStart = frameN  # exact frame index
        indicate5.tStart = t  # local t and not account for scr refresh
        indicate5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate5, 'tStartRefresh')  # time at next scr refresh
        indicate5.setAutoDraw(True)
    
    # *instructions5* updates
    if instructions5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions5.frameNStart = frameN  # exact frame index
        instructions5.tStart = t  # local t and not account for scr refresh
        instructions5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions5, 'tStartRefresh')  # time at next scr refresh
        instructions5.setAutoDraw(True)
    
    # *ashamed_slider* updates
    if ashamed_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ashamed_slider.frameNStart = frameN  # exact frame index
        ashamed_slider.tStart = t  # local t and not account for scr refresh
        ashamed_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ashamed_slider, 'tStartRefresh')  # time at next scr refresh
        ashamed_slider.setAutoDraw(True)
    
    # *inspired_slider* updates
    if inspired_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inspired_slider.frameNStart = frameN  # exact frame index
        inspired_slider.tStart = t  # local t and not account for scr refresh
        inspired_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inspired_slider, 'tStartRefresh')  # time at next scr refresh
        inspired_slider.setAutoDraw(True)
    
    # *nervous_slider* updates
    if nervous_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nervous_slider.frameNStart = frameN  # exact frame index
        nervous_slider.tStart = t  # local t and not account for scr refresh
        nervous_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nervous_slider, 'tStartRefresh')  # time at next scr refresh
        nervous_slider.setAutoDraw(True)
    
    # *ashamed* updates
    if ashamed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ashamed.frameNStart = frameN  # exact frame index
        ashamed.tStart = t  # local t and not account for scr refresh
        ashamed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ashamed, 'tStartRefresh')  # time at next scr refresh
        ashamed.setAutoDraw(True)
    
    # *inspired* updates
    if inspired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inspired.frameNStart = frameN  # exact frame index
        inspired.tStart = t  # local t and not account for scr refresh
        inspired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inspired, 'tStartRefresh')  # time at next scr refresh
        inspired.setAutoDraw(True)
    
    # *nervous* updates
    if nervous.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nervous.frameNStart = frameN  # exact frame index
        nervous.tStart = t  # local t and not account for scr refresh
        nervous.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nervous, 'tStartRefresh')  # time at next scr refresh
        nervous.setAutoDraw(True)
    
    # *next_q5* updates
    waitOnFlip = False
    if next_q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q5.frameNStart = frameN  # exact frame index
        next_q5.tStart = t  # local t and not account for scr refresh
        next_q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q5, 'tStartRefresh')  # time at next scr refresh
        next_q5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q5.status == STARTED and not waitOnFlip:
        theseKeys = next_q5.getKeys(keyList=['space'], waitRelease=False)
        _next_q5_allKeys.extend(theseKeys)
        if len(_next_q5_allKeys):
            next_q5.keys = _next_q5_allKeys[-1].name  # just the last key pressed
            next_q5.rt = _next_q5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_5" ---
for thisComponent in postq_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ashamed_slider.response', ashamed_slider.getRating())
thisExp.addData('inspired_slider.response', inspired_slider.getRating())
thisExp.addData('nervous_slider.response', nervous_slider.getRating())
# the Routine "postq_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header6.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_6.setText('Indicate the way you felt playing this game:\n')
determined_slider.reset()
attentive_slider.reset()
jittery_slider.reset()
next_q6.keys = []
next_q6.rt = []
_next_q6_allKeys = []
# keep track of which components have finished
postq_6Components = [header6, indicate_6, instructions6, determined_slider, attentive_slider, jittery_slider, determined, attentive, jittery, next_q6]
for thisComponent in postq_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header6* updates
    if header6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header6.frameNStart = frameN  # exact frame index
        header6.tStart = t  # local t and not account for scr refresh
        header6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header6, 'tStartRefresh')  # time at next scr refresh
        header6.setAutoDraw(True)
    
    # *indicate_6* updates
    if indicate_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_6.frameNStart = frameN  # exact frame index
        indicate_6.tStart = t  # local t and not account for scr refresh
        indicate_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_6, 'tStartRefresh')  # time at next scr refresh
        indicate_6.setAutoDraw(True)
    
    # *instructions6* updates
    if instructions6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions6.frameNStart = frameN  # exact frame index
        instructions6.tStart = t  # local t and not account for scr refresh
        instructions6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions6, 'tStartRefresh')  # time at next scr refresh
        instructions6.setAutoDraw(True)
    
    # *determined_slider* updates
    if determined_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        determined_slider.frameNStart = frameN  # exact frame index
        determined_slider.tStart = t  # local t and not account for scr refresh
        determined_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(determined_slider, 'tStartRefresh')  # time at next scr refresh
        determined_slider.setAutoDraw(True)
    
    # *attentive_slider* updates
    if attentive_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        attentive_slider.frameNStart = frameN  # exact frame index
        attentive_slider.tStart = t  # local t and not account for scr refresh
        attentive_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(attentive_slider, 'tStartRefresh')  # time at next scr refresh
        attentive_slider.setAutoDraw(True)
    
    # *jittery_slider* updates
    if jittery_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jittery_slider.frameNStart = frameN  # exact frame index
        jittery_slider.tStart = t  # local t and not account for scr refresh
        jittery_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jittery_slider, 'tStartRefresh')  # time at next scr refresh
        jittery_slider.setAutoDraw(True)
    
    # *determined* updates
    if determined.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        determined.frameNStart = frameN  # exact frame index
        determined.tStart = t  # local t and not account for scr refresh
        determined.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(determined, 'tStartRefresh')  # time at next scr refresh
        determined.setAutoDraw(True)
    
    # *attentive* updates
    if attentive.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        attentive.frameNStart = frameN  # exact frame index
        attentive.tStart = t  # local t and not account for scr refresh
        attentive.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(attentive, 'tStartRefresh')  # time at next scr refresh
        attentive.setAutoDraw(True)
    
    # *jittery* updates
    if jittery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        jittery.frameNStart = frameN  # exact frame index
        jittery.tStart = t  # local t and not account for scr refresh
        jittery.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(jittery, 'tStartRefresh')  # time at next scr refresh
        jittery.setAutoDraw(True)
    
    # *next_q6* updates
    waitOnFlip = False
    if next_q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q6.frameNStart = frameN  # exact frame index
        next_q6.tStart = t  # local t and not account for scr refresh
        next_q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q6, 'tStartRefresh')  # time at next scr refresh
        next_q6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q6.status == STARTED and not waitOnFlip:
        theseKeys = next_q6.getKeys(keyList=['space'], waitRelease=False)
        _next_q6_allKeys.extend(theseKeys)
        if len(_next_q6_allKeys):
            next_q6.keys = _next_q6_allKeys[-1].name  # just the last key pressed
            next_q6.rt = _next_q6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_6" ---
for thisComponent in postq_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('determined_slider.response', determined_slider.getRating())
thisExp.addData('attentive_slider.response', attentive_slider.getRating())
thisExp.addData('jittery_slider.response', jittery_slider.getRating())
# the Routine "postq_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header7.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_7.setText('Indicate the way you felt playing this game:\n')
active_slider.reset()
afraid_slider.reset()
next_q7.keys = []
next_q7.rt = []
_next_q7_allKeys = []
# keep track of which components have finished
postq_7Components = [header7, indicate_7, instructions7, active_slider, afraid_slider, active, afraid, next_q7]
for thisComponent in postq_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header7* updates
    if header7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header7.frameNStart = frameN  # exact frame index
        header7.tStart = t  # local t and not account for scr refresh
        header7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'header7.started')
        header7.setAutoDraw(True)
    
    # *indicate_7* updates
    if indicate_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_7.frameNStart = frameN  # exact frame index
        indicate_7.tStart = t  # local t and not account for scr refresh
        indicate_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'indicate_7.started')
        indicate_7.setAutoDraw(True)
    
    # *instructions7* updates
    if instructions7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions7.frameNStart = frameN  # exact frame index
        instructions7.tStart = t  # local t and not account for scr refresh
        instructions7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions7.started')
        instructions7.setAutoDraw(True)
    
    # *active_slider* updates
    if active_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        active_slider.frameNStart = frameN  # exact frame index
        active_slider.tStart = t  # local t and not account for scr refresh
        active_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(active_slider, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'active_slider.started')
        active_slider.setAutoDraw(True)
    
    # *afraid_slider* updates
    if afraid_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        afraid_slider.frameNStart = frameN  # exact frame index
        afraid_slider.tStart = t  # local t and not account for scr refresh
        afraid_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(afraid_slider, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'afraid_slider.started')
        afraid_slider.setAutoDraw(True)
    
    # *active* updates
    if active.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        active.frameNStart = frameN  # exact frame index
        active.tStart = t  # local t and not account for scr refresh
        active.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(active, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'active.started')
        active.setAutoDraw(True)
    
    # *afraid* updates
    if afraid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        afraid.frameNStart = frameN  # exact frame index
        afraid.tStart = t  # local t and not account for scr refresh
        afraid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(afraid, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'afraid.started')
        afraid.setAutoDraw(True)
    
    # *next_q7* updates
    waitOnFlip = False
    if next_q7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_q7.frameNStart = frameN  # exact frame index
        next_q7.tStart = t  # local t and not account for scr refresh
        next_q7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_q7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'next_q7.started')
        next_q7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_q7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_q7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_q7.status == STARTED and not waitOnFlip:
        theseKeys = next_q7.getKeys(keyList=['space'], waitRelease=False)
        _next_q7_allKeys.extend(theseKeys)
        if len(_next_q7_allKeys):
            next_q7.keys = _next_q7_allKeys[-1].name  # just the last key pressed
            next_q7.rt = _next_q7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_7" ---
for thisComponent in postq_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('active_slider.response', active_slider.getRating())
thisExp.addData('active_slider.rt', active_slider.getRT())
thisExp.addData('afraid_slider.response', afraid_slider.getRating())
thisExp.addData('afraid_slider.rt', afraid_slider.getRT())
# check responses
if next_q7.keys in ['', [], None]:  # No response was made
    next_q7.keys = None
thisExp.addData('next_q7.keys',next_q7.keys)
if next_q7.keys != None:  # we had a response
    thisExp.addData('next_q7.rt', next_q7.rt)
thisExp.nextEntry()
# the Routine "postq_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_8" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header8.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_8.setText('Indicate the way you felt playing this game:\n')
believe_slider_1.reset()
believe_slider_2.reset()
next_8.keys = []
next_8.rt = []
_next_8_allKeys = []
# keep track of which components have finished
postq_8Components = [header8, indicate_8, instructions8, believe_slider_1, believe_slider_2, believe_1, believe_2, next_8]
for thisComponent in postq_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_8" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header8* updates
    if header8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header8.frameNStart = frameN  # exact frame index
        header8.tStart = t  # local t and not account for scr refresh
        header8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header8, 'tStartRefresh')  # time at next scr refresh
        header8.setAutoDraw(True)
    
    # *indicate_8* updates
    if indicate_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_8.frameNStart = frameN  # exact frame index
        indicate_8.tStart = t  # local t and not account for scr refresh
        indicate_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_8, 'tStartRefresh')  # time at next scr refresh
        indicate_8.setAutoDraw(True)
    
    # *instructions8* updates
    if instructions8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions8.frameNStart = frameN  # exact frame index
        instructions8.tStart = t  # local t and not account for scr refresh
        instructions8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions8, 'tStartRefresh')  # time at next scr refresh
        instructions8.setAutoDraw(True)
    
    # *believe_slider_1* updates
    if believe_slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        believe_slider_1.frameNStart = frameN  # exact frame index
        believe_slider_1.tStart = t  # local t and not account for scr refresh
        believe_slider_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(believe_slider_1, 'tStartRefresh')  # time at next scr refresh
        believe_slider_1.setAutoDraw(True)
    
    # *believe_slider_2* updates
    if believe_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        believe_slider_2.frameNStart = frameN  # exact frame index
        believe_slider_2.tStart = t  # local t and not account for scr refresh
        believe_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(believe_slider_2, 'tStartRefresh')  # time at next scr refresh
        believe_slider_2.setAutoDraw(True)
    
    # *believe_1* updates
    if believe_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        believe_1.frameNStart = frameN  # exact frame index
        believe_1.tStart = t  # local t and not account for scr refresh
        believe_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(believe_1, 'tStartRefresh')  # time at next scr refresh
        believe_1.setAutoDraw(True)
    
    # *believe_2* updates
    if believe_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        believe_2.frameNStart = frameN  # exact frame index
        believe_2.tStart = t  # local t and not account for scr refresh
        believe_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(believe_2, 'tStartRefresh')  # time at next scr refresh
        believe_2.setAutoDraw(True)
    
    # *next_8* updates
    waitOnFlip = False
    if next_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_8.frameNStart = frameN  # exact frame index
        next_8.tStart = t  # local t and not account for scr refresh
        next_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_8, 'tStartRefresh')  # time at next scr refresh
        next_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_8.status == STARTED and not waitOnFlip:
        theseKeys = next_8.getKeys(keyList=['space'], waitRelease=False)
        _next_8_allKeys.extend(theseKeys)
        if len(_next_8_allKeys):
            next_8.keys = _next_8_allKeys[-1].name  # just the last key pressed
            next_8.rt = _next_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_8" ---
for thisComponent in postq_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('believe_slider_1.response', believe_slider_1.getRating())
thisExp.addData('believe_slider_2.response', believe_slider_2.getRating())
# the Routine "postq_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postq_9" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
header9.setText('Please answer the following questions about your experiences during the virtual party game. ')
indicate_9.setText('Indicate the way you felt playing this game:\n')
bother_slider.reset()
happy_slider_3.reset()
next_9.keys = []
next_9.rt = []
_next_9_allKeys = []
# keep track of which components have finished
postq_9Components = [header9, indicate_9, instructions9, bother_slider, happy_slider_3, bother, happy, next_9]
for thisComponent in postq_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postq_9" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *header9* updates
    if header9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        header9.frameNStart = frameN  # exact frame index
        header9.tStart = t  # local t and not account for scr refresh
        header9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(header9, 'tStartRefresh')  # time at next scr refresh
        header9.setAutoDraw(True)
    
    # *indicate_9* updates
    if indicate_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        indicate_9.frameNStart = frameN  # exact frame index
        indicate_9.tStart = t  # local t and not account for scr refresh
        indicate_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(indicate_9, 'tStartRefresh')  # time at next scr refresh
        indicate_9.setAutoDraw(True)
    
    # *instructions9* updates
    if instructions9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions9.frameNStart = frameN  # exact frame index
        instructions9.tStart = t  # local t and not account for scr refresh
        instructions9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions9, 'tStartRefresh')  # time at next scr refresh
        instructions9.setAutoDraw(True)
    
    # *bother_slider* updates
    if bother_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bother_slider.frameNStart = frameN  # exact frame index
        bother_slider.tStart = t  # local t and not account for scr refresh
        bother_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bother_slider, 'tStartRefresh')  # time at next scr refresh
        bother_slider.setAutoDraw(True)
    
    # *happy_slider_3* updates
    if happy_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        happy_slider_3.frameNStart = frameN  # exact frame index
        happy_slider_3.tStart = t  # local t and not account for scr refresh
        happy_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(happy_slider_3, 'tStartRefresh')  # time at next scr refresh
        happy_slider_3.setAutoDraw(True)
    
    # *bother* updates
    if bother.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bother.frameNStart = frameN  # exact frame index
        bother.tStart = t  # local t and not account for scr refresh
        bother.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bother, 'tStartRefresh')  # time at next scr refresh
        bother.setAutoDraw(True)
    
    # *happy* updates
    if happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        happy.frameNStart = frameN  # exact frame index
        happy.tStart = t  # local t and not account for scr refresh
        happy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(happy, 'tStartRefresh')  # time at next scr refresh
        happy.setAutoDraw(True)
    
    # *next_9* updates
    waitOnFlip = False
    if next_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_9.frameNStart = frameN  # exact frame index
        next_9.tStart = t  # local t and not account for scr refresh
        next_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_9, 'tStartRefresh')  # time at next scr refresh
        next_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_9.status == STARTED and not waitOnFlip:
        theseKeys = next_9.getKeys(keyList=['space'], waitRelease=False)
        _next_9_allKeys.extend(theseKeys)
        if len(_next_9_allKeys):
            next_9.keys = _next_9_allKeys[-1].name  # just the last key pressed
            next_9.rt = _next_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postq_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postq_9" ---
for thisComponent in postq_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('bother_slider.response', bother_slider.getRating())
thisExp.addData('happy_slider_3.response', happy_slider_3.getRating())
# the Routine "postq_9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "done" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [done_text]
for thisComponent in doneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "done" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done_text* updates
    if done_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_text.frameNStart = frameN  # exact frame index
        done_text.tStart = t  # local t and not account for scr refresh
        done_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'done_text.started')
        done_text.setAutoDraw(True)
    if done_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            done_text.tStop = t  # not accounting for scr refresh
            done_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'done_text.stopped')
            done_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "done" ---
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
