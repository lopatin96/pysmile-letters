import os

import pysmile
import pysmile_license

from tkinter import *
from tkinter import messagebox


class LettersClassifier:
    def __init__(self):
        self.net = None
        self.letter = None
        self.evidences = {
            'spam': ['free', 'satisfied', 'acceptance', 'won', 'access', 'online', 'bargain',
                     'best price', 'call now', 'call free', 'cash bonus', 'chance', 'click', 'credit', 'free access',
                     'free money', 'gift certificate', 'limited', 'lifetime'],
            'love': ['love you', 'loved you', 'for always', 'the words to describe', 'how much you', 'let my heart',
                     'express', 'do that for', 'thinking of', 'want you', 'share', 'excited', 'feeling', 'hot',
                     'romantic'
                     ],
            'cv': ['confident', 'flexible', 'adaptable', 'hard-working', 'reliable', 'dedicated', 'creative', 'dynamic',
                   'business', 'enthusiastic', 'resourceful', 'diplomatic', 'co-operative', 'consistent',
                   'people-oriented', 'curious', 'passionate']
        }

    def set_net(self, net_path):
        net = pysmile.Network()
        net.read_file(net_path)
        self.net = net

    def set_display(self, display):
        self.display = display

    def set_letter(self, letter):
        self.letter = letter.strip().lower()

    def _do(self):
        for k, evidences in self.evidences.items():
            for evidence in evidences:
                if evidence.strip().lower() in self.letter:
                    self.net.set_evidence(f'{k}_{evidence.strip().replace(" ", "_").replace("-", "_").lower()}', 'y')
                    continue
                self.net.set_evidence(f'{k}_{evidence.strip().replace(" ", "_").replace("-", "_").lower()}', 'n')
                self.net.update_beliefs()

    def get_node_value(self, node):
        self._do()
        return self.net.get_node_value(node)

    def evaluate(self):
        self.set_letter(self.display.get('1.0', 'end'))
        results = ''
        for type in self.evidences.keys():
            beliefs = lettersClassifier.get_node_value(f'{type}_RESULT')
            results += f'{type}: {round(beliefs[0] * 100, 2)}%\n'
        messagebox.showinfo("Results", results)


if __name__ == '__main__':
    net_name = 'LettersClassifierNet_Result1'
    net_path = os.getcwd()

    lettersClassifier = LettersClassifier()
    lettersClassifier.set_net(f'{net_path}\\{net_name}.xdsl')

    letters = {
        'spam': 'You have won $46,000. Seem impossible? Call now, it\'s free or click here for details (no, there is no "catch")...',
        'love': 'Honey,nThere are not enough words to express what you mean to me. I cherish every moment and every new memory. Every second that we share is seared into my mind and in my heart forever. You\'ve left an imprint deep upon my soul. I love you more than you could ever imagine. Forever yours,',
        'cv': 'A creative, curious, confident and enthusiastic full stack web developer. Constantly eager to learn new technologies and languages.'
    }

    # create window
    app = Tk()
    app.title('SBL')
    app.resizable(width=False, height=False)

    # create text
    text = Text(app, width=40, height=10)
    lettersClassifier.set_display(text)
    text.insert('1.0', 'Copy your letter text here...')
    text.grid(row=1, pady=(20, 20), padx=(20, 20))

    # create button
    Button(app, text='Evaluate', width=20, height=3,
           command=lettersClassifier.evaluate, bg='green', foreground='white').grid(row=2, pady=(20, 20), padx=10)

    app.mainloop()
