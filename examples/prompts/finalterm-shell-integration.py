#!/usr/bin/env python
"""
Mark the start and end of the prompt with Final term (iterm2) escape sequences.
See: https://iterm2.com/finalterm.html
"""
from __future__ import unicode_literals

from prompt_toolkit import prompt
import sys


BEFORE_PROMPT = '\033]133;A\a'
AFTER_PROMPT = '\033]133;B\a'
BEFORE_OUTPUT = '\033]133;C\a'
AFTER_OUTPUT = '\033]133;D;{command_status}\a' # command_status is the command status, 0-255


def get_prompt_text(app):
    # Generate the text fragments for the prompt.
    # Important: use the `ZeroWidthEscape` fragment only if you are sure that
    #            writing this as raw text to the output will not introduce any
    #            cursor movements.
    return [
        ('[ZeroWidthEscape]', BEFORE_PROMPT),
        ('', 'Say something: # '),
        ('[ZeroWidthEscape]', AFTER_PROMPT),
    ]


if __name__ == '__main__':
    answer = prompt(get_prompt_text=get_prompt_text)

    sys.stdout.write(BEFORE_OUTPUT)
    print('You said: %s' % answer)
    sys.stdout.write(AFTER_OUTPUT.format(command_status=0))
