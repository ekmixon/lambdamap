import base64
import cloudpickle


def handler(event, context):
    """
    """

    payload = cloudpickle.loads(base64.b64decode(event))
    func = payload['func']
    args = payload['args']
    kwargs = payload['kwargs']

    result = func(*args, **kwargs)
    return cloudpickle.dumps(result)
