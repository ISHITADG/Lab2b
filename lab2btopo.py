""" Custom topology example

One switch with server and client on either side:

   host --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        server = self.addHost('PC2', ip='10.10.1.1/24' )
        client = self.addHost('PC1', ip='10.10.3.2/24' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )

        # Add links
        self.addLink( client, switch2 )
        self.addLink( switch2, switch1 )
        self.addLink( switch1, server )


topos = { 'mytopo': ( lambda: MyTopo() ) }
