def drange(start, stop, step):
    temp = start
    while temp < stop:
        yield temp
        temp += step

numbers = ["%g" % x for x in drange(0, 10, 0.01)]
appendix = ['{}.{}0'.format(y, x) for x in range(0, 10) for y in range(0, 10)]

all = numbers + appendix + ['0.0', '10', '10.0', '10.00']
template = open('badge-template.svg', 'r').read()
color_ok = "#44cc11"
color_warning = "#dfb317"
color_red = "#e05f44"
color = color_ok

for score in all:
    if float(score) < 3.0:
        color = color_red
    elif float(score) >= 3.0 and float(score) < 7.0:
        color = color_warning
    else:
        color = color_ok

    score_file = open('badges/{score}.svg'.format(score=score), 'w+')
    score_file.write(template.format(score=score, color=color))
    score_file.close()
