__author__ = 'nightblues'

import re



# Напишите функцию, которая проверяет введенный пользователем e-mail на соответствие следующим правилам:
#
# 1. e-mail состоит из имени и доменной части, эти части разделяются символом "@";
#
# 2. доменная часть не короче 3 символов и не длиннее 256, является набором непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой;
#
# 3. каждый компонент доменной части не может начинаться или заканчиваться символом "-";
#
# 4. имя (до @) не длиннее 128 символов, состоит из символов a-z0-9"._-;
#
# 5. в имени не допускаются две точки подряд;
#
# 6. если в имени есть двойные кавычки ", то они должны быть парными;
#
# 7. в имени могут встречаться символы "!,:", но только между парными двойными кавычками.

email_conds = []
# cond 1
email_conds.append([re.compile(r"[^@]+@[^@]+$"), True])
# cond 2,3
email_conds.append([re.compile(r"@[a-z0-9_]((?![.]-|-[.])[a-z0-9_.-])+[a-z0-9_]$"), False])
email_conds.append([re.compile(r"@[a-z0-9._-]{3,256}$"), False])
# cond 4,5
email_conds.append([re.compile(r'((?![.]{2})[a-z0-9"._!,:-]){0,128}@'), True])
# cond 6,7
email_conds.append([re.compile(r'(("[a-z0-9._!,:-]*?")|([a-z0-9._-])+)+@'), True])

def check_mail(mail):
    for c in email_conds:
        if c[1]:
            if not c[0].match(mail):
                return False
        else:
            # http://docs.python.org/2.7/howto/regex.html :
            # Sometimes you’ll be tempted to keep using re.match(), and just add .* to the front of your RE.
            # Resist this temptation and use re.search() instead. The regular expression compiler does some analysis
            # of REs in order to speed up the process of looking for a match. One such analysis figures out what the
            # first character of a match must be;
            if not c[0].search(mail):
                return False
    return True