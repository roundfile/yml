# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IkawaCmd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eIkawaCmd.proto\x12\x04test\"|\n\x07Message\x12\x10\n\x08\x63md_type\x18\x01 \x02(\x05\x12\x0b\n\x03seq\x18\x02 \x02(\x05\x12(\n\x0bprofile_set\x18\x04 \x01(\x0b\x32\x13.test.CmdProfileSet\x12(\n\x0bsetting_get\x18\x05 \x01(\x0b\x32\x13.test.CmdSettingGet\"4\n\rCmdProfileSet\x12#\n\x07profile\x18\x01 \x02(\x0b\x32\x12.test.RoastProfile\"\x1e\n\rCmdSettingGet\x12\r\n\x05\x66ield\x18\x01 \x02(\x05\"\x9f\x08\n\rIkawaResponse\x12\x0b\n\x03seq\x18\x01 \x02(\x05\x12&\n\x04resp\x18\x02 \x02(\x0e\x32\x18.test.IkawaResponse.Resp\x12\x43\n\x1bresp_bootloader_get_version\x18\x03 \x01(\x0b\x32\x1e.test.RespBootloaderGetVersion\x12\x36\n\x13resp_mach_prop_type\x18\x04 \x01(\x0b\x32\x19.test.RespMachPropGetType\x12-\n\x0cresp_mach_id\x18\x05 \x01(\x0b\x32\x17.test.RespMachPropGetID\x12@\n\x1aresp_mach_status_get_error\x18\x0c \x01(\x0b\x32\x1c.test.RespMachStatusGetError\x12<\n\x18resp_mach_status_get_all\x18\r \x01(\x0b\x32\x1a.test.RespMachStatusGetAll\x12I\n\x1fresp_hist_get_total_roast_count\x18\x0f \x01(\x0b\x32 .test.RespHistGetTotalRoastCount\x12.\n\x10resp_profile_get\x18\x10 \x01(\x0b\x32\x14.test.RespProfileGet\x12.\n\x10resp_setting_get\x18\x11 \x01(\x0b\x32\x14.test.RespSettingGet\x12I\n\x1fresp_mach_prop_get_support_info\x18\x15 \x01(\x0b\x32 .test.RespMachPropGetSupportInfo\"\xb6\x03\n\x04Resp\x12\x05\n\x01\x41\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16\x42OOTLOADER_GET_VERSION\x10\x03\x12 \n\x1cHIST_GET_PROFILE_ROAST_COUNT\x10\x0e\x12\x1e\n\x1aHIST_GET_TOTAL_ROAST_COUNT\x10\x0f\x12\x0b\n\x07MACH_ID\x10\x05\x12\x16\n\x12MACH_PROP_GET_NAME\x10\x18\x12\x1e\n\x1aMACH_PROP_GET_SUPPORT_INFO\x10\x15\x12\x12\n\x0eMACH_PROP_TYPE\x10\x04\x12\x17\n\x13MACH_STATUS_GET_ALL\x10\r\x12\x19\n\x15MACH_STATUS_GET_ERROR\x10\x0c\x12\x1b\n\x17MACH_STATUS_GET_SENSORS\x10\x14\x12\x18\n\x14MACH_STATUS_GET_TIME\x10\x17\x12\x0f\n\x0bPROFILE_GET\x10\x10\x12\x15\n\x11ROAST_SUMMARY_GET\x10\x19\x12\x0f\n\x0bSETTING_GET\x10\x11\x12\x14\n\x10SETTING_GET_INFO\x10\x12\x12\x14\n\x10SETTING_GET_LIST\x10\x13\x12\x13\n\x0fTEST_STATUS_GET\x10\x16\"\xdd\x03\n\x14RespMachStatusGetAll\x12\x0c\n\x04time\x18\x01 \x02(\x05\x12\x12\n\ntemp_above\x18\x02 \x01(\x05\x12\x0b\n\x03\x66\x61n\x18\x03 \x02(\x05\x12\r\n\x05state\x18\x04 \x02(\x05\x12\x0e\n\x06heater\x18\x05 \x02(\x05\x12\t\n\x01p\x18\x06 \x02(\x05\x12\t\n\x01i\x18\x07 \x02(\x05\x12\t\n\x01\x64\x18\x08 \x02(\x05\x12\x10\n\x08setpoint\x18\t \x02(\x05\x12\x14\n\x0c\x66\x61n_measured\x18\n \x02(\x05\x12\x12\n\nboard_temp\x18\x0b \x01(\x05\x12\x12\n\ntemp_below\x18\x0c \x01(\x05\x12\x18\n\x10\x66\x61n_rpm_measured\x18\r \x01(\x05\x12\x18\n\x10\x66\x61n_rpm_setpoint\x18\x0e \x01(\x05\x12\r\n\x05\x66\x61n_i\x18\x10 \x01(\x05\x12\r\n\x05\x66\x61n_p\x18\x0f \x01(\x05\x12\r\n\x05\x66\x61n_d\x18\x11 \x01(\x05\x12\x11\n\tfan_power\x18\x12 \x01(\x05\x12\t\n\x01j\x18\x13 \x01(\x05\x12\x13\n\x0brelay_state\x18\x14 \x01(\x05\x12\x12\n\npid_sensor\x18\x15 \x01(\x05\x12\x1b\n\x13temp_above_filtered\x18\x16 \x01(\x05\x12\x1b\n\x13temp_below_filtered\x18\x17 \x01(\x05\x12\x11\n\tror_above\x18\x18 \x01(\x05\x12\x11\n\tror_below\x18\x19 \x01(\x05\"\'\n\x16RespMachStatusGetError\x12\r\n\x05\x65rror\x18\x01 \x02(\x05\"5\n\x0eRespProfileGet\x12#\n\x07profile\x18\x01 \x02(\x0b\x32\x12.test.RoastProfile\"\xa4\x02\n\x0cRoastProfile\x12\x0e\n\x06schema\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x02(\x0c\x12\x0c\n\x04name\x18\x03 \x02(\t\x12$\n\x0btemp_points\x18\x04 \x03(\x0b\x32\x0f.test.TempPoint\x12\"\n\nfan_points\x18\x05 \x03(\x0b\x32\x0e.test.FanPoint\x12\x13\n\x0btemp_sensor\x18\x06 \x02(\x05\x12$\n\x0c\x63ooldown_fan\x18\x07 \x02(\x0b\x32\x0e.test.FanPoint\x12\x13\n\x0b\x63offee_name\x18\x08 \x02(\t\x12\x0f\n\x07user_id\x18\t \x02(\t\x12\x11\n\tcoffee_id\x18\n \x02(\t\x12\x16\n\x0e\x63offee_web_url\x18\x0b \x02(\t\x12\x14\n\x0cprofile_type\x18\x0c \x02(\t\"\'\n\x08\x46\x61nPoint\x12\x0c\n\x04time\x18\x01 \x02(\x05\x12\r\n\x05power\x18\x02 \x02(\x05\"\'\n\tTempPoint\x12\x0c\n\x04time\x18\x01 \x02(\x05\x12\x0c\n\x04temp\x18\x02 \x02(\x05\".\n\x0eRespSettingGet\x12\r\n\x05\x66ield\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\"7\n\x1aRespHistGetTotalRoastCount\x12\x19\n\x11total_roast_count\x18\x01 \x02(\x05\"4\n\x1aRespMachPropGetSupportInfo\x12\x16\n\x0eprofile_schema\x18\x01 \x02(\x05\"=\n\x18RespBootloaderGetVersion\x12\x0f\n\x07version\x18\x01 \x02(\x05\x12\x10\n\x08revision\x18\x02 \x02(\t\"5\n\x13RespMachPropGetType\x12\r\n\x05type_\x18\x01 \x02(\x05\x12\x0f\n\x07variant\x18\x02 \x02(\x05\" \n\x11RespMachPropGetID\x12\x0b\n\x03id_\x18\x01 \x02(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'IkawaCmd_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=24
  _MESSAGE._serialized_end=148
  _CMDPROFILESET._serialized_start=150
  _CMDPROFILESET._serialized_end=202
  _CMDSETTINGGET._serialized_start=204
  _CMDSETTINGGET._serialized_end=234
  _IKAWARESPONSE._serialized_start=237
  _IKAWARESPONSE._serialized_end=1292
  _IKAWARESPONSE_RESP._serialized_start=854
  _IKAWARESPONSE_RESP._serialized_end=1292
  _RESPMACHSTATUSGETALL._serialized_start=1295
  _RESPMACHSTATUSGETALL._serialized_end=1772
  _RESPMACHSTATUSGETERROR._serialized_start=1774
  _RESPMACHSTATUSGETERROR._serialized_end=1813
  _RESPPROFILEGET._serialized_start=1815
  _RESPPROFILEGET._serialized_end=1868
  _ROASTPROFILE._serialized_start=1871
  _ROASTPROFILE._serialized_end=2163
  _FANPOINT._serialized_start=2165
  _FANPOINT._serialized_end=2204
  _TEMPPOINT._serialized_start=2206
  _TEMPPOINT._serialized_end=2245
  _RESPSETTINGGET._serialized_start=2247
  _RESPSETTINGGET._serialized_end=2293
  _RESPHISTGETTOTALROASTCOUNT._serialized_start=2295
  _RESPHISTGETTOTALROASTCOUNT._serialized_end=2350
  _RESPMACHPROPGETSUPPORTINFO._serialized_start=2352
  _RESPMACHPROPGETSUPPORTINFO._serialized_end=2404
  _RESPBOOTLOADERGETVERSION._serialized_start=2406
  _RESPBOOTLOADERGETVERSION._serialized_end=2467
  _RESPMACHPROPGETTYPE._serialized_start=2469
  _RESPMACHPROPGETTYPE._serialized_end=2522
  _RESPMACHPROPGETID._serialized_start=2524
  _RESPMACHPROPGETID._serialized_end=2556
# @@protoc_insertion_point(module_scope)
