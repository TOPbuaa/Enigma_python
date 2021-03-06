from Enigma import *


def offset_print(*a):
    for offset in a:
        if isinstance(offset, str):
            print(offset)
        else:
            print(chr(ord('A')+offset))


def get_offset(letter):
    return ord(letter)-ord('A')


def test_panel():
    panel = patch_panel('bq cr di ej kw mt os px uz gh')
    assert(panel.panel_in('C') == get_offset('R'))
    assert(panel.panel_out(get_offset('Z')) == 'U')


def test_reflect():
    r = reflector(UKW_B)
    assert(r.reflect(get_offset('F')) == get_offset('S'))
    assert(r.reflect(get_offset('G')) == get_offset('L'))


def test_rotor():
    rotor1 = rotor(Wheel_I, 'A')
    assert(rotor1.rotor_in(get_offset('D')) == get_offset('F'))
    assert(rotor1.rotor_out(get_offset('S')) == get_offset('S'))
    rotor2 = rotor(Wheel_II, 'A')
    assert(rotor2.rotor_in(get_offset('C')) == get_offset('D'))
    assert(rotor2.rotor_out(get_offset('S')) == get_offset('E'))
    rotor3 = rotor(Wheel_III, 'I')
    assert(rotor3.rotor_in(get_offset('C')) == get_offset('P'))
    assert(rotor3.rotor_out(get_offset('O')) == get_offset('J'))


def test_Enigma():
    e = Enigma([Wheel_I, Wheel_II, Wheel_III], ['P', 'E', 'Z'], UKW_B, '')
    e1 = Enigma([Wheel_I, Wheel_II, Wheel_III], ['P', 'E', 'Z'], UKW_B, '')
    fplaintext = open('plaintext', 'r')
    plaintext = fplaintext.readline()
    fciphertext = open('ciphertext', 'r')
    ciphertext = fciphertext.readline().upper().replace(' ', '')
    assert(e.code(plaintext) == ciphertext)
    assert(e1.code(ciphertext) == plaintext)
    fplaintext.close()
    fciphertext.close()


def test_Enigma_singlecode():
    e = Enigma([Wheel_I, Wheel_II, Wheel_III], ['A', 'A', 'A'], UKW_B, "")
    assert(e.single_code('A') == 'B')
    e = Enigma([Wheel_I, Wheel_II, Wheel_III], ['N', 'C', 'Q'], UKW_B, "")
    assert(e.single_code('W') == 'G')
    e = Enigma([Wheel_I, Wheel_II, Wheel_III], ['Q', 'E', 'R'], UKW_B, "")
    assert(e.single_code('S') == 'W')


def test_Enigma_code():
    e = Enigma([Wheel_III, Wheel_I, Wheel_II], ['N', 'C', 'C'], UKW_B, "")
    assert(e.code("HELLOWORLD") == "TGNGVBCDBC")
    e = Enigma([Wheel_V, Wheel_IV, Wheel_III], ['A', 'Q', 'L'], UKW_B, "bq cr di ej kw mt os px uz gh")
    assert(e.code("ENIGMA") == "TKHUER")

test_rotor()
test_panel()
test_reflect()
test_Enigma()
test_Enigma_singlecode()
test_Enigma_code()
print('tests passed')
