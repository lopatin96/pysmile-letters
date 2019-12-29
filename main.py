import pysmile
import pysmile_license


class LettersClassifier:
    def __init__(self):
        self.net = None
        self.letter = None
        self.evidences = {
            'spam': ['free', 'Satisfied', 'Accept credit cards', 'Acceptance', 'access', 'Accordingly'],
            'love': ['love you', 'loved you', 'for always', 'the words to describe', 'how much you', 'let my heart',
                     'express', 'do that for', 'thinking of', 'want you', 'share', 'excited', 'feeling', 'hot',
                     'romantic', 'honey', 'every moment', 'every second', 'heart', 'forever', 'happy', 'my dear',
                     'unforgettable', 'meet']
        }

    def set_net(self, net_path):
        net = pysmile.Network()
        net.read_file(net_path)
        self.net = net

    def set_letter(self, letter):
        self.letter = letter.strip().lower()

    def _do(self):
        for k, evidences in self.evidences.items():
            for evidence in evidences:
                if evidence.strip().lower() in self.letter:
                    self.net.set_evidence(f'{k}_{evidence.strip().replace(" ", "_").lower()}', 'y')
                    continue
                self.net.set_evidence(f'{k}_{evidence.strip().replace(" ", "_").lower()}', 'n')  # ?
        self.net.update_beliefs()

    def get_node_value(self, node):
        self._do()
        return self.net.get_node_value(node)


if __name__ == '__main__':
    net_name = 'LettersClassifierNet'
    net_path = 'C:\\Users\\SuperPC\\PycharmProjects\\sc-letters\\'

    lettersClassifier = LettersClassifier()
    lettersClassifier.set_net(net_path + net_name + '.xdsl')

    # love letter
    lettersClassifier.set_letter('Honey,nThere are not enough words to express what you mean to me. I cherish every moment and every new memory. Every second that we share is seared into my mind and in my heart forever. You\'ve left an imprint deep upon my soul. I love you more than you could ever imagine. Forever yours,')
    print('Love letter')
    beliefs = lettersClassifier.get_node_value('spam_RESULT')
    print('spam:', beliefs)
    beliefs = lettersClassifier.get_node_value('love_RESULT')
    print('love:', beliefs)
    print('---------')

    # random text
    lettersClassifier.set_letter('Wordclouds.com is a free online word cloud generator and tag cloud creator. Wordclouds.com works on your PC, Tablet or smartphone. Paste text, upload a document or open an URL to automatically generate a word- or tag cloud. Customize your cloud with shapes, themes, colors and fonts. You can also edit the word list, cloud size and gap size. Wordclouds.com can also generate clickable word clouds with links (image map). When you are satisfied with the result, save the image and share it online.')
    print('Random text')
    beliefs = lettersClassifier.get_node_value('spam_RESULT')
    print('spam:', beliefs)
    beliefs = lettersClassifier.get_node_value('love_RESULT')
    print('love:', beliefs)
    print('---------')

