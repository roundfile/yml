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
    strlist.append(QApplication.translate('HelpDlg','AUTOSAVE DIALOG'))
    strlist.append("</b>")
    tbl_Autosave = prettytable.PrettyTable()
    tbl_Autosave.field_names = [QApplication.translate('HelpDlg','Dialog Field'),QApplication.translate('HelpDlg','Meaning')]
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Autosave [a]'),QApplication.translate('HelpDlg','Turn Autosave ON or OFF.  When sampling, the keyboard &#39;a&#39; will save the profile at that moment.\nNOTE: Files with the same file name will be silently overwritten.  Use ~currdatetime in the file name prefix to get unique file names.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Add to recent file list'),QApplication.translate('HelpDlg','When checked, Autosaved files will be added to the Files>> Open Recent files list.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','File Name Prefix'),QApplication.translate('HelpDlg','Defines the file name to use for Autosave.  See the Autosave Fields section below.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Preview:'),QApplication.translate('HelpDlg','Shows an example of the file name based on the File Name Prefix field.\nA &#39;While Recording:&#39; example will also be shown if the file name will be different when the scope is sampling.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Path'),QApplication.translate('HelpDlg','Where to store the Autosaved files.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Save Also'),QApplication.translate('HelpDlg','Allows to save an additional file.  Choose the file type from the pull-down menu.')])
    tbl_Autosave.add_row([QApplication.translate('HelpDlg','Path'),QApplication.translate('HelpDlg','Where to store the additional files.')])
    strlist.append(tbl_Autosave.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','AUTOSAVE FIELDS'))
    strlist.append("</b>")
    tbl_AutosaveFields = prettytable.PrettyTable()
    tbl_AutosaveFields.field_names = [QApplication.translate('HelpDlg','Prefix Field'),QApplication.translate('HelpDlg','Source'),QApplication.translate('HelpDlg','Example')]
    tbl_AutosaveFields.add_row(['~batchprefix',QApplication.translate('HelpDlg','The batch prefix set in Config>Batch>Prefix'),'Prod-'])
    tbl_AutosaveFields.add_row(['~batchcounter',QApplication.translate('HelpDlg','The current batch number'),653])
    tbl_AutosaveFields.add_row(['~batch',QApplication.translate('HelpDlg','Same as "~batchprefix~batchnum"'),'Prod-653'])
    tbl_AutosaveFields.add_row(['~batchposition',QApplication.translate('HelpDlg','The current batch position, or "Roast of the Day"'),9])
    tbl_AutosaveFields.add_row(['~batch_long',QApplication.translate('HelpDlg','Same as Batch field in Roast Properties\n"~batchprefix~batchnum (~batchposition)"'),'Prod-653 (9)'])
    tbl_AutosaveFields.add_row(['~title',QApplication.translate('HelpDlg','From Roast>Properties>Title'),'Ethiopia Guji'])
    tbl_AutosaveFields.add_row(['~beans_nn',QApplication.translate('HelpDlg','Replace “nn” with 10, 15, 20, 25, or 30 to show the first “nn” characters of the Beans field.\nFrom Roast>Properties>Beans'),'Ethiopia G'])
    tbl_AutosaveFields.add_row(['~beans_line',QApplication.translate('HelpDlg','The entire first line From Roast>Properties>Beans'),'Ethiopia Guji purchased from Royal'])
    tbl_AutosaveFields.add_row(['~date',QApplication.translate('HelpDlg','Roast date in format yy-MM-dd'),'20-02-05'])
    tbl_AutosaveFields.add_row(['~date_long',QApplication.translate('HelpDlg','Roast date in format yyyy-MM-dd'),'2020-02-05'])
    tbl_AutosaveFields.add_row(['~time',QApplication.translate('HelpDlg','Roast time in format hhmm'),1742])
    tbl_AutosaveFields.add_row(['~datetime',QApplication.translate('HelpDlg','Roast date and time in format yy-MM-dd_hhmm'),'20-02-05_1742'])
    tbl_AutosaveFields.add_row(['~datetime_long',QApplication.translate('HelpDlg','Roast date and time in format yyyy-MM-dd_hhmm'),'2020-02-05_1742'])
    tbl_AutosaveFields.add_row(['~yyyy',QApplication.translate('HelpDlg','Roast year in format yyyy'),2020])
    tbl_AutosaveFields.add_row(['~yy',QApplication.translate('HelpDlg','Roast year in format yy'),20])
    tbl_AutosaveFields.add_row(['~mmm',QApplication.translate('HelpDlg','Roast month in format MMM (localized)'),'Feb'])
    tbl_AutosaveFields.add_row(['~mm',QApplication.translate('HelpDlg','Roast month in format MM'),'02'])
    tbl_AutosaveFields.add_row(['~ddd',QApplication.translate('HelpDlg','Roast day in format ddd (localized)'),'Wed'])
    tbl_AutosaveFields.add_row(['~dd',QApplication.translate('HelpDlg','Roast day in format dd'),'05'])
    tbl_AutosaveFields.add_row(['~hour',QApplication.translate('HelpDlg','Roast hour in format hh'),17])
    tbl_AutosaveFields.add_row(['~minute',QApplication.translate('HelpDlg','Roast minute in format mm'),42])
    tbl_AutosaveFields.add_row(['~currtime',QApplication.translate('HelpDlg','Current date and time with seconds in format yy-MM-dd_hhmmss.  Not the same as roast time. '),'21-01-18_093609'])
    tbl_AutosaveFields.add_row(['~operator',QApplication.translate('HelpDlg','From Roast>Properties>Operator'),'Dave'])
    tbl_AutosaveFields.add_row(['~organization',QApplication.translate('HelpDlg','From Roast>Properties>Organization'),'Dave&#39;s Coffee'])
    tbl_AutosaveFields.add_row(['~machine',QApplication.translate('HelpDlg','From Roast>Properties>Machine'),'SF-6'])
    tbl_AutosaveFields.add_row(['~weight',QApplication.translate('HelpDlg','From Roast>Properties>Weight Green'),3])
    tbl_AutosaveFields.add_row(['~roastedweight',QApplication.translate('HelpDlg','From Roast>Properties>Weight Roasted'),2.6])
    tbl_AutosaveFields.add_row(['~weightunits',QApplication.translate('HelpDlg','From Roast>Properties>Weight'),'Kg'])
    tbl_AutosaveFields.add_row(['~weightloss',QApplication.translate('HelpDlg','Calculated weight loss in percent (the  “-” sign is not shown, it can be added manually in front of the field if desired)'),14.1])
    tbl_AutosaveFields.add_row(['~volume',QApplication.translate('HelpDlg','From Roast>Properties>Volume Green'),4.1])
    tbl_AutosaveFields.add_row(['~roastedvolume',QApplication.translate('HelpDlg','From Roast>Properties>Volume Roasted'),6.8])
    tbl_AutosaveFields.add_row(['~volumeunits',QApplication.translate('HelpDlg','From Roast>Properties>Volume'),'l'])
    tbl_AutosaveFields.add_row(['~volumegain',QApplication.translate('HelpDlg','Calculated volume gain in percent'),61.5])
    tbl_AutosaveFields.add_row(['~density',QApplication.translate('HelpDlg','From Roast>Properties>Density Green'),756.4])
    tbl_AutosaveFields.add_row(['~roasteddensity',QApplication.translate('HelpDlg','From Roast>Properties>Density Roasted'),375.2])
    tbl_AutosaveFields.add_row(['~densityunits',QApplication.translate('HelpDlg','From Roast>Properties>Density'),'g_l'])
    tbl_AutosaveFields.add_row(['~densityloss',QApplication.translate('HelpDlg','Calculated density loss in percent (the  “-” sign is not shown, it can be added manually in front of the field if desired)'),46.8])
    tbl_AutosaveFields.add_row(['~moisture',QApplication.translate('HelpDlg','From Roast>Properties>Moisture Green'),11.7])
    tbl_AutosaveFields.add_row(['~roastedmoisture',QApplication.translate('HelpDlg','From Roast>Properties>Moisture Roasted'),2.8])
    tbl_AutosaveFields.add_row(['~moistureloss',QApplication.translate('HelpDlg','Calculated moisture loss in percent (the  “-” sign is not shown, it can be added manually in front of the field if desired)'),8.1])
    tbl_AutosaveFields.add_row(['~drumspeed',QApplication.translate('HelpDlg','From Roast>Properties>Drum Speed'),64])
    tbl_AutosaveFields.add_row(['~colorwhole',QApplication.translate('HelpDlg','From Roast>Properties>Color Whole'),103])
    tbl_AutosaveFields.add_row(['~colorground',QApplication.translate('HelpDlg','From Roast>Properties>Color Ground'),98])
    tbl_AutosaveFields.add_row(['~colorsystem',QApplication.translate('HelpDlg','From Roast>Properties>Color System'),'Tonino'])
    tbl_AutosaveFields.add_row(['~screenmin',QApplication.translate('HelpDlg','From Roast>Properties>Screen Min'),16])
    tbl_AutosaveFields.add_row(['~screenmax',QApplication.translate('HelpDlg','From Roast>Properties>Screen Max'),18])
    tbl_AutosaveFields.add_row(['~greenstemp',QApplication.translate('HelpDlg','From Roast>Properties>(Green) Beans Temperature'),'68.0'])
    tbl_AutosaveFields.add_row(['~ambtemp',QApplication.translate('HelpDlg','From Roast>Properties>Ambient Temperature'),'70.0'])
    tbl_AutosaveFields.add_row(['~ambhumidity',QApplication.translate('HelpDlg','From Roast>Properties>Ambient Humidity'),35.1])
    tbl_AutosaveFields.add_row(['~ambpressure',QApplication.translate('HelpDlg','From Roast>Properties>Ambient Pressure'),1023.8])
    tbl_AutosaveFields.add_row(['~devtime',QApplication.translate('HelpDlg','Calculated time from FCs to DROP in seconds'),112])
    tbl_AutosaveFields.add_row(['~devtime_long',QApplication.translate('HelpDlg','Calculated time from FCs to DROP in min_secs'),'01_52'])
    tbl_AutosaveFields.add_row(['~dtr',QApplication.translate('HelpDlg','From Profile Statistics - DTR (in percent)'),22.1])
    tbl_AutosaveFields.add_row(['~auc',QApplication.translate('HelpDlg','From the Profile Statistics - AUC'),218])
    tbl_AutosaveFields.add_row(['~aucbase',QApplication.translate('HelpDlg','From the Profile Statistics - AUC Base'),300])
    tbl_AutosaveFields.add_row(['~chargeet',QApplication.translate('HelpDlg','From the Profile - ET at CHARGE'),379.4])
    tbl_AutosaveFields.add_row(['~chargebt',QApplication.translate('HelpDlg','From the Profile - BT at CHARGE'),375.2])
    tbl_AutosaveFields.add_row(['~fcset',QApplication.translate('HelpDlg','From the Profile - ET at FCs'),397.4])
    tbl_AutosaveFields.add_row(['~fcsbt',QApplication.translate('HelpDlg','From the Profile -BT at FCs'),386.7])
    tbl_AutosaveFields.add_row(['~dropet',QApplication.translate('HelpDlg','From the Profile - ET at DROP'),378.6])
    tbl_AutosaveFields.add_row(['~dropbt',QApplication.translate('HelpDlg','From the Profile - BT at DROP'),412.5])
    tbl_AutosaveFields.add_row(['~droptime',QApplication.translate('HelpDlg','From the Profile - DROP time in seconds'),617])
    tbl_AutosaveFields.add_row(['~droptime_long',QApplication.translate('HelpDlg','From the Profile - DROP time in min_secs'),'10_17'])
    tbl_AutosaveFields.add_row(['~roastingnotes_nn',QApplication.translate('HelpDlg','Replace “nn” with 10, 15, 20, 25, or 30 to show the first “nn” characters of the Roasting Notes field.\nFrom Roast>Properties>Roasting Notes'),'No crash, '])
    tbl_AutosaveFields.add_row(['~roastingnotes_line',QApplication.translate('HelpDlg','The entire first line From Roast>Properties>Roasting Notes'),'No crash, maintained RoR'])
    tbl_AutosaveFields.add_row(['~cupptingnotes_nn',QApplication.translate('HelpDlg','Replace “nn” with 10, 15, 20, 25, or 30 to show the first “nn” characters of the Cupping Notes field.\nFrom Roast>Properties>Cupping Notes'),'Lots of be'])
    tbl_AutosaveFields.add_row(['~cupptingnotes_line',QApplication.translate('HelpDlg','The entire first line From Roast>Properties>Cupping Notes'),'Lots of berries and chocolate'])
    tbl_AutosaveFields.add_row(['~btubatch',QApplication.translate('HelpDlg','From the Profile Energy Use - Total energy used by the batch in BTU'),8943.2])
    tbl_AutosaveFields.add_row(['~co2batch',QApplication.translate('HelpDlg','From the Profile Energy Use - CO2 produced by the batch in g'),923.3])
    tbl_AutosaveFields.add_row(['~btupreheat',QApplication.translate('HelpDlg','From the Profile Energy Use - Energy used during preheat in BTU'),2538.8])
    tbl_AutosaveFields.add_row(['~co2preheat',QApplication.translate('HelpDlg','From the Profile Energy Use - CO2 produced during preheat in g'),443.9])
    tbl_AutosaveFields.add_row(['~btubbp',QApplication.translate('HelpDlg','From the Profile Energy Use - Energy used during Between Batch Protocol in BTU'),1019.7])
    tbl_AutosaveFields.add_row(['~co2bbp',QApplication.translate('HelpDlg','From the Profile Energy Use - CO2 produced during Between Batch Protocol in g'),254.1])
    tbl_AutosaveFields.add_row(['~bturoast',QApplication.translate('HelpDlg','From the Profile Energy Use - Energy used from CHARGE to DROP in BTU'),7843.2])
    tbl_AutosaveFields.add_row(['~co2roast',QApplication.translate('HelpDlg','From the Profile Energy Use - CO2 produced from CHARGE to DROP in g'),873.9])
    tbl_AutosaveFields.add_row(['~co2pergreenkg',QApplication.translate('HelpDlg','From the Profile Energy Use - CO2 produced per kg of green beans in g'),354.3])
    strlist.append(tbl_AutosaveFields.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_AutosaveFieldsbottom = prettytable.PrettyTable()
    tbl_AutosaveFieldsbottom.header = False
    tbl_AutosaveFieldsbottom.add_row(['NOTES:\nAnything between single quotes &#39; will show in the file name only when ON.\nExample: &#39;REC ~batch&#39;\n\nAnything between double quotes " will show in the file name only when OFF. \nExample: "~operator"\n\nFor backward compatibility, when the Prefix field is text only the date and time are appended to the file name.\nExample: &#39;Autosave&#39; will result in file name &#39;Autosave_20-01-13_1705&#39;.\nTo show only the text place a single &#39;!&#39; at the start of the Prefix field\nExample: &#39;!Autosave&#39; will result in file name &#39;Autosave&#39;.\n\nTo maintain cross platform compatibility, file names may contain only letters, numbers, spaces, \nand the following special characters:  \n_ - . ( )'])
    strlist.append(tbl_AutosaveFieldsbottom.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','EXAMPLES'))
    strlist.append("</b>")
    tbl_Examplestop = prettytable.PrettyTable()
    tbl_Examplestop.header = False
    tbl_Examplestop.add_row([QApplication.translate('HelpDlg','Data used to replace the fields in the Autosave File Name Prefix are pulled from the current Roast Properties.  ')])
    strlist.append(tbl_Examplestop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Examples = prettytable.PrettyTable()
    tbl_Examples.field_names = [QApplication.translate('HelpDlg','Autosave Field'),QApplication.translate('HelpDlg','Example File Name')]
    tbl_Examples.add_row([QApplication.translate('HelpDlg','~title Roasted on ~date'),QApplication.translate('HelpDlg','Burundi Roasted on 20-04-25.alog')])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','~batchcounter ~title ~date_long'),QApplication.translate('HelpDlg','1380 Burundi 2020-04-25_1136.alog')])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','~beans ~machine ~drumspeedRPM ~weight~weightunits ~poisturePCT ~operator ~date ~batch(~batchposition)'),QApplication.translate('HelpDlg','Burundi Kiganda Murambi Lot44 SF-25 64RPM 10.3Kg 10.2PCT Roberto 20-04-25 Prod-1380(6).alog')])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','\u0027Recording ~batchcounter&#39; "~batch" ~title ~datetime_long'),QApplication.translate('HelpDlg','When OFF:\nProd-1380 Burundi Kiganda Murambi 2020-04-25_1136.alog\nWhile Recording:\nRecording 1380  Burundi KigandaMurambi 2020-04-25_1136.alog')])
    tbl_Examples.add_row([QApplication.translate('HelpDlg','\u0027Recording ~batchcounter&#39; "~batch" ~title ~date_long_&#39;~currtime&#39;"~time"'),QApplication.translate('HelpDlg','Creates a unique filename for multiple saves while sampling by using ~currtime.\nWhen OFF:\nProd-1380 Burundi Kiganda Murambi 2020-04-25_1136.alog\nWhile Recording. \nRecording 1380  Burundi KigandaMurambi 2020-04-25_113809.alog')])
    strlist.append(tbl_Examples.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("</body>")
    helpstr = "".join(strlist)
    helpstr = re.sub(r"&amp;", r"&",helpstr)
    return helpstr