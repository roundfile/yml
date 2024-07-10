import prettytable
import re
try:
  from PyQt5.QtWidgets import QApplication
except Exception:
  from PyQt6.QtWidgets import QApplication

def content():
    strlist = []
    helpstr = ''  #@UnusedVariable
    newline = '\n'  #@UnusedVariable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append("<b>")
    strlist.append(QApplication.translate('HelpDlg','ALARMS',None))
    strlist.append("</b>")
    tbl_Alarmstop = prettytable.PrettyTable()
    tbl_Alarmstop.header = False
    tbl_Alarmstop.add_row([QApplication.translate('HelpDlg','Each alarm is only triggered once.\nAlarms are scanned in order from the top of the table to the bottom.',None)])
    strlist.append(tbl_Alarmstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Alarms = prettytable.PrettyTable()
    tbl_Alarms.field_names = [QApplication.translate('HelpDlg','Field',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Nr',None),QApplication.translate('HelpDlg','Alarm number for reference.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Status',None),QApplication.translate('HelpDlg','Activate or Deactivate the alarm.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','If Alarm',None),QApplication.translate('HelpDlg','Alarm triggered only if the alarm with the given number was triggered before. Use 0 for no guard.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','But Not',None),QApplication.translate('HelpDlg','Alarm triggered only if the alarm with the given number was not triggered before. Use 0 for no guard.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','From',None),QApplication.translate('HelpDlg','Alarm only triggered after the given event.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Time',None),QApplication.translate('HelpDlg','If not 00:00, alarm is triggered mm:ss after the event "From" happens.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Source',None),QApplication.translate('HelpDlg','The observed temperature source.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Condition',None),QApplication.translate('HelpDlg','Alarm is triggered if source rises above or below the specified temperature.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Temp',None),QApplication.translate('HelpDlg','The specified temperature limit.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Action',None),QApplication.translate('HelpDlg','The action to be triggered if all conditions are fulfilled.',None)])
    tbl_Alarms.add_row([QApplication.translate('HelpDlg','Description',None),QApplication.translate('HelpDlg','Commands for alarms with an action go here.  Anything after a &#39;#&#39; character is considerd a comment and is ignored when processing the alarm.  ',None)])
    strlist.append(tbl_Alarms.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','ALARM CONFIGURATION OPTIONS',None))
    strlist.append("</b>")
    tbl_Options = prettytable.PrettyTable()
    tbl_Options.field_names = [QApplication.translate('HelpDlg','Option',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Options.add_row([QApplication.translate('HelpDlg','Add',None),QApplication.translate('HelpDlg','Adds a new alarm to the bottom of the table.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Insert',None),QApplication.translate('HelpDlg','Inserts a new alarm above the selected alarm.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Delete',None),QApplication.translate('HelpDlg','Deletes the selected alarm.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Copy Table',None),QApplication.translate('HelpDlg','Copy the alarm table in tab separated format to the clipboard.  Option or ALT click to copy a tabular format to the clipboard.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','All On',None),QApplication.translate('HelpDlg','Enables all alarms.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','All Off',None),QApplication.translate('HelpDlg','Disables all alarms.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Load',None),QApplication.translate('HelpDlg','Load alarm definition from a file.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Save',None),QApplication.translate('HelpDlg','Save the alarm definitions to a file.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Clear',None),QApplication.translate('HelpDlg','Clears all alarms from the table.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Help',None),QApplication.translate('HelpDlg','Opens this window.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Load from Profile',None),QApplication.translate('HelpDlg','when ticked will replace the alarm table when loading a profile with the alarms stored in the profile.  If there are no alarms in the profile the alarm table will be cleared.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Load from Background',None),QApplication.translate('HelpDlg','when ticked will replace the alarm table when loading a background profile with the alarms stored in the profile.  If there are no alarms in the profile the alarm table will be cleared.',None)])
    tbl_Options.add_row([QApplication.translate('HelpDlg','PopUp TimeOut',None),QApplication.translate('HelpDlg','A PopUp will automatically close after this time if the OK button has not been clicked.',None)])
    strlist.append(tbl_Options.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','Alarm Actions',None))
    strlist.append("</b>")
    tbl_Actionstop = prettytable.PrettyTable()
    tbl_Actionstop.header = False
    tbl_Actionstop.add_row([QApplication.translate('HelpDlg','Enter the Command into the Description field of the Alarm.',None)])
    strlist.append(tbl_Actionstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Actions = prettytable.PrettyTable()
    tbl_Actions.field_names = [QApplication.translate('HelpDlg','Action',None),QApplication.translate('HelpDlg','Command',None),QApplication.translate('HelpDlg','Meaning',None)]
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Pop Up',None),QApplication.translate('HelpDlg','<text>',None),QApplication.translate('HelpDlg','the text to  be displayed in the pop up',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Call Program',None),QApplication.translate('HelpDlg','A program/script path (absolute or relative)',None),QApplication.translate('HelpDlg','start an external program',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Event Button',None),QApplication.translate('HelpDlg','<button number>',None),QApplication.translate('HelpDlg','triggers the button, the button number comes from the Events Buttons configuration',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Slider <1>',None),QApplication.translate('HelpDlg','<value>',None),QApplication.translate('HelpDlg','set the slider for special event nr. 1 to the value',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Slider <2>',None),QApplication.translate('HelpDlg','<value>',None),QApplication.translate('HelpDlg','set the slider for special event nr. 2 to the value',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Slider <3>',None),QApplication.translate('HelpDlg','<value>',None),QApplication.translate('HelpDlg','set the slider for special event nr. 3 to the value',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Slider <4>',None),QApplication.translate('HelpDlg','<value>',None),QApplication.translate('HelpDlg','set the slider for special event nr. 4 to the value',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','START',None),'&#160;',QApplication.translate('HelpDlg','trigger START',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','DRY',None),'&#160;',QApplication.translate('HelpDlg','trigger the DRY event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','FCs',None),'&#160;',QApplication.translate('HelpDlg','trigger the FCs event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','FCe',None),'&#160;',QApplication.translate('HelpDlg','trigger the FCe event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','SCs',None),'&#160;',QApplication.translate('HelpDlg','trigger the SCs event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','SCe',None),'&#160;',QApplication.translate('HelpDlg','trigger the SCe event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','DROP',None),'&#160;',QApplication.translate('HelpDlg','trigger the DROP event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','COOL END',None),'&#160;',QApplication.translate('HelpDlg','trigger the COOL END event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','OFF',None),'&#160;',QApplication.translate('HelpDlg','trigger OFF',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','CHARGE',None),'&#160;',QApplication.translate('HelpDlg','trigger the CHARGE event',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','RampSoak ON',None),'&#160;',QApplication.translate('HelpDlg','turns PID on and switches to RampSoak mode',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','RampSoak OFF',None),'&#160;',QApplication.translate('HelpDlg','turns PID off and switches to manual mode',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Set Canvas Color',None),QApplication.translate('HelpDlg','<color>',None),QApplication.translate('HelpDlg','sets the canvas to <color>, can be in hex format, e.g. "#ffaa55" or a color name, e.g. "blue"',None)])
    tbl_Actions.add_row([QApplication.translate('HelpDlg','Reset Canvas Color',None),'&#160;',QApplication.translate('HelpDlg','reset the canvas color to the color specified in Config>>Colors\ncanvas color resets automatically at OFF',None)])
    strlist.append(tbl_Actions.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("</body>")
    helpstr = "".join(strlist)
    helpstr = re.sub(r"&amp;", r"&",helpstr)
    return helpstr