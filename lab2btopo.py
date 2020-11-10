""" Custom topology example

One switch with server and client on either side:

   host --- switch --- host
               |
              host

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
        # 653: ADD HOSTS HERE
        switch = self.addSwitch( 's3' )

        # Add links (DO NOT MODIFY OR CHANGE THIS ORDER BELOW)
        self.addLink( h1, switch )
        self.addLink( h2, switch )
        self.addLink( switch, h3 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
