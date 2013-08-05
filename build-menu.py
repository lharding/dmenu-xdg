from xdg.DesktopEntry import DesktopEntry
import glob
import md5
#import sys
import os
import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)  

HOMEDIR = os.getenv("HOME") 

execfile(HOMEDIR+'/.config/dmenu-xdg')

menuFile = codecs.open(HOMEDIR+'/bin/xdg-dmenu.cache', 'w', encoding='utf-8')
execFile = codecs.open(HOMEDIR+'/bin/xdg-exec.cache', 'w', encoding='utf-8')

execs = {}

def printEntry(catName, de, mainGroup):
    exc = de.getExec()
    hsh = md5.new(exc).hexdigest()

    name = de.getName() if mainGroup else "    " + de.getName()
    mimeStr = str(de.getMimeTypes()) if de.getMimeTypes() else ""
    comment = de.getComment()
    genericName = (" (" + de.getGenericName() + ")") if de.getGenericName() else ""
    line = (u"%s / %s%s: %s %s" % (catName, name, genericName, comment, mimeStr)).ljust(250)+" "+hsh+"\n"
    menuFile.write(line)

    if de.getType() == "Link":
        exc = BROWSER_CMD + de.getURL()
    else:
        #munch field codes we can't do anything with:
        for c in 'fFuUdDnNickvm':
            exc = exc.replace('%'+c, '')

        if de.getTerminal():
            exc = TERM_CMD + exc

        if de.getPath():
            exc = "cd '"+de.getPath()+"'; "+exc
    
    execs[hsh] = hsh + " " + exc + "\n"

categories = {}

for dir in SEARCH_DIRS:
    fnames = glob.glob(dir+'/*/*.desktop')

    for fname in fnames:
        de = DesktopEntry(fname)
        cats = de.getCategories() or ["All"]
        for cat in cats:
            if not cat in categories:
                categories[cat] = []
            
            categories[cat].append(de)

for k, v in sorted(categories.items()):
    catName = k
    for de in v:
        if de.getNoDisplay() or de.getHidden():
            continue

        mainGroup = de.defaultGroup
        printEntry(catName, de, True)

        for group in de.groups():
            if group != mainGroup:
                de.defaultGroup = group
                printEntry(catName, de, False)

for exc in execs.values():
    execFile.write(exc)

menuFile.close()
execFile.close()
