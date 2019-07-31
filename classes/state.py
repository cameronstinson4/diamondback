class AbstractState:
    """
    Abstract class that defines key state variables and functions
    """

    def __init__(self, Next, End=None, Comment=None, InputPath=None, OutputPath=None):
        """
        Constructor

            Args:
                Next: State, required. The name of the next state that is run when the current state finishes. Some state types, such as Choice, allow multiple transition states.
                End: boolean, optional. Designates this state as a terminal state (ends the execution) if set to true. There can be any number of terminal states per state machine. Only one of Next or End can be used in a state. Some state types, such as Choice, don't support or use the End field.
                Comment: string, optional. Holds a human-readable description of the state.
                InputPath: string, optional. A path that selects a portion of the state's input to be passed to the state's task for processing. If omitted, it has the value $ which designates the entire input.
                OutputPath: string, optional. A path that selects a portion of the state's input to be passed to the state's output. If omitted, it has the value $ which designates the entire input. 
        """
        self.Next = Next
        self.End = End
        self.Comment = Comment
        self.InputPath = InputPath
        self.OutputPath = OutputPath

    def __repr__(self):
        """
        Unambiguous string representation of this object
        
            Returns:
                String representation of this object
        """

        return [a for a in dir(self) if not a.startswith('__')]


class TaskState(AbstractState):
    """
    Task class that defines task state variables and functions
    """

    def __init__(self, Resource, Parameters=None, ResultPath=None, Retry=None, Catch=None, TimeoutSeconds=None, HeartbeatSeconds=None):
        """
        Constructor

            Args:
                Resource: string, required. A URI, especially an Amazon Resource Name (ARN) that uniquely identifies the specific task to execute.
                Parameters: dict, optional. Used to pass information to the API actions of connected resources. 
                ResultPath: string, optional. Specifies where (in the input) to place the results of executing the task that's specified in Resource. 
                Retry: object arry, optional. An array of objects, called Retriers, that define a retry policy if the state encounters runtime errors.
                Catch: object array, optional. An array of objects, called Catchers, that define a fallback state. 
                TimeoutSeconds: integrer, optional. If the task runs longer than the specified seconds, this state fails with a States.Timeout error name. 
                HeartbeatSeconds: integer, optional. If more time than the specified seconds elapses between heartbeats from the task, this state fails with a States.

         """
        self.Resource = Resource
        self.Parameters = Parameters
        self.ResultPath = ResultPath
        self.Retry = Retry
        self.Catch = Catch
        self.TimeoutSeconds = TimeoutSeconds
        self.HeartbeatSeconds = HeartbeatSeconds


class FailState(AbstractState):
    """
    Fail class that defines Fail state variables and functions
    """

    def __init__(self, error, cause):
        self.Error = error
        self.Cause = cause


class PassState(AbstractState):
    """
    Pass class that defines pass state variables and functions
    """

    def __init__(self, error, cause):
        self.Error = error
        self.Cause = cause


class WaitState(AbstractState):
    """
    Wait class that defines Wait state variables and functions
    """

    def __init__(self, error, cause):
        self.Error = error
        self.Cause = cause


class SucceedState(AbstractState):
    """
    Succeed state class that defines success state variables and functions
    """

    def __init__(self, error, cause):
        self.Error = error
        self.Cause = cause


class ParallelState(AbstractState):
    """
    Parallel class that defines parallel state variables and functions
    """

    def __init__(self, error, cause):
        self.Error = error
        self.Cause = cause


class ChoiceState(AbstractState):
    """
    Choice class that defines Choice state variables and functions
    """

    def __init__(self, choices, Default):
        self.Choices = choices
        self.Default = Default
