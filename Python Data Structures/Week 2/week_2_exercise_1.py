file_name=open('words.txt')
read_io=file_name.read()
read_strip=read_io.rstrip()
upper_case=read_strip.upper()
print(upper_case)
