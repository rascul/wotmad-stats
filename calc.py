#!/usr/bin/python3

# this python script will might take over

import fileinput

count = 0

total_str = 0.0
total_int = 0.0
total_wil = 0.0
total_dex = 0.0
total_con = 0.0
total_sum = 0.0

min_str = 0
min_int = 0
min_wil = 0
min_dex = 0
min_con = 0
min_sum = 0

max_str = 0
max_int = 0
max_wil = 0
max_dex = 0
max_con = 0
max_sum = 0

count = 0

for line in fileinput.input():
	line = line.strip()
	
	fields = line.split(',')
	
	if count > 0:
		stat_sum = int(fields.pop())
		stat_con = int(fields.pop())
		stat_dex = int(fields.pop())
		stat_wil = int(fields.pop())
		stat_int = int(fields.pop())
		stat_str = int(fields.pop())
		
		total_str += stat_str
		total_int += stat_int
		total_wil += stat_wil
		total_dex += stat_dex
		total_con += stat_con
		total_sum += stat_sum
		
		if count == 1:
			min_str = stat_str
			min_int = stat_int
			min_wil = stat_wil
			min_dex = stat_dex
			min_con = stat_con
			min_sum = stat_sum
			
			max_str = stat_str
			max_int = stat_int
			max_wil = stat_wil
			max_dex = stat_dex
			max_con = stat_con
			max_sum = stat_sum
		
		if stat_str < min_str:
			min_str = stat_str
		elif stat_str > max_str:
			max_str = stat_str
		
		if stat_int < min_int:
			min_int = stat_int
		elif stat_int > max_int:
			max_int = stat_int
		
		if stat_wil < min_wil:
			min_wil = stat_wil
		elif stat_wil > max_wil:
			max_wil = stat_wil
		
		if stat_dex < min_dex:
			min_dex = stat_dex
		elif stat_dex > max_dex:
			max_dex = stat_dex
		
		if stat_con < min_con:
			min_con = stat_con
		elif stat_con > max_con:
			max_con = stat_con
		
		if stat_sum < min_sum:
			min_sum = stat_sum
		elif stat_sum > max_sum:
			max_sum = stat_sum
	
	count += 1


count -= 1

print("""
<table>
<thead>
	<th></th>
	<th>Str</th>
	<th>Int</th>
	<th>Wil</th>
	<th>Dex</th>
	<th>Con</th>
	<th>Sum</th>
</thead>
""")
print("<tr><td align=\"center\">minimum</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td></tr>".format(min_str, min_int, min_wil, min_dex, min_con, min_sum))
print("<tr><td align=\"center\">maximum</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td></tr>".format(max_str, max_int, max_wil, max_dex, max_con, max_sum))
print("<tr><td align=\"center\">average</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td><td align=\"center\">{}</td></tr>".format(round(total_str / count, 1), round(total_int / count, 1), round(total_wil / count, 1), round(total_dex / count, 1), round(total_con / count, 1), round(total_sum / count, 1)))
print("</table>")









