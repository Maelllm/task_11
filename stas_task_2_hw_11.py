data_input = input('Enter your data ')


def snap(data):
    assert data, 'How dare you snap False!'
    try:
        b = data.__iter__
    except AttributeError:
        raise AttributeError('You did not have the power for snap')
    else:
        gauntlet = {k: v for k, v in zip(range(0, len(data)), data)}
        print(f' You did make a {gauntlet}')
    finally:
        print('I am inevitable')
    return


# print(snap(data_input))
print(snap(1))
# print(snap(False))
