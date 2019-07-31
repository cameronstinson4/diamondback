class StateMachine:
    """
    This class represents the encompassing state machine object
    """

    def __init__(self, StartAt, States={}, Comment=None, TimeoutSeconds=None, Version=None):
        """
        Constructor

            Args:
                StartAt: State, required. A string that must exactly match (is case sensitive) the name of one of the state objects.
                Comment: string optional. A human-readable description of the state machine.
                TimeoutSeconds: integer, optional. The maximum number of seconds an execution of the state machine can run. If it runs longer than the specified time, the execution fails with a States.Timeout Error Name.
                Version: The version of the Amazon States Language used in the state machine (default is "1.0").

        """
        self.StartAt = StartAt
        self.States = States
        self.Comment = Comment
        self.TimeoutSeconds = TimeoutSeconds
        self.Version = Version

    def addState(self, state, stateName):
        """
        Adds a state to the state machine object
        """
        self.States[stateName] = state

class StateMachineBuilder():
    """
    This class represents the encompassing state machine object with no required
    """

    def __init__(self, StartAt=None, States=None, Comment=None, TimeoutSeconds=None, Version=None):
        """
        Constructor

            Args:
                StartAt: State, required. A string that must exactly match (is case sensitive) the name of one of the state objects.
                Comment: string optional. A human-readable description of the state machine.
                TimeoutSeconds: integer, optional. The maximum number of seconds an execution of the state machine can run. If it runs longer than the specified time, the execution fails with a States.Timeout Error Name.
                Version: The version of the Amazon States Language used in the state machine (default is "1.0").

        """
        self.StartAt = StartAt
        self.States = States
        self.Comment = Comment
        self.TimeoutSeconds = TimeoutSeconds
        self.Version = Version

    def addState(self, state, stateName):
        """
        Adds a state to the state machine object
        """
        self.States[stateName] = state
    
    def setStartAtStart(self, state):
        """
        Sets the state to start at
        """
        pass

    def build(self):
        """
        Builds the state machine object
        """

        return