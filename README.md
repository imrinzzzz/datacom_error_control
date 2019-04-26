# datacom_error_control

> In data communication, error can happen during the transmission of data from the sender to
> the receiver over unreliable medium.
> ![Sender and Receiver plus unreliable transmission](https://raw.githubusercontent.com/imrinzzzz/datacom_error_control/master/assignment1.jpg)
> In order to help the receiver check for error, redundancy bits are added to the dataword to help
> the receiver verifies the validity of the received data (codeword).

In this project, I have implemented the knowledge I learnt in class by writing the programs and functions.

### The functions are as follows:
#### 1. Unreliable transmission: output = *unreliable_transmission*(input, p)

  > Input:
  > 1. bit string of any size up to k (input frame).
  > 2. Probability of having a bit in error (p).
  >
  > Output:
  > 1. bit string of size k defined by the input bit string (output frame).
  >
  > Behavior:
  > The function randomly generates errors on the bits of the input frame. A bit can be in error with probability p. The function outputs output frame which could be a corrupted or uncorrupted frame.
  
#### 2. Parity bit:

  Generator: codeword = *parity_gen*(dataword, parity_type, size)
    
  > Input:
  > 1. A bit string of any size up to k (input frame) where k ≥ 9 (input frame)
  > 2. Type of parity (even, odd, two-dimensional-even, two-dimensional-odd)
  > 3. Size of two-dimensional block for dataword (if two-dimensional parity bit is used).
  >
  > Output:
  > 1. A code word based on the type of parity
  >
  > Behavior:
  > This function calculates the redundancy bit(s) for the dataword and output the codeword. If two-dimensional parity check is used, the size of the two-dimensional block for dataword must be specify. For example, 3x3, 4x4.

  Checker: validity = *parity_check*(codeword, parity_type, size)

  > Input:
  > 1. A bit string of any size up to k (codeword)
  > 2. Type of parity (even, odd, two-dimensional-even, two-dimensional-odd)
  > 3. Size of two-dimensional block for dataword (if two-dimensional parity bit is used).
  >
  > Output:
  > 1. Validity of codeword
  >
  > Behavior:
  > This function verifies the codeword.
  
#### 3. CRC
  
  Generator: codeword = *CRC_gen*(dataword, divisor)
 
  > Input:
  > 1. Dataword of size k
  > 2. Divisor
  >
  > Output:
  > 1. A codeword based on CRC
  >
  > Behavior: 
  > This function calculates the redundancy bit(s) for the dataword and output the codeword for CRC. Hint: you have to create a modulo-2 division function.
  
  Checker: validity = *CRC_check*(codeword, divisor)
  
  > Input:
  > 1. codeword size k
  > 2. divisor
  >
  > Output:
  > 1. Validity of codeword
  >
  > Behavior:
  > This function verifies the CRC codeword.
  
#### 4. Checksum

  Generator: codeword = *Checksum_gen*(datawords, word_size, num_blocks)

  > Input:
  > 1. A set of datawords
  > 2. Size of each dataword (word_size)
  > 3. Number of datawords used (num_blocks)
  >
  > Output:
  > 1. A codeword based on Checksum
  >
  > Behavior:
  > This function calculates the redundancy bit(s) for the dataword and output the codeword for Checksum.
  
  Checker: validity = *Checksum_check*(codeword, word_size, num_blocks)
  
  > Input:
  > 1. codeword
  > 2. Size of each dataword (word_size)
  > 3. Number of datawords used (num_blocks)
  >
  > Output:
  > 1. Validity of codeword
  >
  > Behavior:
  > This function verifies the CRC codeword.

#### 5. Hamming code

  Generator: codeword = Hamming_gen(dataword)

  > Input:
  > 1. A dataword
  >
  > Output:
  > 1. A codeword based on Hamming code
  >
  > Behavior:
  > This function calculates the redundancy bit(s) for the dataword and output the codeword for Hamming code.
  
  Checker: error_pos = *Hamming_check*(codeword)
  
  > Input:
  > 1. codeword
  >
  > Output:
  > 1. Position of error (in case of a single bit error)
  >
  > Behavior:
  > This function verifies the Hamming codeword and report the location of error for the case of single bit error.
  
  
  ____


  #### TLDR; I have created a program that implements the knowledge of error control I learnt in class.


  The file named "datacomm" is a module used in the file "6088122_DataComm". It contains all the functions in the assignment. 

  To run those functions, you have to install python on your computer first. You can follow this [link](https://realpython.com/installing-python/) to download python step by step.

  For python2, type: `python 6088122_DataComm.py` <br>
  For python3, type: `python3 6088122_DataComm.py`

  After that, the file will run. Please follow the instruction of the file carefully. 

============================================================
Enjoy!!
