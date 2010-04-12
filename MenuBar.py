import objc
from Foundation import *
from AppKit import *
from sys import *

# the NSStatusItem we'll create
statusItem = 0

inactiveIcon = 0
activeIcon = 0
isActive = 0

myApp = 0

# called on load and reload
def load( scriptFilePath ):
    global statusItem, inactiveIcon, activeIcon, myApp

    myApp = NSApplication.sharedApplication()

    # create a new NSStatusItem
    thickness = NSStatusBar.systemStatusBar().thickness()
    statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(thickness)
    statusItem.setToolTip_("Colloquy Status")
    statusItem.setHighlightMode_(1)

    bundle = NSBundle.mainBundle()
    
    path = bundle.pathForImageResource_("roomTabNewHighlightMessage.png")
    activeIcon = NSImage.alloc().initWithContentsOfFile_(path)

    path = bundle.pathForImageResource_("roomTab.png")
    inactiveIcon = NSImage.alloc().initWithContentsOfFile_(path)

    statusItem.setImage_(inactiveIcon)


# called on unload and relead
def unload():
    global statusItem
    if statusItem != 0:
        statusItem.statusBar().removeStatusItem_(statusItem)

# return an array of NSMenuItems that should be dispalyed for 'item' associated with 'view'
def contextualMenuItems( item, view ):
    global inactiveIcon, myApp

    if inactiveIcon != 0 and myApp.isActive():
        statusItem.setImage_(inactiveIcon)

# return an array of toolbar item identifier strings that can be associated with 'view'
def toolbarItemIdentifiers( view ):
    pass

# return an NSToolbarItem for 'identifier' associated with 'view'
def toolbarItem( identifier, view, willBeInserted ):
    pass

# perform the action associated with 'toolbarItem' for 'view'
def handleClickedToolbarItem( toolbarItem, view ):
    pass

# process the command and return true if you handle it or False to pass on to another plugin
def processUserCommand( command, arguments, connection, view ):
    # return true if the command was handled or to prevent other plugins or Colloquy from handling it
    return False

# handle a ctcp request and return true if you handle it or False to pass on to another plugin
def processSubcodeRequest( command, arguments, user ):
    # return true if the command was handled or to prevent other plugins or Colloquy from handling it
    return False

# handle a ctcp reply and return true if you handle it or False to pass on to another plugin
def processSubcodeReply( command, arguments, user ):
    # return true if the command was handled or to prevent other plugins or Colloquy from handling it
    return False

# called when 'connection' connects
def connected( connection ):
    pass

# called when 'connection' is disconnecting
def disconnecting( connection ):
    pass

# perform a notification
def performNotification( identifier, context, preferences ):
    global activeIcon
    
    active_on = (
        'JVChatAdditionalMessages', # Additional Private Messages
        'JVChatFirstMessage', # First Private Message
        'JVChatMentioned', # Highlight word was mentioned
    )
    
    if identifier in active_on and activeIcon != 0:
        statusItem.setImage_(activeIcon)

# called when an unhandled URL scheme is clicked in 'view'
def handleClickedLink( url, view ):
    # return true if the link was handled or to prevent other plugins or Colloquy from handling it
    return False

# called for each incoming message, the message is mutable
def processIncomingMessage( message, view ):
    pass

# called for each outgoing message, the message is mutable
def processOutgoingMessage( message, view ):
    pass

# called when a member joins 'room'
def memberJoined( member, room ):
    pass

# called when a member parts 'room'
def memberParted( member, room, reason ):
    pass

# called when a member is kicked from 'room' for 'reason'
def memberKicked( member, room, by, reason ):
    pass

# called when the local user joins 'room'
def joinedRoom( room ):
    pass

# called when the local user is parting 'room'
def partingFromRoom( room ):
    pass

# called when the local user is kicked from 'room' for 'reason'
def kickedFromRoom( room, by, reason ):
    pass

# called when the topic changes in 'room' by 'user'
def topicChanged( topic, room, user ):
    pass

