import sys
from wsgiref.simple_server import make_server

from spyne import Application, rpc, ServiceBase
from spyne import Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.test.interop.server.soap11.soap_http_basic import port
from twisted.pair import ip


class SomeSampleServices(ServiceBase):

    @rpc(Unicode, Unicode_returns = Unicode)
    def make_project(self, name, version):
        pass


if __name__ == "__main__":
    soap_app = Application([SomeSampleServices],
                           'SampleServices',
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)
    server = make_server(ip, port, wsgi_app)

    sys.exit(server.serve_forever())
