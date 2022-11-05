import ctypes

ntdll = ctypes.windll.ntdll
SeShutdownPrivilege = 19

def GetNtError(err):
	return ntdll.RtlNtStatusToDosError(err)

def BSOD(stop_code):
	enabled = ctypes.c_bool()
	res = ntdll.RtlAdjustPrivileges(SeShutdownPrivilege, True, False, ctypes.pointer(enabled))
	print(enabled)
	if not res:
		print("Privilege adjusted successfully!")
	else:
		print("Privileges could not be adjusted :(")
		raise ctypes.WinError(GetNtError(res))
	response = ctypes.c_ulong()
	res = ntdll.NtRaiseHardError(stop_code, 0, 0, 0, 6, ctypes.byref(response))

	if not res:
		print("Bluescreen successful")
	else:
		print("Bluescreen failed!")
		raise ctypes.WinError(GetNtError(res))

BSOD(0xDEADDEAD)
