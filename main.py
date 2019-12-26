import pysmile
import pysmile_license


if __name__ == '__main__':
    net = pysmile.Network()
    net.read_file("111.xdsl")
    net.set_evidence("Forecast", "Moderate")
    net.update_beliefs()
    beliefs = net.get_node_value("Success")
    print(beliefs)

    net = pysmile.Network()
    net.read_file("111.xdsl")
    net.set_evidence("Success", "Success")
    net.update_beliefs()
    beliefs = net.get_node_value("Forecast")
    print(beliefs)
