import cocotb
from cocotb.triggers import Timer, FallingEdge, ClockCycles, RisingEdge, Join, First
from cocotb.binary import BinaryValue, BinaryRepresentation 
from cocotb.clock import Clock

calc_values_sin = ['01100101', '01110110', '00011101', '10101110', '10000101', '11000000', '00110011', '01111001', '01010110', '11110100', '10010010', '10010101', '11111011', '01011101', '01111010', '00101001', '10111011', '10000100', '10110100', '00100011', '01110110', '01100000', '00000100', '10011010', '10001101', '11101011', '01010001', '01111100', '00111111', '11001000', '10000011', '10101011', '00001111', '01110001', '01101010', '00000101', '10100100', '10001000', '11010100', '01000110', '01111011', '01000100', '11011100', '10000111', '10011111', '00000101', '01101011', '01110010', '00010101', '10101000', '10000111', '11000110', '00111001', '01111001', '01010111', '11101100', '10001110', '10010101', '11111011', '01100001', '01111000', '00100101', '10111011', '10000101', '10111010', '00101101', '01111000', '01011100', '11111100', '10010110', '10001111', '11110001', '01010101', '01111100', '00110111', '11000000', '10000100', '10101111', '00010101', '01110011', '01100110', '11111101', '10100000', '10001010', '11011101', '01001100', '01111110', '01000100', '11010110', '10000101', '10100011', '00000101', '01101011', '01101110', '00001101', '10101010', '10000111', '11001110', '00111111', '01111011', '01010001', '11100100', '10001010', '10011011', '00000001', '01100101', '01110110', '00011101', '10110011', '10000101', '11000000', '00110011', '01111001', '01010110', '11110100', '10010010', '10010011', '11110001', '01011001', '01111010', '00110001', '11000000', '10000100', '10110100', '00011101', '01110110', '01100110', '00000100', '10011010', '10001101', '11100011', '01010001', '01111100', '00111111', '11001110', '10000011', '10100111', '00001111', '01101101', '01101010', '00000101', '10100100', '10000111', '11010100', '01000110', '01111011', '01001100', '11011100', '10001001', '10011111', '11111111', '01100101', '01110110', '00010101', '10101110', '10000101', '11000000', '00111001', '01111001', '01010111', '11110100', '10001110', '10010101', '11111011', '01011101', '01111000', '00101001', '10111011', '10000100', '10111010', '00100011', '01111000', '01100000', '11111100', '10010110', '10001111', '11101011', '01010101', '01111100', '00110111', '11001000', '10000011', '10101011', '00010101', '01110001', '01101010', '00000101', '10100000', '10001000', '11011101', '01000110', '01111010', '01000100', '11010110', '10000111', '10100011', '00000101', '01101011', '01110010', '00001101', '10101000', '10000111', '11000110', '00111111', '01111011', '01010001', '11101100', '10001010', '10011011', '00000001', '01100001', '01110110', '00100101', '10110011', '10000101', '10111010', '00101101', '01111001', '01011100', '11111100', '10010110', '10010011', '11110001', '01011001', '01111100', '00110001', '11000000', '10000100', '10101111', '00011101', '01110011', '01100110', '11111101', '10011010', '10001010', '11100011', '01001100', '01111100', '00111111', '11001110', '10000101', '10100111', '00001111', '01101101', '01101110', '00001101', '10101010', '10000111', '11001110', '00111111', '01111011', '01001100', '11100100', '10001001', '10011011', '11111111', '01100101', '01110110', '00011101', '10101110', '10000101', '11000000', '00110011', '01111001', '01010110', '11110100', '10010010', '10010101', '11111011', '01011101', '01111010', '00101001', '10111011', '10000100', '10110100', '00100011', '01110110', '01100000', '00000100', '10011010', '10001101', '11101011', '01010001', '01111100', '00111111', '11001000', '10000011', '10101011', '00001111', '01110001', '01101010', '00000101', '10100100', '10001000', '11010100', '01000110', '01111011', '01000100', '11011100', '10000111']
calc_values_sawtooth = ['00000001', '00000010', '00000011', '00000100', '00000101', '00000110', '00000111', '00001000', '00001001', '00001010', '00001011', '00001100', '00001101', '00001110', '00001111', '00010000', '00010001', '00010010', '00010011', '00010100', '00010101', '00010110', '00010111', '00011000', '00011001', '00011010', '00011011', '00011100', '00011101', '00011110', '00011111', '00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '10100111', '10101000', '10101001', '10101010', '10101011', '10101100', '10101101', '10101110', '10101111', '10110000', '10110001', '10110010', '10110011', '10110100', '10110101', '10110110', '10110111', '10111000', '10111001', '10111010', '10111011', '10111100', '10111101', '10111110', '10111111', '11000000', '11000001', '11000010', '11000011', '11000100', '11000101', '11000110', '11000111', '11001000', '11001001', '11001010', '11001011', '11001100', '11001101', '11001110', '11001111', '11010000', '11010001', '11010010', '11010011', '11010100', '11010101', '11010110', '11010111', '11011000', '11011001', '11011010', '11011011', '11011100', '11011101', '11011110', '11011111', '11100000', '11100001', '11100010', '11100011', '11100100', '11100101', '11100110', '11100111', '11101000', '11101001', '11101010', '11101011', '11101100', '11101101', '11101110', '11101111', '11110000', '11110001', '11110010', '11110011', '11110100', '11110101', '11110110', '11110111', '11111000', '11111001', '11111010', '11111011', '11111100', '11111101', '11111110', '11111111', '00000000', '00000001', '00000010', '00000011', '00000100', '00000101', '00000110', '00000111', '00001000', '00001001', '00001010', '00001011', '00001100', '00001101', '00001110', '00001111', '00010000', '00010001', '00010010', '00010011', '00010100', '00010101', '00010110', '00010111', '00011000', '00011001', '00011010', '00011011', '00011100', '00011101', '00011110', '00011111', '00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '10100111', '10101000', '10101001', '10101010', '10101011', '10101100', '10101101', '10101110', '10101111', '10110000', '10110001', '10110010', '10110011', '10110100', '10110101', '10110110', '10110111', '10111000', '10111001', '10111010', '10111011', '10111100', '10111101', '10111110', '10111111', '11000000', '11000001', '11000010', '11000011', '11000100', '11000101', '11000110']
calc_values_triangle = ['00000001', '00000010', '00000011', '00000100', '00000101', '00000110', '00000111', '00001000', '00001001', '00001010', '00001011', '00001100', '00001101', '00001110', '00001111', '00010000', '00010001', '00010010', '00010011', '00010100', '00010101', '00010110', '00010111', '00011000', '00011001', '00011010', '00011011', '00011100', '00011101', '00011110', '00011111', '00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '01011001', '01011000', '01010111', '01010110', '01010101', '01010100', '01010011', '01010010', '01010001', '01010000', '01001111', '01001110', '01001101', '01001100', '01001011', '01001010', '01001001', '01001000', '01000111', '01000110', '01000101', '01000100', '01000011', '01000010', '01000001', '01000000', '00111111', '00111110', '00111101', '00111100', '00111011', '00111010', '00111001', '00111000', '00110111', '00110110', '00110101', '00110100', '00110011', '00110010', '00110001', '00110000', '00101111', '00101110', '00101101', '00101100', '00101011', '00101010', '00101001', '00101000', '00100111', '00100110', '00100101', '00100100', '00100011', '00100010', '00100001', '00100000', '00011111', '00011110', '00011101', '00011100', '00011011', '00011010', '00011001', '00011000', '00010111', '00010110', '00010101', '00010100', '00010011', '00010010', '00010001', '00010000', '00001111', '00001110', '00001101', '00001100', '00001011', '00001010', '00001001', '00001000', '00000111', '00000110', '00000101', '00000100', '00000011', '00000010', '00000001', '00000000', '11111111', '11111110', '11111101', '11111100', '11111011', '11111010', '11111001', '11111000', '11110111', '11110110', '11110101', '11110100', '11110011', '11110010', '11110001', '11110000', '11101111', '11101110', '11101101', '11101100', '11101011', '11101010', '11101001', '11101000', '11100111', '11100110', '11100101', '11100100', '11100011', '11100010', '11100001', '11100000', '11011111', '11011110', '11011101', '11011100', '11011011', '11011010', '11011001', '11011000', '11010111', '11010110', '11010101', '11010100', '11010011', '11010010', '11010001', '11010000', '11001111', '11001110', '11001101', '11001100', '11001011', '11001010', '11001001', '11001000', '11000111', '11000110', '11000101', '11000100', '11000011', '11000010', '11000001', '11000000', '10111111', '10111110', '10111101', '10111100', '10111011', '10111010', '10111001', '10111000', '10110111', '10110110', '10110101', '10110100', '10110011', '10110010', '10110001', '10110000', '10101111', '10101110', '10101101', '10101100', '10101011', '10101010', '10101001', '10101000', '10100111', '10100111', '10101000', '10101001', '10101010', '10101011', '10101100', '10101101', '10101110', '10101111', '10110000', '10110001', '10110010', '10110011', '10110100', '10110101', '10110110', '10110111', '10111000', '10111001', '10111010', '10111011', '10111100', '10111101', '10111110', '10111111', '11000000', '11000001', '11000010', '11000011', '11000100', '11000101', '11000110']
calc_values_square_pulse = ['10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '10000001', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111', '01111111']

calc_values_cos = ['01000110', '11010100', '10001000', '10100100', '00000101', '01101010', '01110001', '00001111', '10101011', '10000011', '11001000', '00111111', '01111100', '01010001', '11101011', '10001101', '10011010', '00000100', '01100000', '01110110', '00100011', '10110100', '10000100', '10111011', '00101001', '01111010', '01011101', '11111011', '10010101', '10010010']
calc_values_sin = ['01100101', '01110110', '00011101', '10101110', '10000101', '11000000', '00110011', '01111001', '01010110', '11110100', '10010010', '10010101', '11111011', '01011101', '01111010', '00101001', '10111011', '10000100', '10110100', '00100011', '01110110', '01100000', '00000100', '10011010', '10001101', '11101011', '01010001', '01111100', '00111111', '11001000']
calc_values_z = ['00000000', '11111111', '00000000', '11111111', '00000000', '11111111', '00000000', '11111111', '00000000', '11111111', '00000000', '11111111', '11111110', '11111111', '00000000', '11111111', '11111110', '11111111', '00000000', '11111111', '00000000', '11111111', '00000000', '00000001', '00000000', '11111111', '00000000', '00000001', '00000000', '11111111']

calc_values_xc = ['01001011', '00000000', '00000000', '00000000', '01001011', '01001011', '01001011', '01001011', '00000000', '00000000', '00000000', '01001011', '01001011', '01001011', '00000000', '00000000', '00000000', '00000000', '01001011', '01001011', '01001011', '00000000', '00000000', '00000000', '01001011', '01001011', '01001011', '00000000', '00000000', '00000000']
calc_values_yc = ['00000000', '01001011', '01001011', '10110101', '00000000', '00000000', '00000000', '00000000', '01001011', '10110101', '10110101', '00000000', '00000000', '00000000', '01001011', '01001011', '10110101', '10110101', '00000000', '00000000', '00000000', '01001011', '10110101', '10110101', '00000000', '00000000', '00000000', '01001011', '01001011', '10110101']
calc_values_zc = ['00100111', '00001110', '00110101', '11011100', '11000011', '11101010', '00010001', '00111000', '00011111', '11000110', '11101101', '11010100', '11111011', '00100010', '00001001', '00110000', '11010111', '11111110', '11100101', '00001100', '00110011', '00011010', '11000001', '11101000', '11001111', '11110110', '00011101', '00000100', '00101011', '11010010']

calc_values_xi = ['01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011', '01001011']
calc_values_yi = ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']
calc_values_zi = ['00100111', '01001110', '01110101', '10011100', '11000011', '11101010', '00010001', '00111000', '01011111', '10000110', '10101101', '11010100', '11111011', '00100010', '01001001', '01110000', '10010111', '10111110', '11100101', '00001100', '00110011', '01011010', '10000001', '10101000', '11001111', '11110110', '00011101', '01000100', '01101011', '10010010']

async def reset_dut(reset_n, duration_ns):
    reset_n.value = 0
    await Timer(duration_ns, units="ns")
    reset_n.value = 1
    reset_n._log.info("Reset complete")


@cocotb.test()
async def cosim_tt_sin(dut):

    # init values for dut
    dut.ena.value = 1
    dut.enable.value = 0
    dut.set_phase.value = 0
    dut.set_amplitude.value = 0
    dut.waveform.value = BinaryValue('00') # set mode to sinus
    dut.data_i.value = BinaryValue('00000000')


    # start clock
    cocotb.start_soon(Clock(dut.clk, 16, units="ns").start())

    # reset dut
    await reset_dut(dut.rst_n, 20)

    # set amplitude and phase
    
    await RisingEdge(dut.clk)
    dut.data_i.value = BinaryValue('00100111')
    dut.set_phase.value = 1

    await RisingEdge(dut.clk)
    dut.set_phase.value = 0

    await RisingEdge(dut.clk)
    dut.data_i.value = BinaryValue('01001011')
    dut.set_amplitude.value = 1

    await RisingEdge(dut.clk)
    dut.set_amplitude.value = 0
    
    dut.enable.value = 1

    forked = cocotb.start_soon(print_test_value(dut, calc_values_yi))
    # await cocotb.start_soon(enable_control(dut))

    await Join(forked)

    dut._log.info('Test finished')


# @cocotb.test()
# async def cosim_tt_sawtooth(dut):

#     # init values for dut
#     dut.ena.value = 1
#     dut.enable.value = 0
#     dut.set_phase.value = 0
#     dut.set_amplitude.value = 0
#     dut.waveform.value = BinaryValue('10') # set mode to sinus
#     dut.data_i.value = BinaryValue('00000000')


#     # start clock
#     cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

#     # reset dut
#     await reset_dut(dut.rst_n, 20)

#     # set amplitude and phase
    
#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('00000001')
#     dut.set_phase.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_phase.value = 0

#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('01011000')
#     dut.set_amplitude.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_amplitude.value = 0
    
#     dut.enable.value = 1

#     forked = cocotb.start_soon(check_value(dut, calc_values_sawtooth))
#     await cocotb.start_soon(enable_control(dut))

#     await Join(forked)

#     dut._log.info('Test finished')


# @cocotb.test()
# async def cosim_tt_triangle(dut):

#     # init values for dut
#     dut.ena.value = 1
#     dut.enable.value = 0
#     dut.set_phase.value = 0
#     dut.set_amplitude.value = 0
#     dut.waveform.value = BinaryValue('11') # set mode to sinus
#     dut.data_i.value = BinaryValue('00000000')


#     # start clock
#     cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

#     # reset dut
#     await reset_dut(dut.rst_n, 20)

#     # set amplitude and phase
    
#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('00000001')
#     dut.set_phase.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_phase.value = 0

#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('01011000')
#     dut.set_amplitude.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_amplitude.value = 0
    
#     dut.enable.value = 1

#     forked = cocotb.start_soon(check_value(dut, calc_values_triangle))
#     await cocotb.start_soon(enable_control(dut))

#     await Join(forked)

#     dut._log.info('Test finished')

# @cocotb.test()
# async def cosim_tt_square_puls(dut):

#     # init values for dut
#     dut.ena.value = 1
#     dut.enable.value = 0
#     dut.set_phase.value = 0
#     dut.set_amplitude.value = 0
#     dut.waveform.value = BinaryValue('01') # set mode to sinus
#     dut.data_i.value = BinaryValue('00000000')


#     # start clock
#     cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

#     # reset dut
#     await reset_dut(dut.rst_n, 20)

#     # set amplitude and phase
    
#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('00000001')
#     dut.set_phase.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_phase.value = 0

#     await RisingEdge(dut.clk)
#     dut.data_i.value = BinaryValue('00011001')
#     dut.set_amplitude.value = 1

#     await RisingEdge(dut.clk)
#     dut.set_amplitude.value = 0
    
#     dut.enable.value = 1

#     forked = cocotb.start_soon(check_value(dut, calc_values_square_pulse))
#     await cocotb.start_soon(enable_control(dut))

#     await Join(forked)

#     dut._log.info('Test finished')

async def check_value(dut, calc_values):
    dut._log.info(f'#{0:>03} -> {"dut".center(8)} | {"python".center(8)}')
    for i in range(len(calc_values)):

        await FallingEdge(dut.spi_cs)
        
        dut._log.info(f'#{i:>03} -> {dut.data_o.value.binstr} | {calc_values[i]}')

        assert dut.data_o.value.binstr == calc_values[i]

        sample_str = calc_values[i]
        for k in range(8):
            t1 = RisingEdge(dut.spi_clk)
            t2 = RisingEdge(dut.spi_cs)
            t_ret = await First(t1, t2)
            if t_ret is t2:
                assert False
            dut._log.info(f'----- #{k:>03} -> {dut.spi_mosi.value.binstr}  | {sample_str[k]}')
            assert dut.spi_mosi.value.binstr == sample_str[k]
            assert dut.spi_cs.value == 0

        await RisingEdge(dut.spi_cs)


async def print_value(dut, calc_values):
    dut._log.info(f'#{0:>03} -> {"dut".center(8)} | {"python".center(8)}')
    for i in range(len(calc_values)):

        await FallingEdge(dut.spi_cs)
        
        dut._log.info(f'#{i:>03} -> {dut.data_o.value.binstr} | {calc_values[i]}')

        # assert dut.data_o.value.binstr == calc_values[i]

        sample_str = calc_values[i]
        for k in range(8):
            t1 = RisingEdge(dut.spi_clk)
            t2 = RisingEdge(dut.spi_cs)
            t_ret = await First(t1, t2)
            if t_ret is t2:
                assert False
            dut._log.info(f'----- #{k:>03} -> {dut.spi_mosi.value.binstr}  | {sample_str[k]}')
            # assert dut.spi_mosi.value.binstr == sample_str[k]
            # assert dut.spi_cs.value == 0

        await RisingEdge(dut.spi_cs)


async def print_test_value(dut, calc_values):
    dut._log.info(f'#{0:>03} -> {"dut".center(8)} | {"python".center(8)}')
    for i in range(len(calc_values)):

        await FallingEdge(dut.spi_cs)
        
        dut._log.info(f'#{i:>03} -> {dut.data_o.value.binstr} | {calc_values[i]} | {dut.data_o.value.binstr == calc_values[i]}')

        # assert dut.data_o.value.binstr == calc_values[i]

        await RisingEdge(dut.spi_cs)

async def enable_control(dut):
    await Timer(2000, units='ns')
    dut.enable.value = 0
    await ClockCycles(dut.clk, 70)
    dut.enable.value = 1