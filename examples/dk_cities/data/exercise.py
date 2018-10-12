f = open('dk_cities.csv', 'r', encoding='utf-8')
content = f.readlines()
f.close()

txt = ""

for line in content:
    for character in line:
        if character == 'Å':
            txt += 'Aa'
        elif character == 'å':
            txt += 'aa'
        elif character == 'Ø':
            txt += 'Oe'
        elif character == 'ø':
            txt += 'oe'
        elif character == 'Æ':
            txt += 'Ae'
        elif character == 'æ':
            txt += 'ae'
        else:
            txt += character

f = open('dk_cities_ascii.csv', 'w')
f.write(txt)
f.close()


    