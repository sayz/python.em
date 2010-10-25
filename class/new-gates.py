class LogicGate:
        def __init__(self,n):
                self.label = n
                self.output = None

        def getLabel(self):
                return self.label

        def getOutput(self):
                self.output = self.performGateLogic()
                return self.output

class BinaryGate(LogicGate):
        def __init__(self,n):
                LogicGate.__init__(self,n)
                self.pinA, self.pinB = None, None

        def setNextPin(self,source):
                if self.pinA == None:
                        self.pinA = source
                else:
                        if self.pinB == None:
                                self.pinB = source
                        else:
                                print "Cannot Connect: NO EMPTY PINS"

class AndGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pina, self.pinb = pinA, pinB
        def performGateLogic(self):
                if self.pina==1 and self.pinb==1:
                        return 1
                else:
                        return 0

class NandGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pina, self.pinb = pinA, pinB
        def performGateLogic(self):
                if self.pina==1 and self.pinb==1:
                        return 0
                else:
                        return 1

class OrGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pina, self.pinb = pinA, pinB
        def performGateLogic(self):
                if self.pina==0 and self.pinb==0:
                        return 0
                else:
                        return 1

class XorGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pina, self.pinb = pinA, pinB
        def performGateLogic(self):
                if self.pina==self.pinb:
                        return 0
                else:
                        return 1

class NorGate(BinaryGate):
        def __init__(self, n, pinA=None, pinB=None):
                BinaryGate.__init__(self,n)
                self.pina, self.pinb = pinA, pinB
        def performGateLogic(self):
                if self.pina==0 and self.pinb==0:
                        return 1
                else:
                        return 0

class UnaryGate(LogicGate):
        def __init__(self, n):
                LogicGate.__init__(self,n)
                self.pin = None
        def setNextPin(self,source):
                if self.pin == None:
                        self.pin = source
                else:
                        print "Cannot Connect: NO EMPTY PINS"

class NotGate(UnaryGate):
        def __init__(self, n, pin=None):
                UnaryGate.__init__(self,n)
                self.p = pin
        def performGateLogic(self):
                if self.pin==1:
                        return 0
                else:
                        return 1

class Connector:
        def __init__(self, fgate, tgate):
                self.fromgate = fgate
                self.togate   = tgate
                tgate.setNextPin(self)

        def getFrom(self):
                return self.fromgate

        def getTo(self):
                return self.togate


g1 = AndGate("G1",1,1)
print g1.getOutput()
g2 = NandGate("G2",0,0)
print g2.getOutput()
g3 = XorGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print g3.getOutput()
print g4.getOutput()


