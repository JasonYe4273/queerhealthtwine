# Input:
# - text: list of tuples (message, sender), where message is a string and sender is True for you and False for friend
# - delay: delay between messages. Default 3 seconds
# - typing_delay: delay between message and typing animation. Default 1 second.
# Output: HTML
def texting_convo_gen(text, delay=3, typing_delay=1):
    html = ""
    i = 0
    t = 0
    for (m, s) in text:
        c = "youtexting" if s else "texting"
        t += typing_delay
        html += '<<timed '+str(t)+'s>><span id="typing'+str(i)+'"><div class="'+c+'">\n'
        html += '  <div class="typing__dot1" />\n'
        html += '  <div class="typing__dot2" />\n'
        html += '  <div class="typing__dot3" />\n'
        html += '</div></span><</timed>>\n'
        t += delay - typing_delay
        html += '<<timed '+str(t)+'s>><<replace "#typing'+str(i)+'">>\n'
        html += '<div class="'+c+'">' + m + '\n'
        html += '</div><</replace>><</timed>>\n'
        i += 1
    print(html)

texting_convo_gen([
    ("", True),
    ("", False),
])