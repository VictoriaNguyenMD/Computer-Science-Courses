from call_me import GetCalled

def call_nested(n, m ):

    call_me = GetCalled()
    
    for i1 in range(n):
        for i2 in range(m):
            call_me.call()

    return call_me
