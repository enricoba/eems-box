import interface


interface = interface.RMI()
message = {
    '1': 20,
    '2': 30
}
interface.send_single('test', message)

