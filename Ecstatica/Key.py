# coding: utf-8

#Created on 18.01.2012

#Copyright (C) 2013 Fabian Hachenberg
#This file is part of EcstaticaLib. 
#EcstaticaLib is free software: you can redistribute it and/or modify 
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation, either version 3 of the License, or 
#(at your option) any later version. 
#More information about the license is provided in the LICENSE file.

from . import Event

class Key(object):
    def __init__(self, action):
        self.action = action
        
        self.events = []
        
    def addEvent(self, event):
        assert event != None
        
        self.events.append(event)
        sort(self.events, key= lambda a: -Event.EventPriority[a.event_type])
