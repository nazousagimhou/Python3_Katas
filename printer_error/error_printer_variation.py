def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m" or i < 'a':
            errors += 1
    return str(errors) + "/" + str(count)

print(printer_error("AAAAX"))