import pysmile
import pysmile_license


class LettersClassifier:
    def __init__(self):
        self.net = None
        self.letter = None
        self.evidences = {
            'spam': ['free', 'satisfied', 'accept credit cards', 'acceptance', 'won', 'access', 'online', 'bargain',
                'best price', 'call now', 'call free', 'cash bonus', 'chance', 'click', 'credit', 'free access',
                'free money', 'gift certificate', 'limited', 'lifetime'],
            'love': ['love you', 'loved you', 'for always', 'the words to describe', 'how much you', 'let my heart',
                'express', 'do that for', 'thinking of', 'want you', 'share', 'excited', 'feeling', 'hot',
                'romantic']
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
                self.net.set_evidence(f'{k}_{evidence.strip().replace(" ", "_").lower()}', 'n') # ?
                self.net.update_beliefs()

    def get_node_value(self, node):
        self._do()
        return self.net.get_node_value(node)


if __name__ == '__main__':
    net_name = 'LettersClassifierNet1'
    net_path = 'C:\\Users\\SuperPC\\PycharmProjects\\sc-letters\\'

    lettersClassifier = LettersClassifier()
    lettersClassifier.set_net(net_path + net_name + '.xdsl')

    letters = {
        'spam': 'Avangar Technologies announces the beginning of a new unprecendented global employment campaign. reviser yeller winers butchery twenties Due to company\'s exploding growth Avangar is expanding business to the European region. During last employment campaign over 1500 people worldwide took part in Avangar\'s business and more than half of them are currently employed by the company. And now we are offering you ne more opportunity to earn extra money working with Avangar Technologies. druggists blame classy gentry Aladdin',
        'love': 'Honey,nThere are not enough words to express what you mean to me. I cherish every moment and every new memory. Every second that we share is seared into my mind and in my heart forever. You\'ve left an imprint deep upon my soul. I love you more than you could ever imagine. Forever yours,'
    }

    for type, letter in letters.items():
        lettersClassifier.set_letter(letter)
        print(f'___ {type} ___')
        for type in letters.keys():
                beliefs = lettersClassifier.get_node_value(f'{type}_RESULT')
                print(f'| {type}: {round(beliefs[0] * 100, 2)}%')
        print('_______\n')