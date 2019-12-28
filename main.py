import pysmile
import pysmile_license


class LettersClassifier:
    def __init__(self):
        self.net = None
        self.letter = None
        self.evidences = {
            'spam': ['free', 'Satisfied', 'Accept credit cards']
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
    net_path = 'C:\\Users\\SuperPC\\PycharmProjects\\sc-letters\\222.xdsl'

    lettersClassifier = LettersClassifier()
    lettersClassifier.set_net(net_path)
    lettersClassifier.set_letter('wewe we w satisfiedewew')
    beliefs = lettersClassifier.get_node_value('r')

    print(beliefs)

