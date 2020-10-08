import time
'''
trying to support value until infinity 
top = number[0]
base = number[-3:]
middle = []
if len(number)/2 == 2:
	pass
if len(number)/2 == 3:
	middle.append(number[-5:-3])
if len(number)/2 == 4:
	middle.append([number[-7:-5],number[-5:-3]])
print(middle)
'''
def format_num(number):
	number = str(number)
	length = len(number)

	if length <= 3:
		result = number
		breakpoint

	elif length == 4:
		result = ','.join([number[0],number[-3:]])
		breakpoint

	elif length == 5:
		result = ','.join([number[0:2],number[-3:]])
		breakpoint

	elif length == 6:
		result = ','.join([number[0],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 7:
		result = ','.join([number[0:2],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 8:
		result = ','.join([number[0],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 9:
		result = ','.join([number[0:2],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 10:
		result = ','.join([number[0],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 11:
		result = ','.join([number[0:2],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 12:
		result = ','.join([number[0],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 13:
		result = ','.join([number[0:2],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 14:
		result = ','.join([number[0],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 15:
		result = ','.join([number[0:2],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 16:
		result = ','.join([number[0],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 17:
		result = ','.join([number[0:2],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 18:
		result = ','.join([number[0],number[-17:-15],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 19:
		result = ','.join([number[0:2],number[-17:-15],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 20:
		result = ','.join([number[0],number[-19:-17],number[-17:-15],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length == 21:
		result = ','.join([number[0:2],number[-19:-17],number[-17:-15],number[-15:-13],number[-13:-11],number[-11:-9],number[-9:-7],number[-7:-5],number[-5:-3],number[-3:]])
		breakpoint

	elif length > 21:
		print(f"""
Raise unsupported value range error:
Value range unsupported enter value between 0-21
given range {length}""")
		result = number

	return result

